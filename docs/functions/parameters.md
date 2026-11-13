# ប៉ារ៉ាម៉ែត្រ (Parameters)

```{translation-meta} functions/parameters
```

ប៉ារ៉ាម៉ែត្រ (Parameter) គឺជាតម្លៃដែលអនុគមន៍ទទួល។ របៀបដែលអ្នកប្រកាសប៉ារ៉ាម៉ែត្រ
កំណត់ថាតើអនុគមន៍អាចកែតម្លៃរបស់អ្នកហៅបានឬអត់។

## ការផ្ដល់តម្លៃដោយចម្លង (pass by value)

```cpp
void by_value(int x) {
    x = 99;      // កែតែច្បាប់ចម្លង
}

int a = 1;
by_value(a);     // a នៅតែ 1
```

## ការផ្ដល់តម្លៃដោយយោង (pass by reference)

```cpp
void by_reference(int& x) {
    x = 99;      // កែអថេរដើម
}

int b = 1;
by_reference(b); // b ក្លាយជា 99
```

ប្រើ `const` នៅពេលអនុគមន៍មិនត្រូវកែតម្លៃ។ វាជៀសវាងការចម្លងវត្ថុធំ
(ដូចជា `std::string` ឬ `std::vector`) ហើយបង្ហាញចេតនាច្បាស់៖

```cpp
void print(const std::string& text) {
    std::cout << text << '\n';
}
```

## តម្លៃលំនាំដើម (default arguments)

```cpp
void greet(const std::string& name, int times = 1);
```

បើអ្នកហៅ `greet("Sok")` នោះ `times` គឺ `1`។

:::{warning}
តម្លៃលំនាំដើមត្រូវសរសេរតែក្នុងការប្រកាសប៉ុណ្ណោះ។ បើអ្នកសរសេរវាទាំងក្នុងការប្រកាស
និងការកំណត់ នោះជាកំហុសពេលបកប្រែ។
:::

## តារាងសង្ខេប

| របៀប | សរសេរ | កែតម្លៃអ្នកហៅ? | ចម្លងទិន្នន័យ? |
| --- | --- | --- | --- |
| ដោយចម្លង | `int x` | ទេ | បាទ |
| ដោយយោង | `int& x` | បាទ | ទេ |
| ដោយយោងថេរ | `const int& x` | ទេ | ទេ |
| ដោយចង្អុល | `int* x` | បាទ (បើមិន `const`) | ទេ |

## អារេជាប៉ារ៉ាម៉ែត្រ

អារេបាត់បង់ទំហំពេលផ្ដល់ទៅអនុគមន៍ (array decay)។ ដូច្នេះត្រូវផ្ដល់ទំហំដោយឡែក
ឬប្រើ `std::vector` / `std::array`៖

```cpp
void sum(const int values[], int count);
```

## `main` ក៏មានប៉ារ៉ាម៉ែត្រដែរ

```cpp
int main(int argc, char* argv[]) {
    // argc = ចំនួនអាគុយម៉ង់, argv[0] = ឈ្មោះកម្មវិធី
    return 0;
}
```

## កូដឧទាហរណ៍

```{literalinclude} ../../examples/functions/parameters.cpp
:language: cpp
```

លទ្ធផល៖

```text
after value: 1
after reference: 99
hello from const reference
```

## អានបន្ថែម

- [cppreference: functions](https://en.cppreference.com/w/cpp/language/function)
- [cppreference: default arguments](https://en.cppreference.com/w/cpp/language/default_arguments)
