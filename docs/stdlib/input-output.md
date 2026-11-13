# បណ្ណាល័យបញ្ចូល/បញ្ចេញ

```{translation-meta} stdlib/input-output
```

បណ្ណាល័យបញ្ចូល/បញ្ចេញ (I/O) របស់ C++ ផ្ដល់ `std::cin`, `std::cout`, `std::cerr`
និងធុងទិន្នន័យសម្រាប់ឯកសារ និងខ្សែអក្សរ។ វាមានក្នុងឯកសារក្បាល
`<iostream>`, `<fstream>`, `<sstream>`។

## ការបញ្ចេញ និងបញ្ចូលមូលដ្ឋាន

```cpp
std::cout << "Hello, " << name << '\n';
std::cin >> value;
```

- `std::cout` — បញ្ចេញទៅ stdout។
- `std::cerr` — បញ្ចេញកំហុស (មិនបាន buffer)។
- `std::cin` — អានពី stdin។

## ធុងខ្សែអក្សរ (string streams)

```cpp
std::istringstream in("42 3.14");
int n; double d;
in >> n >> d;

std::ostringstream out;
out << "value=" << n;
std::string result = out.str();
```

`std::istringstream` អានពីខ្សែអក្សរ; `std::ostringstream` សរសេរទៅខ្សែអក្សរ។
វាល្អសម្រាប់ការបំប្លែង និងការបំបែកទិន្នន័យ។

## ឯកសារ (file streams)

```cpp
std::ofstream out("data.txt");
out << "hello\n";

std::ifstream in("data.txt");
std::string line;
while (std::getline(in, line)) {
    std::cout << line << '\n';
}
```

ត្រូវពិនិត្យថាឯកសារបើកបាន៖ `if (!in) { /* error */ }`។ ឯកសារត្រូវបានបិទដោយស្វ័យប្រវត្តិនៅ destructor នៃ stream object។

:::{note}
ចាប់ពី **C++20** មាន `std::format` ដែលផ្ដល់ការបញ្ចេញដូច `printf` ប៉ុន្តែ
មានសុវត្ថិភាពប្រភេទ។ ឧទាហរណ៍៖ `std::format("x={}", 42)`។
:::

## កូដឧទាហរណ៍

```{literalinclude} ../../examples/stdlib/input-output.cpp
:language: cpp
```

លទ្ធផល៖

```text
Hello, world
parsed: 42
value=42
```

## អានបន្ថែម

- [cppreference: `<iostream>`](https://en.cppreference.com/w/cpp/header/iostream)
- [cppreference: `<sstream>`](https://en.cppreference.com/w/cpp/header/sstream)
- [cppreference: `<fstream>`](https://en.cppreference.com/w/cpp/header/fstream)
