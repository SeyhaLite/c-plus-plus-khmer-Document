# ឧបករណ៍ប្រើប្រាស់ (Utilities)

```{translation-meta} stdlib/utilities
```

បណ្ណាល័យឧបករណ៍ប្រើប្រាស់ (utilities) ផ្ដល់ប្រភេទ និងអនុគមន៍ទូទៅដែលប្រើ
ទូទាំងបណ្ណាល័យស្តង់ដារ។

## ប្រភេទសំខាន់ៗ

- `std::pair<T1, T2>` — គូតម្លៃពីរ។
- `std::tuple<...>` — តូប៉ូលតម្លៃច្រើន។
- `std::optional<T>` (C++17) — តម្លៃដែលអាច «គ្មាន» បាន។
- `std::variant<Ts...>` (C++17) — តម្លៃដែលអាចជាប្រភេទណាមួយក្នុងចំណោមប្រភេទទាំងនោះ។
- `std::any` (C++17) — តម្លៃប្រភេទណាមួយ (type-erased)។

## `std::optional`

```cpp
std::optional<int> find(int key) {
    if (key == 42) return 42;
    return std::nullopt;
}

auto result = find(42);
if (result) {
    std::cout << *result << '\n';
}
```

ប្រើ `std::optional` ជំនួស «តម្លៃពិសេស» ដូចជា -1 ឬ nullptr ដើម្បីបង្ហាញ
ថាលទ្ធផលមិនមាន។ ការប្រើ `std::optional` និង `std::variant` ធ្វើឱ្យកូដទូទៅមានសុវត្ថិភាពជាងការប្រើ pointer ឬតម្លៃពិសេស។

## `std::variant`

```cpp
std::variant<int, std::string> value = "hello";
if (std::holds_alternative<std::string>(value)) {
    std::cout << std::get<std::string>(value) << '\n';
}
```

`std::visit` អនុញ្ញាតឱ្យអ្នកគ្រប់គ្រងគ្រប់ប្រភេទដែលអាចកើតមាន ក្នុងពេលបកប្រែ៖

```cpp
std::visit([](auto&& v) { std::cout << v << '\n'; }, value);
```

## structured bindings (C++17)

```cpp
std::pair<int, std::string> p{1, "one"};
auto [id, name] = p;      // បំបែកជាអថេរពីរ
```

## កូដឧទាហរណ៍

```{literalinclude} ../../examples/stdlib/utilities.cpp
:language: cpp
```

លទ្ធផល៖

```text
1 one
bound: 1 one
optional: 42
empty has value: no
variant holds string: 1
```

## អានបន្ថែម

- [cppreference: `<utility>`](https://en.cppreference.com/w/cpp/header/utility)
- [cppreference: `std::optional`](https://en.cppreference.com/w/cpp/utility/optional)
- [cppreference: `std::variant`](https://en.cppreference.com/w/cpp/utility/variant)
- [cppreference: `std::tuple`](https://en.cppreference.com/w/cpp/utility/tuple)
