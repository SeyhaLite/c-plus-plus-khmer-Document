# RAII (ការទទួលបានធនធានគឺជាការចាប់ផ្ដើម)

```{translation-meta} advanced/raii
```

RAII មកពី «Resource Acquisition Is Initialization»៖ ការទទួលបានធនធាន
គឺជាការចាប់ផ្ដើមតម្លៃ។ គំនិតសាមញ្ញគឺ៖ **ធនធានមួយត្រូវកាន់កាប់ដោយវត្ថុ**
ដែលទទួលវានៅ constructor និងដោះលែងវានៅ destructor។

## ហេតុអ្វីវាសំខាន់

Destructor ត្រូវហៅជានិច្ច ទោះកម្មវិធីចេញដោយធម្មតា ឬដោយសារករណីលើកលែង
(stack unwinding)។ ដូច្នេះធនធានមិនអាចលេចធ្លាយបានទេ។

```cpp
void work() {
    std::vector<int> values(1000);
    throw std::runtime_error("failed");   // values នៅតែត្រូវបំផ្លាញ
}
```

## គំរូសាមញ្ញ

```cpp
class Buffer {
public:
    explicit Buffer(int size) : data_(new int[size]), size_(size) {}

    ~Buffer() {
        delete[] data_;      // ដោះលែងដោយស្វ័យប្រវត្តិ
    }

    Buffer(const Buffer&) = delete;             // ការពារការចម្លងខុស
    Buffer& operator=(const Buffer&) = delete;

private:
    int* data_;
    int size_;
};
```

ឥឡូវអ្នកប្រើ `Buffer` ដោយមិនចាំបាច់គិតពី `delete` ទេ៖

```cpp
{
    Buffer buffer(1024);
    // ប្រើ buffer
}   // ដោះលែងស្វ័យប្រវត្តិ ទោះមាន exception ក៏ដោយ
```

## គំរូធនធានផ្សេងទៀត

RAII មិនមែនសម្រាប់តែអង្គចងចាំទេ៖

| ធនធាន | គំរូ RAII ក្នុងបណ្ណាល័យស្តង់ដារ |
| --- | --- |
| អង្គចងចាំ heap | `std::vector`, `std::string`, `std::unique_ptr` |
| ឯកសារ | `std::fstream` (បិទនៅ destructor) |
| Mutex | `std::lock_guard`, `std::unique_lock` |
| ខ្សែស្រឡាយ | `std::jthread` (C++20, join ស្វ័យប្រវត្តិ) |

## `std::lock_guard` — ឧទាហរណ៍ខ្លី

```cpp
std::mutex mutex;

void safe_increment() {
    std::lock_guard<std::mutex> lock(mutex);   // ចាក់សោ
    ++shared_counter;
}   // ដោះសោស្វ័យប្រវត្តិ ទោះមាន exception
```

បើគ្មាន RAII អ្នកត្រូវចងចាំហៅ `mutex.unlock()` គ្រប់ផ្លូវចេញ ដែលងាយភ្លេច។

:::{warning}
RAII ពឹងលើ destructor ដែលធានាថាត្រូវហៅ។ បើអ្នកបង្កើតវត្ថុដោយ `new` ហើយភ្លេច `delete`
នោះ destructor មិនត្រូវហៅទេ ហើយ RAII បាត់បង់ប្រសិទ្ធភាព។ ដូច្នេះកុំប្រើ `new`
ដោយផ្ទាល់។
:::

## កូដឧទាហរណ៍

```{literalinclude} ../../examples/advanced/raii.cpp
:language: cpp
```

លទ្ធផល៖

```text
allocate 4
value: 42
release 4
done
```

សង្កេតថា `release` កើតឡើងមុន `done` ដោយស្វ័យប្រវត្តិ នៅចុងប្លុក។

## អានបន្ថែម

- [cppreference: destructors](https://en.cppreference.com/w/cpp/language/destructor)
- [isocpp.org: RAII](https://isocpp.org/wiki/faq/ctors#resource-acquisition-is-initialization)
