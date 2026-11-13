# ប្រព័ន្ធឯកសារ (std::filesystem)

```{translation-meta} stdlib/filesystem
```

`std::filesystem` គឺជាបណ្ណាល័យស្តង់ដារសម្រាប់ការងារជាមួយផ្លូវឯកសារ និងថត។
វាមានតាំងពី **C++17** ក្នុងឯកសារក្បាល `<filesystem>`។

## `std::filesystem::path`

```cpp
std::filesystem::path p = "a/b/c.txt";
p.filename();       // "c.txt"
p.extension();      // ".txt"
p.stem();           // "c"
p.parent_path();    // "a/b"
p / "d.txt";        // "a/b/c.txt/d.txt" (ប្រុងប្រយ័ត្ន)
```

ការប្រើ `/` បន្ថែមផ្នែកផ្លូវគឺងាយស្រួល ប៉ុន្តែត្រូវប្រាកដថាផ្លូវមេគឺថត។

## ប្រតិបត្តិការឯកសារ និងថត

```cpp
std::filesystem::exists(p);
std::filesystem::is_regular_file(p);
std::filesystem::is_directory(p);
std::filesystem::file_size(p);
std::filesystem::create_directories("a/b/c");
std::filesystem::remove(p);            // លុបឯកសារ
std::filesystem::remove_all(dir);      // លុបថតទាំងមូល
```

## ការដើរកាត់ថត

```cpp
for (const auto& entry : std::filesystem::directory_iterator(dir)) {
    std::cout << entry.path() << '\n';
}
// រួមទាំងថតកូន៖
for (const auto& entry : std::filesystem::recursive_directory_iterator(dir)) {
    std::cout << entry.path() << '\n';
}
```

## ការគ្រប់គ្រងកំហុស

អនុគមន៍ភាគច្រើនមានពីរទម្រង់៖ បោះ exception ឬត្រឡប់ `std::error_code`៖

```cpp
std::error_code ec;
auto size = std::filesystem::file_size(p, ec);
if (ec) {
    std::cerr << ec.message() << '\n';
}
```

:::{warning}
ផ្លូវអាចមាន Unicode។ `std::filesystem::path` គាំទ្រ Unicode ប៉ុន្តែការបោះពុម្ព
និងការបំប្លែងទៅ `std::string` អាចខុសគ្នាតាមប្រព័ន្ធប្រតិបត្តិការ។
:::

## កូដឧទាហរណ៍

```{literalinclude} ../../examples/stdlib/filesystem.cpp
:language: cpp
```

លទ្ធផល៖

```text
filename: c.txt
extension: .txt
parent: a/b
temp exists: yes
is dir: yes
```

## អានបន្ថែម

- [cppreference: `<filesystem>`](https://en.cppreference.com/w/cpp/header/filesystem)
- [cppreference: `std::filesystem::path`](https://en.cppreference.com/w/cpp/filesystem/path)
