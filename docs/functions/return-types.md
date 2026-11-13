# ប្រភេទតម្លៃត្រឡប់ (Return Types)

```{translation-meta} functions/return-types
```

ប្រភេទតម្លៃត្រឡប់ (return type) កំណត់ប្រភេទទិន្នន័យដែលអនុគមន៍ផ្ដល់ត្រឡប់ទៅអ្នកហៅ។

## `void`

```cpp
void log_message(const std::string& text) {
    std::cout << text << '\n';
    // គ្មាន return តម្លៃ
}
```

## តម្លៃតែមួយ

```cpp
int add(int a, int b) {
    return a + b;
}
```

## `auto` និង trailing return type

ចាប់ពី **C++11** អ្នកអាចឱ្យកម្មវិធីបកប្រែសន្និដ្ឋានប្រភេទត្រឡប់ពី `return`៖

```cpp
auto add(int a, int b) {
    return a + b;      // -> int
}
```

ឬសរសេរប្រភេទច្បាស់នៅខាងក្រោយ (trailing return type)៖

```cpp
auto add(int a, int b) -> int {
    return a + b;
}
```

ទម្រង់ trailing មានប្រយោជន៍នៅពេលប្រភេទត្រឡប់អាស្រ័យលើប៉ារ៉ាម៉ែត្រ
(សម្រាប់ពុម្ព)។

## តម្លៃច្រើនតាមរយៈ struct ឬ pair

C++ មិនអាចត្រឡប់តម្លៃច្រើនដោយផ្ទាល់បានទេ។ គេប្រើ `std::pair`
ឬ `struct` (ឬ `std::tuple`)។

```cpp
#include <utility>

std::pair<int, int> minmax(int a, int b) {
    if (a < b) {
        return {a, b};
    }
    return {b, a};
}
```

ចាប់ពី **C++17** អ្នកអាចបំបែកតម្លៃដោយ structured bindings៖

```cpp
auto [lo, hi] = minmax(9, 4);
```

## `[[nodiscard]]` (C++17)

```cpp
[[nodiscard]] int compute();
```

បើអ្នកហៅ `compute();` ហើយមិនប្រើតម្លៃត្រឡប់ កម្មវិធីបកប្រែនឹងព្រមាន។
នេះមានប្រយោជន៍សម្រាប់អនុគមន៍ដែលគ្មានផលរំខានផ្សេង (no side effect)។

:::{warning}
ការត្រឡប់យោង (reference) ទៅអថេរមូលដ្ឋានជាកំហុសធ្ងន់ធ្ងរ៖

```cpp
int& bad() {
    int local = 5;
    return local;   // local ត្រូវបំផ្លាញនៅចុងអនុគមន៍
}
```

ការប្រើតម្លៃត្រឡប់នោះគឺជាឥរិយាបថមិនកំណត់។
:::

## កូដឧទាហរណ៍

```{literalinclude} ../../examples/functions/return-types.cpp
:language: cpp
```

លទ្ធផល៖

```text
add = 5
lo = 4, hi = 9
important = 42
```

## អានបន្ថែម

- [cppreference: functions](https://en.cppreference.com/w/cpp/language/function)
- [cppreference: `return` statement](https://en.cppreference.com/w/cpp/language/return)
