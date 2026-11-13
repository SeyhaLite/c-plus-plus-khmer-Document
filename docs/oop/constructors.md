# អ្នកសាងសង់ (Constructors)

```{translation-meta} oop/constructors
```

អ្នកសាងសង់ (constructor) គឺជាអនុគមន៍ពិសេសដែលត្រូវហៅដោយស្វ័យប្រវត្តិនៅពេល
បង្កើតវត្ថុ។ វាមានឈ្មោះដូចថ្នាក់ និងគ្មានប្រភេទតម្លៃត្រឡប់។

## រូបមន្ត

```cpp
class Person {
public:
    Person() = default;                       // អ្នកសាងសង់លំនាំដើម
    Person(std::string name, int age);        // អ្នកសាងសង់មានប៉ារ៉ាម៉ែត្រ

private:
    std::string name_;
    int age_ = 0;
};
```

## បញ្ជីចាប់ផ្ដើមសមាជិក (member initializer list)

```cpp
Person::Person(std::string name, int age)
    : name_(std::move(name)), age_(age) {
    // តួអង្គកម្មវិធី
}
```

ការចាប់ផ្ដើមសមាជិកនៅក្នុងបញ្ជី `:` គឺជាការចាប់ផ្ដើមផ្ទាល់ មិនមែនការដាក់តម្លៃ
ក្រោយការបង្កើតទេ។ វាជាវិធីតែមួយគត់សម្រាប់សមាជិក `const` និងយោង (reference)។
លំដាប់នៃការចាប់ផ្ដើមគឺតាមលំដាប់ប្រកាសសមាជិកក្នុងថ្នាក់ មិនមែនតាមលំដាប់ក្នុងបញ្ជីទេ។

## អ្នកសាងសង់បន្ត (delegating constructor, C++11)

```cpp
Person(std::string name) : Person(std::move(name), 0) {}
```

អ្នកសាងសង់មួយអាចហៅអ្នកសាងសង់ផ្សេងក្នុងថ្នាក់តែមួយ ដើម្បីជៀសវាងការសរសេរស្ទួន។

## `explicit`

```cpp
class Meter {
public:
    explicit Meter(double value) : value_(value) {}
private:
    double value_;
};
```

បើគ្មាន `explicit` ទេ កម្មវិធីបកប្រែអាចបំប្លែង `double` ទៅ `Meter` ដោយស្វ័យប្រវត្តិ
ដែលអាចបង្កកំហុសដែលពិបាករក។ សូមប្រើ `explicit` លើអ្នកសាងសង់មួយប៉ារ៉ាម៉ែត្រ
ជាធម្មតា។

## អ្នកសាងសង់លំនាំដើម

បើអ្នកមិនសរសេរអ្នកសាងសង់ណាមួយទេ កម្មវិធីបកប្រែបង្កើតអ្នកសាងសង់លំនាំដើម
ឱ្យដោយស្វ័យប្រវត្តិ។ ប៉ុន្តែបើអ្នកសរសេរអ្នកសាងសង់ផ្សេង អ្នកសាងសង់លំនាំដើម
នឹងមិនត្រូវបង្កើតទេ លុះត្រាតែអ្នកសរសេរ `= default`។

## កូដឧទាហរណ៍

```{literalinclude} ../../examples/oop/constructors.cpp
:language: cpp
```

លទ្ធផល៖

```text
unknown (0)
Sok (21)
Dara (0)
```

## អានបន្ថែម

- [cppreference: constructors](https://en.cppreference.com/w/cpp/language/constructor)
- [cppreference: default constructor](https://en.cppreference.com/w/cpp/language/default_constructor)
