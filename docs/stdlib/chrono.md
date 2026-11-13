# ពេលវេលា (std::chrono)

```{translation-meta} stdlib/chrono
```

`std::chrono` ផ្ដល់ប្រភេទសម្រាប់ពេលវេលា និងរយៈពេល ដែលមានសុវត្ថិភាពប្រភេទ។
វាមានតាំងពី **C++11** ក្នុងឯកសារក្បាល `<chrono>`។

## រយៈពេល (durations)

```cpp
using namespace std::chrono;
seconds s{2};
minutes m{1};
auto total = m + s;          // 62 វិនាទី
total.count();               // 62
```

`std::chrono::duration` រក្សាទុកចំនួន និង ratio។ ការប្រតិបត្តិការរវាងរយៈពេល
ដែលមានឯកតាផ្សេងគ្នា ត្រូវបំប្លែងដោយស្វ័យប្រវត្តិ បើអាចបំប្លែងបាន។

## នាឡិកា (clocks)

| នាឡិកា | អត្ថន័យ |
| --- | --- |
| `std::chrono::system_clock` | ពេលវេលាប្រព័ន្ធ (wall clock) |
| `std::chrono::steady_clock` | មិនថយក្រោយ សម្រាប់ការវាស់រយៈពេល |
| `std::chrono::high_resolution_clock` | កម្រិតខ្ពស់បំផុត |

```cpp
auto start = std::chrono::steady_clock::now();
// ... ការងារ ...
auto end = std::chrono::steady_clock::now();
auto ms = std::chrono::duration_cast<std::chrono::milliseconds>(end - start);
```

## time_point

`time_point` គឺជាពេលវេលាដែលចង្អុលដោយនាឡិកា។ ការដក `time_point` ពីរ
ផ្ដល់ `duration`។

## C++20៖ calendars និង time zones

ចាប់ពី **C++20** `std::chrono` គាំទ្រកាលប្បវត្តិ (calendars) និងតំបន់ពេលវេលា
(time zones)៖

```cpp
std::chrono::year_month_day today{std::chrono::floor<std::chrono::days>(
    std::chrono::system_clock::now())};
```

:::{note}
ការគាំទ្រ calendars/time zones ទាមទារកម្មវិធីបកប្រែ និងបណ្ណាល័យដែលគាំទ្រ C++20
ពេញលេញ (GCC 11+, Clang 13+ ជាមួយ libc++)។
:::

## កូដឧទាហរណ៍

```{literalinclude} ../../examples/stdlib/chrono.cpp
:language: cpp
```

លទ្ធផល៖

```text
elapsed ms >= 10: yes
total seconds: 62
```

## អានបន្ថែម

- [cppreference: `<chrono>`](https://en.cppreference.com/w/cpp/header/chrono)
- [cppreference: `std::chrono::duration`](https://en.cppreference.com/w/cpp/chrono/duration)
