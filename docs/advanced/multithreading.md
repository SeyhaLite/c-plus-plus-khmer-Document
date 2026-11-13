# ការប្រើខ្សែស្រឡាយច្រើន

```{translation-meta} advanced/multithreading
```

ខ្សែស្រឡាយ (thread) អនុញ្ញាតឱ្យកម្មវិធីធ្វើការច្រើនក្នុងពេលតែមួយ។
C++ ផ្ដល់ការគាំទ្រខ្សែស្រឡាយជាផ្នែកនៃបណ្ណាល័យស្តង់ដារចាប់ពី **C++11**
ក្នុងឯកសារក្បាល `<thread>`។

## ការបង្កើតខ្សែស្រឡាយ

```cpp
#include <iostream>
#include <thread>

int main() {
    std::thread worker([] {
        std::cout << "from worker\n";
    });

    std::cout << "from main\n";
    worker.join();      // រង់ចាំខ្សែស្រឡាយបញ្ចប់
    return 0;
}
```

## `join` និង `detach`

| វិធីសាស្ត្រ | អត្ថន័យ |
| --- | --- |
| `join()` | រង់ចាំខ្សែស្រឡាយបញ្ចប់ មុនបន្ត |
| `detach()` | ឱ្យវាដំណើរការឯករាជ្យ |
| `joinable()` | ពិនិត្យថាតើអាច `join` បានឬអត់ |

:::{warning}
បើវត្ថុ `std::thread` ត្រូវបំផ្លាញនៅពេលវានៅ `joinable` នោះកម្មវិធីត្រូវ
`std::terminate` ភ្លាម។ ដូច្នេះត្រូវ `join()` ឬ `detach()` ជានិច្ច។
ចាប់ពី **C++20** `std::jthread` join ដោយស្វ័យប្រវត្តិនៅ destructor។
:::

## ការផ្ដល់អាគុយម៉ង់

```cpp
void work(int id, const std::string& label);

std::thread t(work, 7, "job");   // អាគុយម៉ង់ត្រូវចម្លងចូលខ្សែស្រឡាយ
```

បើត្រូវការយោង ត្រូវប្រើ `std::ref(x)` ដោយយល់ថាអ្នកទទួលខុសត្រូវថាវត្ថុនោះរស់គ្រប់ពេល។

## ការរាយការណ៍កំហុសក្នុងខ្សែស្រឡាយ

Exception ដែលមិនត្រូវចាប់នៅក្នុងខ្សែស្រឡាយ ធ្វើឱ្យកម្មវិធីបញ្ចប់ទាំងមូល។
ដូច្នេះត្រូវចាប់កំហុសនៅក្នុងខ្សែស្រឡាយ ហើយផ្ទេរព័ត៌មានត្រឡប់ទៅខ្សែស្រឡាយមេ
(ឧទាហរណ៍ តាម `std::promise`/`std::future`)។

## កូដឧទាហរណ៍

```{literalinclude} ../../examples/advanced/multithreading.cpp
:language: cpp
```

លទ្ធផល៖

```text
thread id valid: yes
total: 499500
joinable after join: no
```

## អានបន្ថែម

- [cppreference: `std::thread`](https://en.cppreference.com/w/cpp/thread/thread)
- [cppreference: `std::jthread`](https://en.cppreference.com/w/cpp/thread/jthread)
