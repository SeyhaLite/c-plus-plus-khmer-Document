# មរតក (Inheritance)

```{translation-meta} oop/inheritance
```

មរតក (inheritance) អនុញ្ញាតឱ្យថ្នាក់ថ្មី (ថ្នាក់កូន, derived) ទទួលសមាជិកពីថ្នាក់ដែល
មានស្រាប់ (ថ្នាក់មូលដ្ឋាន, base)។

## រូបមន្ត

```cpp
class Animal {
public:
    void eat() const { std::cout << "eating\n"; }
};

class Dog : public Animal {
public:
    void bark() const { std::cout << "barking\n"; }
};
```

`Dog` មានទាំង `eat()` និង `bark()`។

## ការចាប់ផ្ដើមថ្នាក់មូលដ្ឋាន

ថ្នាក់មូលដ្ឋានត្រូវបានបង្កើត **មុន** សមាជិកថ្នាក់កូន ហើយត្រូវបំផ្លាញ **ក្រោយ**
គេ៖

```cpp
class Dog : public Animal {
public:
    Dog() : Animal() {      // ហៅ constructor របស់ base មុន
        std::cout << "Dog created\n";
    }
};
```

បើថ្នាក់មូលដ្ឋានមាន constructor ដែលត្រូវការប៉ារ៉ាម៉ែត្រ អ្នកត្រូវហៅវាក្នុង
បញ្ជីចាប់ផ្ដើមសមាជិក៖ `Dog(std::string name) : Animal(std::move(name)) {}`។

## កម្រិតចូលដំណើរការ

`protected` មានន័យថាថ្នាក់កូនអាចចូលបាន ប៉ុន្តែអ្នកខាងក្រៅមិនអាច។

| ការទទួលមរតក | `public` នៅ base | `protected` នៅ base |
| --- | --- | --- |
| `public` | `public` | `protected` |
| `protected` | `protected` | `protected` |
| `private` | `private` | `private` |

ការទទួលមរតកបែប `public` គឺជាទម្រង់ដែលគេប្រើស្ទើរតែទាំងអស់។

:::{warning}
បើអ្នកនឹងលុបវត្ថុថ្នាក់កូនតាមរយៈពោយន្ត័រទៅថ្នាក់មូលដ្ឋាន អ្នកបំផ្លាញរបស់ថ្នាក់មូលដ្ឋាន
**ត្រូវ** ជា `virtual`។ បើមិនដូច្នេះ ឥរិយាបថគឺមិនកំណត់។
:::

## `final` (C++11)

```cpp
class Dog final : public Animal { };    // មិនអាចទទួលមរតកបន្ត
class Cat : public Dog { };             // កំហុសពេលបកប្រែ
```

## មរតកច្រើនថ្នាក់

C++ គាំទ្រការទទួលមរតកពីច្រើនថ្នាក់ក្នុងពេលតែមួយ (`class C : public A, public B`)។
វាមានប្រយោជន៍ក្នុងករណីខ្លះ ប៉ុន្តែអាចបង្កភាពស្មុគស្មាញ (ដូចជា diamond problem)។
ជាធម្មតា ការប្រើ composition គឺច្បាស់លាស់ជាង។

## កូដឧទាហរណ៍

```{literalinclude} ../../examples/oop/inheritance.cpp
:language: cpp
```

លទ្ធផល៖

```text
Animal(Rex)
Dog()
Rex eats
Rex barks
name: Rex
~Dog()
~Animal(Rex)
```

## អានបន្ថែម

- [cppreference: derived classes](https://en.cppreference.com/w/cpp/language/derived_class)
- [cppreference: access specifiers](https://en.cppreference.com/w/cpp/language/access)
