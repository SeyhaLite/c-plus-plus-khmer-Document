# អ្នកបំផ្លាញ (Destructors)

```{translation-meta} oop/destructors
```

អ្នកបំផ្លាញ (destructor) ត្រូវហៅដោយស្វ័យប្រវត្តិនៅពេលវត្ថុបញ្ចប់អាយុកាល។
វាមានឈ្មោះដូចថ្នាក់ ប៉ុន្តែមាន `~` នៅពីមុខ ហើយគ្មានប៉ារ៉ាម៉ែត្រ។

## រូបមន្ត

```cpp
class File {
public:
    explicit File(const char* path);
    ~File();            // អ្នកបំផ្លាញ
};
```

## ពេលណាត្រូវហៅ

- វត្ថុដែលបង្កើតក្នុងប្លុក ត្រូវបំផ្លាញនៅចុងប្លុក។
- វត្ថុដែលបង្កើតដោយ `new` ត្រូវបំផ្លាញនៅពេលហៅ `delete`។
- សមាជិករបស់វត្ថុត្រូវបំផ្លាញបន្ទាប់ពីតួអង្គកម្មវិធីរបស់អ្នកបំផ្លាញបញ្ចប់។
  លំដាប់គឺផ្ទុយពីលំដាប់បង្កើត។

## ហេតុអ្វីសំខាន់

អ្នកបំផ្លាញជាមូលដ្ឋាននៃ **RAII**៖ ធនធាន (ឯកសារ អង្គចងចាំ lock) ត្រូវដោះលែង
ដោយស្វ័យប្រវត្តិ ទោះកម្មវិធីចេញដោយធម្មតា ឬដោយសារករណីលើកលែង។
នេះជួយការពារការលេចធ្លាយអង្គចងចាំ (memory leak)។

```cpp
void work() {
    std::vector<int> values(1000);   // បង្កើត
    // ... បើមាន exception នៅទីនេះ vector នៅតែត្រូវបំផ្លាញ
}   // អ្នកបំផ្លាញរបស់ vector ត្រូវហៅនៅទីនេះ
```

## អ្នកបំផ្លាញនិម្មិត (virtual destructor)

បើអ្នកលុបវត្ថុតាមរយៈពោយន្ត័រទៅថ្នាក់មូលដ្ឋាន អ្នកបំផ្លាញ **ត្រូវ** ជា `virtual`៖

```cpp
class Base {
public:
    virtual ~Base() = default;
};

Base* ptr = new Derived();
delete ptr;      // បើ ~Base មិន virtual នេះជា undefined behavior
```

មើល [អនុគមន៍និម្មិត](virtual-functions.md) សម្រាប់ព័ត៌មានបន្ថែម។

:::{note}
អ្នកបំផ្លាញមិនអាចមានប៉ារ៉ាម៉ែត្រ និងមិនអាចមាន overload បានទេ។
ថ្នាក់មួយមានអ្នកបំផ្លាញតែមួយប៉ុណ្ណោះ។
:::

## កូដឧទាហរណ៍

```{literalinclude} ../../examples/oop/destructors.cpp
:language: cpp
```

លទ្ធផល៖

```text
begin
construct inner
destroy inner
after block
construct outer
end of main
destroy outer
```

សង្កេតថា `inner` ត្រូវបំផ្លាញនៅចុងប្លុក មុន `outer` ត្រូវបង្កើត។

## អានបន្ថែម

- [cppreference: destructors](https://en.cppreference.com/w/cpp/language/destructor)
