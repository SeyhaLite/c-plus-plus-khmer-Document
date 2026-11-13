# ការខ្ចប់ទិន្នន័យ (Encapsulation)

```{translation-meta} oop/encapsulation
```

ការខ្ចប់ទិន្នន័យ (encapsulation) គឺការលាក់រចនាសម្ព័ន្ធខាងក្នុងរបស់ថ្នាក់
ហើយបង្ហាញតែចំណុចប្រទាក់ (interface) ដែលអ្នកប្រើត្រូវការ។

## កម្រិតចូលដំណើរការ

| កម្រិត | អាចចូលបានពី |
| --- | --- |
| `public` | គ្រប់កន្លែង |
| `protected` | ថ្នាក់ខ្លួនឯង និងថ្នាក់កូន |
| `private` | តែថ្នាក់ខ្លួនឯង (និង friend) |

## ហេតុអ្វីត្រូវលាក់

សមាជិក `private` ការពារ **invariant** របស់ថ្នាក់ — លក្ខខណ្ឌដែលត្រូវពិតជានិច្ច។
ឧទាហរណ៍ គណនីធនាគារមិនគួរមានសមតុល្យអវិជ្ជមានដោយគ្មានការត្រួតពិនិត្យ។
បើ `balance` ជា `public` នោះកូដណាមួយក៏អាចកែវាបានដោយផ្ទាល់។

## រូបមន្ត

```cpp
class BankAccount {
public:
    explicit BankAccount(int balance) : balance_(balance) {}

    void deposit(int amount);      // ចំណុចប្រទាក់សាធារណៈ
    int balance() const { return balance_; }

private:
    int balance_;                  // លាក់ទិន្នន័យ
};
```

## Getters និង setters

អនុគមន៍អាន (getter) គួរជា `const`។ អនុគមន៍កែ (setter) គួរត្រួតពិនិត្យតម្លៃ
ដើម្បីរក្សា invariant៖

```cpp
void set_age(int age) {
    if (age < 0) {
        throw std::invalid_argument("age must not be negative");
    }
    age_ = age;
}
```

## `friend`

ថ្នាក់ ឬអនុគមន៍ដែលប្រកាសជា `friend` អាចចូលដល់សមាជិក `private`។
ប្រើវាតែនៅពេលចាំបាច់ (ឧទាហរណ៍ ប្រមាណវិធី `<<` សម្រាប់បញ្ចេញវត្ថុ)។
ការប្រើ `friend` ច្រើនពេកធ្វើឱ្យការខ្ចប់ចុះខ្សោយ។

:::{note}
នៅ C++ `private` អនុវត្តនៅកម្រិត **ថ្នាក់** មិនមែនកម្រិតវត្ថុទេ។
ដូច្នេះអនុគមន៍សមាជិករបស់ថ្នាក់តែមួយអាចចូលដល់សមាជិក `private`
របស់វត្ថុផ្សេងក្នុងថ្នាក់ដូចគ្នា។
:::

## កូដឧទាហរណ៍

```{literalinclude} ../../examples/oop/encapsulation.cpp
:language: cpp
```

លទ្ធផល៖

```text
balance = 150
rejected: invalid amount
balance = 150
```

## អានបន្ថែម

- [cppreference: access specifiers](https://en.cppreference.com/w/cpp/language/access)
- [cppreference: `friend`](https://en.cppreference.com/w/cpp/language/friend)
