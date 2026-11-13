# ការកំណត់អនុគមន៍ (Definition)

```{translation-meta} functions/definition
```

ការកំណត់អនុគមន៍ (definition) គឺជាការប្រកាស **បូកជាមួយតួអង្គកម្មវិធី**។
វាជាកន្លែងដែលកូដពិតប្រាកដរបស់អនុគមន៍ស្ថិតនៅ។

## រូបមន្ត

```cpp
return_type function_name(parameter_list) {
    // តួអង្គកម្មវិធី
    return value;   // បើ return_type មិនមែន void
}
```

```cpp
int cube(int x) {
    return x * x * x;
}

void greet() {
    std::cout << "Hello\n";
    // គ្មាន return ត្រូវការ ព្រោះ void
}
```

## ច្បាប់ one definition rule

អនុគមន៍ដែលមិនមែន `inline` ត្រូវកំណត់តែម្តងក្នុងកម្មវិធីទាំងមូល។
បើអ្នកកំណត់វាក្នុងឯកសារក្បាល ហើយឯកសារនោះត្រូវបញ្ចូលពីពីរឯកសារ
នោះអ្នកនឹងឃើញកំហុស «multiple definition» ពេលភ្ជាប់។

## `inline`

`inline` អនុញ្ញាតឱ្យអនុគមន៍ត្រូវកំណត់ក្នុងឯកសារក្បាលដោយមិនបំពាន one definition rule។
វាក៏ជាការណែនាំឱ្យកម្មវិធីបកប្រែដាក់កូដចូលកន្លែងហៅផងដែរ។

```cpp
inline int maximum(int a, int b) {
    return a > b ? a : b;
}
```

:::{note}
`inline` គឺជាការណែនាំ មិនមែនការបញ្ជាទេ។ កម្មវិធីបកប្រែសម្រេចខ្លួនឯងថាតើ
ត្រូវ inline ឬអត់។ ចាប់ពី C++17 អនុគមន៍ដែលកំណត់ក្នុងថ្នាក់ (class) គឺ
inline ដោយស្វ័យប្រវត្តិ។
:::

## ការបកប្រែដោយឡែក

ក្នុងគម្រោងធំ គេបកប្រែឯកសារ `.cpp` ដោយឡែក រួចភ្ជាប់៖

```bash
g++ -std=c++17 -c math_utils.cpp -o math_utils.o
g++ -std=c++17 -c main.cpp -o main.o
g++ main.o math_utils.o -o app
```

បើអ្នកភ្លេចភ្ជាប់ `math_utils.o` អ្នកនឹងឃើញកំហុស «undefined reference»។
នេះជាកំហុសភ្ជាប់ (link error) មិនមែនកំហុសបកប្រែទេ។

## កូដឧទាហរណ៍

```{literalinclude} ../../examples/functions/definition.cpp
:language: cpp
```

លទ្ធផល៖

```text
cube(3) = 27
```

## អានបន្ថែម

- [cppreference: functions](https://en.cppreference.com/w/cpp/language/function)
- [cppreference: `inline` specifier](https://en.cppreference.com/w/cpp/language/inline)
