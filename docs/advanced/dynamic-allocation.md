# ការបែងចែកអង្គចងចាំឌីណាមិក

```{translation-meta} advanced/dynamic-allocation
```

ការបែងចែកឌីណាមិក (dynamic allocation) មានន័យថាបង្កើតវត្ថុនៅពេលដំណើរការ
ដោយទំហំដែលអាចដឹងតែពេលនោះ។ C++ ធ្វើវាដោយ `new` និង `delete`។

## `new` និង `delete`

```cpp
int* value = new int(42);   // បង្កើត int មួយ តម្លៃ 42
std::cout << *value;
delete value;               // ដោះលែងមួយវត្ថុ
```

សម្រាប់អារេ ត្រូវប្រើ `new[]` និង `delete[]` ជាគូ៖

```cpp
int* values = new int[10];
// ...
delete[] values;            // ត្រូវតែជា delete[] មិនមែន delete
```

:::{warning}
ការលាយ `new` ជាមួយ `delete[]` ឬ `new[]` ជាមួយ `delete` គឺជា
**ឥរិយាបថមិនកំណត់**។ កម្មវិធីបកប្រែអាចមិនរាយការណ៍ តែកម្មវិធីអាចខូចនៅពេលដំណើរការ។
:::

## ការចាប់ផ្ដើមតម្លៃ

```cpp
int* a = new int;        // តម្លៃមិនកំណត់
int* b = new int();      // តម្លៃសូន្យ (value-initialized)
int* c = new int(7);     // 7
int* d = new int[4]();   // អារេទាំងអស់សូន្យ
```

## ករណីខ្វះអង្គចងចាំ

បើ `new` មិនអាចបែងចែកអង្គចងចាំបាន វាបោះ `std::bad_alloc`។
បើអ្នកមិនចង់ប្រើករណីលើកលែង អ្នកអាចប្រើទម្រង់ `nothrow`៖

```cpp
#include <new>

int* big = new (std::nothrow) int[1000];
if (big == nullptr) {
    // បែងចែកមិនបាន
}
delete[] big;
```

## ហេតុអ្វីមិនគួរប្រើ `new` ដោយផ្ទាល់

កូដខាងក្រោមមានបញ្ហា៖

```cpp
void risky() {
    int* data = new int[100];
    might_throw();          // បើបោះ exception នៅទីនេះ...
    delete[] data;          // ...បន្ទាត់នេះមិនត្រូវរត់ → លេចធ្លាយ
}
```

ដំណោះស្រាយគឺប្រើធុងទិន្នន័យ ឬ smart pointer ដែលដោះលែងដោយស្វ័យប្រវត្តិ៖

```cpp
void safe() {
    std::vector<int> data(100);   // គ្មានការលេចធ្លាយ
    might_throw();
}
```

## កូដឧទាហរណ៍

```{literalinclude} ../../examples/advanced/dynamic-allocation.cpp
:language: cpp
```

លទ្ធផល៖

```text
single: 42
sum: 6
zeroed: 0
```

## អានបន្ថែម

- [cppreference: `new` expression](https://en.cppreference.com/w/cpp/language/new)
- [cppreference: `delete` expression](https://en.cppreference.com/w/cpp/language/delete)
