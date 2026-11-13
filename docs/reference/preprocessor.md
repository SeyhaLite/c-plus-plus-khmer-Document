# ព្រៃដំណើរការ (Preprocessor)

```{translation-meta} reference/preprocessor
```

ព្រៃដំណើរការ (preprocessor) ដំណើរការមុនកម្មវិធីបកប្រែ។ វាធ្វើការជំនួសអត្ថបទ
និងការ compile ដោយលក្ខខណ្ឌ។ ពាក្យបញ្ជាទាំងអស់ចាប់ផ្ដើមដោយ `#`។

## ការរួមបញ្ចូលឯកសារ

```cpp
#include <iostream>      // ឯកសារក្បាលប្រព័ន្ធ
#include "myheader.h"    // ឯកសារក្បាលផ្ទាល់ខ្លួន
```

## ម៉ាក្រូ (macros)

```cpp
#define PI 3.14159
#define SQUARE(x) ((x) * (x))
#undef PI
```

ម៉ាក្រូអនុគមន៍ត្រូវប្រើវង់ក្រចកជុំវិញប៉ារ៉ាម៉ែត្រ និងបញ្ចូលទាំងមូល
ដើម្បីជៀសវាងកំហុសអាទិភាព។

:::{warning}
ម៉ាក្រូមិនមានប្រភេទ និង scope ទេ។ ចាប់ពី C++11 គួរប្រើ `constexpr`
ឬ `inline` ជំនួសម៉ាក្រូតម្លៃ និង `template`/`inline` ជំនួសម៉ាក្រូអនុគមន៍
ដើម្បីទទួលបានសុវត្ថិភាពប្រភេទ និងការ debug។
:::

## ការ compile ដោយលក្ខខណ្ឌ

```cpp
#if DEBUG
    // កូដ debug
#elif defined(RELEASE)
    // កូដ release
#else
    // លំនាំដើម
#endif

#ifndef HEADER_H
#define HEADER_H
// មាតិកា
#endif
```

`#pragma once` គឺជាវិធីងាយស្រួលជំនួស include guard។

## ម៉ាក្រូដែលកំណត់រួច

| ម៉ាក្រូ | អត្ថន័យ |
| --- | --- |
| `__FILE__` | ឈ្មោះឯកសារ |
| `__LINE__` | លេខបន្ទាត់ |
| `__DATE__` | ថ្ងៃ compile |
| `__TIME__` | ម៉ោង compile |
| `__cplusplus` | តម្លៃស្តង់ដារ (ឧ. 201709L) |
| `__func__` | ឈ្មោះអនុគមន៍បច្ចុប្បន្ន |

## កូដឧទាហរណ៍

```{literalinclude} ../../examples/reference/preprocessor.cpp
:language: cpp
```

លទ្ធផល៖

```text
PI: 3.14159
SQUARE(4): 16
debug on
cpp standard: 201703
```

## អានបន្ថែម

- [cppreference: preprocessor](https://en.cppreference.com/w/cpp/preprocessor)
- [cppreference: `#define`](https://en.cppreference.com/w/cpp/preprocessor/replace)
- [cppreference: conditional inclusion](https://en.cppreference.com/w/cpp/preprocessor/conditional)
