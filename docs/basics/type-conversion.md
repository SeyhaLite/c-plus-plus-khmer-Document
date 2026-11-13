# ការបំប្លែងប្រភេទ (Type Conversion)

```{translation-meta} basics/type-conversion
```

ការបំប្លែងប្រភេទ (Type Conversion) គឺជាការប្ដូរតម្លៃពីប្រភេទមួយទៅប្រភេទមួយទៀត។
C++ ធ្វើការបំប្លែងខ្លះដោយស្វ័យប្រវត្តិ ហើយខ្លះទៀតត្រូវសរសេរដោយច្បាស់លាស់។

## ការបំប្លែងដោយស្វ័យប្រវត្តិ (implicit conversion)

```cpp
int count = 7;
double average = count / 2.0;   // int បំប្លែងជា double ដោយស្វ័យប្រវត្តិ
```

ការបំប្លែងទិសដៅ «តូចទៅធំ» (ឧទាហរណ៍ `int` → `double`) មានសុវត្ថិភាពជាធម្មតា។
ចំណែកទិសដៅ «ធំទៅតូច» (ឧទាហរណ៍ `double` → `int`) បាត់បង់ទិន្នន័យ៖

```cpp
double price = 9.99;
int truncated = price;   // 9  — ផ្នែកទសភាគត្រូវបាត់
```

## ការបំប្លែងដែលគ្រោះថ្នាក់

**សញ្ញា (signedness)។** ការលាយ `int` អវិជ្ជមានជាមួយ `unsigned int` អាចផ្ដល់
លទ្ធផលដែលមិនគួរឱ្យជឿ៖

```cpp
int a = -1;
unsigned int b = 1;
bool less = a < b;   // ជាធម្មតា false! ព្រោះ a បំប្លែងជា unsigned ធំ
```

កម្មវិធីបកប្រែជាច្រើនព្រមានអំពីរឿងនេះដោយ `-Wsign-compare`។ សូមអានការព្រមាន។

**ការបំប្លែងខុសចន្លោះប្រភេទ។** ការបំប្លែងតម្លៃដែលលើសជួររបស់ប្រភេទគោលដៅ
(ឧទាហរណ៍ `int` ធំទៅ `char`) អាចបង្កើតតម្លៃមិនកំណត់ ឬលទ្ធផលមិនត្រឹមត្រូវ។

## ការបំប្លែងដោយច្បាស់លាស់ (explicit cast)

C++ ផ្ដល់ cast បួនប្រភេទ ដែលអានងាយជាង C-style cast និងអាចស្វែងរកបានក្នុងកូដ៖

| Cast | ប្រើសម្រាប់ |
| --- | --- |
| `static_cast<T>(x)` | ការបំប្លែងធម្មតាដែលគេដឹងនៅពេលបកប្រែ |
| `dynamic_cast<T>(x)` | ការបំប្លែងក្នុងឋានានុក្រមថ្នាក់ដែលមានអនុគមន៍និម្មិត |
| `const_cast<T>(x)` | ដក ឬបន្ថែម `const` |
| `reinterpret_cast<T>(x)` | បកស្រាយ bit ឡើងវិញ (គ្រោះថ្នាក់) |

```cpp
int a = 7;
int b = 2;
double ratio = static_cast<double>(a) / b;   // 3.5
```

:::{warning}
សូមជៀសវាង C-style cast ដូចជា `(double)a`។ វាអាចលាក់ការបំប្លែងដែលមិនសុវត្ថិភាព
ហើយឧបករណ៍ស្វែងរកកូដមិនអាចរកវាបានងាយ។ សូមប្រើ `static_cast` ជាដើម។
:::

## ការបំប្លែងខ្សែអក្សរ និងលេខ

```cpp
#include <string>

std::string text = std::to_string(42);        // "42"
int value = std::stoi("123");                 // 123
double pi = std::stod("3.14");                // 3.14
```

`std::to_string` មានតាំងពី **C++11**។ `std::stoi` បោះ `std::invalid_argument`
បើខ្សែអក្សរមិនមែនលេខ (ផ្នែក [ករណីលើកលែង](../advanced/index.md) នឹងពន្យល់លម្អិតនៅពេលបកប្រែរួច)។

## កូដឧទាហរណ៍

```{literalinclude} ../../examples/basics/type-conversion.cpp
:language: cpp
```

លទ្ធផល៖

```text
integer division: 3
double division: 3.5
truncated: 9
bool from 42: 1
```

## អានបន្ថែម

- [cppreference: implicit conversions](https://en.cppreference.com/w/cpp/language/implicit_conversion)
- [cppreference: `static_cast`](https://en.cppreference.com/w/cpp/language/static_cast)
- [cppreference: explicit conversions](https://en.cppreference.com/w/cpp/language/explicit_cast)
