# វត្ថុ (Objects)

```{translation-meta} oop/objects
```

វត្ថុ (object) គឺជាការបង្កើតជាក់ស្តែងពីថ្នាក់។ បើថ្នាក់ជាគំរូ វត្ថុគឺជារបស់ពិត
ដែលមានទិន្នន័យរៀងៗខ្លួន។

## ការបង្កើតវត្ថុ

```cpp
Rectangle box;              // វត្ថុនៅលើ stack
Rectangle* ptr = new Rectangle();   // វត្ថុនៅលើ heap (ត្រូវ delete)
```

ការបង្កើតវត្ថុហៅ constructor ដោយស្វ័យប្រវត្តិ (មើល [អ្នកសាងសង់](constructors.md))។

## វត្ថុនីមួយៗមានទិន្នន័យរៀងៗខ្លួន

```cpp
Counter a;
Counter b;

a.increment();   // ប៉ះពាល់តែ a
```

`a` និង `b` ជាវត្ថុពីរផ្សេងគ្នា ទោះមានប្រភេទដូចគ្នាក៏ដោយ។

## ការចូលដល់សមាជិក

```cpp
box.set_size(3, 4);      // វត្ថុធម្មតា ប្រើ .
ptr->set_size(3, 4);     // ពោយន្ត័រ ប្រើ ->
```

## ការចម្លងវត្ថុ

```cpp
Counter copy = a;    // copy-initialization — ចម្លងសមាជិកទាំងអស់
```

ការចម្លងលំនាំដើមគឺជាការចម្លងសមាជិកម្តងមួយៗ (member-wise copy)។
បើវត្ថុកាន់ធនធាន (ឧទាហរណ៍ ពោយន្ត័រទៅអង្គចងចាំ) ការចម្លងលំនាំដើមអាចមិនត្រឹមត្រូវ
ហើយត្រូវសរសេរអ្នកសាងសង់ចម្លង (copy constructor) ដោយខ្លួនឯង។

## អាយុកាល

វត្ថុដែលបង្កើតក្នុងប្លុក `{ }` ត្រូវបំផ្លាញនៅចុងប្លុក (destructor ត្រូវហៅ)។
វត្ថុដែលបង្កើតដោយ `new` រស់រហូតដល់អ្នកហៅ `delete`។

## កូដឧទាហរណ៍

```{literalinclude} ../../examples/oop/objects.cpp
:language: cpp
```

លទ្ធផល៖

```text
a = 2
b = 1
copy = 3
a after copy = 2
```

ចំណុចសំខាន់៖ ការកែ `copy` មិនប៉ះពាល់ `a` ទេ ព្រោះវាជាវត្ថុដាច់ដោយឡែក។

## អានបន្ថែម

- [cppreference: objects](https://en.cppreference.com/w/cpp/language/object)
