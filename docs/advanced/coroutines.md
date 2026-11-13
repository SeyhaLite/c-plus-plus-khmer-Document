# កូរូទីន (Coroutines)

```{translation-meta} advanced/coroutines
```

កូរូទីន (coroutine) គឺជាអនុគមន៍ដែលអាចផ្អាក (suspend) និងបន្ត (resume) ដោយរក្សា
ស្ថានភាពរបស់ខ្លួន។ វាជាលក្ខណៈ **C++20** ក្នុងឯកសារក្បាល `<coroutine>`។

## ពាក្យគន្លឹះបី

| ពាក្យគន្លឹះ | អត្ថន័យ |
| --- | --- |
| `co_await` | ផ្អាករង់ចាំលទ្ធផល |
| `co_yield` | ផ្ដល់តម្លៃមួយ ហើយផ្អាក |
| `co_return` | បញ្ចប់កូរូទីន ជាមួយតម្លៃ |

អនុគមន៍ដែលមានពាក្យគន្លឹះណាមួយក្នុងចំណោមនេះ គឺជាកូរូទីនដោយស្វ័យប្រវត្តិ។

## ឧទាហរណ៍៖ generator

កូរូទីនផលិតតម្លៃម្តងមួយៗ ដែលអ្នកប្រើទាញយកនៅពេលត្រូវការ៖

```cpp
Generator count_to(int limit) {
    for (int i = 1; i <= limit; ++i) {
        co_yield i;      // ផ្ដល់តម្លៃ ហើយផ្អាក
    }
}
```

## `promise_type`

កម្មវិធីបកប្រែទាមទារឱ្យប្រភេទត្រឡប់មាន `promise_type` ដែលកំណត់ឥរិយាបថ៖

- `initial_suspend()` — តើផ្អាកភ្លាមពេលចាប់ផ្ដើមឬអត់។
- `yield_value(value)` — អ្វីត្រូវធ្វើពេល `co_yield`។
- `final_suspend()` — អ្វីត្រូវធ្វើពេលបញ្ចប់។
- `return_void()` ឬ `return_value(v)`។
- `unhandled_exception()` — ពេលមាន exception មិនត្រូវចាប់។

ការគ្រប់គ្រងកូរូទីនធ្វើតាម `std::coroutine_handle` ដែលអនុញ្ញាតឱ្យ `resume()`,
`done()` និង `destroy()`។

## កូដឧទាហរណ៍

```{literalinclude} ../../examples/advanced/coroutines.cpp
:language: cpp
```

លទ្ធផល៖

```text
1
2
3
done
```

ឧទាហរណ៍នេះសរសេរ generator តូចមួយដោយដៃ។ ក្នុងកូដពិត គេច្រើនប្រើបណ្ណាល័យ
ដូចជា [`cppcoro`](https://github.com/lewissbaker/cppcoro) ឬ `std::generator` នៃ C++23។

:::{note}
`std::generator` ជារបស់ **C++23** មិនមែន C++20 ទេ។ នៅ C++20 អ្នកត្រូវសរសេរ
promise type ដោយខ្លួនឯង ឬប្រើបណ្ណាល័យខាងក្រៅ។
:::

## ការប្រើប្រាស់ជាក់ស្តែង

- ការអានទិន្នន័យជាលំដាប់ដោយមិនផ្ទុកទាំងអស់ក្នុងអង្គចងចាំ។
- ការងារអសមកាល (asynchronous) ដោយសរសេរកូដដូចលំដាប់ធម្មតា។
- state machine ដែលអានយល់ងាយជាងការសរសេរដោយដៃ។

## អានបន្ថែម

- [cppreference: coroutines](https://en.cppreference.com/w/cpp/language/coroutines)
- [cppreference: `<coroutine>`](https://en.cppreference.com/w/cpp/header/coroutine)
