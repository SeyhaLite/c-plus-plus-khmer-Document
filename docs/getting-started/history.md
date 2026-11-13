# ប្រវត្តិ និងស្តង់ដារ C++

```{translation-meta} getting-started/history
```

## បន្ទាត់ពេលវេលា

| ឆ្នាំ | ព្រឹត្តិការណ៍ |
| --- | --- |
| 1979 | Bjarne Stroustrup ចាប់ផ្ដើម «C with Classes» នៅ Bell Labs |
| 1983 | ប្ដូរឈ្មោះជា C++ |
| 1985 | ចេញ C++ 1.0 ជាមួយសៀវភៅ *The C++ Programming Language* |
| 1989 | C++ 2.0 បន្ថែម multiple inheritance និង abstract classes |
| 1998 | **C++98** — ស្តង់ដារ ISO ដំបូង (ISO/IEC 14882:1998) |
| 2003 | **C++03** — ការកែកំហុសតូចតាចលើ C++98 មិនមែនលក្ខណៈថ្មីទេ |
| 2011 | **C++11** — ការផ្លាស់ប្ដូរធំបំផុត៖ `auto`, lambdas, move semantics, `nullptr`, ខ្សែស្រឡាយ |
| 2014 | **C++14** — ការកែលម្អលើ C++11 ដូចជា generic lambdas |
| 2017 | **C++17** — structured bindings, `std::optional`, `std::filesystem`, `if constexpr` |
| 2020 | **C++20** — concepts, ranges, coroutines, modules, `constexpr` កាន់តែខ្លាំង |
| 2023 | **C++23** — ចេញជាស្តង់ដារ ISO/IEC 14882:2024 (`std::expected`, `std::print`) |
| 2026 | **C++26** — កំពុងអភិវឌ្ឍ (ព្រាង) |

## របៀបអានតារាងនេះ

**C++03 មិនមែនជាស្តង់ដារថ្មីទេ។** វាជាការកែកំហុស (technical corrigendum)
លើ C++98។ ដូច្នេះឯកសារជាច្រើនសរសេររួមគ្នាថា «C++98/03»។

**ចាប់ពី C++11 មក មានវដ្ដ ៣ ឆ្នាំ។** គណៈកម្មាធិការ WG21 ចេញស្តង់ដារថ្មីរៀងរាល់
បីឆ្នាំ។ នេះជាហេតុផលដែលអ្នកឃើញ C++11, C++14, C++17, C++20, C++23 ។

**C++26 គឺជាព្រាង។** នៅពេលសរសេរឯកសារនេះ C++26 មិនទាន់ចេញជាស្តង់ដារ
ផ្លូវការនៅឡើយទេ។ លក្ខណៈណាដែលមកពី C++26 ត្រូវសម្គាល់ថា **ព្រាង**
ហើយកម្មវិធីបកប្រែជាច្រើនអាចមិនគាំទ្រវា។ យើងមិនដាក់ស្លាកវាថា
«ស្តង់ដារផ្លូវការ» ឡើយ។

## ម៉ាក្រូ `__cplusplus`

កម្មវិធីបកប្រែកំណត់ម៉ាក្រូ `__cplusplus` ជាតម្លៃដែលបង្ហាញកំណែស្តង់ដារ៖

| ស្តង់ដារ | តម្លៃ `__cplusplus` |
| --- | --- |
| C++98 / C++03 | `199711L` |
| C++11 | `201103L` |
| C++14 | `201402L` |
| C++17 | `201703L` |
| C++20 | `202002L` |
| C++23 | `202302L` |

```{literalinclude} ../../examples/getting-started/history.cpp
:language: cpp
```

លទ្ធផលនៅពេលបកប្រែដោយ `-std=c++17`៖

```text
__cplusplus = 201703
structured bindings and if constexpr are available
```

:::{warning}
កម្មវិធីបកប្រែ MSVC មិនកំណត់ `__cplusplus` ត្រឹមត្រូវតាមលំនាំដើមទេ។
ត្រូវបន្ថែម `/Zc:__cplusplus` ដើម្បីឱ្យតម្លៃនេះត្រូវនឹងស្តង់ដារពិត។
MSVC ក៏មានម៉ាក្រូ `_MSVC_LANG` សម្រាប់គោលបំណងដូចគ្នាដែរ។
:::

## ហេតុអ្វីរឿងនេះសំខាន់សម្រាប់អ្នក

កូដដែលប្រើលក្ខណៈ C++17 នឹងមិនបកប្រែដោយ `-std=c++11` ឡើយ។
ពេលអ្នកឃើញកំហុសដូចជា «`if constexpr` only available with -std=c++17» នោះ
មានន័យថាអ្នកត្រូវប្ដូរស្តង់ដារនៅពេលបកប្រែ (មើល
[ការបកប្រែ និងការប្រតិបត្តិ](compile-and-run.md))។

## អានបន្ថែម

- [cppreference: C++ history](https://en.cppreference.com/w/cpp/language/history)
- [isocpp.org: The Standard](https://isocpp.org/std/the-standard)
- [WG21 — គណៈកម្មាធិការស្តង់ដារ](https://www.open-std.org/jtc1/sc22/wg21/)
