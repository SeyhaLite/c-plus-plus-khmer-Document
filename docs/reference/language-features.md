# លក្ខណៈភាសាតាមស្តង់ដារ

```{translation-meta} reference/language-features
```

C++ បន្ថែមលក្ខណៈថ្មីនៅស្តង់ដារនីមួយៗ។ ទំព័រនេះសង្ខេបលក្ខណៈសំខាន់ៗ
តាមស្តង់ដារ។

## C++11

- `auto`, `decltype` — ការសន្និដ្ឋានប្រភេទ។
- range-based for — `for (auto& x : container)`។
- lambda — `[](int x) { return x * 2; }`។
- `nullptr` — ពោយន្ត័រទទេប្រភេទសុវត្ថិភាព។
- `constexpr`, `noexcept`។
- smart pointers, move semantics, threads, atomics។

## C++14

- generic lambdas, auto return type។
- `std::make_unique`។
- variable templates, `decltype(auto)`។

## C++17

- structured bindings — `auto [a, b] = pair;`។
- `if constexpr`, fold expressions។
- `std::optional`, `std::variant`, `std::any`។
- `std::string_view`, `std::filesystem`។
- inline variables, nested namespaces។

## C++20

- concepts, ranges, coroutines, modules (មើលទំព័រ rieng)។
- `consteval`, `constinit`។
- `std::format` (បណ្ណាល័យ)។
- spaceship operator `<=>`។
- designated initializers (មួយផ្នែក)។

## C++23

- `std::print`, `std::println`។
- `std::expected`, `std::generator` (C++23)។
- `std::flat_map`, `std::mdspan`។
- deducing `this` (explicit object parameter)។

## C++26 (ព្រាង)

- contracts, reflection (ព្រាង)។
- `std::execution` (sender/receiver) (ព្រាង)។

:::{note}
លក្ខណៈ C++26 នៅជា **ព្រាង** (draft)។ កម្មវិធីបកប្រែភាគច្រើនមិនគាំទ្រពេញលេញទេ។
សូមពិនិត្យកម្មវិធីបកប្រែរបស់អ្នកសម្រាប់ការគាំទ្រពិតប្រាកដ។
:::

ការជ្រើសរើសស្តង់ដារអប្បបរមាដែលត្រូវការ ជួយឱ្យកូដអាច compile បាននៅ
កម្មវិធីបកប្រែចាស់ និងថ្មី។ គួរប្រើ `-std=c++17` ឬ `-std=c++20` សម្រាប់
គម្រោងថ្មី។

## កូដឧទាហរណ៍

```{literalinclude} ../../examples/reference/language-features.cpp
:language: cpp
```

លទ្ធផល៖

```text
sum: 6 square(4): 16
structured binding ok
optional: 7
constexpr: 25
```

## អានបន្ថែម

- [cppreference: C++11](https://en.cppreference.com/w/cpp/11)
- [cppreference: C++14](https://en.cppreference.com/w/cpp/14)
- [cppreference: C++17](https://en.cppreference.com/w/cpp/17)
- [cppreference: C++20](https://en.cppreference.com/w/cpp/20)
- [cppreference: C++23](https://en.cppreference.com/w/cpp/23)
