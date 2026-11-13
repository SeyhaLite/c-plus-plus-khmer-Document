# ការហៅខ្លួនឯង (Recursion)

```{translation-meta} functions/recursion
```

អនុគមន៍បែបហៅខ្លួនឯង (recursive function) គឺអនុគមន៍ដែលហៅខ្លួនឯង។
វាត្រូវមាន **ករណីគោល** (base case) ដើម្បីបញ្ចប់ បើមិនដូច្នេះវានឹងហៅមិនឈប់។

## រូបមន្ត

```cpp
long long factorial(int n) {
    if (n <= 1) {
        return 1;              // ករណីគោល
    }
    return n * factorial(n - 1);   // ករណីហៅខ្លួនឯង
}
```

## របៀបវាដំណើរការ

សម្រាប់ `factorial(4)` ការហៅកើតឡើងជាជាន់៖

```text
factorial(4) = 4 * factorial(3)
             = 4 * 3 * factorial(2)
             = 4 * 3 * 2 * factorial(1)
             = 4 * 3 * 2 * 1
             = 24
```

ការហៅនីមួយៗរង់ចាំលទ្ធផលពីការហៅខាងក្នុង ដូច្នេះអង្គចងចាំត្រូវរក្សាជាន់ទាំងអស់។

:::{warning}
ការហៅជាន់ច្រើនពេកអាចធ្វើឱ្យ stack ហូរលើស (stack overflow) ហើយកម្មវិធីគាំង។
សម្រាប់ទិន្នន័យធំ ការប្រើរង្វិលជុំជាញឹកញាប់មានសុវត្ថិភាពជាង។
:::

## Recursion ឬ iteration?

- **Recursion** អានងាយសម្រាប់បញ្ហាដែលមានរចនាសម្ព័ន្ធបែងចែកខ្លួនឯង
  (ដូចជាដើរលើដើមឈើ binary tree)។
- **Iteration** លឿនជាង និងសន្សំអង្គចងចាំជាងសម្រាប់បញ្ហាធម្មតា។

ស្តង់ដារ C++ **មិនធានា** ការបំប្លែង recursion ជា iteration (tail-call optimization) ទេ។
ដូច្នេះកុំពឹងលើវា។

## Fibonacci

```cpp
long long fib(int n) {
    if (n < 2) {
        return n;
    }
    return fib(n - 1) + fib(n - 2);
}
```

កូដនេះត្រឹមត្រូវ ប៉ុន្តែយឺតខ្លាំងសម្រាប់ `n` ធំ ព្រោះវាគណនាតម្លៃដដែលៗច្រើនដង។
ដំណោះស្រាយគឺ memoization ឬរង្វិលជុំ។

## កូដឧទាហរណ៍

```{literalinclude} ../../examples/functions/recursion.cpp
:language: cpp
```

លទ្ធផល៖

```text
5! = 120
10! = 3628800
fib(10) = 55
```

## អានបន្ថែម

- [cppreference: functions](https://en.cppreference.com/w/cpp/language/function)
- [cppreference: undefined behavior](https://en.cppreference.com/w/cpp/language/ub)
