# ជួរ (std::ranges)

```{translation-meta} stdlib/ranges
```

`std::ranges` គឺជាបណ្ណាល័យថ្មីក្នុង **C++20** ដែលផ្ដល់ទិដ្ឋភាពស្រស់ស្អាត
នៃអាល់ហ្គោរីត និង views ដែលអាចបញ្ចូលគ្នាបាន (composable)។ វាកាត់បន្ថយ
ការប្រើអ្នកដើរកាត់ដោយដៃ។

## views

View គឺជាទិដ្ឋភាពទៅជួរដែលមិនចម្លងទិន្នន័យ។ វាធ្វើការ «តាមតម្រូវការ» (lazy)៖

```cpp
auto even = values | std::views::filter([](int x) { return x % 2 == 0; });
auto doubled = values | std::views::transform([](int x) { return x * 2; });
```

## ការបញ្ចូល views (pipelines)

```cpp
auto result = values
    | std::views::filter([](int x) { return x % 2 == 0; })
    | std::views::transform([](int x) { return x * 2; })
    | std::views::take(3);
```

ជួរដើមមិនត្រូវបានផ្លាស់ប្ដូរទេ។ ធាតុត្រូវបានគណនាបន្ទាប់ពីបញ្ចូល views។ Views មិនចម្លងទិន្នន័យទេ ដូច្នេះវាអាចប្រើជាមួយជួរដ៏ធំបានដោយគ្មានការចំណាយអង្គចងចាំបន្ថែម។

## អាល់ហ្គោរីត ranges

```cpp
std::ranges::sort(values);
std::ranges::find(values, 8);
int n = std::ranges::count_if(values, [](int x) { return x > 0; });
```

អាល់ហ្គោរីតទាំងនេះទទួល `range` ដោយផ្ទាល់ មិនចាំបាច់ `.begin()/.end()`។

## កូដឧទាហរណ៍

```{literalinclude} ../../examples/stdlib/ranges.cpp
:language: cpp
```

លទ្ធផល៖

```text
2 4 6
2 4 6
count even: 3
```

## អានបន្ថែម

- [cppreference: ranges](https://en.cppreference.com/w/cpp/ranges)
- [cppreference: `std::views`](https://en.cppreference.com/w/cpp/ranges#Range_adaptors)
- [cppreference: `<ranges>`](https://en.cppreference.com/w/cpp/header/ranges)
