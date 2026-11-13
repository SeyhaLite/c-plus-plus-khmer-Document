# ពហុរូបភាព (Polymorphism)

```{translation-meta} oop/polymorphism
```

ពហុរូបភាព (polymorphism) មានន័យថា «រូបភាពច្រើន»៖ ការហៅដូចគ្នាអាចផ្ដល់
ឥរិយាបថខុសគ្នាអាស្រ័យលើប្រភេទពិតរបស់វត្ថុ។

C++ គាំទ្រពហុរូបភាពតាមពីររបៀប៖

- **Compile-time** — overload អនុគមន៍ និងពុម្ព (templates)។
- **Runtime** — អនុគមន៍និម្មិត (virtual functions)។

ទំព័រនេះផ្ដោតលើ runtime polymorphism។

## អនុគមន៍និម្មិត

```cpp
class Shape {
public:
    virtual ~Shape() = default;
    virtual double area() const = 0;      // pure virtual
};

class Square : public Shape {
public:
    explicit Square(double side) : side_(side) {}
    double area() const override { return side_ * side_; }
private:
    double side_;
};
```

## ការហៅតាមរយៈយោង ឬពោយន្ត័រ

```cpp
Square square(3.0);
Shape& shape = square;        // យោងទៅ base
shape.area();                 // ហៅ Square::area() — dynamic dispatch
```

បើអ្នកហៅតាមតម្លៃ (`Shape shape = square;`) នោះវត្ថុត្រូវកាត់ចោលផ្នែកថ្នាក់កូន
(object slicing) ហើយលទ្ធផលនឹងខុស។

## ឧទាហរណ៍ជាក់ស្តែង

```{literalinclude} ../../examples/oop/polymorphism.cpp
:language: cpp
```

លទ្ធផល៖

```text
square: 9
circle: 3.14159
```

រង្វិលជុំដូចគ្នាហៅ `name()` និង `area()` លើវត្ថុផ្សេងគ្នា ហើយទទួលលទ្ធផលផ្សេងគ្នា។
នេះជាគុណសម្បត្តិចម្បងរបស់ polymorphism៖ កូដថ្មីអាចបន្ថែមដោយមិនកែរង្វិលជុំ។

## overload, override និង hiding

| ពាក្យ | អត្ថន័យ |
| --- | --- |
| **overload** | អនុគមន៍ឈ្មោះដូចគ្នាក្នុងវិសាលភាពតែមួយ ប៉ុន្តែប៉ារ៉ាម៉ែត្រខុសគ្នា |
| **override** | ថ្នាក់កូនកំណត់អនុគមន៍និម្មិតរបស់ base ឡើងវិញ |
| **hiding** | ថ្នាក់កូនប្រកាសអនុគមន៍ឈ្មោះដូចគ្នា ប៉ុន្តែមិនមែន override |

ប្រើ `override` ជានិច្ច (C++11) ដើម្បីឱ្យកម្មវិធីបកប្រែចាប់កំហុសនៅពេលហត្ថលេខាមិនត្រូវ។

## តម្លៃនៃ virtual

ការហៅអនុគមន៍និម្មិតត្រូវរកអនុគមន៍ត្រឹមត្រូវនៅពេលដំណើរការ ដូច្នេះវាមិនអាច
inline បានស្រួលដូចការហៅធម្មតាទេ។ សម្រាប់កូដដែលត្រូវការល្បឿនខ្ពស់បំផុត
សូមវាស់សិន មុននឹងសន្និដ្ឋានថា virtual ជាដែនកំណត់។

## អានបន្ថែម

- [cppreference: `virtual`](https://en.cppreference.com/w/cpp/language/virtual)
- [cppreference: `override`](https://en.cppreference.com/w/cpp/language/override)
