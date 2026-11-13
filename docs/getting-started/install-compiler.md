# ការដំឡើងកម្មវិធីបកប្រែ C++

```{translation-meta} getting-started/install-compiler
```

ដើម្បីសរសេរ និងដំណើរការកម្មវិធី C++ អ្នកត្រូវការកម្មវិធីបកប្រែ (compiler)
មួយ។ កម្មវិធីបកប្រែបំប្លែងកូដ C++ ទៅជាកម្មវិធីដែលដំណើរការបាន។

## Linux (Ubuntu / Debian)

```bash
sudo apt update
sudo apt install build-essential
```

កញ្ចប់ `build-essential` ដំឡើង `g++` និងឧបករណ៍ដែលត្រូវការ។
នៅ Fedora ឬ RHEL សូមប្រើ៖

```bash
sudo dnf install gcc-c++
```

## macOS

```bash
xcode-select --install
```

ពាក្យបញ្ជានេះដំឡើង Command Line Tools ដែលរួមមាន `clang++`។

:::{note}
នៅ macOS ពាក្យបញ្ជា `g++` ជាធម្មតាជា alias ទៅ `clang++` មិនមែន GCC ពិតប្រាកដទេ។
នេះមិនជាបញ្ហាទេ ព្រោះ `clang++` គឺជាកម្មវិធីបកប្រែ C++ ពេញលេញ។
:::

## Windows

ជម្រើសដែលគេប្រើច្រើនបំផុតគឺ **Visual Studio Build Tools** (ឬ Visual Studio)
ជាមួយ workload «Desktop development with C++»។ ក្រោយដំឡើង សូមបើក
«Developer Command Prompt for VS» ហើយពិនិត្យថា `cl` ដំណើរការ។

ជម្រើសទីពីរគឺ **MinGW-w64** ដែលផ្ដល់ `g++` សម្រាប់ Windows។

## ផ្ទៀងផ្ទាត់ការដំឡើង

រត់ពាក្យបញ្ជាមួយក្នុងចំណោមនេះ តាមកម្មវិធីបកប្រែរបស់អ្នក៖

```bash
g++ --version
clang++ --version
cl
```

បើអ្នកឃើញលេខកំណែ (ឧទាហរណ៍ `g++ (Ubuntu 13.3.0) 13.3.0`) នោះការដំឡើងជោគជ័យ។

បន្ទាប់មក ផ្ទៀងផ្ទាត់ថាកម្មវិធីបកប្រែគាំទ្រ C++17 ដោយបកប្រែកម្មវិធីតូចមួយ៖

```{literalinclude} ../../examples/getting-started/install-compiler.cpp
:language: cpp
```

```bash
g++ -std=c++17 -Wall -Wextra check.cpp -o check
./check
```

លទ្ធផលដែលរំពឹង៖

```text
standard macro: 201703
C++17 or newer: ok
```

បើអ្នកឃើញ `C++17 or newer: missing` នោះមានន័យថាអ្នកបានបកប្រែដោយស្តង់ដារចាស់។
សូមប្រើ `-std=c++17` ឬថ្មីជាង។

## បញ្ហាដែលជួបញឹកញាប់

**`g++: command not found`** — កម្មវិធីបកប្រែមិនទាន់ដំឡើង ឬមិននៅក្នុង `PATH`។
សូមដំឡើងឡើងវិញ ឬបើក terminal ថ្មី។

**`error: 'auto' is not allowed here` ឬកំហុសពី C++11** — អ្នកបកប្រែដោយស្តង់ដារ
ចាស់ពេក។ កម្មវិធីបកប្រែចាស់ជាង GCC 4.8 មិនគាំទ្រ C++11 ពេញលេញទេ។
សូមប្រើកម្មវិធីបកប្រែថ្មី (GCC 13 ឬថ្មីជាងនេះគឺជាជម្រើសល្អ)។

**`fatal error: iostream: No such file or directory`** — អ្នកកំពុងប្រើកម្មវិធីបកប្រែ C
(`gcc`) ជំនួស C++ (`g++`)។ សម្រាប់ C++ ត្រូវប្រើ `g++` ឬ `clang++`។

## ជំហានបន្ទាប់

ឥឡូវអ្នកមានកម្មវិធីបកប្រែហើយ។ សូមបន្តទៅ
[កម្មវិធី C++ ដំបូង](first-program.md)។

## អានបន្ថែម

- [isocpp.org: Get Started](https://isocpp.org/get-started)
- [GCC installation instructions](https://gcc.gnu.org/install/)
