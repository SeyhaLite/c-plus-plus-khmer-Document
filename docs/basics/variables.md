# អថេរ (Variables)

```{translation-meta} basics/variables
```

អថេរ (Variable) គឺជាទីតាំងផ្ទុកទិន្នន័យដែលមានឈ្មោះសម្គាល់។ ឈ្មោះអនុញ្ញាតឱ្យអ្នក
អាន និងកែតម្លៃទិន្នន័យនោះដោយមិនចាំបាច់ដឹងអាសយដ្ឋានអង្គចងចាំ។

## ការប្រកាស និងការចាប់ផ្ដើមតម្លៃ

```cpp
int count;              // ប្រកាសតែប៉ុណ្ណោះ — តម្លៃមិនកំណត់
int a = 10;             // ការចាប់ផ្ដើមតម្លៃដោយចម្លង (copy-initialization)
int b(20);              // ការចាប់ផ្ដើមតម្លៃដោយផ្ទាល់ (direct-initialization)
int c{30};              // ការចាប់ផ្ដើមតម្លៃដោយវង់ក្រចកអង្គុយ (list-initialization)
int d{};                // តម្លៃសូន្យ (value-initialization) — d == 0
```

ចាប់ពី **C++11** ការប្រើវង់ក្រចកអង្គុយ `{}` ត្រូវបានណែនាំ ព្រោះវាមិនអនុញ្ញាត
ការបំប្លែងប្រភេទដែលបាត់បង់ទិន្នន័យ (narrowing) ដោយស្វ័យប្រវត្តិ។
ឧទាហរណ៍ `int x{3.7};` ជាកំហុសពេលបកប្រែ។

:::{warning}
អថេរដែលប្រកាសដោយគ្មានតម្លៃ (`int count;`) មានតម្លៃ **មិនកំណត់** បើវានៅក្នុង
អនុគមន៍។ ការអានតម្លៃនោះគឺជាឥរិយាបថមិនកំណត់ (undefined behavior)។
សូមចាប់ផ្ដើមតម្លៃជានិច្ច។
:::

## វិសាលភាព (scope) និងអាយុកាល (lifetime)

អថេរដែលប្រកាសក្នុងប្លុក `{}` មានវិសាលភាពត្រឹមប្លុកនោះ៖

```cpp
int main() {
    int outer = 1;
    {
        int inner = 2;   // មើលឃើញតែក្នុងប្លុកនេះ
        outer = inner;   // បាន — outer នៅខាងក្រៅ
    }
    // inner មិនអាចប្រើនៅទីនេះបានទេ
    return outer;
}
```

## `auto`

ចាប់ពី **C++11** អ្នកអាចឱ្យកម្មវិធីបកប្រែសន្និដ្ឋានប្រភេទពីតម្លៃចាប់ផ្ដើម៖

```cpp
auto count = 42;        // int
auto ratio = 2.5;       // double
auto letter = 'A';      // char
```

`auto` មិនមែនជាប្រភេទឌីណាមិកទេ។ ប្រភេទត្រូវកំណត់នៅពេលបកប្រែ ហើយមិនផ្លាស់ប្តូរ
នៅពេលដំណើរការឡើយ។

## កូដឧទាហរណ៍

```{literalinclude} ../../examples/basics/variables.cpp
:language: cpp
```

លទ្ធផល៖

```text
count = 3
total = 25.5
label = score
```

## ទម្លាប់ល្អ

- ដាក់ឈ្មោះឱ្យមានអត្ថន័យ៖ `student_count` ល្អជាង `n`។
- ប្រកាសអថេរនៅកន្លែងដែលអ្នកចាប់ផ្ដើមប្រើវា មិនមែនទាំងអស់នៅដើមអនុគមន៍។
- ប្រើ `const` ពេលតម្លៃមិនត្រូវផ្លាស់ប្តូរ (មើល [ថេរ](constants.md))។

## អានបន្ថែម

- [cppreference: declarations](https://en.cppreference.com/w/cpp/language/declarations)
- [cppreference: initialization](https://en.cppreference.com/w/cpp/language/initialization)
