# ឯកសារក្បាលស្តង់ដារ (Standard Headers)

```{translation-meta} reference/headers
```

ឯកសារក្បាលស្តង់ដារ (standard header) ផ្ដល់ការប្រកាសសម្រាប់បណ្ណាល័យ C++។
អ្នករួមបញ្ចូលវាដោយ `#include <...>`។ ឯកសារក្បាលផ្ទាល់ខ្លួនប្រើ `"..."`។

## ឯកសារក្បាលសំខាន់ៗតាមប្រភេទ

| ប្រភេទ | ឯកសារក្បាល |
| --- | --- |
| ការបញ្ចូល/បញ្ចេញ | `<iostream>`, `<fstream>`, `<sstream>`, `<cstdio>` |
| ខ្សែអក្សរ | `<string>`, `<string_view>`, `<cstring>` |
| ធុងទិន្នន័យ | `<vector>`, `<map>`, `<set>`, `<array>`, `<deque>` |
| អាល់ហ្គោរីត | `<algorithm>`, `<numeric>`, `<iterator>` |
| ឧបករណ៍ | `<utility>`, `<tuple>`, `<optional>`, `<variant>`, `<any>` |
| ពេលវេលា/ឯកសារ | `<chrono>`, `<filesystem>` |
| ខ្សែស្រឡាយ | `<thread>`, `<mutex>`, `<atomic>`, `<future>` |
| ភាសា | `<concepts>`, `<coroutine>`, `<ranges>`, `<format>` |
| គណិត | `<cmath>`, `<complex>`, `<random>` |
| ប្រព័ន្ធ | `<cstdlib>`, `<csignal>`, `<csetjmp>`, `<new>` |

## ការរួមបញ្ចូលតែអ្វីដែលត្រូវការ

ការរួមបញ្ចូលឯកសារក្បាលច្រើនពេក អាចបង្កើនពេល compile។ ការរួមបញ្ចូលតែ
អ្វីដែលត្រូវការ ធ្វើឱ្យកូដស្អាត និង compile លឿនជាង។

:::{note}
ឯកសារក្បាលស្តង់ដារអាចរួមបញ្ចូលឯកសារក្បាលផ្សេងទៀតដោយស្វ័យប្រវត្តិ។
ដូច្នេះកុំពឹងផ្អែកលើវា — ត្រូវ `#include` ឯកសារក្បាលដែលអ្នកប្រើដោយផ្ទាល់។
:::

## កូដឧទាហរណ៍

```{literalinclude} ../../examples/reference/headers.cpp
:language: cpp
```

លទ្ធផល៖

```text
sorted: 1 2 3
sum: 6
filesystem header ok
```

## អានបន្ថែម

- [cppreference: headers](https://en.cppreference.com/w/cpp/header)
- [cppreference: standard library](https://en.cppreference.com/w/cpp/standard_library)
