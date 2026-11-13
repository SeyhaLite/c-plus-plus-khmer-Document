# គំនិត (Concepts)

```{translation-meta} advanced/concepts
```

គំនិត (concept) គឺជាលក្ខខណ្ឌដែលប្រភេទត្រូវបំពេញ ដែលអាចពិនិត្យបាននៅពេលបកប្រែ។
វាជាលក្ខណៈ **C++20** ហើយជំនួសវិធីសាស្ត្រ SFINAE ចាស់ដែលអានយល់ខ្លាំង។

## ហេតុអ្វីត្រូវការ

ដោយគ្មាន concept កំហុសក្នុងពុម្ពបង្ហាញជាសារវែងខ្លាំងនៅខាងក្នុងបណ្ណាល័យ
ដែលពិបាកយល់។ ជាមួយ concept កំហុសបង្ហាញត្រង់ចំណុច៖ «ប្រភេទនេះមិនបំពេញ
លក្ខខណ្ឌដែលត្រូវការ»។

## ការប្រើ concept ស្តង់ដារ

```cpp
#include <concepts>

template <typename T>
    requires std::integral<T>
T twice(T value) {
    return value * 2;
}
```

បើអ្នកហៅ `twice(2.5)` នោះកម្មវិធីបកប្រែនឹងបដិសេធភ្លាម ព្រោះ `double`
មិនមែន `std::integral`។

## ទម្រង់ខ្លី (abbreviated template)

```cpp
void print(const std::integral auto& value);
void print(const std::floating_point auto& value);
```

ទម្រង់នេះសរសេរតិចជាង ប៉ុន្តែន័យដូចគ្នា។

## ការកំណត់ concept ផ្ទាល់ខ្លួន

```cpp
template <typename T>
concept Addable = requires(T a, T b) {
    { a + b } -> std::convertible_to<T>;
};

template <Addable T>
T sum(T a, T b) {
    return a + b;
}
```

`requires` ពិនិត្យថាកន្សោមនៅខាងក្នុងអាចបកប្រែបានជាមួយប្រភេទនោះ។

## concepts ស្តង់ដារសំខាន់ៗ

| concept | ត្រូវការ |
| --- | --- |
| `std::integral` | ប្រភេទចំនួនគត់ |
| `std::floating_point` | ប្រភេទចំនុចអណ្តែត |
| `std::same_as<T, U>` | ប្រភេទដូចគ្នា |
| `std::convertible_to<From, To>` | អាចបំប្លែងបាន |
| `std::copyable`, `std::movable` | អាចចម្លង ឬផ្លាស់ទីបាន |

## `static_assert` ជាមួយ concept

```cpp
static_assert(std::integral<int>);
static_assert(!std::integral<double>);
```

នេះជាការត្រួតពិនិត្យនៅពេលបកប្រែ ដែលមិនមានតម្លៃនៅពេលដំណើរការទេ។

:::{note}
concepts មិនប្រែប្រួលលក្ខណៈរបស់ C++ នៅពេលដំណើរការទេ។ វាជាការត្រួតពិនិត្យ
នៅពេលបកប្រែ ដែលជួយឱ្យកូដទូទៅមានសុវត្ថិភាព និងអានយល់ជាង។
:::

## កូដឧទាហរណ៍

```{literalinclude} ../../examples/advanced/concepts.cpp
:language: cpp
```

លទ្ធផល៖

```text
twice: 42
int-like: 7
float-like: 2.5
static asserts passed
```

## អានបន្ថែម

- [cppreference: constraints and concepts](https://en.cppreference.com/w/cpp/language/constraints)
- [cppreference: `<concepts>`](https://en.cppreference.com/w/cpp/header/concepts)
