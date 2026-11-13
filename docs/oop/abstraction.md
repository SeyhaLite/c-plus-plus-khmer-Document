# អរូបីកម្ម (Abstraction)

```{translation-meta} oop/abstraction
```

អរូបីកម្ម (abstraction) គឺការបង្ហាញតែអ្វីដែលចាំបាច់ ហើយលាក់ព័ត៌មានលម្អិត។
នៅ C++ គេធ្វើវាដោយ **ថ្នាក់អរូបី** (abstract class) ដែលមានអនុគមន៍
**និម្មិតសុទ្ធ** (pure virtual)។

## អនុគមន៍និម្មិតសុទ្ធ

```cpp
class Logger {
public:
    virtual ~Logger() = default;
    virtual void log(const std::string& message) = 0;   // = 0 មានន័យថា pure
};
```

ថ្នាក់ដែលមានអនុគមន៍និម្មិតសុទ្ធយ៉ាងតិចមួយ គឺជាថ្នាក់អរូបី។ អ្នក **មិនអាច**
បង្កើតវត្ថុពីវាដោយផ្ទាល់បានទេ៖

```cpp
Logger logger;      // កំហុសពេលបកប្រែ
```

## ការអនុវត្ត

```cpp
class ConsoleLogger : public Logger {
public:
    void log(const std::string& message) override {
        std::cout << "[console] " << message << '\n';
    }
};
```

## ការសរសេរកូដតាមចំណុចប្រទាក់

អនុគមន៍ដែលទទួល `Logger&` មិនខ្វល់ថាជា logger ប្រភេទណាទេ៖

```cpp
void run(Logger& logger) {
    logger.log("started");
}
```

នេះជាគោលការណ៍ «program to an interface, not an implementation»។
អ្នកអាចបន្ថែម `FileLogger` ថ្មីដោយមិនកែ `run` សោះ។

## ថ្នាក់អរូបី និង destructor

ថ្នាក់អរូបីដែលមានអនុគមន៍និម្មិតសុទ្ធ **គួរ** មានអ្នកបំផ្លាញនិម្មិត (`virtual ~Logger() = default;`)
ដើម្បីឱ្យការលុបតាមពោយន្ត័រទៅថ្នាក់មូលដ្ឋានមានសុវត្ថិភាព។

:::{note}
ថ្នាក់អរូបីអាចមានសមាជិកទិន្នន័យ និងអនុគមន៍ដែលបានកំណត់រួចដែរ។
វាមិនចាំបាច់ជា «interface សុទ្ធ» ដូចភាសាខ្លះទេ។
:::

## កូដឧទាហរណ៍

```{literalinclude} ../../examples/oop/abstraction.cpp
:language: cpp
```

លទ្ធផល៖

```text
[console] started
[file] started
```

## អានបន្ថែម

- [cppreference: abstract classes](https://en.cppreference.com/w/cpp/language/abstract_class)
- [cppreference: `virtual`](https://en.cppreference.com/w/cpp/language/virtual)
