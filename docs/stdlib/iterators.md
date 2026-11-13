# អ្នកដើរកាត់ (Iterators)

```{translation-meta} stdlib/iterators
```

អ្នកដើរកាត់ (iterator) គឺជាវត្ថុដែលចង្អុលទៅធាតុក្នុងធុង ហើយអាចផ្លាស់ទីទៅមុខ
ឬថយក្រោយ។ វាជាដំណាក់កាលតភ្ជាប់រវាងធុងទិន្នន័យ និងអាល់ហ្គោរីត។

## ប្រភេទអ្នកដើរកាត់

<|end|> ប្រភេទ | អាចធ្វើ |
| --- | --- |
| Input | អានតែម្ដង ទៅមុខ |
| Output | សរសេរតែម្ដង ទៅមុខ |
| Forward | អាន/សរសេរ ទៅមុខបានច្រើនដង |
| Bidirectional | ទៅមុខ និងថយក្រោយ |
| Random access | លោតទៅកន្លែងណាក៏បាន (ដូចពោយន្ត័រ) |

`std::vector` ផ្ដល់ random access iterator; `std::list` ផ្ដល់ bidirectional;
`std::forward_list` ផ្ដល់ forward។

## ការប្រើប្រាស់សាមញ្ញ

```cpp
std::vector<int> values{1, 2, 3, 4};
for (auto it = values.begin(); it != values.end(); ++it) {
    std::cout << *it << ' ';
}
```

- `begin()` — អ្នកដើរកាត់ទៅធាតុដំបូង។
- `end()` — អ្នកដើរកាត់ «បន្ទាប់ពី» ធាតុចុងក្រោយ (មិនមែនធាតុចុងក្រោយ)។
- `cbegin()`/`cend()` — អ្នកដើរកាត់ថេរ (const)។
- `rbegin()`/`rend()` — អ្នកដើរកាត់បញ្ច្រាស។

## ប្រតិបត្តិការ

```cpp
auto it = values.begin();
*it;             // អានតម្លៃ
++it;            // ទៅមុខមួយជំហាន
it + 2;          // លោត (random access)
std::distance(a, b);   // ចំនួនជំហាន
std::next(it, 3);      // ទៅមុខ 3
std::prev(it, 1);      // ថយក្រោយ 1
```

:::{warning}
ការប្រើអ្នកដើរកាត់បន្ទាប់ពីធុងត្រូវបានផ្លាស់ប្ដូរ (បន្ថែម/លុប) អាចធ្វើឱ្យវា
**មិនត្រឹមត្រូវ** (invalidated)។ ឧទាហរណ៍ `push_back` លើ `std::vector` អាច
ចាក់សោអង្គចងចាំឡើងវិញ ហើយអ្នកដើរកាត់ចាស់ទាំងអស់ក្លាយជាមិនត្រឹមត្រូវ។
:::

## កូដឧទាហរណ៍

```{literalinclude} ../../examples/stdlib/iterators.cpp
:language: cpp
```

លទ្ធផល៖

```text
1 2 3 4
4 3 2 1
found: 3 at offset 2
distance begin-end: 4
```

## អានបន្ថែម

- [cppreference: iterators](https://en.cppreference.com/w/cpp/iterator)
- [cppreference: `std::begin`](https://en.cppreference.com/w/cpp/iterator/begin)
