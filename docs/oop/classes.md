# ថ្នាក់ (Classes)

```{translation-meta} oop/classes
```

ថ្នាក់ (class) គឺជាគំរូ (blueprint) ដែលកំណត់ថាវត្ថុនីមួយៗនឹងមានទិន្នន័យអ្វី
និងប្រតិបត្តិការអ្វី។ វាជាមូលដ្ឋាននៃកម្មវិធីនិយមវត្ថុក្នុង C++។

## រូបមន្ត

```cpp
class Rectangle {
public:
    void set_size(int w, int h) {
        width_ = w;
        height_ = h;
    }

    int area() const {
        return width_ * height_;
    }

private:
    int width_ = 0;
    int height_ = 0;
};
```

ធាតុសំខាន់ៗ៖

- **`class`** បង្កើតប្រភេទថ្មី។
- **`public`** និង **`private`** គឺជាកម្រិតចូលដំណើរការ (access specifiers)។
- **សមាជិកទិន្នន័យ** (data members) ដូចជា `width_` និង `height_`។
- **អនុគមន៍សមាជិក** (member functions) ដូចជា `set_size` និង `area`។

## `class` និង `struct`

ភាពខុសគ្នាតែមួយគត់គឺកម្រិតចូលដំណើរការលំនាំដើម៖

- `class` — សមាជិកជា `private` តាមលំនាំដើម។
- `struct` — សមាជិកជា `public` តាមលំនាំដើម។

នៅ C++ គេប្រើ `struct` សម្រាប់បណ្តុំទិន្នន័យសាមញ្ញ និង `class` សម្រាប់ប្រភេទ
ដែលមាន invariant ត្រូវការពារ។

## អនុគមន៍សមាជិក `const`

`const` នៅចុងបញ្ជីប៉ារ៉ាម៉ែត្រ ប្រាប់ថាអនុគមន៍នោះមិនកែសមាជិកទិន្នន័យ៖

```cpp
int area() const;   // អាចហៅលើវត្ថុ const បាន
```

វាជាទម្លាប់ល្អក្នុងការដាក់ `const` លើអនុគមន៍អាន (getters) ទាំងអស់។

## ការចាប់ផ្ដើមសមាជិកនៅក្នុងថ្នាក់ (C++11)

```cpp
class Counter {
    int value_ = 0;   // default member initializer
};
```

លក្ខណៈនេះមានតាំងពី **C++11** ហើយជួយជៀសវាងសមាជិកដែលមានតម្លៃមិនកំណត់។

## កូដឧទាហរណ៍

```{literalinclude} ../../examples/oop/classes.cpp
:language: cpp
```

លទ្ធផល៖

```text
area = 20
```

## អានបន្ថែម

- [cppreference: classes](https://en.cppreference.com/w/cpp/language/classes)
- [cppreference: class declaration](https://en.cppreference.com/w/cpp/language/class)
