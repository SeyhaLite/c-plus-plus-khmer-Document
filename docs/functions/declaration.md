# ការប្រកាសអនុគមន៍ (Declaration)

```{translation-meta} functions/declaration
```

ការប្រកាសអនុគមន៍ (function declaration) ប្រាប់កម្មវិធីបកប្រែថាអនុគមន៍មួយមាន
ឈ្មោះ ប៉ារ៉ាម៉ែត្រ និងប្រភេទតម្លៃត្រឡប់អ្វី ដោយមិនផ្ដល់តួអង្គកម្មវិធី។
គេហៅវាថា «prototype» ដែរ។

## រូបមន្ត

```cpp
return_type function_name(parameter_list);
```

```cpp
int square(int x);                 // ប្រកាស
double average(double a, double b);
void print_report();
```

## ហេតុអ្វីត្រូវការការប្រកាស

កម្មវិធីបកប្រែអានឯកសារពីលើចុះក្រោម។ បើអ្នកហៅអនុគមន៍មុនពេលវាត្រូវបានគេស្គាល់
នោះត្រូវមានការប្រកាសជាមុន៖

```cpp
#include <iostream>

int square(int x);   // ប្រកាសមុន

int main() {
    std::cout << square(5) << '\n';   // ហៅបាន ព្រោះដឹងរូបមន្តរួច
}

int square(int x) {  // កំណត់នៅក្រោយ
    return x * x;
}
```

## ការប្រកាសក្នុងឯកសារក្បាល

នៅពេលកូដធំឡើង គេដាក់ការប្រកាសក្នុងឯកសារក្បាល (`.h` ឬ `.hpp`)
ហើយការកំណត់ក្នុងឯកសារ `.cpp`៖

```cpp
// math_utils.h
#pragma once

int square(int x);
```

```cpp
// main.cpp
#include "math_utils.h"

int main() {
    return square(5) == 25 ? 0 : 1;
}
```

`#pragma once` ការពារការបញ្ចូលឯកសារក្បាលច្រើនដង។ វាមិនមែនជាផ្នែកនៃស្តង់ដារ C++
ទេ ប៉ុន្តែកម្មវិធីបកប្រែសំខាន់ៗគាំទ្រវា។ ជម្រើសស្តង់ដារគឺ include guard៖

```cpp
#ifndef MATH_UTILS_H
#define MATH_UTILS_H
// ...
#endif
```

## ច្បាប់សំខាន់ៗ

- អនុគមន៍មួយអាច **ប្រកាស** បានច្រើនដង ប៉ុន្តែ **កំណត់** បានតែម្តង (one definition rule)។
- ការប្រកាសទាំងអស់ត្រូវត្រូវគ្នា (ប្រភេទត្រឡប់ និងប្រភេទប៉ារ៉ាម៉ែត្រ)។
- តម្លៃលំនាំដើម (default arguments) ត្រូវសរសេរក្នុងការប្រកាស មិនមែនក្នុងការកំណត់
  ម្តងទៀតទេ (មើល [ប៉ារ៉ាម៉ែត្រ](parameters.md))។

## កូដឧទាហរណ៍

```{literalinclude} ../../examples/functions/declaration.cpp
:language: cpp
```

លទ្ធផល៖

```text
square(5) = 25
```

## អានបន្ថែម

- [cppreference: functions](https://en.cppreference.com/w/cpp/language/function)
