# ធុងទិន្នន័យ (Containers)

```{translation-meta} stdlib/containers
```

ធុងទិន្នន័យ (container) គឺជាបណ្ណាល័យស្តង់ដារដែលរក្សាទុក និងគ្រប់គ្រងកំណត់ទិន្នន័យ។
ការជ្រើសរើសធុងត្រឹមត្រូវគឺសំខាន់ជាងការសរសេរអាល់ហ្គោរីតដោយខ្លួនឯង។

## ធុងជាបន្ទាត់ (sequence)

| ធុង | អត្ថន័យ | ពេលប្រើ |
| --- | --- | --- |
| `std::vector` | អារេដែលអាចពង្រីក | ជម្រើសលំនាំដើម |
| `std::array` | អារេទំហំថេរ | ទំហំដឹងពេលបកប្រែ |
| `std::deque` | ជួរពីរក្បាល | push/pop តែត្រឹមចុង |
| `std::list` | បញ្ជីភ្ជាប់ | លុប/បញ្ចូលកណ្ដាល |

## ធុងដែលស្វែងរក (associative)

| ធុង | លក្ខណៈ |
| --- | --- |
| `std::map` | ជាលំដាប់ ស្វែងរក O(log n) |
| `std::set` | សំណុំតែមួយ ជាលំដាប់ |
| `std::unordered_map` | តារាង hash ស្វែងរក O(1) ជាមធ្យម |
| `std::unordered_set` | សំណុំ hash |

`std::map` ត្រូវការប្រភេទ key មាន `operator<` ឬ comparator ផ្ទាល់ខ្លួន។
`std::unordered_map` ត្រូវការ `std::hash` និង `operator==`។

## ប្រតិបត្តិការសំខាន់ៗ

```cpp
std::vector<int> values{10, 20, 30};
values.push_back(40);
values.pop_back();
values.size();          // ចំនួនធាតុ
values.empty();         // ត្រឹមត្រូវ/ខុស
values.front();         // ធាតុដំបូង
values.back();          // ធាតុចុងក្រោយ
values.at(1);           // ចូលដោយពិនិត្យសីមា (បោះ exception)
values[1];              // ចូលដោយគ្មានការពិនិត្យ
```

:::{note}
`at()` ពិនិត្យសីមា ហើយបោះ `std::out_of_range` បើខុស។
`[]` មិនពិនិត្យ ហើយបើខុសគឺឥរិយាបថមិនកំណត់ — ប្រើ `at()` នៅពេលដែល
ទិន្នន័យមកពីអ្នកប្រើ។
:::

## កូដឧទាហរណ៍

```{literalinclude} ../../examples/stdlib/containers.cpp
:language: cpp
```

លទ្ធផល៖

```text
size: 4
front: 10 back: 40
Alice: 30
Bob: 25
count Alice: 1
```

## អានបន្ថែម

- [cppreference: containers](https://en.cppreference.com/w/cpp/container)
- [cppreference: `std::vector`](https://en.cppreference.com/w/cpp/container/vector)
- [cppreference: `std::map`](https://en.cppreference.com/w/cpp/container/map)
