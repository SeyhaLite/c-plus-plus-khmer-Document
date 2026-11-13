# ពោយន្ត័រ (Pointers)

```{translation-meta} advanced/pointers
```

ពោយន្ត័រ (Pointer) គឺជាអថេរដែលផ្ទុក **អាសយដ្ឋានអង្គចងចាំ** របស់វត្ថុផ្សេង។
ជំនួសឱ្យការផ្ទុកតម្លៃដោយផ្ទាល់ វាប្រាប់ថាតើតម្លៃនោះស្ថិតនៅទីណា។

## ប្រមាណវិធីពីរដែលត្រូវដឹង

| ប្រមាណវិធី | អត្ថន័យ |
| --- | --- |
| `&x` | យកអាសយដ្ឋានរបស់ `x` |
| `*p` | អាន ឬកែតម្លៃដែល `p` ចង្អុលទៅ (dereference) |

```cpp
int number = 41;
int* ptr = &number;    // ptr ផ្ទុកអាសយដ្ឋានរបស់ number
std::cout << *ptr;     // 41
*ptr = 42;             // កែ number តាមរយៈពោយន្ត័រ
```

## `nullptr`

ចាប់ពី **C++11** គេប្រើ `nullptr` សម្រាប់ពោយន្ត័រដែលមិនចង្អុលទៅអ្វី។
វាមានប្រភេទផ្ទាល់ខ្លួន `std::nullptr_t` ដូច្នេះវាមិនបង្កភាពមិនច្បាស់ដូច `0` ឬ `NULL` ទេ។

```cpp
int* nothing = nullptr;
if (nothing == nullptr) {
    // មិនចង្អុលទៅអ្វី
}
```

:::{warning}
ការ dereference ពោយន្ត័រ `nullptr` គឺជាឥរិយាបថមិនកំណត់ (undefined behavior)
ហើយជាធម្មតាធ្វើឱ្យកម្មវិធីគាំង។ សូមពិនិត្យពោយន្ត័រមុនប្រើជានិច្ច។
:::

## ពោយន្ត័រ និងអារេ

ឈ្មោះអារេរលាយទៅជាពោយន្ត័រទៅធាតុដំបូង (array decay) នៅក្នុងកន្សោមភាគច្រើន៖

```cpp
int values[] = {10, 20, 30};
int* cursor = values;      // ស្មើនឹង &values[0]

cursor[1];                 // 20
*(cursor + 1);             // 20 — ដូចគ្នា
```

`cursor + 1` មិនបូក 1 byte ទេ ប៉ុន្តែបូកមួយធាតុ (`sizeof(int)` byte)។
នេះជាហេតុផលដែលពោយន្ត័រត្រូវមានប្រភេទ។

## `const` និងពោយន្ត័រ

```cpp
int value = 5;

const int* a = &value;   // អានបាន កែមិនបាន (*a = 9 ខុស)
int* const b = &value;   // ពោយន្ត័រខ្លួនឯងថេរ (b = ... ខុស) ប៉ុន្តែ *b = 9 បាន
const int* const c = &value;   // ទាំងពីរថេរ
```

សូមអានពីស្ដាំទៅឆ្វេង៖ `int* const b` គឺ «ពោយន្ត័រថេរ ដែលចង្អុលទៅ int»។

## កូដឧទាហរណ៍

```{literalinclude} ../../examples/advanced/pointers.cpp
:language: cpp
```

លទ្ធផល៖

```text
value: 41
after: 42
second: 20
nullptr check: yes
```

## តើគួរប្រើពោយន្ត័រពេលណា?

នៅ C++ ទំនើប ពោយន្ត័រ «ឆៅ» (raw pointer) ត្រូវប្រើតែសម្រាប់ការមើល (observation)
មិនមែនសម្រាប់ការកាន់កាប់ (ownership)។ សម្រាប់ការកាន់កាប់ សូមប្រើ
[smart pointers](smart-pointers.md)។ សម្រាប់ប៉ារ៉ាម៉ែត្រ សូមប្រើ [យោង](references.md)។

## អានបន្ថែម

- [cppreference: pointer declaration](https://en.cppreference.com/w/cpp/language/pointer)
- [cppreference: `nullptr`](https://en.cppreference.com/w/cpp/language/nullptr)
