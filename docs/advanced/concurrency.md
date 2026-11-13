# ការប្រតិបត្តិព្រមគ្នា (Concurrency)

```{translation-meta} advanced/concurrency
```

នៅពេលខ្សែស្រឡាយច្រើនចូលដល់ទិន្នន័យដូចគ្នា អ្នកត្រូវធ្វើសមកាលកម្ម (synchronisation)។
បើគ្មាន នោះកើតមាន **data race** ដែលជាឥរិយាបថមិនកំណត់ — មិនមែនគ្រាន់តែ
លទ្ធផលខុសទេ តែកម្មវិធីអាចខូចទាំងស្រុង។

## Data race

```cpp
int counter = 0;

void increment() {
    for (int i = 0; i < 1000; ++i) {
        ++counter;    // ខុស! ខ្សែស្រឡាយពីរកែទិន្នន័យតែមួយដោយគ្មានការការពារ
    }
}
```

## ដំណោះស្រាយទី១៖ `std::mutex`

Mutex ធានាថាមានតែខ្សែស្រឡាយមួយចូលផ្នែកសំខាន់ក្នុងពេលតែមួយ៖

```cpp
#include <mutex>

std::mutex mutex;
int counter = 0;

void increment() {
    for (int i = 0; i < 1000; ++i) {
        std::lock_guard<std::mutex> lock(mutex);   // ចាក់សោ
        ++counter;
    }   // ដោះសោស្វ័យប្រវត្តិ (RAII)
}
```

## ដំណោះស្រាយទី២៖ `std::atomic`

សម្រាប់ប្រតិបត្តិការសាមញ្ញលើតម្លៃតែមួយ អ្នកអាចប្រើ atomic ដែលមានតម្លៃទាបជាង
mutex៖

```cpp
#include <atomic>

std::atomic<int> counter{0};

void increment() {
    for (int i = 0; i < 1000; ++i) {
        counter.fetch_add(1, std::memory_order_relaxed);
    }
}
```

`std::memory_order` កំណត់កម្រិតនៃការរៀបចំលំដាប់រវាងខ្សែស្រឡាយ។
`relaxed` គឺគ្រប់គ្រាន់សម្រាប់ការរាប់សាមញ្ញ ប៉ុន្តែសម្រាប់ការធ្វើសមកាលកម្មទិន្នន័យ
ត្រូវប្រើ `acquire`/`release`។

## Deadlock

Deadlock កើតឡើងនៅពេលខ្សែស្រឡាយពីររង់ចាំគ្នាទៅវិញ។ ឧទាហរណ៍
ខ្សែស្រឡាយ A កាន់ mutex 1 ហើយចង់បាន mutex 2 ខណៈ B កាន់ mutex 2 ហើយចង់បាន 1។
ដំណោះស្រាយ៖ ចាក់សោតាមលំដាប់ដូចគ្នាគ្រប់កន្លែង ឬប្រើ `std::scoped_lock` (C++17)
ដែលចាក់សោច្រើនក្នុងពេលតែមួយដោយសុវត្ថិភាព។

## ការរកកំហុស concurrency

- `-fsanitize=thread` (GCC/Clang) រកឃើញ data race។
- `-fsanitize=address` រកឃើញការប្រើអង្គចងចាំខុស។
- សូមដំណើរការការធ្វើតេស្តច្រើនដង — កំហុស concurrency មិនកើតឡើងរាល់ដងទេ។

:::{warning}
ការបន្ថែម `std::atomic` ឬ mutex មិនធ្វើឱ្យកូដត្រឹមត្រូវដោយស្វ័យប្រវត្តិទេ។
អ្នកត្រូវគិតថាតើទិន្នន័យណាត្រូវការពារ និងតើការរៀបចំលំដាប់បែបណាត្រូវការ។
:::

## កូដឧទាហរណ៍

```{literalinclude} ../../examples/advanced/concurrency.cpp
:language: cpp
```

លទ្ធផល៖

```text
worker done
worker done
worker done
worker done
counter: 4000
```

## អានបន្ថែម

- [cppreference: `std::mutex`](https://en.cppreference.com/w/cpp/thread/mutex)
- [cppreference: `std::atomic`](https://en.cppreference.com/w/cpp/atomic/atomic)
- [cppreference: memory order](https://en.cppreference.com/w/cpp/atomic/memory_order)
