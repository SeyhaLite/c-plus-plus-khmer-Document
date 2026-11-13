# ការបញ្ចូល និងការបញ្ចេញ (I/O)

```{translation-meta} basics/input-output
```

C++ ប្រើស្ទ្រីម (stream) សម្រាប់ការបញ្ចូល និងការបញ្ចេញ។ ស្ទ្រីមគឺជាលំហូរនៃតួអក្សរ
ដែលភ្ជាប់កម្មវិធីទៅឧបករណ៍ខាងក្រៅ។ ឯកសារក្បាលដែលត្រូវការគឺ `<iostream>`។

## ស្ទ្រីមស្តង់ដារ

| ស្ទ្រីម | អត្ថន័យ |
| --- | --- |
| `std::cin` | ការបញ្ចូលស្តង់ដារ (ក្តារចុច) |
| `std::cout` | ការបញ្ចេញស្តង់ដារ (អេក្រង់) |
| `std::cerr` | ការបញ្ចេញកំហុស (មិនបើក buffer) |
| `std::clog` | ការបញ្ចេញកំហុស (បើក buffer) |

## ការបញ្ចេញ

```cpp
#include <iostream>

int main() {
    std::cout << "x = " << 42 << '\n';
    std::cerr << "something went wrong\n";
    return 0;
}
```

`<<` ត្រូវបានហៅថា «ប្រមាណវិធីបញ្ចូលទៅស្ទ្រីម» (stream insertion)។
អ្នកអាចភ្ជាប់វាជាបន្តបន្ទាប់ ដូចជា `std::cout << a << b << c;`។

## ការបញ្ចូល

```cpp
#include <iostream>
#include <string>

int main() {
    std::string name;
    int age = 0;

    std::cout << "Enter name and age: ";
    std::cin >> name >> age;      // អានពីរតម្លៃ បំបែកដោយចន្លោះ
    std::cout << "Hello " << name << ", age " << age << '\n';
    return 0;
}
```

`std::cin >> name` អានតួអក្សររហូតដល់ចន្លោះទំនេរ។ ដូច្នេះវាមិនអានឈ្មោះដែលមាន
ចន្លោះទំនេរពេញលេញទេ។ ដើម្បីអានបន្ទាត់ទាំងមូល ត្រូវប្រើ `std::getline`៖

```cpp
std::string line;
std::getline(std::cin, line);   // អានរហូតដល់ចុងបន្ទាត់
```

:::{warning}
បើអ្នកប្រើ `std::cin >>` រួច `std::getline` បន្ទាប់មក `getline` នឹងអានតួអក្សរ
បន្ទាត់ថ្មីដែលនៅសល់ ហើយត្រឡប់ខ្សែអក្សរទទេ។ ដំណោះស្រាយ៖ ហៅ `std::cin.ignore()`
មួយដង ឬប្រើ `getline` សម្រាប់ការអានទាំងអស់។
:::

## កូដឧទាហរណ៍ដែលអាចធ្វើតេស្តបាន

កម្មវិធីដែលអានពីក្តារចុចមិនអាចធ្វើតេស្តស្វ័យប្រវត្តិបានទេ។ ដូច្នេះឧទាហរណ៍ខាងក្រោម
ប្រើ `std::istringstream` ដែលមានឥរិយាបថដូច `std::cin` ប៉ុន្តែអានពីខ្សែអក្សរថេរ។
វិធីនេះជាវិធីស្តង់ដារសម្រាប់ធ្វើតេស្តកូដ I/O។

```{literalinclude} ../../examples/basics/input-output.cpp
:language: cpp
```

លទ្ធផល៖

```text
name: Sok
age: 21
next year: 22
city: Phnom Penh
city: Siem Reap
```

## ស្តង់ដារ

ស្ទ្រីមស្តង់ដារមានតាំងពី C++98។ `std::istringstream` និង `std::ostringstream`
មកពីឯកសារក្បាល `<sstream>` ហើយក៏មានតាំងពី C++98។

## អានបន្ថែម

- [cppreference: I/O library](https://en.cppreference.com/w/cpp/io)
- [cppreference: `std::cout`](https://en.cppreference.com/w/cpp/io/cout)
- [cppreference: `std::cin`](https://en.cppreference.com/w/cpp/io/cin)
