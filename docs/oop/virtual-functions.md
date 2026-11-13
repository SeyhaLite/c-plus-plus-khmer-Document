# អនុគមន៍និម្មិត (Virtual Functions)

```{translation-meta} oop/virtual-functions
```

អនុគមន៍និម្មិត (virtual function) គឺជាអនុគមន៍សមាជិកដែលការហៅរបស់វាត្រូវសម្រេច
នៅពេលដំណើរការ ដោយផ្អែកលើប្រភេទពិតរបស់វត្ថុ។ នេះជាយន្តការសម្រាប់
runtime polymorphism។

## ការភ្ជាប់ឋិតិវន្ត និងឌីណាមិក

```cpp
class Base {
public:
    virtual ~Base() = default;
    virtual std::string speak() const { return "base"; }
    std::string static_speak() const { return "base-static"; }
};

class Derived : public Base {
public:
    std::string speak() const override { return "derived"; }
    std::string static_speak() const { return "derived-static"; }
};
```

```cpp
Derived d;
Base& ref = d;

ref.speak();          // "derived"  — dynamic binding (virtual)
ref.static_speak();   // "base-static" — static binding (មិន virtual)
```

## `override` និង `final`

```cpp
class Derived : public Base {
public:
    std::string speak() const override;   // ត្រូវតែ override អនុគមន៍និម្មិត
};

class Leaf final : public Derived { };    // មិនអាចទទួលមរតកបន្ត
```

ប្រើ `override` ជានិច្ច។ បើហត្ថលេខាមិនត្រូវ (ឧទាហរណ៍ ភ្លេច `const`)
កម្មវិធីបកប្រែនឹងរាយការណ៍ជំនួសឱ្យបង្កើតអនុគមន៍ថ្មីស្ងាត់ៗ។

## Object slicing

```cpp
Derived d;
Base value = d;    // កាត់ផ្នែក Derived ចោល
value.speak();     // "base"
```

នេះជាហេតុផលដែលគេផ្ដល់វត្ថុ polymorphic តាមយោង ឬពោយន្ត័រ មិនមែនតាមតម្លៃ។

## អ្នកបំផ្លាញនិម្មិត

បើថ្នាក់មួយត្រូវប្រើជា base សម្រាប់ការលុបតាមពោយន្ត័រ អ្នកបំផ្លាញ **ត្រូវ** ជា virtual៖

```cpp
class Base {
public:
    virtual ~Base() = default;
};
```

បើមិនដូច្នេះ `delete` តាម `Base*` នឹងមិនហៅអ្នកបំផ្លាញរបស់ថ្នាក់កូន
ដែលជាឥរិយាបថមិនកំណត់។

## ការហៅ virtual ក្នុង constructor/destructor

:::{warning}
ក្នុងអំឡុងពេលបង្កើត ឬបំផ្លាញវត្ថុ ការហៅអនុគមន៍និម្មិត **មិន** ទៅដល់ថ្នាក់កូនទេ។
វាត្រូវដោះស្រាយទៅថ្នាក់បច្ចុប្បន្នដែលកំពុងត្រូវបង្កើត/បំផ្លាញ។ ដូច្នេះកុំពឹងលើ
polymorphism ក្នុង constructor ឬ destructor។
:::

## តម្លៃ

ការហៅអនុគមន៍និម្មិតត្រូវរកអនុគមន៍ត្រឹមត្រូវនៅពេលដំណើរការ (ជាទូទៅតាម
តារាងអនុគមន៍និម្មិត — implementation detail ដែលស្តង់ដារមិនកំណត់)។
នេះអាចរារាំងការ inline ហើយធ្វើឱ្យវត្ថុធំជាងបន្តិច។

## កូដឧទាហរណ៍

```{literalinclude} ../../examples/oop/virtual-functions.cpp
:language: cpp
```

លទ្ធផល៖

```text
virtual: derived
non-virtual: base-static
sliced: base
```

## អានបន្ថែម

- [cppreference: `virtual`](https://en.cppreference.com/w/cpp/language/virtual)
- [cppreference: `final`](https://en.cppreference.com/w/cpp/language/final)
