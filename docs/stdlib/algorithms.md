# អាល់ហ្គោរីត (Algorithms)

```{translation-meta} stdlib/algorithms
```

អាល់ហ្គោរីតស្តង់ដារ (standard algorithms) គឺជាអនុគមន៍ទូទៅដែលដំណើរការលើជួរ
(range) តាមរយៈអ្នកដើរកាត់។ វាមានក្នុងឯកសារក្បាល `<algorithm>` និង `<numeric>`។

## ការរៀបចំ និងការស្វែងរក

```cpp
std::sort(values.begin(), values.end());
std::sort(values.begin(), values.end(), std::greater<>{});

auto it = std::find(values.begin(), values.end(), 8);
bool has = std::binary_search(values.begin(), values.end(), 8);
```

`std::binary_search` ត្រូវការជួរដែលបានរៀបចំរួច។ ការជ្រើសរើសអាល់ហ្គោរីតត្រឹមត្រូវ ជំនួសការសរសេរ loop ដោយដៃ ធ្វើឱ្យកូដអានយល់ងាយ និងមានកំហុសតិចជាង។

## ការផ្លាស់ប្ដូរ

```cpp
std::transform(in.begin(), in.end(), out.begin(), [](int x) { return x * 2; });
std::copy_if(in.begin(), in.end(), std::back_inserter(out), [](int x) { return x > 0; });
std::remove_if(values.begin(), values.end(), [](int x) { return x < 0; });
```

:::{note}
`std::remove` និង `std::remove_if` មិនលុបធាតុពីធុងទេ — វាគ្រាន់តែផ្លាស់ទី
ធាតុដែលត្រូវលុបទៅចុង ហើយត្រឡប់អ្នកដើរកាត់ថ្មី។ ដើម្បីលុបពិតប្រាកដ ត្រូវប្រើ
`erase-remove idiom`៖

```cpp
values.erase(std::remove(values.begin(), values.end(), 0), values.end());
```
:::

## ការបូក និងការគណនា

```cpp
int sum = std::accumulate(values.begin(), values.end(), 0);
std::iota(values.begin(), values.end(), 1);   // 1, 2, 3, ...
```

## កូដឧទាហរណ៍

```{literalinclude} ../../examples/stdlib/algorithms.cpp
:language: cpp
```

លទ្ធផល៖

```text
1 2 5 8 9
found 8: yes
sum: 50
gt10 count: 2
```

## អានបន្ថែម

- [cppreference: algorithms](https://en.cppreference.com/w/cpp/algorithm)
- [cppreference: `std::sort`](https://en.cppreference.com/w/cpp/algorithm/sort)
- [cppreference: `<numeric>`](https://en.cppreference.com/w/cpp/header/numeric)
