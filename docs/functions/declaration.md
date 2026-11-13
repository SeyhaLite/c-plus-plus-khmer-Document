# ការប្រកាសអនុគមន៍ (Function Declaration)

```{translation-meta} functions/declaration
```

ការប្រកាសអនុគមន៍ (function declaration) គឺជាការប្រាប់កម្មវិធីបកប្រែអំពីឈ្មោះអនុគមន៍ ប្រភេទតម្លៃត្រឡប់ និងប្រភេទប៉ារ៉ាម៉ែត្ររបស់វា។ វាអនុញ្ញាតឱ្យយើងហៅអនុគមន៍បាន មុនពេលសរសេរតួអង្គកម្មវិធី (function body) របស់វា។

ចំណុចសំខាន់៖ **ការប្រកាស** ប្រាប់ថាអនុគមន៍មានរូបរាងយ៉ាងដូចម្ដេច ចំណែក **ការកំណត់** ផ្ដល់កូដដែលត្រូវដំណើរការ។

## ១. ទម្រង់មូលដ្ឋាន

```cpp
return_type function_name(parameter_list);
```

ឧទាហរណ៍៖

```cpp
int add(int a, int b);
double average(double total, int count);
void print_message();
```

| ផ្នែក | អត្ថន័យ | ឧទាហរណ៍ |
| --- | --- | --- |
| `return_type` | ប្រភេទតម្លៃដែលអនុគមន៍ត្រឡប់ | `int`, `double`, `void` |
| `function_name` | ឈ្មោះសម្រាប់ហៅអនុគមន៍ | `add`, `average` |
| `parameter_list` | បញ្ជីប៉ារ៉ាម៉ែត្រ ដែលបំបែកដោយសញ្ញាក្បៀស | `int a, int b` |
| `;` | បញ្ចប់ការប្រកាស | `;` |

ឧទាហរណ៍ `int add(int a, int b);` មានន័យថា៖
- `int`៖ អនុគមន៍នឹងត្រឡប់តម្លៃចំនួនគត់។
- `add`៖ ឈ្មោះអនុគមន៍។
- `int a, int b`៖ ទទួលប៉ារ៉ាម៉ែត្រចំនួនគត់ពីរ។
- `;`៖ បញ្ចប់ការប្រកាស ដោយមិនមានតួអង្គកម្មវិធីនៅទីនេះ។

## ២. ការប្រកាស និងការកំណត់ ខុសគ្នាយ៉ាងដូចម្ដេច?

**ការប្រកាស (declaration)** មិនមានតួអង្គកម្មវិធីទេ៖

```cpp
int multiply(int a, int b);
```

**ការកំណត់ (definition)** មានតួអង្គកម្មវិធីនៅក្នុង `{ }`៖

```cpp
int multiply(int a, int b) {
    return a * b;
}
```

អាចប្រកាសអនុគមន៍មុន ហើយកំណត់វានៅខាងក្រោមបាន៖

```cpp
#include <iostream>

int square(int value);  // ប្រកាសជាមុន

int main() {
    std::cout << square(5);
}

int square(int value) {  // កំណត់នៅទីនេះ
    return value * value;
}
```

ពេលកម្មវិធីបកប្រែទៅដល់ការហៅ `square(5)` វាបានស្គាល់រួចហើយថា `square` ទទួល `int` មួយ និងត្រឡប់ `int`។ ដូច្នេះវាអាចពិនិត្យការហៅនោះបាន។

## ៣. ឈ្មោះប៉ារ៉ាម៉ែត្រអាចដាក់ ឬមិនដាក់

នៅក្នុងការប្រកាស ឈ្មោះប៉ារ៉ាម៉ែត្រមិនមែនជាកាតព្វកិច្ចទេ។

```cpp
int divide(int numerator, int denominator);
int divide(int, int);
```

ទាំងពីរបន្ទាត់ខាងលើប្រកាសអនុគមន៍ដែលមានប្រភេទប៉ារ៉ាម៉ែត្រដូចគ្នា។ ការដាក់ឈ្មោះជួយឱ្យអ្នកអានយល់ពីតួនាទីរបស់ប៉ារ៉ាម៉ែត្រ។ ឈ្មោះដែលដាក់ក្នុងការប្រកាសមិនចាំបាច់ដូចឈ្មោះក្នុងការកំណត់ទេ៖

```cpp
int divide(int top, int bottom);

int divide(int a, int b) {
    return a / b;
}
```

ចំណាំ៖ កូដខាងលើសន្មតថា `bottom` មិនស្មើសូន្យ។ ការប្រកាសមិនធ្វើឱ្យការត្រួតពិនិត្យលក្ខខណ្ឌនេះកើតឡើងដោយស្វ័យប្រវត្តិទេ។

## ៤. បញ្ជីប៉ារ៉ាម៉ែត្រ

### អនុគមន៍គ្មានប៉ារ៉ាម៉ែត្រ

ក្នុង C++ `()` មានន័យថា អនុគមន៍មិនទទួលប៉ារ៉ាម៉ែត្រទេ៖

```cpp
void start();
int get_version();
```

`void start(void);` ក៏មានន័យថាគ្មានប៉ារ៉ាម៉ែត្រដែរ ប៉ុន្តែជាទូទៅគេប្រើ `void start();` ក្នុង C++។ កុំច្រឡំ `void` នៅកន្លែងប្រភេទតម្លៃត្រឡប់ជាមួយ `void` ក្នុងបញ្ជីប៉ារ៉ាម៉ែត្រ។

### ប៉ារ៉ាម៉ែត្រមានតម្លៃលំនាំដើម

ការប្រកាសអាចកំណត់តម្លៃលំនាំដើម (default argument) បាន៖

```cpp
void greet(const std::string& name, int times = 1);
```

បើហៅ `greet("Dara")` នោះ `times` នឹងប្រើតម្លៃ `1`។ បើហៅ `greet("Dara", 3)` នោះវាប្រើ `3`។ នៅពេលមានប៉ារ៉ាម៉ែត្រមួយទទួលតម្លៃលំនាំដើម ប៉ារ៉ាម៉ែត្រដែលនៅខាងស្ដាំវាក៏ត្រូវមានតម្លៃលំនាំដើមដែរ។

```cpp
void set_range(int minimum, int maximum = 100); // ត្រឹមត្រូវ
// void set_range(int minimum = 0, int maximum); // មិនត្រឹមត្រូវ
```

កុំសរសេរតម្លៃលំនាំដើមម្ដងទៀតក្នុងការកំណត់ ប្រសិនបើបានប្រកាសវារួចហើយ។ សូមមើល [មេរៀនប៉ារ៉ាម៉ែត្រ](parameters.md) សម្រាប់ការប្រើប្រាស់បន្ថែម។

### ប៉ារ៉ាម៉ែត្របែប variadic

សញ្ញា `...` អនុញ្ញាតឱ្យអនុគមន៍ទទួលអាគុយម៉ង់ចំនួនប្រែប្រួល។ វាជារបៀបចាស់ដែលប្រើក្នុង C-style variadic function៖

```cpp
int print_values(const char* format, ...);
```

របៀបនេះមិនអាចពិនិត្យប្រភេទអាគុយម៉ង់បន្ថែមបានរឹងមាំដូច template ទេ។ ក្នុងកម្មវិធី C++ ថ្មីៗ គួរពិចារណា variadic templates ឬឧបករណ៍បណ្ណាល័យស្តង់ដារ ជំនួសពេលសមស្រប។

## ៥. ការប្រកាសដដែល និងការផ្ទុកលើស (Overloading)

អនុគមន៍មួយអាចមានការប្រកាសដដែលច្រើនកន្លែងបាន ប្រសិនបើការប្រកាសទាំងនោះសំដៅលើអនុគមន៍ដូចគ្នា និងត្រូវគ្នា៖

```cpp
int calculate(int value);
int calculate(int value); // ប្រកាសដដែល មិនមែនអនុគមន៍ថ្មីទេ
```

ការផ្ទុកលើស (function overloading) គឺការមានអនុគមន៍ច្រើនដែលមានឈ្មោះដូចគ្នា ប៉ុន្តែមានបញ្ជីប្រភេទប៉ារ៉ាម៉ែត្រខុសគ្នា៖

```cpp
int convert(int value);
double convert(double value);
```

កម្មវិធីបកប្រែជ្រើសរើសអនុគមន៍ដោយមើលប្រភេទអាគុយម៉ង់ដែលអ្នកផ្ដល់ពេលហៅ។

**មិនអាចបង្កើត overload ដោយប្ដូរតែប្រភេទតម្លៃត្រឡប់បានទេ៖**

```cpp
int get_value(int value);
// double get_value(int value); // Error: បញ្ជីប៉ារ៉ាម៉ែត្រដូចគ្នា
```

សម្រាប់ការបង្កើត overload ក៏ត្រូវចងចាំថា `int` និង `const int` ដែលជា parameter តាមតម្លៃ គឺមិនខុសគ្នាក្នុង function signature ទេ៖

```cpp
void show(int value);
// void show(const int value); // មិនមែន overload ថ្មីទេ
```

ប៉ុន្តែ `int*` និង `const int*` ជាប្រភេទ pointer ខុសគ្នា ដូច្នេះអាចបង្កើត overload ផ្សេងគ្នាបាន។

## ៦. Function signature និង function type

ពាក្យទាំងពីរនេះមានន័យជិតគ្នា ប៉ុន្តែមិនដូចគ្នាទេ។

**Function signature** ជាព័ត៌មានដែលប្រើសម្គាល់អនុគមន៍ ដូចជា៖
- ឈ្មោះអនុគមន៍។
- បញ្ជីប្រភេទប៉ារ៉ាម៉ែត្រ។
- លំហឈ្មោះ (namespace) ឬថ្នាក់ដែលជាម្ចាស់អនុគមន៍។
- សម្រាប់ member function វាក៏ពាក់ព័ន្ធនឹង `const`, `volatile`, `&`, `&&` និង `requires` clause តាមច្បាប់របស់ភាសា។

**Function type** រួមមានប្រភេទតម្លៃត្រឡប់ និងប្រភេទប៉ារ៉ាម៉ែត្រ ព្រមទាំង qualifier ដែលពាក់ព័ន្ធ។ ចាប់ពី C++17 `noexcept` ក៏ជាផ្នែកនៃ function type ដែរ។ ប៉ុន្តែ `noexcept` មិនមែនជាផ្នែកនៃ function signature ទេ។

ចំណុចងាយចាំ៖ ប្រភេទតម្លៃត្រឡប់មិនអាចប្រើតែម្នាក់ឯងដើម្បីបំបែក overload បានទេ។

## ៧. Qualifier សម្រាប់ member function

ក្នុងថ្នាក់ (class) អាចបន្ថែម qualifier នៅក្រោយ `()` ដើម្បីកំណត់ថាអនុគមន៍អាចហៅលើវត្ថុប្រភេទណា ឬមានសិទ្ធិកែប្រែវត្ថុដែរឬទេ។

```cpp
class Document {
public:
    void read() const;
    void edit() &;
    void save() &&;
};
```

- `read() const`៖ អនុគមន៍សន្យាមិនកែសមាជិករបស់វត្ថុតាមរយៈ `this`។
- `edit() &`៖ អាចហៅលើវត្ថុប្រភេទ lvalue។
- `save() &&`៖ អាចហៅលើវត្ថុប្រភេទ rvalue ដូចជា `Document{}`។

`&` និង `&&` នៅទីនេះមិនមែនជាប្រភេទត្រឡប់ទេ។ វាជា ref-qualifier របស់ member function ហើយមានចាប់ពី C++11។

### `noexcept`

`noexcept` បញ្ជាក់ថាអនុគមន៍មិនគួរបោះករណីលើកលែងចេញក្រៅទេ៖

```cpp
void release_resource() noexcept;
void may_fail() noexcept(false);
```

បើអនុគមន៍ដែលបានប្រកាសជា `noexcept` បោះករណីលើកលែងចេញក្រៅ នោះកម្មវិធីនឹងហៅ `std::terminate()`។ `noexcept` មានតាំងពី C++11 ហើយចាប់ពី C++17 វាជាផ្នែកនៃ function type។

## ៨. Trailing return type

ចាប់ពី C++11 អាចសរសេរប្រភេទតម្លៃត្រឡប់នៅខាងក្រោយ `->` បាន។ របៀបនេះមានប្រយោជន៍នៅពេលប្រភេទត្រឡប់អាស្រ័យលើប៉ារ៉ាម៉ែត្រ៖

```cpp
template<class T, class U>
auto add(T first, U second) -> decltype(first + second);
```

`auto` ជាផ្នែកនៃទម្រង់សរសេរ ហើយ `decltype(first + second)` ប្រាប់ប្រភេទតម្លៃត្រឡប់ដោយផ្អែកលើកន្សោមបូករបស់ប៉ារ៉ាម៉ែត្រទាំងពីរ។

## ៩. ការសន្និដ្ឋានប្រភេទតម្លៃត្រឡប់ដោយ `auto`

ចាប់ពី C++14 អាចឱ្យកម្មវិធីបកប្រែសន្និដ្ឋានប្រភេទតម្លៃត្រឡប់ពី `return` ក្នុងតួអង្គកម្មវិធីបាន៖

```cpp
auto get_answer() {
    return 42; // ប្រភេទតម្លៃត្រឡប់ត្រូវបានសន្និដ្ឋានជា int
}
```

អាចប្រើ `decltype(auto)` ដើម្បីឱ្យការសន្និដ្ឋានអនុវត្តតាមច្បាប់របស់ `decltype` ដែលអាចរក្សា reference បាន៖

```cpp
int score = 90;

auto get_score_copy() {
    return (score); // ត្រឡប់ int ជាច្បាប់ចម្លង
}

decltype(auto) get_score_reference() {
    return (score); // ត្រឡប់ int&
}
```

ចំណាំសំខាន់ៗ៖
- បើមាន `return` ច្រើន កន្សោមទាំងនោះត្រូវនាំទៅប្រភេទត្រឡប់ដែលសន្និដ្ឋានបានដូចគ្នា។
- `auto` function ដែលត្រូវសន្និដ្ឋានប្រភេទពីតួអង្គកម្មវិធី ត្រូវមាននិយមន័យឱ្យកម្មវិធីបកប្រែឃើញ មុនពេលប្រើកន្លែងដែលត្រូវការប្រភេទនោះ។
- កុំត្រឡប់ reference ទៅអថេរមូលដ្ឋានដែលនឹងត្រូវបំផ្លាញពេលចេញពីអនុគមន៍។

## ១០. Function template និង `requires`

អនុគមន៍អាចជាពុម្ព (function template) ដើម្បីទទួលប្រភេទទិន្នន័យច្រើនប្រភេទ៖

```cpp
template<class T>
T identity(T value);
```

ចាប់ពី C++20 អាចប្រើ `requires` ដើម្បីកំណត់លក្ខខណ្ឌលើប្រភេទដែលអនុគមន៍អនុញ្ញាត៖

```cpp
#include <concepts>

template<class T>
requires std::integral<T>
T double_value(T value);
```

ក្នុង C++20 ក៏អាចប្រើ `auto` ជាប្រភេទប៉ារ៉ាម៉ែត្រ ដើម្បីសរសេរ abbreviated function template បានដែរ៖

```cpp
void print_value(const auto& value); // C++20
```

ក្នុងករណីនេះ `auto` មិនមានន័យថាអនុគមន៍ទទួលតែប្រភេទ `auto` ទេ។ វាបង្កើត function template ដែលកម្មវិធីបកប្រែសន្និដ្ឋានប្រភេទនៅពេលហៅ។

## ១១. Explicit object parameter ក្នុង C++23

ចាប់ពី C++23 member function អាចប្រកាសប៉ារ៉ាម៉ែត្រវត្ថុដោយសរសេរ `this` នៅដើមបញ្ជីប៉ារ៉ាម៉ែត្រ។ លក្ខណៈនេះត្រូវបានគេហៅថា *deducing this*៖

```cpp
struct Counter {
    int value = 0;
    void increment(this Counter& self);
};
```

`self` សំដៅលើវត្ថុដែលបានហៅអនុគមន៍។ Explicit object parameter ត្រូវនៅទីតាំងដំបូង ហើយ member function ប្រភេទនេះមិនអាចជា `static` ឬ `virtual` បានទេ។ វាក៏មិនប្រើ `const` ឬ ref-qualifier នៅក្រោយ `()` ដែរ ព្រោះលក្ខខណ្ឌលើវត្ថុត្រូវបានសរសេរនៅក្នុង parameter រួចហើយ។

## ១២. Attributes លើការប្រកាស

Attributes ជាព័ត៌មានបន្ថែមដែលផ្ដល់ឱ្យកម្មវិធីបកប្រែអំពីអនុគមន៍។ ឧទាហរណ៍៖

```cpp
[[nodiscard]] int calculate_total();
[[noreturn]] void stop_program();
```

- `[[nodiscard]]` (C++17) ស្នើឱ្យកម្មវិធីបកប្រែព្រមាន បើអ្នកហៅអនុគមន៍ហើយមិនប្រើតម្លៃត្រឡប់។
- `[[noreturn]]` (C++11) បញ្ជាក់ថាអនុគមន៍មិនត្រឡប់ទៅកន្លែងដែលបានហៅវិញតាមធម្មតាទេ។

Attributes មិនជំនួសប្រភេទតម្លៃត្រឡប់ ឬប្រភេទប៉ារ៉ាម៉ែត្រឡើយ។

## ១៣. របៀបអាន pointer ទៅអនុគមន៍

សញ្ញាវង់ក្រចកអាចធ្វើឱ្យការប្រកាសមើលទៅស្មុគស្មាញ។ សូមប្រៀបធៀប៖

```cpp
int* make_value();       // អនុគមន៍ត្រឡប់ pointer ទៅ int
int (*operation)();      // អថេរ operation ជា pointer ទៅអនុគមន៍
```

ចំណុចសំខាន់គឺមើលថាតើឈ្មោះស្ថិតនៅជាមួយ `()` មុន ឬស្ថិតក្នុងវង់ក្រចកជាមួយ `*`។ ការប្រកាស pointer ទៅអនុគមន៍មិនមែនជាការប្រកាសអនុគមន៍ដែលមានឈ្មោះនោះផ្ទាល់ទេ។

## ១៤. ច្បាប់ និងកំហុសដែលជួបញឹកញាប់

| ច្បាប់ | អ្វីដែលត្រូវចងចាំ |
| --- | --- |
| ប្រកាសដដែល | អាចមានច្រើនដង ប្រសិនបើត្រូវគ្នា |
| និយមន័យ | អនុវត្តតាម One Definition Rule; កុំកំណត់អនុគមន៍ធម្មតាដដែលច្រើនដង |
| ប្រភេទត្រឡប់ | មិនអាចប្រើតែមួយគត់ដើម្បីបង្កើត overload |
| ប៉ារ៉ាម៉ែត្រតាមតម្លៃ | `int` និង `const int` មិនបង្កើត overload ផ្សេងគ្នា |
| តម្លៃលំនាំដើម | កុំប្រកាសតម្លៃដូចគ្នាម្ដងទៀតក្នុង scope ដដែល |
| ប្រភេទត្រឡប់ជា function/array | មិនអនុញ្ញាតឱ្យត្រឡប់ដោយផ្ទាល់ទេ ប៉ុន្តែអាចត្រឡប់ pointer ឬ reference ទៅវាបាន |
| បញ្ជីប៉ារ៉ាម៉ែត្រ | លំដាប់ និងប្រភេទប៉ារ៉ាម៉ែត្រមានសារៈសំខាន់ |

## ១៥. លំហាត់សាកល្បង

**លំហាត់ទី១៖** តើបន្ទាត់ណាជាការប្រកាស មិនមែនជាការកំណត់?

```cpp
A. int sum(int a, int b);
B. int sum(int a, int b) { return a + b; }
```

**លំហាត់ទី២៖** តើអាចបង្កើត overload ដោយប្ដូរតែប្រភេទតម្លៃត្រឡប់ពី `int` ទៅ `double` បានទេ? សូមពន្យល់មូលហេតុ។

**លំហាត់ទី៣៖** តើ `void run();` មានប៉ារ៉ាម៉ែត្រប៉ុន្មាន? តើ `void` នៅទីនេះមានន័យអ្វី?

សូមសាកល្បងសរសេរកូដ ហើយបកប្រែដោយប្រើ `-std=c++14`, `-std=c++17`, `-std=c++20` ឬ `-std=c++23` តាមលក្ខណៈដែលអ្នកកំពុងសិក្សា។

## ចំណាំអំពីព្រាង C++26

ប្រភពយោងមួយចំនួនបង្ហាញ syntax ថ្មីៗដូចជា function contracts (`pre` និង `post`) ឬការបន្ថែមលើ deleted function។ លក្ខណៈទាំងនេះពាក់ព័ន្ធនឹងព្រាង C++26 ហើយស្ថានភាពអាចផ្លាស់ប្ដូរបាន។ គិតត្រឹមថ្ងៃទី 13 ខែវិច្ឆិកា ឆ្នាំ 2026 C++23 នៅតែជាស្តង់ដារដែលបានបោះពុម្ពចុងក្រោយ ខណៈព្រាង C++26 កំពុងឆ្លងកាត់ការកែសម្រួល។ ដូច្នេះ មេរៀននេះមិនបង្ហាញ syntax ព្រាងទាំងនោះជាច្បាប់ដែលមានសុពលភាពទូទៅឡើយ។

## កូដឧទាហរណ៍

```{literalinclude} ../../examples/functions/declaration.cpp
:language: cpp
```

លទ្ធផល៖

```text
square(5) = 25
```

## អានបន្ថែម

- [cppreference: Function declaration](https://en.cppreference.com/w/cpp/language/function) — syntax, parameter, function type និង signature។
- [cppreference: Function overloading](https://en.cppreference.com/w/cpp/language/overload_resolution) — របៀបជ្រើស overload នៅពេលហៅអនុគមន៍។
- [cppreference: Member functions](https://en.cppreference.com/w/cpp/language/member_functions) — `const`, ref-qualifier និង explicit object parameter។
- [សេចក្ដីព្រាងស្តង់ដារ C++](https://eel.is/c++draft/dcl.fct) — ច្បាប់បច្ចេកទេសសម្រាប់ function declarator។
