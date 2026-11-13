# ការផ្ទុកលើសអនុគមន៍ (Overloading)

```{translation-meta} functions/overloading
```

ការផ្ទុកលើស (Overloading) គឺការប្រើឈ្មោះអនុគមន៍តែមួយសម្រាប់អនុគមន៍ច្រើន
ដែលមានបញ្ជីប៉ារ៉ាម៉ែត្រខុសគ្នា។ កម្មវិធីបកប្រែជ្រើសរើសអនុគមន៍ត្រឹមត្រូវ
តាមប្រភេទអាគុយម៉ង់។

## ឧទាហរណ៍

```cpp
void show(int value);
void show(double value);
void show(const std::string& value);

show(7);            // ហៅ show(int)
show(2.5);          // ហៅ show(double)
show("text");       // ហៅ show(const std::string&)
```

## អ្វីដែលធ្វើឱ្យខុសគ្នាបាន

- ចំនួនប៉ារ៉ាម៉ែត្រ
- ប្រភេទប៉ារ៉ាម៉ែត្រ
- លំដាប់ប្រភេទប៉ារ៉ាម៉ែត្រ

:::{warning}
**ប្រភេទតម្លៃត្រឡប់មិនអាចបែងចែក overload បានទេ។**

```cpp
int  get();
double get();   // កំហុស: ខុសគ្នាតែប្រភេទត្រឡប់
```
:::

## ការជ្រើសរើស overload

កម្មវិធីបកប្រែជ្រើសអនុគមន៍ដែលត្រូវគ្នាបំផុត តាមលំដាប់៖

1. ត្រូវគ្នាដោយផ្ទាល់ (exact match)
2. ការលើកកម្រិត (promotion) ដូចជា `char` → `int`
3. ការបំប្លែងធម្មតា (conversion) ដូចជា `int` → `double`

បើគ្មានជម្រើសច្បាស់លាស់ វាជាកំហុស **ambiguity**៖

```cpp
void f(long value);
void f(double value);

f(1);   // មិនច្បាស់: int -> long ឬ int -> double?
```

## ជាមួយតម្លៃលំនាំដើម

តម្លៃលំនាំដើមអាចបង្កើតភាពមិនច្បាស់ដែរ៖

```cpp
void draw(int x, int y = 0);
void draw(int x);

draw(5);   // មិនច្បាស់: តើហៅមួយណា?
```

## `const` និង overload

ចំពោះអនុគមន៍សមាជិក គុណលក្ខណៈ `const` អាចបែងចែក overload បាន៖

```cpp
class Buffer {
public:
    char& at(int index);
    const char& at(int index) const;
};
```

## កូដឧទាហរណ៍

```{literalinclude} ../../examples/functions/overloading.cpp
:language: cpp
```

លទ្ធផល៖

```text
int: 7
double: 2.5
string: text
```

## អានបន្ថែម

- [cppreference: overload resolution](https://en.cppreference.com/w/cpp/language/overload_resolution)
