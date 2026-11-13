# ថេរ និង constexpr

```{translation-meta} basics/constants
```

ថេរ (constant) គឺជាតម្លៃដែលមិនអាចផ្លាស់ប្តូរបាន។ ការប្រើថេរធ្វើឱ្យកូដអានងាយ
និងជួយកម្មវិធីបកប្រែចាប់កំហុសពេលអ្នកព្យាយាមកែតម្លៃដោយអចេតនា។

## `const`

`const` ប្រាប់ថាតម្លៃមិនអាចកែបានបន្ទាប់ពីចាប់ផ្ដើម៖

```cpp
const int max_attempts = 3;
// max_attempts = 5;   // កំហុសពេលបកប្រែ
```

`const` មានតាំងពី C++98។ វាអាចប្រើបានទាំងអថេរក្នុងអនុគមន៍ និងប៉ារ៉ាម៉ែត្រ
(ដើម្បីបង្ហាញថាអនុគមន៍មិនកែប៉ារ៉ាម៉ែត្រនោះ)។

## `constexpr`

ចាប់ពី **C++11** `constexpr` មានន័យថា «អាចគណនានៅពេលបកប្រែ»។
វាខ្លាំងជាង `const`៖ តម្លៃត្រូវដឹងនៅពេលបកប្រែ ដូច្នេះវាអាចប្រើជាទំហំអារេ
ឬក្នុងបរិបទដែលត្រូវការតម្លៃថេរពិតប្រាកដ។

```cpp
constexpr int buffer_size = 256;
int buffer[buffer_size];   // បាន ព្រោះជាតម្លៃថេរនៅពេលបកប្រែ
```

`constexpr` ក៏អាចប្រើលើអនុគមន៍បានដែរ៖

```cpp
constexpr int square(int x) { return x * x; }

constexpr int area = square(5);   // គណនានៅពេលបកប្រែ
```

## ភាពខុសគ្នារវាង `const` និង `constexpr`

| ទិដ្ឋភាព | `const` | `constexpr` |
| --- | --- | --- |
| មិនអាចកែតម្លៃ | បាទ | បាទ |
| ត្រូវដឹងតម្លៃនៅពេលបកប្រែ | មិនចាំបាច់ | បាទ |
| មានតាំងពី | C++98 | C++11 |

```cpp
int read_value();                 // អនុគមន៍ខាងក្រៅ
const int a = read_value();       // បាន — តម្លៃដឹងពេលដំណើរការ
// constexpr int b = read_value(); // មិនបាន — មិនមែនតម្លៃថេរពេលបកប្រែ
```

## `consteval` និង `constinit` (C++20)

C++20 បន្ថែម `consteval` សម្រាប់អនុគមន៍ដែល **ត្រូវ** គណនានៅពេលបកប្រែ
និង `constinit` សម្រាប់ធានាការចាប់ផ្ដើមតម្លៃនៅពេលបកប្រែ។
លក្ខណៈទាំងនេះជារបស់ C++20 ហើយត្រូវការកម្មវិធីបកប្រែថ្មី។

:::{note}
របៀបចាស់ដែលគេប្រើគឺ `#define MAX 3`។ វាមិនមានប្រភេទ និងមិនគោរពវិសាលភាព
ដូច្នេះយើងមិនណែនាំវាសម្រាប់តម្លៃថេរធម្មតាឡើយ។ សូមប្រើ `constexpr` ជំនួស។
:::

## កូដឧទាហរណ៍

```{literalinclude} ../../examples/basics/constants.cpp
:language: cpp
```

លទ្ធផល៖

```text
circle area = 78.5398
max attempts = 3
```

## អានបន្ថែម

- [cppreference: cv qualifiers](https://en.cppreference.com/w/cpp/language/cv)
- [cppreference: `constexpr`](https://en.cppreference.com/w/cpp/language/constexpr)
- [cppreference: constant expressions](https://en.cppreference.com/w/cpp/language/constant_expression)
