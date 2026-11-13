# ករណីលើកលែង (Exceptions)

```{translation-meta} advanced/exceptions
```

ករណីលើកលែង (Exception) គឺជាយន្តការសម្រាប់រាយការណ៍កំហុសដែលមិនអាចដោះស្រាយ
នៅកន្លែងកើតឡើង។ វាបំបែកកូដធម្មតាចេញពីកូដគ្រប់គ្រងកំហុស។

## `throw`, `try` និង `catch`

```cpp
int parse_positive(int value) {
    if (value <= 0) {
        throw std::invalid_argument("value must be positive");
    }
    return value;
}

int main() {
    try {
        int value = parse_positive(5);
    } catch (const std::invalid_argument& error) {
        std::cerr << error.what() << '\n';
    }
}
```

## ច្បាប់សំខាន់ៗ

- **ចាប់តាមយោងថេរ** (`const std::exception&`) ដើម្បីជៀសវាងការចម្លង និងការកាត់ផ្នែក
  (slicing)។
- ចាប់ពីកូនទៅមេ៖ `catch (const ValidationError&)` ត្រូវមកមុន `catch (const std::exception&)`។
- បើគ្មាន `catch` ត្រូវគ្នា កម្មវិធីត្រូវបញ្ចប់ដោយ `std::terminate`។

## ថ្នាក់ករណីលើកលែងផ្ទាល់ខ្លួន

```cpp
class ValidationError : public std::runtime_error {
public:
    explicit ValidationError(const std::string& message)
        : std::runtime_error(message) {}
};
```

ការទទួលមរតកពី `std::exception` ធ្វើឱ្យកូដអ្នកហៅអាចចាប់កំហុសទូទៅបាន
ដោយមិនចាំបាច់ស្គាល់ថ្នាក់ជាក់លាក់។

## stack unwinding និង RAII

នៅពេល exception ត្រូវបោះ កម្មវិធីបំផ្លាញវត្ថុទាំងអស់ក្នុងដែនកំណត់ដែលកំពុងចាកចេញ
តាមលំដាប់។ ដូច្នេះ destructor ត្រូវហៅជានិច្ច៖

```cpp
void work() {
    std::vector<int> data(100);
    throw std::runtime_error("failed");
    // data ត្រូវបំផ្លាញទោះ exception ត្រូវបោះ
}
```

## `noexcept`

```cpp
void cleanup() noexcept;      // សន្យាថាមិនបោះ exception
```

បើអនុគមន៍ `noexcept` បោះ exception នោះកម្មវិធីត្រូវ `std::terminate`។
អនុគមន៍ផ្លាស់ទី (move constructor) គួរជា `noexcept` ដើម្បីឱ្យធុងទិន្នន័យអាចប្រើវា
នៅពេលពង្រីកទំហំ។

:::{warning}
**កុំបោះ exception ពី destructor។** បើ destructor បោះ exception នៅពេលដែលមាន
exception ផ្សេងកំពុងដំណើរការ នោះកម្មវិធីត្រូវបញ្ចប់ភ្លាម។ ចាប់ពី C++11 destructor
ជា `noexcept` តាមលំនាំដើម។
:::

## កូដឧទាហរណ៍

```{literalinclude} ../../examples/advanced/exceptions.cpp
:language: cpp
```

លទ្ធផល៖

```text
parsed: 5
caught base: yes
```

## អានបន្ថែម

- [cppreference: exceptions](https://en.cppreference.com/w/cpp/language/exceptions)
- [cppreference: `try`-`catch`](https://en.cppreference.com/w/cpp/language/try_catch)
- [cppreference: `noexcept`](https://en.cppreference.com/w/cpp/language/noexcept_spec)
