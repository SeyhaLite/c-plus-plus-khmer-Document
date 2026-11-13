# រង្វិលជុំ while

```{translation-meta} control-flow/while
```

`while` ប្រតិបត្តិម្តងហើយម្តងទៀត ដរាបណាលក្ខខណ្ឌនៅពិត។ វាសមស្របនៅពេល
អ្នកមិនដឹងចំនួនជុំជាមុន។

## រូបមន្ត

```cpp
while (condition) {
    // ប្រតិបត្តិដរាបណា condition ពិត
}
```

លក្ខខណ្ឌត្រូវពិនិត្យ **មុន** ជុំនីមួយៗ។ បើវាមិនពិតតាំងពីដំបូង ប្លុកកូដ
មិនត្រូវប្រតិបត្តិសោះ។

## ឧទាហរណ៍

```cpp
int n = 987;
int digits = 0;

while (n > 0) {
    n /= 10;
    ++digits;
}
```

រង្វិលជុំនេះរាប់ចំនួនខ្ទង់របស់ `n`។ វាបញ្ចប់ព្រោះ `n` តូចចុះរាល់ជុំ។

## រង្វិលជុំគ្មានទីបញ្ចប់

```cpp
while (true) {
    // ...
    if (should_stop()) {
        break;
    }
}
```

`while (true)` ជាទម្រង់ធម្មតាសម្រាប់រង្វិលជុំដែលឈប់តាមលក្ខខណ្ឌខាងក្នុង។
ត្រូវធានាថាមានផ្លូវចេញ (`break` ឬ `return`) ជានិច្ច។

:::{warning}
កំហុសញឹកញាប់បំផុតគឺភ្លេចធ្វើឱ្យលក្ខខណ្ឌប្រែជាមិនពិត។ ឧទាហរណ៍ បើអ្នកភ្លេច
`++i` ក្នុងរង្វិលជុំ នោះកម្មវិធីនឹងរត់មិនឈប់ (infinite loop)។
:::

## `while` ឬ `for`?

- ដឹងចំនួនជុំ → `for`។
- អាស្រ័យលើលក្ខខណ្ឌដែលមិនដឹងចំនួន → `while`។
- ត្រូវរត់យ៉ាងតិចម្តង → `do-while` (មើល [do-while](do-while.md))។

## កូដឧទាហរណ៍

```{literalinclude} ../../examples/control-flow/while.cpp
:language: cpp
```

លទ្ធផល៖

```text
digits = 3
attempts = 3
```

## អានបន្ថែម

- [cppreference: `while` loop](https://en.cppreference.com/w/cpp/language/while)
