# ខ្សែអក្សរ (std::string)

```{translation-meta} stdlib/strings
```

`std::string` គឺជាធុងទិន្នន័យសម្រាប់ខ្សែអក្សរដែលគ្រប់គ្រងអង្គចងចាំដោយស្វ័យប្រវត្តិ។
វាទទួលបានការប្រើប្រាស់ច្រើនជាង `char*` ព្រោះវាផ្ដល់សុវត្ថិភាព និងប្រតិបត្តិការស្រេច។

## ការប្រតិបត្តិការសាមញ្ញ

```cpp
std::string text = "Hello";
text += " World";              // បន្ថែម
text.size();                   // ប្រវែង
text.empty();                  // ទទេឬអត់
text.front();                  // តួអក្សរដំបូង
text.back();                   // តួអក្សរចុងក្រោយ
text.substr(6, 5);             // "World"
text.find("World");            // 6 (ឬ npos បើមិនឃើញ)
text.replace(0, 5, "Hi");      // "Hi World"
```

## `std::string_view` (C++17)

`std::string_view` គឺជាទិដ្ឋភាពទៅខ្សែអក្សរដែលមិនកាន់កាប់អង្គចងចាំ។
វាមានតម្លៃទាប និងគួរប្រើជាប៉ារ៉ាម៉ែត្រអនុគមន៍ដែលគ្រាន់តែអាន៖

```cpp
void print(std::string_view text) {
    std::cout << text << '\n';
}
print("literal");       // មិនចម្លង
print(std::string("x"));
```

:::{warning}
`std::string_view` មិនកាន់កាប់អង្គចងចាំទេ។ បើខ្សែអក្សរដើមត្រូវបំផ្លាញ
មុនពេល `string_view` ត្រូវប្រើ នោះកើតមាន dangling reference — ឥរិយាបថមិនកំណត់។
:::

## ខ្សែអក្សរ៖ ឯកសារក្បាលសំខាន់ៗ

- `<string>` — `std::string`, `std::wstring` ជាដើម។
- `<string_view>` — `std::string_view` (C++17)។
- `<cstring>` — អនុគមន៍ C ដូចជា `strlen`, `strcmp`។

## កូដឧទាហរណ៍

```{literalinclude} ../../examples/stdlib/strings.cpp
:language: cpp
```

លទ្ធផល៖

```text
Hello World (size 11)
substr: World
view: Hello World
find 'World': 6
empty? no
```

## អានបន្ថែម

- [cppreference: `std::basic_string`](https://en.cppreference.com/w/cpp/string/basic_string)
- [cppreference: `std::string_view`](https://en.cppreference.com/w/cpp/string/basic_string_view)
