# និយមន័យចលនា (Move Semantics)

```{translation-meta} advanced/move-semantics
```

និយមន័យចលនា (move semantics) អនុញ្ញាតឱ្យធនធាន (អង្គចងចាំ ខ្សែអក្សរ ឯកសារ)
ត្រូវ **ផ្ទេរ** ពីវត្ថុមួយទៅវត្ថុមួយទៀត ជំនួសឱ្យការចម្លង។
វាមានតាំងពី **C++11**។

## lvalue និង rvalue

- **lvalue** — កន្សោមដែលមានទីតាំងក្នុងអង្គចងចាំ ដូចជាអថេរ។ អ្នកអាចយកអាសយដ្ឋានវាបាន។
- **rvalue** — តម្លៃបណ្ដោះអាសន្ន ដូចជា `42` ឬ `std::string("hello")`។

`std::move(x)` មិនផ្លាស់ទីអ្វីទេ។ វាគ្រាន់តែបំប្លែង `x` ទៅជា rvalue ដើម្បីឱ្យ
កម្មវិធីបកប្រែជ្រើស move constructor ឬ move assignment។

## ការចម្លង និងការផ្លាស់ទី

```cpp
std::string a = "a long string value";
std::string b = a;              // ចម្លង (copy) — ចំណាយ
std::string c = std::move(a);   // ផ្លាស់ទី (move) — តម្លៃ a ប្ដូរទៅ c
```

ក្រោយ `std::move(a)` ស្ថានភាពរបស់ `a` គឺ «ត្រឹមត្រូវ ប៉ុន្តែមិនកំណត់»។
អ្នកអាចដាក់តម្លៃថ្មី ឬបំផ្លាញវា ប៉ុន្តែមិនគួរអានតម្លៃចាស់របស់វាឡើយ។

## សរសេរថ្នាក់ដែលអាចផ្លាស់ទី

```cpp
class Buffer {
public:
    Buffer(Buffer&& other) noexcept
        : data_(other.data_), size_(other.size_) {
        other.data_ = nullptr;    // ទុកឱ្យវត្ថុដើមមិនកាន់កាប់ធនធានទៀត
        other.size_ = 0;
    }

    Buffer& operator=(Buffer&& other) noexcept { /* ផ្ទេរ និងដោះលែងចាស់ */ return *this; }

private:
    int* data_ = nullptr;
    int size_ = 0;
};
```

## ក្បួនប្រាំ (rule of five)

បើអ្នកសរសេរមួយក្នុងចំណោមទាំងនេះ អ្នកគួរពិចារណាសរសេរទាំងអស់៖

1. destructor
2. copy constructor
3. copy assignment
4. move constructor
5. move assignment

បើថ្នាក់មិនកាន់កាប់ធនធានដោយផ្ទាល់ (ប្រើ `std::vector` ជាដើម) អ្នកមិនចាំបាច់
សរសេរទាំងនេះទេ — «rule of zero»។ នេះជាជម្រើសដែលគួរពេញចិត្ត។

:::{note}
ការត្រឡប់តម្លៃពីអនុគមន៍មិនត្រូវការ `std::move` ទេ។ កម្មវិធីបកប្រែអនុវត្ត
copy elision ឬផ្លាស់ទីដោយស្វ័យប្រវត្តិ។ ការសរសេរ `return std::move(x);` អាចរារាំង
ការបង្កើនប្រសិទ្ធភាព។
:::

## កូដឧទាហរណ៍

```{literalinclude} ../../examples/advanced/move-semantics.cpp
:language: cpp
```

លទ្ធផល៖

```text
copy a
move a
a name: (moved)
c name: a
move x
size: 1
```

## អានបន្ថែម

- [cppreference: move constructor](https://en.cppreference.com/w/cpp/language/move_constructor)
- [cppreference: `std::move`](https://en.cppreference.com/w/cpp/utility/move)
