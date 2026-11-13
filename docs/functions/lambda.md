# កន្សោម Lambda

```{translation-meta} functions/lambda
```

កន្សោម lambda (lambda expression) គឺជាអនុគមន៍គ្មានឈ្មោះ ដែលអ្នកសរសេរនៅកន្លែងប្រើ។
វាមានតាំងពី **C++11** ហើយជាឧបករណ៍សំខាន់ក្នុងកូដទំនើប។

## រូបមន្ត

```text
[capture](parameters) -> return_type { body }
```

```cpp
auto add = [](int a, int b) { return a + b; };
std::cout << add(2, 3);   // 5
```

## ការចាប់តម្លៃពីខាងក្រៅ (capture)

lambda អាចប្រើអថេរនៅខាងក្រៅរបស់ខ្លួន តាមរយៈបញ្ជីចាប់ (capture list)៖

| ទម្រង់ | អត្ថន័យ |
| --- | --- |
| `[]` | មិនចាប់អ្វីទេ |
| `[x]` | ចាប់ `x` ដោយចម្លង |
| `[&x]` | ចាប់ `x` ដោយយោង |
| `[=]` | ចាប់អថេរទាំងអស់ដោយចម្លង |
| `[&]` | ចាប់អថេរទាំងអស់ដោយយោង |

```cpp
int factor = 3;
auto times = [factor](int x) { return x * factor; };

int total = 0;
auto accumulate = [&total](int x) { total += x; };
```

:::{warning}
ការចាប់ដោយយោង `[&]` មានហានិភ័យបើ lambda រស់យូរជាងអថេរដើម។
ឧទាហរណ៍ បើអ្នករក្សា lambda ទុកហៅក្រោយពេលអនុគមន៍បញ្ចប់ នោះយោងនឹងក្លាយជា
យោងខូច (dangling reference)។
:::

## `mutable`

តាមលំនាំដើម lambda មិនអាចកែតម្រូវតម្លៃដែលចាប់ដោយចម្លងបានទេ។
ប្រើ `mutable` ដើម្បីអនុញ្ញាត៖

```cpp
int counter = 0;
auto next = [counter]() mutable { return ++counter; };
```

ការកែនេះប៉ះពាល់តែច្បាប់ចម្លងនៅក្នុង lambda ប៉ុណ្ណោះ មិនប៉ះអថេរដើមទេ។

## Generic lambda (C++14)

ចាប់ពី **C++14** ប៉ារ៉ាម៉ែត្រអាចប្រើ `auto`៖

```cpp
auto twice = [](auto x) { return x + x; };
twice(2);      // 4
twice(1.5);    // 3.0
```

## ការប្រើជាមួយអាល់ហ្គោរីត

```cpp
std::vector<int> values{1, 2, 3, 4};
auto even_count = std::count_if(values.begin(), values.end(),
                                [](int x) { return x % 2 == 0; });
```

## កូដឧទាហរណ៍

```{literalinclude} ../../examples/functions/lambda.cpp
:language: cpp
```

លទ្ធផល៖

```text
times(4) = 12
total = 6
even count = 1
```

## អានបន្ថែម

- [cppreference: lambda expressions](https://en.cppreference.com/w/cpp/language/lambda)
