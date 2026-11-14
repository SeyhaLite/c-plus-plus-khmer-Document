# ការដំឡើងកម្មវិធីចងក្រង C++

```{translation-meta} getting-started/install-compiler
```

ដើម្បីសរសេរ និងដំណើរការកម្មវិធី C++ អ្នកត្រូវការកម្មវិធីចងក្រង (compiler)
មួយ។ កម្មវិធីចងក្រងបម្លែងកូដ C++ ទៅជា object code ឬកូដដែលអាចយកទៅភ្ជាប់
បង្កើតកម្មវិធីបាន។

## Linux (Ubuntu / Debian)

```bash
sudo apt update
sudo apt install build-essential
```

កញ្ចប់ `build-essential` ដំឡើង `g++` និងឧបករណ៍សម្រាប់អភិវឌ្ឍកម្មវិធី។
នៅ Fedora ឬ RHEL សូមប្រើ៖

```bash
sudo dnf install gcc-c++
```

## macOS

```bash
xcode-select --install
```

ពាក្យបញ្ជានេះដំឡើង Xcode Command Line Tools ដែលរួមមាន `clang++`។

:::{note}
នៅ macOS ពាក្យបញ្ជា `g++` ដែលមកជាមួយ Xcode Command Line Tools ជាទូទៅ
ជាឈ្មោះហៅទៅកាន់ Clang មិនមែន GNU GCC ទេ។ បើអ្នកចង់បាន GCC ពិតប្រាកដ
ត្រូវដំឡើងវាដាច់ដោយឡែក។
:::

## Windows

មានជម្រើសសំខាន់ពីរ៖

**ជម្រើសទី ១ — MSVC។** ដំឡើង Visual Studio ឬ Visual Studio Build Tools
ហើយជ្រើស workload «Desktop development with C++»។ បន្ទាប់មកបើក
«Developer Command Prompt for VS» ដើម្បីប្រើពាក្យបញ្ជា `cl`។

**ជម្រើសទី ២ — MinGW-w64។** ដំឡើង MinGW-w64 ដែលផ្ដល់ `g++` សម្រាប់ Windows។
ពេលប្រើជម្រើសនេះ ត្រូវប្រាកដថាថត `bin` របស់វាត្រូវបានបន្ថែមទៅ `PATH`។

## ផ្ទៀងផ្ទាត់ការដំឡើង

ជំហាននេះត្រូវអនុវត្តតាមកម្មវិធីចងក្រងដែលអ្នកបានដំឡើង។

### GCC ឬ MinGW-w64

```bash
g++ --version
```

### Clang

```bash
clang++ --version
```

### MSVC

បើក Developer Command Prompt ហើយរត់៖

```bat
cl
```

វានឹងបង្ហាញព័ត៌មានកំណែរបស់ Microsoft C/C++ Compiler។ កុំប្រើពាក្យបញ្ជា
`g++` ដើម្បីផ្ទៀងផ្ទាត់ MSVC លុះត្រាតែអ្នកបានដំឡើង MinGW-w64 ផងដែរ។

## សាកល្បងថាគាំទ្រ C++17

ចម្លងកូដខាងក្រោមទៅក្នុងឯកសារឈ្មោះ `check.cpp`៖

```{literalinclude} ../../examples/getting-started/install-compiler.cpp
:language: cpp
```

### GCC, Clang ឬ MinGW-w64

```bash
g++ -std=c++17 -Wall -Wextra check.cpp -o check
./check
```

បើប្រើ Clang សូមប្ដូរ `g++` ទៅជា `clang++`។

### MSVC

នៅក្នុង Developer Command Prompt៖

```bat
cl /std:c++17 /Zc:__cplusplus /W4 /EHsc check.cpp /Fe:check.exe
check.exe
```

លទ្ធផលដែលរំពឹងសម្រាប់កម្មវិធីចងក្រងទាំងនេះ៖

```text
standard macro: 201703
C++17 or newer: ok
```

បើអ្នកឃើញ `C++17 or newer: missing` សូមពិនិត្យថាអ្នកបានជ្រើស `C++17`
ឬស្តង់ដារថ្មីជាងនេះហើយឬនៅ។ បើប្រើ MSVC សូមរក្សាជម្រើស
`/Zc:__cplusplus` ដើម្បីឱ្យតម្លៃម៉ាក្រូត្រូវតាមស្តង់ដារ។

## បញ្ហាដែលជួបញឹកញាប់

**`g++: command not found`** — GCC មិនទាន់ដំឡើង ឬថត `bin` មិនស្ថិតក្នុង
`PATH`។ សូមដំឡើងកញ្ចប់ត្រឹមត្រូវ ឬកំណត់ `PATH` រួចបើក terminal ថ្មី។

**កូដថ្មីមិនអាចចងក្រងបាន** — ពិនិត្យជម្រើស `-std=c++17` ឬ
`/std:c++17` និងពិនិត្យថាកម្មវិធីចងក្រងមានកំណែដែលគាំទ្រលក្ខណៈនោះ។

**`fatal error: iostream: No such file or directory`** — ជាញឹកញាប់វាបង្ហាញថា
បរិស្ថាន C++ standard library មិនទាន់ដំឡើង ឬកំណត់ត្រឹមត្រូវ។ សូមពិនិត្យ
ការដំឡើង compiler និង C++ standard library របស់អ្នក។ នៅ GCC/MinGW
សូមប្រើ `g++` សម្រាប់កម្មវិធី C++។

## ជំហានបន្ទាប់

ឥឡូវអ្នកមានកម្មវិធីចងក្រងហើយ។ សូមបន្តទៅ
[កម្មវិធី C++ ដំបូង](first-program.md)។

## អានបន្ថែម

- [isocpp.org: Get Started](https://isocpp.org/get-started)
- [GCC installation instructions](https://gcc.gnu.org/install/)
- [Microsoft C++ installation guide](https://learn.microsoft.com/en-us/cpp/build/vscpp-step-0-installation)
