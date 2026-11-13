# ពាក្យគន្លឹះ (Keywords)

```{translation-meta} reference/keywords
```

ពាក្យគន្លឹះ (keyword) គឺជាពាក្យដែលភាសា C++ រក្សាទុកសម្រាប់ប្រើប្រាស់ពិសេស។
អ្នកមិនអាចប្រើវាជាឈ្មោះអថេរ អនុគមន៍ ឬថ្នាក់បានទេ។ ពាក្យគន្លឹះគឺ
case-sensitive ហើយមិនអាច override បាន។

## ប្រភេទទិន្នន័យ

`bool`, `char`, `char8_t`, `char16_t`, `char32_t`, `wchar_t`, `short`, `int`,
`long`, `signed`, `unsigned`, `float`, `double`, `void`, `auto`, `decltype`,
`nullptr_t` (តាមរយៈ `nullptr`)។

## ការគ្រប់គ្រងលំហូរ

`if`, `else`, `switch`, `case`, `default`, `for`, `while`, `do`, `break`,
`continue`, `return`, `goto`, `co_await`, `co_return`, `co_yield`។

## អនុគមន៍ និងថ្នាក់

`inline`, `constexpr`, `consteval`, `constinit`, `virtual`, `override`, `final`,
`static`, `extern`, `friend`, `explicit`, `mutable`, `const`, `volatile`,
`noexcept`, `operator`, `template`, `typename`, `concept`, `requires`។

## ការគ្រប់គ្រងអង្គចងចាំ

`new`, `delete`, `this`, `sizeof`, `alignof`, `alignas`, `static_cast`,
`dynamic_cast`, `const_cast`, `reinterpret_cast`។

## ករណីលើកលែង និងការប្រកាស

`try`, `catch`, `throw`, `namespace`, `using`, `class`, `struct`, `union`,
`enum`, `typedef`, `public`, `private`, `protected`។

:::{note}
បញ្ជីពេញលេញ និងព័ត៌មានលម្អិតសម្រាប់ស្តង់ដារនីមួយៗ សូមមើល
[cppreference: keywords](https://en.cppreference.com/w/cpp/keyword)។
:::

ពាក្យគន្លឹះថ្មីត្រូវបន្ថែមនៅស្តង់ដារនីមួយៗ ដូច្នេះកូដដែលសរសេរសម្រាប់ C++11
អាចប្រើពាក្យដែលមិនមាននៅ C++98 បាន។ ការប្រើពាក្យគន្លឹះជាឈ្មោះអថេរ
នឹងធ្វើឱ្យកម្មវិធីបកប្រែបដិសេធភ្លាម។

## កូដឧទាហរណ៍

```{literalinclude} ../../examples/reference/keywords.cpp
:language: cpp
```

លទ្ធផល៖

```text
value: 25
doubled: 50
tripled: 75
is int: 1
static_assert passed
```

## អានបន្ថែម

- [cppreference: keywords](https://en.cppreference.com/w/cpp/keyword)
- [cppreference: `constexpr`](https://en.cppreference.com/w/cpp/language/constexpr)
