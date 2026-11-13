# GCC, Clang និង MSVC

```{translation-meta} getting-started/compilers
```

កម្មវិធីបកប្រែ C++ សំខាន់ៗមានបីគ្រួសារ។ ទាំងបីបកប្រែ C++ ស្តង់ដារ ប៉ុន្តែ
ខុសគ្នាខាងពាក្យបញ្ជា វេទិកា និងកម្រិតគាំទ្រលក្ខណៈថ្មីៗ។

## ការប្រៀបធៀបខ្លី

| កម្មវិធីបកប្រែ | ពាក្យបញ្ជា | វេទិកា | ចំណុចលេចធ្លោ |
| --- | --- | --- | --- |
| GCC | `g++` | Linux, Windows (MinGW), macOS | ស្តង់ដារបើកចំហ ប្រើយូរណាស់មកហើយ |
| Clang | `clang++` | macOS, Linux, Windows | សារកំហុសច្បាស់លាស់ ល្បឿនបកប្រែលឿន |
| MSVC | `cl` | Windows | រួមបញ្ចូលជាមួយ Visual Studio |

## GCC (GNU Compiler Collection)

GCC ជាកម្មវិធីបកប្រែស្តង់ដារនៅ Linux ភាគច្រើន។ ពាក្យបញ្ជាសម្រាប់ C++ គឺ `g++`។
GCC 13 និង 14 គាំទ្រ C++20 ស្ទើរតែទាំងស្រុង និង C++23 មួយផ្នែក។
បណ្ណាល័យស្តង់ដារដែលភ្ជាប់មកជាមួយគឺ **libstdc++**។

```bash
g++ -std=c++20 -Wall -Wextra main.cpp -o main
```

## Clang (LLVM)

Clang ជាកម្មវិធីបកប្រែលំនាំដើមរបស់ macOS (តាមរយៈ Xcode Command Line Tools)។
វាត្រូវបានគេស្គាល់ដោយសារសារកំហុសដែលអានងាយ និងឧបករណ៍វិភាគកូដល្អ។
នៅ Linux វាប្រើ **libstdc++** ជាធម្មតា ហើយនៅ macOS ប្រើ **libc++**។

```bash
clang++ -std=c++20 -Wall -Wextra main.cpp -o main
```

## MSVC (Microsoft Visual C++)

MSVC ជាកម្មវិធីបកប្រែរបស់ Microsoft សម្រាប់ Windows។ ពាក្យបញ្ជាគឺ `cl`
ហើយត្រូវប្រើក្នុង «Developer Command Prompt»។ MSVC ប្រើទម្រង់ពាក្យបញ្ជាផ្សេង
ពី GCC/Clang៖

| គោលបំណង | GCC / Clang | MSVC |
| --- | --- | --- |
| ជ្រើសស្តង់ដារ | `-std=c++20` | `/std:c++20` |
| បើកការព្រមាន | `-Wall -Wextra` | `/W4` |
| បង្កើនប្រសិទ្ធភាព | `-O2` | `/O2` |
| ព័ត៌មាន debug | `-g` | `/Zi` |
| កំណត់ឈ្មោះឯកសារចេញ | `-o main` | `/Fe:main.exe` |

```bat
cl /std:c++20 /W4 /EHsc main.cpp
```

:::{warning}
MSVC មិនកំណត់ `__cplusplus` ត្រឹមត្រូវតាមលំនាំដើមទេ។ ប្រើ `/Zc:__cplusplus`
បើកូដរបស់អ្នកពិនិត្យម៉ាក្រូនេះ។
:::

## តើគួរជ្រើសមួយណា?

- បើអ្នកនៅ Linux៖ `g++` ឬ `clang++` ទាំងពីរល្អ។ ចាប់ផ្ដើមដោយ `g++` ព្រោះវាមានស្រាប់។
- បើអ្នកនៅ macOS៖ `clang++` (បានមកជាមួយ Command Line Tools)។
- បើអ្នកនៅ Windows៖ MSVC ងាយស្រួលបំផុតសម្រាប់អ្នកចាប់ផ្ដើម។

អ្វីដែលសំខាន់ជាងការជ្រើសរើសគឺ **ស្តង់ដារ** ដែលអ្នកបកប្រែ។ កូដក្នុងឯកសារនេះ
បញ្ជាក់ស្តង់ដារអប្បបរមានៅខាងលើរាល់ទំព័រ ដូច្នេះអ្នកដឹងថាត្រូវប្រើ `-std=` អ្វី។

## កម្មវិធីឧទាហរណ៍៖ ស្គាល់កម្មវិធីបកប្រែរបស់អ្នក

```{literalinclude} ../../examples/getting-started/compilers.cpp
:language: cpp
```

លទ្ធផលនៅពេលបកប្រែដោយ `g++`៖

```text
compiler family: GCC
standard: 201703
```

កម្មវិធីនេះប្រើម៉ាក្រូដែលកម្មវិធីបកប្រែកំណត់ដោយខ្លួនឯង (`__clang__`, `__GNUC__`,
`_MSC_VER`) ដើម្បីស្គាល់គ្រួសាររបស់ខ្លួន។ នេះជាបច្ចេកទេសដែលគេប្រើពិត
ក្នុងបណ្ណាល័យឆ្លងវេទិកា។

## អានបន្ថែម

- [GCC](https://gcc.gnu.org/)
- [Clang / LLVM](https://clang.llvm.org/)
- [MSVC — ការដំឡើង](https://learn.microsoft.com/en-us/cpp/build/vscpp-step-0-installation)
