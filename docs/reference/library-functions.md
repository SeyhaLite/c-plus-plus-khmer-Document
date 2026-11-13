# អនុគមន៍បណ្ណាល័យស្តង់ដារ

```{translation-meta} reference/library-functions
```

បណ្ណាល័យស្តង់ដារ C++ ផ្ដល់អនុគមន៍ជាច្រើនសម្រាប់ការងារទូទៅ។
ខាងក្រោមគឺជាបញ្ជីអនុគមន៍ដែលប្រើញឹកញាប់បំផុត។

## ការប្រៀបធៀប និងការផ្លាស់ប្ដូរ

- `std::max(a, b)`, `std::min(a, b)` — តម្លៃធំ/តូចបំផុត។
- `std::clamp(v, lo, hi)` (C++17) — កំណត់តម្លៃក្នុងចន្លោះ។
- `std::swap(a, b)` — ផ្លាស់ប្ដូរតម្លៃ។

## ការបំប្លែងប្រភេទ

- `std::to_string(value)` — លេខទៅខ្សែអក្សរ។
- `std::stoi`, `std::stol`, `std::stod` — ខ្សែអក្សរទៅលេខ។
- `static_cast<T>(x)`, `dynamic_cast`, `const_cast`, `reinterpret_cast`។

## អាល់ហ្គោរីតទូទៅ

- `std::sort`, `std::stable_sort`, `std::partial_sort`។
- `std::find`, `std::find_if`, `std::binary_search`។
- `std::transform`, `std::copy`, `std::copy_if`។
- `std::accumulate`, `std::reduce` (C++17)។

## ឧបករណ៍ជួរ

- `std::begin(c)`, `std::end(c)` — អ្នកដើរកាត់ដំបូង/ចុងក្រោយ។
- `std::size(c)` (C++17) — ចំនួនធាតុ។
- `std::empty(c)` (C++17) — ទទេឬអត់។

## ខ្សែអក្សរ

- `std::getline(stream, line)` — អានមួយបន្ទាត់។
- `std::to_string`, `std::stoi` ជាដើម។

:::{note}
បញ្ជីពេញលេញសម្រាប់ស្តង់ដារនីមួយៗ សូមមើល
[cppreference: standard library](https://en.cppreference.com/w/cpp/standard_library)។
:::

## កូដឧទាហរណ៍

```{literalinclude} ../../examples/reference/library-functions.cpp
:language: cpp
```

លទ្ធផល៖

```text
max(3,7): 7
min(3,7): 3
clamp(10,0,5): 5
swapped: 2 1
to_string: 42
size: 5
```

## អានបន្ថែម

- [cppreference: algorithms](https://en.cppreference.com/w/cpp/algorithm)
- [cppreference: `<utility>`](https://en.cppreference.com/w/cpp/header/utility)
- [cppreference: string conversions](https://en.cppreference.com/w/cpp/string/basic_string/to_string)
