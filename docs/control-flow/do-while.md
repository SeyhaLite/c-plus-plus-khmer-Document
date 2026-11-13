# រង្វិលជុំ do-while

```{translation-meta} control-flow/do-while
```

`do-while` ប្រតិបត្តិប្លុកកូដ **យ៉ាងតិចម្តង** រួចទើបពិនិត្យលក្ខខណ្ឌ។
វាសមស្របនៅពេលអ្នកត្រូវធ្វើអ្វីមួយម្តងជាមុន រួចទើបសម្រេចថាបន្តឬឈប់។

## រូបមន្ត

```cpp
do {
    // ប្រតិបត្តិយ៉ាងតិចម្តង
} while (condition);
```

:::{warning}
ត្រូវមានសញ្ញា `;` បន្ទាប់ពី `while (condition)`។ ការភ្លេចវាជាកំហុសវាក្យសម្ព័ន្ធ
ដែលអានយល់ខុសបានយ៉ាងឆាប់រហ័ស។
:::

## ភាពខុសគ្នាពី `while`

```cpp
int a = 10;
while (a < 5) {
    std::cout << "never printed\n";   // មិនរត់សោះ
}

int b = 10;
do {
    std::cout << "printed once\n";    // រត់ម្តង
} while (b < 5);
```

## ការប្រើប្រាស់ធម្មតា

`do-while` សមស្របសម្រាប់ការអានទិន្នន័យចូល ហើយពិនិត្យថាត្រឹមត្រូវ ដូចជា៖

```cpp
int value = 0;
do {
    std::cout << "Enter a positive number: ";
    std::cin >> value;
} while (value <= 0);
```

ឬសម្រាប់ menu ដែលត្រូវបង្ហាញយ៉ាងតិចម្តង៖

```cpp
int choice = 0;
do {
    show_menu();
    std::cin >> choice;
} while (choice != 0);
```

## កូដឧទាហរណ៍

```{literalinclude} ../../examples/control-flow/do-while.cpp
:language: cpp
```

លទ្ធផល៖

```text
accepted = 5
i = 3
```

ឧទាហរណ៍នេះអានលេខពី `std::istringstream` រហូតជួបលេខវិជ្ជមានដំបូង។
វាបង្ហាញថា `do-while` ធានាការអានយ៉ាងតិចម្តង ទោះតម្លៃដំបូងមិនត្រឹមត្រូវក៏ដោយ។

## អានបន្ថែម

- [cppreference: `do`-`while` loop](https://en.cppreference.com/w/cpp/language/do)
