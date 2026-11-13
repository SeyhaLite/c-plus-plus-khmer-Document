# break, continue និង goto

```{translation-meta} control-flow/jump-statements
```

សេចក្តីថ្លែងការណ៍លោត (jump statements) ផ្លាស់ប្តូរលំហូរបញ្ជាធម្មតា។
C++ មាន `break`, `continue`, `return` និង `goto`។

## `break`

`break` ចាកចេញពីរង្វិលជុំ ឬ `switch` ដែលនៅជិតបំផុត។

```cpp
for (int i = 0; i < 10; ++i) {
    if (i == 4) {
        break;      // ឈប់រង្វិលជុំទាំងស្រុង
    }
    std::cout << i << '\n';   // បង្ហាញ 0 1 2 3
}
```

## `continue`

`continue` រំលងជុំបច្ចុប្បន្ន ហើយបន្តទៅជុំបន្ទាប់។

```cpp
for (int i = 0; i < 5; ++i) {
    if (i % 2 == 0) {
        continue;    // រំលងលេខគូ
    }
    std::cout << i << '\n';   // បង្ហាញ 1 3
}
```

## `return`

`return` ចាកចេញពីអនុគមន៍ទាំងស្រុង ហើយត្រឡប់តម្លៃ (បើមាន)។
វាជាវិធីស្អាតបំផុតក្នុងការបញ្ចប់ការស្វែងរកនៅពេលជួបលទ្ធផល៖

```cpp
int first_negative(const int values[], int count) {
    for (int i = 0; i < count; ++i) {
        if (values[i] < 0) {
            return i;
        }
    }
    return -1;
}
```

## `goto` — ជៀសវាង

`goto` លោតទៅ label ក្នុងអនុគមន៍តែមួយ។ វាធ្វើឱ្យកូដអានយល់ខ្លាំង និងពិបាកតាមដាន។
C++ មានរចនាសម្ព័ន្ធដែលជំនួសបានល្អជាង (រង្វិលជុំ `break`, អនុគមន៍ `return`,
ករណីលើកលែង)។ ករណីតែមួយដែលគេពិចារណាប្រើ `goto` គឺការចាកចេញពី
រង្វិលជុំជាន់គ្នាច្រើនជាន់។

```cpp
for (int i = 0; i < 3; ++i) {
    for (int j = 0; j < 3; ++j) {
        if (i * j == 4) {
            goto done;   // ចេញពីរង្វិលជុំទាំងពីរ
        }
    }
}
done:
```

ជម្រើសល្អជាងគឺដាក់រង្វិលជុំក្នុងអនុគមន៍ ហើយប្រើ `return`។

:::{note}
`break` ក្នុងរង្វិលជុំជាន់គ្នា ចេញតែរង្វិលជុំខាងក្នុងប៉ុណ្ណោះ។
បើអ្នកចង់ចេញពីទាំងអស់ សូមប្រើ `return` ពីអនុគមន៍ ឬ flag។
:::

## កូដឧទាហរណ៍

```{literalinclude} ../../examples/control-flow/jump-statements.cpp
:language: cpp
```

លទ្ធផល៖

```text
i=0
i=1
i=3
first negative index = 2
```

## អានបន្ថែម

- [cppreference: `break`](https://en.cppreference.com/w/cpp/language/break)
- [cppreference: `continue`](https://en.cppreference.com/w/cpp/language/continue)
- [cppreference: `goto`](https://en.cppreference.com/w/cpp/language/goto)
