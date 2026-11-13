# គំរូកូដពិតប្រាកដ

```{translation-meta} practice/real-world
```

កូដក្នុងគំរូពិតប្រាកដមានលក្ខណៈខុសពីឧទាហរណ៍ក្នុងឯកសារ។ វាត្រូវដោះស្រាយ
បញ្ហាជាក់ស្តែង ដូចជាការអានឯកសារ ការញែកទិន្នន័យ និងការបង្ហាញលទ្ធផល។
គំរូទាំងនេះជួយឱ្យអ្នកយល់ពីរបៀបដែល C++ ត្រូវបានប្រើក្នុងកម្មវិធីពិត។

## គោលការណ៍សំខាន់

- សរសេរកូដដែលអាចអាន និងថែទាំបាន។
- ពិនិត្យកំហុស និងផ្ដល់សារប្រាប់អ្នកប្រើ។
- ប្រើបណ្ណាល័យស្តង់ដារ ជំនួសការសរសេរដោយដៃ។
- សាកល្បងជាមួយទិន្នន័យពិត មិនមែនតែគំរូតូចៗទេ។

## គំរូ៖ ញែកខ្សែ CSV

កម្មវិធីពិតជាញឹកញាប់ត្រូវអានទិន្នន័យពីឯកសារ CSV។
កូដខាងក្រោមញែកខ្សែអក្សរមួយតាមសញ្ញាក្បៀស ហើយបង្ហាញវាលនីមួយៗ។

```cpp
#include <iostream>
#include <sstream>
#include <string>
#include <vector>

int main() {
    std::string line = "Alice,30,Engineer";
    std::vector<std::string> fields;
    std::stringstream stream(line);
    std::string item;
    while (std::getline(stream, item, ',')) {
        fields.push_back(item);
    }
    for (const auto& field : fields) {
        std::cout << field << '\n';
    }
    return 0;
}
```

កូដពេញលេញខាងក្រោមបង្ហាញលទ្ធផលដូចគ្នា។

```{literalinclude} ../../examples/practice/real-world.cpp
:language: cpp
```

លទ្ធផល៖

```text
Alice
30
Engineer
```

## ការអនុវត្តបន្ថែម

សាកល្បងកែកូដឱ្យអានពីឯកសារពិតប្រាកដ ដោយប្រើ `std::ifstream`។
បន្ថែមការពិនិត្យថាឯកសារបើកបាន ឬអត់។ ព្យាយាមបញ្ចូលទិន្នន័យដែលមាន
សញ្ញាក្បៀសក្នុងវាល ហើយសង្កេតមើលបញ្ហា។

## ការគ្រប់គ្រងកំហុស

ក្នុងកម្មវិធីពិត កំហុសអាចកើតឡើង ដូចជាឯកសារមិនមាន ឬទិន្នន័យខុសទម្រង់។
ប្រើករណីលើកលែង ឬត្រឡប់តម្លៃកំហុស ដើម្បីឱ្យអ្នកប្រើដឹង។
កុំបន្តដំណើរការដោយស្ងៀមស្ងាត់ នៅពេលទិន្នន័យមិនត្រឹមត្រូវ។

## អានបន្ថែម

- [cppreference: input/output](https://en.cppreference.com/w/cpp/io)
- [cppreference: string](https://en.cppreference.com/w/cpp/string)
