# ការគ្រប់គ្រងអង្គចងចាំ

```{translation-meta} advanced/memory-management
```

C++ មិនមាន garbage collector ទេ។ កម្មវិធីជាអ្នកសម្រេចថាពេលណាបង្កើត
និងពេលណាដោះលែងអង្គចងចាំ។ នេះផ្ដល់ការគ្រប់គ្រងពេញលេញ ប៉ុន្តែក៏ជាប្រភពកំហុស
ញឹកញាប់បំផុតដែរ។

## តំបន់ផ្ទុកទិន្នន័យសំខាន់ៗ

| តំបន់ | របៀបបង្កើត | អាយុកាល |
| --- | --- | --- |
| stack | អថេរមូលដ្ឋានក្នុងអនុគមន៍ | ដល់ចុងប្លុក |
| static / global | អថេរកម្រិតឯកសារ ឬ `static` | ដល់ចុងកម្មវិធី |
| heap (free store) | `new` | ដល់ពេល `delete` |
| thread-local | `thread_local` | ដល់ចុងខ្សែស្រឡាយ |

## អាយុកាលលើ stack

```cpp
void work() {
    int local = 5;      // បង្កើតនៅទីនេះ
    // ...
}                       // local ត្រូវបំផ្លាញនៅទីនេះ
```

ការបង្កើត និងការបំផ្លាញលើ stack មានតម្លៃទាបណាស់ ហើយមិនអាចលេចធ្លាយបានទេ។
ដូច្នេះគួរប្រើ stack ជាជម្រើសដំបូងជានិច្ច។

## អាយុកាលលើ heap

```cpp
int* value = new int(7);   // បង្កើត
// ...
delete value;              // ដោះលែង
```

បើអ្នកភ្លេច `delete` នោះអង្គចងចាំត្រូវលេចធ្លាយ (memory leak)។
បើអ្នក `delete` ពីរដង នោះជាឥរិយាបថមិនកំណត់។

:::{warning}
បញ្ហាបីដែលជួបញឹកញាប់បំផុត៖

1. **លេចធ្លាយ** — ភ្លេច `delete`។
2. **ការប្រើបន្ទាប់ពីដោះលែង** (use after free) — ប្រើពោយន្ត័របន្ទាប់ពី `delete`។
3. **ការដោះលែងពីរដង** (double free) — `delete` ពីរដងលើពោយន្ត័រតែមួយ។
:::

## ដំណោះស្រាយ៖ RAII

ជំនួសឱ្យការគ្រប់គ្រងអង្គចងចាំដោយដៃ សូមឱ្យ **វត្ថុ** គ្រប់គ្រងវា៖
បង្កើតនៅ constructor និងដោះលែងនៅ destructor។

```cpp
std::vector<int> values(1000);   // គ្រប់គ្រងអង្គចងចាំដោយខ្លួនឯង
// គ្មាន new គ្មាន delete គ្មានការលេចធ្លាយ
```

នេះជាគំរូដែលគេហៅថា RAII ហើយត្រូវបានពន្យល់លម្អិតនៅ [RAII](raii.md)។

## តើ `new` នៅតែត្រូវការពេលណា?

កម្រណាស់។ ករណីស្របច្បាប់៖

- ពេលបង្កើត object ដែលត្រូវរស់យូរជាងដែនកំណត់ (ប្រើ `std::unique_ptr` ជំនួស)។
- ក្នុងកូដដែលគ្រប់គ្រងធនធានកម្រិតទាប (ឧទាហរណ៍ ការសរសេរធុងទិន្នន័យដោយខ្លួនឯង)។

ក្នុងកូដធម្មតា សូមប្រើធុងទិន្នន័យស្តង់ដារ និង [smart pointers](smart-pointers.md)។

## កូដឧទាហរណ៍

```{literalinclude} ../../examples/advanced/memory-management.cpp
:language: cpp
```

លទ្ធផល៖

```text
id: 1
id: 2
local: 5
heap: 7
```

## អានបន្ថែម

- [cppreference: storage duration](https://en.cppreference.com/w/cpp/language/storage_duration)
- [cppreference: `new` expression](https://en.cppreference.com/w/cpp/language/new)
- [cppreference: `delete` expression](https://en.cppreference.com/w/cpp/language/delete)
