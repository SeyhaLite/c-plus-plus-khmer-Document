# យោង (References)

```{translation-meta} advanced/references
```

យោង (Reference) គឺជាឈ្មោះផ្សេងសម្រាប់វត្ថុដែលមានស្រាប់។ វាមិនចម្លងទិន្នន័យទេ
ហើយមិនអាចផ្លាស់ប្តូរទៅចង្អុលវត្ថុផ្សេងបានឡើយ។

## ភាពខុសគ្នាពីពោយន្ត័រ

| ទិដ្ឋភាព | យោង | ពោយន្ត័រ |
| --- | --- | --- |
| ត្រូវចាប់ផ្ដើមតម្លៃ | បាទ ជានិច្ច | មិនចាំបាច់ |
| អាចផ្លាស់ទៅវត្ថុផ្សេង | ទេ | បាទ |
| អាចជា `nullptr` | ទេ | បាទ |
| ត្រូវការ dereference | ទេ (ប្រើដូចអថេរធម្មតា) | បាទ (`*p`) |

## ការប្រកាស

```cpp
int number = 10;
int& alias = number;   // alias ជាឈ្មោះផ្សេងរបស់ number

alias += 5;            // number ក្លាយជា 15
```

## យោងជាប៉ារ៉ាម៉ែត្រ

នេះជាការប្រើប្រាស់ញឹកញាប់បំផុត៖ អនុគមន៍អាចកែអាគុយម៉ង់របស់អ្នកហៅ
ដោយមិនចាំបាច់ប្រើពោយន្ត័រ៖

```cpp
void scale(int& value, int factor) {
    value *= factor;
}
```

ដើម្បីជៀសវាងការចម្លងវត្ថុធំ ដោយមិនចង់កែតម្លៃ សូមប្រើយោងថេរ៖

```cpp
void print(const std::string& text);
```

## យោង និងរង្វិលជុំ

```cpp
for (int& value : values) {
    value *= 2;      // កែធាតុពិតក្នុងអារេ
}
```

ប្រើ `const auto&` នៅពេលអានតែប៉ុណ្ណោះ ដើម្បីកុំចម្លងធាតុនីមួយៗ។

:::{warning}
**យោងខូច (dangling reference)។** បើវត្ថុដែលយោងចង្អុលទៅត្រូវបំផ្លាញ នោះយោងនោះ
មិនអាចប្រើបានទៀតទេ ហើយការប្រើវាគឺជាឥរិយាបថមិនកំណត់៖

```cpp
int& bad() {
    int local = 5;
    return local;    // local ត្រូវបំផ្លាញនៅចុងអនុគមន៍
}
```
:::

## កូដឧទាហរណ៍

```{literalinclude} ../../examples/advanced/references.cpp
:language: cpp
```

លទ្ធផល៖

```text
number: 15
scaled: 30
text: hello
values: 246
```

## យោង ឬពោយន្ត័រ?

- បើវត្ថុត្រូវមានជានិច្ច → យោង។ វាមិនអាចជា null ដូច្នេះកូដកាន់តែច្បាស់។
- បើអាច «គ្មានវត្ថុ» → ពោយន្ត័រ (`nullptr`) ឬ `std::optional`។
- បើត្រូវផ្លាស់ចង្អុលទៅវត្ថុផ្សេង → ពោយន្ត័រ។

## អានបន្ថែម

- [cppreference: reference declaration](https://en.cppreference.com/w/cpp/language/reference)
