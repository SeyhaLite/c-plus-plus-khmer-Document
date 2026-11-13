# រង្វិលជុំ for

```{translation-meta} control-flow/for
```

រង្វិលជុំ `for` សមស្របនៅពេលអ្នកដឹងចំនួនជុំជាមុន។

## រូបមន្តបុរាណ

```cpp
for (int i = 0; i < 5; ++i) {
    std::cout << i << '\n';
}
```

មានបីផ្នែក បំបែកដោយ `;`៖

1. **ការចាប់ផ្ដើមតម្លៃ** — `int i = 0` (រត់ម្តង)។
2. **លក្ខខណ្ឌ** — `i < 5` (ពិនិត្យមុនជុំនីមួយៗ)។
3. **បន្ថែម/បន្ថយ** — `++i` (រត់ក្រោយជុំនីមួយៗ)។

អថេរ `i` មានវិសាលភាពត្រឹមរង្វិលជុំប៉ុណ្ណោះ។ នេះជាការកែលម្អពី C++98
ដែលអថេរបែបនេះនៅតែមានបន្ទាប់ពីរង្វិលជុំ (ឥរិយាបថចាស់នៅតែជាការពិត
សម្រាប់កូដដែលប្រកាសអថេរនៅខាងក្រៅ)។

## រង្វិលជុំលើជួរ (range-based for, C++11)

ចាប់ពី **C++11** អ្នកអាចដើរកាត់ធុងទិន្នន័យដោយមិនចាំបាច់ប្រើ index៖

```cpp
std::vector<int> values{10, 20, 30};

for (int value : values) {
    std::cout << value << '\n';
}

for (const auto& value : values) {   // មិនចម្លងទិន្នន័យ
    std::cout << value << '\n';
}
```

ប្រើ `const auto&` នៅពេលអ្នកមិនត្រូវកែតម្លៃ ព្រោះវាជៀសវាងការចម្លងវត្ថុធំៗ។

## រង្វិលជុំជាន់គ្នា

```cpp
for (int row = 1; row <= 2; ++row) {
    for (int col = 1; col <= 2; ++col) {
        std::cout << row << ',' << col << '\n';
    }
}
```

`break` ក្នុងរង្វិលជុំខាងក្នុងឈប់តែរង្វិលជុំខាងក្នុងប៉ុណ្ណោះ។

:::{warning}
ការកែធុងទិន្នន័យ (បន្ថែម ឬលុបធាតុ) នៅពេលកំពុងដើរកាត់ដោយ `for` អាចធ្វើឱ្យ
អ្នកដើរកាត់ (iterator) ខូច។ បើត្រូវកែ សូមប្រើ index ឬប្រមូលអ្វីដែលត្រូវលុប
រួចលុបក្រោយរង្វិលជុំ។
:::

## កូដឧទាហរណ៍

```{literalinclude} ../../examples/control-flow/for.cpp
:language: cpp
```

លទ្ធផល៖

```text
sum = 15
v=10
v=20
v=30
1,1
1,2
2,1
2,2
```

## អានបន្ថែម

- [cppreference: `for` loop](https://en.cppreference.com/w/cpp/language/for)
- [cppreference: range-based for](https://en.cppreference.com/w/cpp/language/range-for)
