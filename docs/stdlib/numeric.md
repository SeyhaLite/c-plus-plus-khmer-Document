# ប្រតិបត្តិការលេខ (Numeric)

```{translation-meta} stdlib/numeric
```

បណ្ណាល័យ `<numeric>` ផ្ដល់អាល់ហ្គោរីតសម្រាប់ការគណនាលេខ ដូចជា ការបូក
ការគុណ និងការបង្កើតលំដាប់។

## អាល់ហ្គោរីតសំខាន់ៗ

- `std::accumulate` — បូក (ឬផ្សំ) ធាតុទាំងអស់។
- `std::reduce` (C++17) — ដូច accumulate ប៉ុន្តែអាចប្ដូរលំដាប់ (parallelizable)។
- `std::inner_product` — ផលបូកនៃផលគុណ។
- `std::iota` — បំពេញលំដាប់កើន (1, 2, 3, ...)។
- `std::partial_sum` — ផលបូកផ្នែក។
- `std::gcd`, `std::lcm` (C++17) — កត្តារួមធំបំផុត និង kelipatan រួមតូចបំផុត។

## ឧទាហរណ៍

```cpp
std::vector<int> values{1, 2, 3, 4};
int sum = std::accumulate(values.begin(), values.end(), 0);   // 10

std::vector<int> out(values.size());
std::partial_sum(values.begin(), values.end(), out.begin());  // 1, 3, 6, 10

std::iota(values.begin(), values.end(), 10);                 // 10, 11, 12, 13

std::gcd(12, 18);   // 6
std::lcm(4, 6);     // 12
```

## ភាពខុសគ្នារវាង accumulate និង reduce

`std::accumulate` ធ្វើការតាមលំដាប់ ហើយប្រើប្រតិបត្តិការ二元ដែលអ្នកផ្ដល់។
`std::reduce` អាចប្ដូរលំដាប់ ដូច្នេះប្រតិបត្តិការត្រូវ **commutative និង associative**។
បើប្រតិបត្តិការមិនមានលក្ខណៈទាំងនេះ ត្រូវប្រើ `accumulate`។

:::{note}
`std::reduce` និង `std::transform_reduce` (C++17) អាចប្រើជាមួយ execution policy
(`std::execution::par`) ដើម្បីគណនាជាខ្សែស្រឡាយច្រើន។
:::

## កូដឧទាហរណ៍

```{literalinclude} ../../examples/stdlib/numeric.cpp
:language: cpp
```

លទ្ធផល៖

```text
sum: 10
iota: 10 11 12 13
gcd(12,18): 6
lcm(4,6): 12
```

## អានបន្ថែម

- [cppreference: `<numeric>`](https://en.cppreference.com/w/cpp/header/numeric)
- [cppreference: `std::accumulate`](https://en.cppreference.com/w/cpp/algorithm/accumulate)
- [cppreference: `std::gcd`](https://en.cppreference.com/w/cpp/numeric/gcd)
