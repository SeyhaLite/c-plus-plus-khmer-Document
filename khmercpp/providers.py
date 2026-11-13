"""Translation providers for the documentation pipeline.

Two providers exist:

``manual``
    A human (or an agent) writes the Khmer page; the pipeline only validates
    and registers it.  This is the default, because a careful translation is
    worth more than a fast one.

``openai``
    The official OpenAI API is the default. A custom OpenAI-compatible endpoint
    can be selected explicitly through environment variables. The API key is
    sent to that endpoint, so only use a provider you trust.
"""

from __future__ import annotations

import json
import os
import urllib.error
import urllib.request
from typing import Any

DEFAULT_BASE_URL = "https://api.openai.com/v1"
DEFAULT_MODEL = "gpt-5.1"


class TranslationError(RuntimeError):
    """Raised when a translation cannot be produced."""


class MissingCredentials(TranslationError):
    """Raised when the API provider has no key configured."""


def _rules(terminology: dict[str, Any], page: dict[str, Any]) -> str:
    glossary = "\n".join(
        f"- {term['en']} -> {term['km']}" for term in terminology["terms"][:60]
    )
    never = ", ".join(terminology["never_translate"][:80])
    sources = "\n".join(f"- {url}" for url in page.get("sources", []))
    return f"""You are a senior C++ engineer and a professional Khmer technical translator.
Translate the supplied C++ reference text into natural, precise Khmer.

Hard rules:
1. Never translate or alter code, identifiers, keywords, or anything inside code fences.
2. Keep these identifiers exactly as written: {never}
3. Khmer text must read naturally for a Khmer developer. Do not translate word by word.
4. On first use of a technical term, write the Khmer term followed by the English term in
   parentheses, for example: អថេរ (Variable).
5. Keep every Markdown structure (headings, lists, tables, code fences) intact.
6. Never invent C++ facts, functions, syntax, or compiler behaviour. If the source does not
   state something, do not add it.
7. Output only the translated Markdown body: no H1 title, no translation-meta directive,
   no commentary about the translation itself.

Use this glossary consistently:
{glossary}

Page id: {page['id']}
Minimum C++ standard: {page['since']}
Authoritative sources to keep as references:
{sources}
"""


def _post(url: str, payload: dict[str, Any], api_key: str, timeout: int = 180) -> dict[str, Any]:
    request = urllib.request.Request(
        url,
        data=json.dumps(payload).encode("utf-8"),
        headers={
            "Content-Type": "application/json",
            "Authorization": f"Bearer {api_key}",
        },
        method="POST",
    )
    try:
        with urllib.request.urlopen(request, timeout=timeout) as response:
            return json.loads(response.read().decode("utf-8"))
    except urllib.error.HTTPError as error:
        # Do not echo arbitrary upstream response bodies into terminal/CI logs.
        raise TranslationError(
            f"API ត្រឡប់ HTTP {error.code}។ សូមពិនិត្យ endpoint និង API credentials។"
        ) from error
    except urllib.error.URLError as error:
        raise TranslationError(f"មិនអាចភ្ជាប់ទៅ API: {error.reason}") from error


def translate(
    source_text: str,
    page: dict[str, Any],
    terminology: dict[str, Any],
    provider: str = "manual",
    model: str | None = None,
) -> str:
    """Return translated Markdown for ``source_text``."""
    if provider == "manual":
        raise TranslationError(
            "provider 'manual': សូមសរសេរឯកសារខ្មែរដោយផ្ទាល់នៅ docs/<id>.md រួចរត់ "
            "`python scripts/pipeline.py verify --page <id>`។"
        )
    if provider != "openai":
        raise TranslationError(f"provider មិនស្គាល់: {provider}")

    api_key = os.environ.get("KHMER_TRANSLATE_API_KEY") or os.environ.get("OPENAI_API_KEY")
    if not api_key:
        raise MissingCredentials(
            "ខ្វះ API key។ សូមកំណត់ env var KHMER_TRANSLATE_API_KEY (ឬ OPENAI_API_KEY) "
            "ក្នុងបរិស្ថានរបស់អ្នក ឬក្នុង Sites/RTD secrets។ មិនត្រូវសរសេរ key ក្នុងឯកសារ repo ទេ។"
        )

    base_url = os.environ.get("KHMER_TRANSLATE_BASE_URL", DEFAULT_BASE_URL).rstrip("/")
    payload = {
        "model": model or os.environ.get("KHMER_TRANSLATE_MODEL", DEFAULT_MODEL),
        "temperature": 0.2,
        "messages": [
            {"role": "system", "content": _rules(terminology, page)},
            {"role": "user", "content": source_text[:60000]},
        ],
    }
    data = _post(f"{base_url}/chat/completions", payload, api_key)
    try:
        content = data["choices"][0]["message"]["content"]
    except (KeyError, IndexError, TypeError) as error:
        raise TranslationError("ចម្លើយពី API មិនស្គាល់ទម្រង់") from error
    if not any("\u1780" <= char <= "\u17ff" for char in content):
        raise TranslationError("ចម្លើយពី API គ្មានអក្សរខ្មែរ — បដិសេធការបកប្រែ")
    return content.strip() + "\n"
