# GCC, Clang និង MSVC

```{translation-meta} getting-started/compilers
```

កម្មវិធីចងក្រង C++ (C++ compilers) មានច្រើនប្រភេទ។ GCC, Clang និង MSVC
ជាជម្រើសដែលគេប្រើជាញឹកញាប់។ ពួកវាខុសគ្នាខាងប្រព័ន្ធប្រតិបត្តិការ ពាក្យបញ្ជា
កំណែ និងកម្រិតគាំទ្រលក្ខណៈពិសេសរបស់ C++។

## ការប្រៀបធៀបខ្លី

| កម្មវិធីចងក្រង | ពាក្យបញ្ជា | ប្រព័ន្ធដែលប្រើជាញឹកញាប់ | ចំណុចសំខាន់ |
| --- | --- | --- | --- |
| GCC | `g++` | Linux, Windows (MinGW-w64), macOS តាមការដំឡើងដាច់ដោយឡែក | គម្រោង open source និងមានការប្រើប្រាស់ទូលំទូលាយ |
| Clang | `clang++` | macOS, Linux, Windows | សារកំហុសងាយអាន និងស្ថិតក្នុងគម្រោង LLVM |
| MSVC | `cl` | Windows | រួមបញ្ចូលជាមួយ Visual Studio និង Windows SDK |

## កំណែថ្មីៗដែលបានផ្ទៀងផ្ទាត់

ព័ត៌មាននេះត្រូវបានពិនិត្យតាមគេហទំព័រផ្លូវការនៅថ្ងៃទី **14 ខែវិច្ឆិកា ឆ្នាំ 2026**។
វាជាលេខកំណែចេញផ្សាយរបស់គម្រោង មិនមែនមានន័យថាប្រព័ន្ធប្រតិបត្តិការរបស់អ្នក
បានដំឡើងកំណែទាំងនេះរួចហើយទេ។

| គម្រោង | កំណែដែលបានចេញផ្សាយចុងក្រោយដែលបានពិនិត្យ | កំណត់សម្គាល់ |
| --- | --- | --- |
| GCC | **16.2** (7 សីហា 2026) | GCC 17 នៅតែជាសាខាកំពុងអភិវឌ្ឍនៅកាលបរិច្ឆេទនេះ |
| LLVM / Clang | **23.1.5** (3 វិច្ឆិកា 2026) | Clang ជាផ្នែកមួយនៃការចេញផ្សាយ LLVM |
| MSVC Build Tools | **14.51** | កំណែ stable សម្រាប់ Visual Studio 2026; ព័ត៌មានលម្អិតស្ថិតក្នុង release notes |

ចំនួនកំណែថ្មីមិនប្រាប់ថាកម្មវិធីចងក្រងគាំទ្រលក្ខណៈ C++ ទាំងអស់ទេ។
ការគាំទ្រត្រូវពិនិត្យតាមលក្ខណៈនីមួយៗ និងតាមកំណែរបស់ standard library ផងដែរ។
សម្រាប់ការងារពិត សូមពិនិត្យតារាង conformance របស់គម្រោងមុនជ្រើសរើសលក្ខណៈថ្មី។

## GCC (GNU Compiler Collection)

GCC ជាកម្មវិធីចងក្រងដែលប្រើទូលំទូលាយនៅលើ Linux។ ពាក្យបញ្ជាសម្រាប់ C++ គឺ
`g++`។ បណ្ណាល័យស្តង់ដារដែលប្រើជាមួយ GCC ជាទូទៅគឺ **libstdc++**។

```bash
g++ -std=c++20 -Wall -Wextra main.cpp -o main
```

## Clang (LLVM)

Clang ជាកម្មវិធីចងក្រងក្នុងគម្រោង LLVM។ នៅ macOS វាមកជាមួយ Xcode
Command Line Tools។ នៅ Linux និង Windows អ្នកអាចដំឡើង Clang ដាច់ដោយឡែក។
នៅ Linux Clang អាចប្រើ **libstdc++** ឬ **libc++** អាស្រ័យលើការដំឡើង។
នៅ macOS ជាទូទៅវាប្រើ **libc++**។

```bash
clang++ -std=c++20 -Wall -Wextra main.cpp -o main
```

## MSVC (Microsoft C++)

MSVC ជាកម្មវិធីចងក្រងរបស់ Microsoft សម្រាប់ Windows។ ពាក្យបញ្ជាគឺ `cl`
ហើយគួររត់ក្នុង «Developer Command Prompt for VS»។ ទម្រង់ជម្រើសរបស់វាខុសពី
GCC និង Clang៖

| គោលបំណង | GCC / Clang | MSVC |
| --- | --- | --- |
| ជ្រើសស្តង់ដារ | `-std=c++20` | `/std:c++20` |
| បើកការព្រមាន | `-Wall -Wextra` | `/W4` |
| បង្កើនប្រសិទ្ធភាព | `-O2` | `/O2` |
| ព័ត៌មាន debug | `-g` | `/Zi` |
| កំណត់ឈ្មោះឯកសារចេញ | `-o main` | `/Fe:main.exe` |

```bat
cl /std:c++20 /W4 /EHsc main.cpp /Fe:main.exe
main.exe
```

:::{warning}
MSVC មិនកំណត់ `__cplusplus` តាមស្តង់ដារបច្ចុប្បន្នដោយលំនាំដើមទេ។
ប្រើ `/Zc:__cplusplus` បើកូដរបស់អ្នកពិនិត្យម៉ាក្រូនេះ។ ជម្រើសនេះត្រូវបាន
ប្រើក្នុងឧទាហរណ៍ផ្ទៀងផ្ទាត់ C++17 នៅមេរៀនមុន។
:::

## តើគួរជ្រើសមួយណា?

- **Linux:** ចាប់ផ្ដើមដោយ GCC (`g++`) ឬ Clang (`clang++`) ដែលមានក្នុង distribution របស់អ្នក។
- **macOS:** ចាប់ផ្ដើមដោយ Clang ដែលបានមកជាមួយ Xcode Command Line Tools។
- **Windows:** MSVC តាម Visual Studio ងាយស្រួលសម្រាប់ការចាប់ផ្ដើម។ MinGW-w64 ក៏ជាជម្រើសបានដែរ។

សំខាន់ជាងការជ្រើសឈ្មោះ compiler គឺត្រូវជ្រើសស្តង់ដារ C++ ដែលកូដត្រូវការ
និងពិនិត្យថាកំណែ compiler និង standard library របស់អ្នកគាំទ្រលក្ខណៈនោះ។

## កម្មវិធីឧទាហរណ៍៖ ស្គាល់កម្មវិធីចងក្រងរបស់អ្នក

```{literalinclude} ../../examples/getting-started/compilers.cpp
:language: cpp
```

លទ្ធផលនៅពេលចងក្រងដោយ GCC និងប្រើ C++17៖

```text
compiler family: GCC
standard: 201703
```

កម្មវិធីនេះប្រើម៉ាក្រូដែលកម្មវិធីចងក្រងកំណត់ដោយខ្លួនឯង
(`__clang__`, `__GNUC__`, `_MSC_VER`) ដើម្បីស្គាល់គ្រួសាររបស់វា។
លទ្ធផលអាចខុសគ្នាតាម compiler ដែលអ្នកប្រើ។

## ប្រភពសម្រាប់ពិនិត្យកំណែ និងការគាំទ្រ

- [GCC — supported releases](https://gcc.gnu.org/)
- [GCC — release history](https://gcc.gnu.org/releases.html)
- [LLVM — latest release](https://github.com/llvm/llvm-project/releases)
- [MSVC — compiler versions](https://learn.microsoft.com/en-us/cpp/overview/compiler-versions)
- [Visual Studio 2026 — release notes](https://learn.microsoft.com/en-us/visualstudio/releases/2026/release-notes)
- [C++ compiler support](https://en.cppreference.com/w/cpp/compiler_support)
