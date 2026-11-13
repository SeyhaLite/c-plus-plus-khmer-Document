# ពោយន្ត័រឆ្លាតវៃ (Smart Pointers)

```{translation-meta} advanced/smart-pointers
```

ពោយន្ត័រឆ្លាតវៃ (smart pointer) គឺជាវត្ថុដែលកាន់កាប់ពោយន្ត័រ និងដោះលែងវា
ដោយស្វ័យប្រវត្តិនៅ destructor។ វាជាការអនុវត្ត RAII សម្រាប់អង្គចងចាំ heap។
បណ្ណាល័យនេះមានតាំងពី **C++11** ក្នុងឯកសារក្បាល `<memory>`។

## ប្រភេទសំខាន់ៗ

| ប្រភេទ | ម្ចាស់ | ពេលប្រើ |
| --- | --- | --- |
| `std::unique_ptr<T>` | តែមួយ | ការកាន់កាប់ផ្ដាច់មុខ (ជម្រើសដំបូង) |
| `std::shared_ptr<T>` | ចែករំលែក | ពេលមានម្ចាស់ច្រើន |
| `std::weak_ptr<T>` | គ្មាន | មើលដោយមិនកាន់កាប់ (ការពារវដ្ដ) |

## `std::unique_ptr`

```cpp
auto resource = std::make_unique<Resource>("unique");
// ប្រើ resource
// ដោះលែងស្វ័យប្រវត្តិនៅចុងដែនកំណត់
```

`unique_ptr` មិនអាចចម្លងបានទេ ប៉ុន្តែអាច **ផ្លាស់ទី** បាន៖

```cpp
auto owner = std::make_unique<Resource>("x");
use(std::move(owner));        // ផ្ទេរការកាន់កាប់
// owner ក្លាយជា nullptr
```

:::{note}
`std::make_unique` មានតាំងពី **C++14**។ បើអ្នកបកប្រែដោយ C++11 ត្រូវសរសេរ
`std::unique_ptr<Resource>(new Resource("x"))`។ `std::make_shared` មានតាំងពី C++11។
:::

## `std::shared_ptr`

```cpp
auto shared = std::make_shared<Resource>("shared");
{
    auto copy = shared;             // ម្ចាស់ទីពីរ
    shared.use_count();             // 2
}
shared.use_count();                 // 1
```

ការបង្កើត `shared_ptr` មានតម្លៃខ្ពស់ជាង `unique_ptr` ព្រោះវាត្រូវរក្សាការរាប់ម្ចាស់
ដែលមានសុវត្ថិភាពពីខ្សែស្រឡាយផ្សេងៗ។ ដូច្នេះកុំប្រើវាដោយស្វ័យប្រវត្តិ។

## `std::weak_ptr` និងវដ្ដយោង

បើវត្ថុពីរកាន់ `shared_ptr` ទៅគ្នាទៅវិញ នោះការរាប់ម្ចាស់មិនដែលធ្លាក់ដល់សូន្យ
ហើយអង្គចងចាំលេចធ្លាយ។ ដំណោះស្រាយគឺប្រើ `weak_ptr` ម្ខាង៖

```cpp
struct Node {
    std::shared_ptr<Node> next;
    std::weak_ptr<Node> prev;   // មិនកាន់កាប់
};
```

## ពេលណាប្រើអ្វី

- ត្រូវការម្ចាស់តែមួយ → `std::unique_ptr` (ជម្រើសលំនាំដើម)។
- ត្រូវការម្ចាស់ច្រើន → `std::shared_ptr` (ពិចារណាសិនថាតើពិតជាចាំបាច់)។
- ត្រូវការមើលដោយគ្មានការកាន់កាប់ → ពោយន្ត័រឆៅ ឬ `weak_ptr`។

## កូដឧទាហរណ៍

```{literalinclude} ../../examples/advanced/smart-pointers.cpp
:language: cpp
```

លទ្ធផល៖

```text
acquire unique
unique_ptr ready
using unique
release unique
first is null: yes
acquire shared
count: 2
count after scope: 1
release shared
```

## អានបន្ថែម

- [cppreference: `std::unique_ptr`](https://en.cppreference.com/w/cpp/memory/unique_ptr)
- [cppreference: `std::shared_ptr`](https://en.cppreference.com/w/cpp/memory/shared_ptr)
- [cppreference: `std::weak_ptr`](https://en.cppreference.com/w/cpp/memory/weak_ptr)
