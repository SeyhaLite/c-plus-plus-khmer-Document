# C++ កម្រិតខ្ពស់

ផ្នែកនេះគ្របដណ្ដប់លក្ខណៈដែលធ្វើឱ្យ C++ ខ្លាំង ប៉ុន្តែស្មុគស្មាញ៖ ពោយន្ត័រ និងយោង
ការគ្រប់គ្រងអង្គចងចាំ RAII ពុម្ព ករណីលើកលែង និង concurrency។

## លំដាប់ការអានដែលណែនាំ

1. [ពោយន្ត័រ](pointers.md) និង [យោង](references.md) — មូលដ្ឋាននៃការចូលដល់ទិន្នន័យ។
2. [ការគ្រប់គ្រងអង្គចងចាំ](memory-management.md) — អាយុកាល និងការលេចធ្លាយ។
3. [RAII](raii.md) — គំរូដែលដោះស្រាយបញ្ហាអង្គចងចាំភាគច្រើន។
4. [ការបែងចែកឌីណាមិក](dynamic-allocation.md) និង [Smart Pointers](smart-pointers.md)។

## មេរៀន

```{track-pages} advanced
```

```{toctree}
:hidden:

pointers
references
memory-management
dynamic-allocation
raii
templates
exceptions
move-semantics
smart-pointers
multithreading
concurrency
concepts
modules
coroutines
```

## ចំណាំអំពីស្តង់ដារ

បីទំព័រចុងក្រោយ (concepts, modules, coroutines) ត្រូវការ **C++20**។
បើអ្នកបកប្រែដោយ C++17 វានឹងមិនដំណើរការទេ។ សូមប្រើ
[ជម្រើសស្តង់ដារ](../index.md) នៅរបារខាងឆ្វេង ដើម្បីមើលតែលក្ខណៈដែលអ្នកអាចប្រើ។
