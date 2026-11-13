# switch និង case

```{translation-meta} control-flow/switch
```

`switch` ជ្រើសសាខាកូដតាមតម្លៃចំនួនគត់ ឬតម្លៃ `enum`។ វាអានងាយជាងខ្សែសង្វាក់
`if` វែងៗ នៅពេលប្រៀបធៀបតម្លៃជាច្រើន។

## រូបមន្ត

```cpp
switch (value) {
    case 1:
        // ...
        break;
    case 2:
        // ...
        break;
    default:
        // ...
        break;
}
```

`value` ត្រូវជាប្រភេទចំនួនគត់ ឬ `enum` (ឬប្រភេទដែលអាចបំប្លែងជាចំនួនគត់)។
មិនអាចប្រើ `std::string` ឬ `double` បានទេ។

## `break` និងការធ្លាក់ចុះ (fallthrough)

បើគ្មាន `break` ទេ ការប្រតិបត្តិនឹងបន្តទៅ `case` បន្ទាប់ (fallthrough)។
នេះអាចជាចេតនា ឬជាកំហុស។

```cpp
switch (level) {
    case 1:
    case 2:
        std::cout << "beginner\n";   // ទាំង 1 និង 2 ចូលទីនេះ
        break;
    case 3:
        std::cout << "advanced\n";
        break;
    default:
        std::cout << "unknown\n";
}
```

ចាប់ពី **C++17** អ្នកអាចសម្គាល់ fallthrough ដែលចេតនាដោយ `[[fallthrough]];`
ដើម្បីប្រាប់កម្មវិធីបកប្រែ និងអ្នកអានថាវាមិនមែនជាកំហុស៖

```cpp
case 1:
    prepare();
    [[fallthrough]];
case 2:
    finish();
```

## `default`

`default` ត្រូវបានប្រតិបត្តិនៅពេលគ្មាន `case` ណាត្រូវនឹងតម្លៃ។
វាមិនចាំបាច់នៅចុងក្រោយទេ ប៉ុន្តែការដាក់នៅចុងក្រោយអានងាយជាង។

:::{warning}
ការប្រកាសអថេរនៅក្នុង `case` អាចបង្កបញ្ហាព្រោះវិសាលភាពរបស់ `switch` គឺតែមួយ។
បើត្រូវការ សូមដាក់វង់ក្រចកអង្គុយ `{ }` ជុំវិញ `case` នោះ។
:::

## ជាមួយ `enum class`

`switch` លើ `enum class` ត្រូវបានណែនាំ ព្រោះកម្មវិធីបកប្រែអាចព្រមានបើអ្នកភ្លេច
តម្លៃណាមួយ (ជាមួយ `-Wswitch`)។

```cpp
enum class State { idle, running, stopped };

switch (state) {
    case State::idle:    /* ... */ break;
    case State::running: /* ... */ break;
    case State::stopped: /* ... */ break;
}
```

`enum class` ជាលក្ខណៈ **C++11**។

## កូដឧទាហរណ៍

```{literalinclude} ../../examples/control-flow/switch.cpp
:language: cpp
```

លទ្ធផល៖

```text
state 2: running
priority: high
```

## អានបន្ថែម

- [cppreference: `switch` statement](https://en.cppreference.com/w/cpp/language/switch)
