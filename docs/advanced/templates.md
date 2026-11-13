# ពុម្ព (Templates)

```{translation-meta} advanced/templates
```

ពុម្ព (Template) អនុញ្ញាតឱ្យអ្នកសរសេរកូដម្តង ហើយប្រើវាជាមួយប្រភេទជាច្រើន។
កម្មវិធីបកប្រែបង្កើតកូដជាក់ស្តែងសម្រាប់ប្រភេទនីមួយៗនៅពេលបកប្រែ។

## ពុម្ពអនុគមន៍

```cpp
template <typename T>
T maximum(T a, T b) {
    return a > b ? a : b;
}
```

ការហៅ `maximum(3, 7)` បង្កើត `int maximum(int, int)` ហើយ `maximum(2.5, 1.5)`
បង្កើតកំណែ `double`។

អ្នកអាចកំណត់ប្រភេទដោយច្បាស់៖

```cpp
maximum<double>(1, 2.5);   // 2.5 — បំប្លែង int ទៅ double
```

## ពុម្ពថ្នាក់

```cpp
template <typename T>
class Box {
public:
    explicit Box(T value) : value_(value) {}
    const T& get() const { return value_; }

private:
    T value_;
};

Box<int> numbers(42);
Box<std::string> text("hello");
```

## ពុម្ពជាមួយប៉ារ៉ាម៉ែត្រច្រើន

```cpp
template <typename Key, typename Value>
struct Pair {
    Key key;
    Value value;
};
```

## ការដាក់កំណត់ (constraints)

ចាប់ពី **C++20** អ្នកអាចកំណត់ថាប្រភេទត្រូវគោរពលក្ខខណ្ឌអ្វី ដោយប្រើ concepts៖

```cpp
#include <concepts>

template <typename T>
    requires std::integral<T>
T add(T a, T b) {
    return a + b;
}
```

ដោយគ្មានការកំណត់ កំហុសនឹងបង្ហាញនៅខាងក្នុងពុម្ពដែលអានយល់ខ្លាំង។
មើល [គំនិត (Concepts)](concepts.md) សម្រាប់ព័ត៌មានបន្ថែម។

:::{note}
ពុម្ពជាធម្មតាត្រូវកំណត់នៅក្នុងឯកសារក្បាល (`.h`/`.hpp`) ព្រោះកម្មវិធីបកប្រែ
ត្រូវឃើញតួអង្គកម្មវិធីពេលបង្កើតកំណែជាក់ស្តែងសម្រាប់ប្រភេទនីមួយៗ។
:::

## កូដឧទាហរណ៍

```{literalinclude} ../../examples/advanced/templates.cpp
:language: cpp
```

លទ្ធផល៖

```text
max int: 7
max double: 2.5
max string: pear
box: 42, hello
```

## អានបន្ថែម

- [cppreference: templates](https://en.cppreference.com/w/cpp/language/templates)
- [cppreference: function templates](https://en.cppreference.com/w/cpp/language/function_template)
