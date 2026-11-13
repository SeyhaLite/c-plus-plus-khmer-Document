# ការរួមចំណែក និងការដាក់ផ្សាយ

គម្រោងនេះត្រូវបានសាងសង់ដើម្បីឱ្យមនុស្សផ្សេងទៀតអាចបន្តបានយ៉ាងងាយ។
ផ្នែកនេះពន្យល់ពីរបៀបបន្ថែមទំព័រថ្មី និងរបៀបដាក់គេហទំព័រនៅលើ Read the Docs។

## រចនាសម្ព័ន្ធគម្រោង

```text
docs/                 ខ្លឹមសារខ្មែរ (MyST Markdown)
docs/conf.py          ការកំណត់ Sphinx
sphinxext/            extension សម្រាប់ស្លាក ស្ថិតិ និងការស្វែងរកខ្មែរ
khmercpp/             ឧបករណ៍រួម៖ inventory, ស្ថិតិ, validation, providers
scripts/pipeline.py   CLI សម្រាប់ការបកប្រែ និងការផ្ទៀងផ្ទាត់
scripts/check_examples.py  បកប្រែ និងដំណើរការគំរូកូដ C++
examples/             គំរូកូដពិត (ឈ្មោះឯកសារត្រូវនឹង id ទំព័រ)
data/inventory.json   បញ្ជីទំព័រត្រូវការ និងស្ថានភាពបកប្រែ
data/terminology.json បញ្ជីពាក្យដែលត្រូវប្រើដោយស៊ីសង្វាក់
data/progress.json    ស្នាមថតស្ថិតិចុងក្រោយ (បង្កើតដោយស្វ័យប្រវត្តិ)
```

## ដំឡើងនៅលើកុំព្យូទ័ររបស់អ្នក

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
make html          # បង្កើតគេហទំព័រនៅ docs/_build/html
make serve         # បើកម៉ាស៊ីនបម្រើក្នុងម៉ាស៊ីនតែមួយ
```

## បន្ថែមទំព័រថ្មី

1. បន្ថែមធាតុទៅ `data/inventory.json` (id, ចំណងជើងខ្មែរ, ស្តង់ដារ, ស្ថានភាព, ប្រភព)។
2. បង្កើតឯកសារ៖ `python scripts/pipeline.py new --page basics/my-topic`។
3. បង្កើតគំរូកូដ៖ `examples/basics/my-topic.cpp` ជាមួយ `// std: c++17`
   និងប្លុក `EXPECT`។
4. សរសេរខ្មែរ ហើយបញ្ចូលគំរូកូដដោយ `literalinclude` ដើម្បីធានាថាកូដក្នុងទំព័រ
   គឺជាកូដដែលគេបកប្រែពិត។
5. ផ្ទៀងផ្ទាត់៖
   ```bash
   python scripts/pipeline.py verify --page basics/my-topic
   python scripts/check_examples.py
   python scripts/pipeline.py validate --strict
   ```
6. ពេលឆ្លងកាត់ទាំងអស់ សូមសម្គាល់ថាបានផ្ទៀងផ្ទាត់៖
   `python scripts/pipeline.py verify --page basics/my-topic --accept`។

## ដំណើរការបកប្រែដោយស្វ័យប្រវត្តិ (ស្រេចចិត្ត)

បើអ្នកមាន API key សម្រាប់ endpoint ដែលគាំទ្រ OpenAI៖

```bash
export KHMER_TRANSLATE_API_KEY="..."      # មិនត្រូវសរសេរក្នុង repo ឡើយ
python scripts/pipeline.py fetch --page basics/my-topic
python scripts/pipeline.py translate --page basics/my-topic --provider openai
```

សេចក្ដីព្រាងដែលបានមកត្រូវមានស្លាក «រង់ចាំត្រួតពិនិត្យ» ជានិច្ច។
យើងមិនដែលដាក់ស្លាក «បានផ្ទៀងផ្ទាត់» ដោយស្វ័យប្រវត្តិឡើយ។

## ការដាក់ផ្សាយលើ Read the Docs (ឥតគិតថ្លៃ)

1. បង្កើត repository នៅ GitHub ហើយ push កូដនេះ។
2. ចូល [readthedocs.org](https://readthedocs.org/) ហើយ «Import a Project»។
3. ជ្រើស repository។ Read the Docs នឹងអាន `.readthedocs.yaml` ដោយស្វ័យប្រវត្តិ។
4. ចុច «Build version»។ បើជោគជ័យ គេហទំព័រនឹងមាននៅ
   `https://<ឈ្មោះគម្រោង>.readthedocs.io/`។
5. រាល់ការ push ទៅសាខា `main` នឹងបង្កើតឯកសារថ្មីដោយស្វ័យប្រវត្តិ។

Read the Docs ផ្ដល់ការបង្កើតឯកសារដោយឥតគិតថ្លៃសម្រាប់គម្រោងសាធារណៈ
ហើយមានដែនកំណត់ពេលវេលាបង្កើតក្នុងមួយខែ។ បើគម្រោងរបស់អ្នកធំឡើង
ហើយជួបដែនកំណត់ សូមពិនិត្យគម្រោងបច្ចុប្បន្នរបស់ពួកគេម្ដងទៀត
ព្រោះលក្ខខណ្ឌអាចផ្លាស់ប្តូរ។

## ច្បាប់គុណភាព

- មិនប្រឌិតលក្ខណៈ C++ ឡើយ។ បើមិនប្រាកដ សូមពិនិត្យជាមួយ cppreference
  ឬសេចក្ដីព្រាងស្តង់ដារ ហើយកត់ត្រាប្រភព។
- កូដទាំងអស់ត្រូវបកប្រែ និងដំណើរការបាន។ `EXPECT` ត្រូវត្រូវនឹងលទ្ធផលពិត។
- ស្តង់ដារត្រូវបញ្ជាក់ឱ្យច្បាស់។ លក្ខណៈ C++26 ត្រូវសម្គាល់ថា «ព្រាង»។
- ពាក្យបច្ចេកទេសត្រូវដូចក្នុង `data/terminology.json`។
