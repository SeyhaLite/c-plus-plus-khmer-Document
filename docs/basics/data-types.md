# ប្រភេទទិន្នន័យ (Data Types)

```{translation-meta} basics/data-types
```

C++ ជាភាសាដែលមានប្រភេទទិន្នន័យច្បាស់លាស់។ រាល់អថេរត្រូវមានប្រភេទកំណត់ ហើយប្រភេទនោះ
កំណត់ថាតើទិន្នន័យបែបណាត្រូវផ្ទុក និងប្រតិបត្តិការអ្វីដែលអាចធ្វើបាន។

## ប្រភេទមូលដ្ឋាន (fundamental types)

| ប្រភេទ | អត្ថន័យ | ឧទាហរណ៍ |
| --- | --- | --- |
| `bool` | ពិត/មិនពិត | `true`, `false` |
| `char` | តួអក្សរមួយ | `'A'` |
| `int` | ចំនួនគត់ | `42`, `-7` |
| `unsigned int` | ចំនួនគត់មិនអវិជ្ជមាន | `42u` |
| `long`, `long long` | ចំនួនគត់ធំជាង | `42L`, `42LL` |
| `float` | ចំនុចអណ្តែតច្បាស់តិច | `3.14f` |
| `double` | ចំនុចអណ្តែតច្បាស់ជាង | `3.14` |
| `long double` | ចំនុចអណ្តែតធំបំផុត | `3.14L` |
| `void` | គ្មានតម្លៃ | ប្រភេទត្រឡប់នៃអនុគមន៍គ្មានតម្លៃ |

## ទំហំមិនត្រូវបានធានាទេ

ស្តង់ដារ C++ កំណត់តែទំហំអប្បបរមា មិនកំណត់ទំហំពិតប្រាកដទេ។
ឧទាហរណ៍ `int` មានយ៉ាងតិច 16 bit ប៉ុន្តែនៅកុំព្យូទ័រទំនើបភាគច្រើនវាមាន 32 bit។
ដូច្នេះកុំសន្និដ្ឋានថា `int` មាន 32 bit ជានិច្ច។

បើអ្នកត្រូវការទំហំច្បាស់លាស់ សូមប្រើប្រភេទពី `<cstdint>`៖

```cpp
#include <cstdint>

std::int32_t  a = 100;   // 32 bit ជានិច្ច
std::uint64_t b = 100u;  // 64 bit មិនអវិជ្ជមាន
```

## ការពិនិត្យទំហំដោយ `sizeof`

ប្រមាណវិធី `sizeof` ត្រឡប់ទំហំជា byte (1 byte = 8 bit ក្នុង C++)។
តម្លៃត្រឡប់មានប្រភេទ `std::size_t`។

```{literalinclude} ../../examples/basics/data-types.cpp
:language: cpp
```

លទ្ធផលនៅលើប្រព័ន្ធ 64-bit ធម្មតា (ឧទាហរណ៍ Linux x86-64 ជាមួយ GCC)៖

```text
sizeof(bool) = 1
sizeof(char) = 1
sizeof(int) = 4
sizeof(double) = 8
sizeof(long) = 8
```

:::{warning}
លទ្ធផលខាងលើអាចខុសគ្នាតាមប្រព័ន្ធ។ នៅ Windows 64-bit `sizeof(long)` គឺ `4`។
នេះជាហេតុផលដែលអ្នកមិនគួរសរសេរកូដពឹងលើទំហំជាក់លាក់ដោយមិនពិនិត្យ។
:::

## ជួរតម្លៃ និងការហូរលើស (overflow)

ចំនួនគត់ដែលមានសញ្ញា (signed) មានជួរកំណត់។ បើតម្លៃលើសជួរ ឥរិយាបថគឺ
**មិនកំណត់** (undefined behavior) សម្រាប់ signed integer។

```cpp
int big = 2147483647;   // INT_MAX នៅប្រព័ន្ធ 32-bit int
// big + 1  ->  undefined behavior  (កុំធ្វើ!)
```

ចំណែក unsigned integer វិលត្រឡប់ (wrap around) តាមលក្ខណៈកំណត់៖
`0u - 1u` ស្មើនឹងតម្លៃធំបំផុតរបស់ប្រភេទនោះ។

## `bool` និង `char`

`bool` មានតម្លៃតែ `true` ឬ `false`។ តម្លៃលេខណាមួយដែលមិនមែនសូន្យបំប្លែងជា `true`។

`char` ផ្ទុកតួអក្សរមួយ ដែលពិតប្រាកដគឺលេខតូចមួយ។ សម្រាប់អក្សរខ្មែរ ត្រូវប្រើ
`std::string` (UTF-8) ឬ `std::u32string` ព្រោះតួអក្សរខ្មែរមួយអាចប្រើច្រើន byte
ក្នុង UTF-8។

## អានបន្ថែម

- [cppreference: types](https://en.cppreference.com/w/cpp/language/types)
- [cppreference: `<cstdint>`](https://en.cppreference.com/w/cpp/header/cstdint)
