# ប្រមាណវិធី (Operators)

```{translation-meta} reference/operators
```

ប្រមាណវិធី (operator) កំណត់របៀបដែលតម្លៃត្រូវប្រតិបត្តិការ។ C++ ផ្ដល់ប្រមាណវិធី
ជាច្រើនប្រភេទ។

## គណិតវិទ្យា

| ប្រមាណវិធី | អត្ថន័យ |
| --- | --- |
| `+`, `-`, `*`, `/` | បូក ដក គុណ ចែក |
| `%` | សំណល់នៃការចែក |
| `++`, `--` | បង្កើន/បន្ថយ ១ |
| `-x`, `+x` | សញ្ញា |

## ការប្រៀបធៀប

`==`, `!=`, `<`, `>`, `<=`, `>=`, `<=>` (spaceship, C++20)។

## តក្កវិទ្យា

`&&` (AND), `||` (OR), `!` (NOT)។ វាប្រើ short-circuit evaluation៖
បើលទ្ធផលអាចដឹងពី operand ទីមួយ នោះ operand ទីពីរមិនត្រូវបានវាយតម្លៃទេ។

## ប៊ីត (bitwise)

`&` (AND), `|` (OR), `^` (XOR), `~` (NOT), `<<` (left shift), `>>` (right shift)។

## ការផ្ដល់តម្លៃ

`=`, `+=`, `-=`, `*=`, `/=`, `%=`, `&=`, `|=`, `^=`, `<<=`, `>>=`។

## ផ្សេងៗ

- `?:` — ប្រមាណវិធីត្រីធាតុ (ternary)។
- `sizeof`, `sizeof...` — ទំហំជាបៃ។
- `alignof` — ការតម្រឹម។
- `typeid` — ប្រភេទពេលដំណើរការ (RTTI)។
- `new`, `delete` — បែងចែក/ដោះលែង។
- `.*`, `->*` — pointer to member។
- `::` — ការកំណត់ដែន (scope resolution)។
- `.` , `->` — ការចូលដល់សមាជិក។

:::{warning}
ការប្រើ `&` និង `&&` ច្រើនច្រលំគ្នា។ `&` គឺ bitwise AND ឬ reference;
`&&` គឺ logical AND ឬ rvalue reference។ បរិបទកំណត់អត្ថន័យ។
:::

## ការអាទិភាព (precedence)

ប្រមាណវិធីមានកម្រិតអាទិភាពខុសគ្នា។ បើមិនប្រាកដ សូមប្រើវង់ក្រចក `()`
ដើម្បីធ្វើឱ្យកូដអានយល់ច្បាស់។

## កូដឧទាហរណ៍

```{literalinclude} ../../examples/reference/operators.cpp
:language: cpp
```

លទ្ធផល៖

```text
a+b: 7
a/b: 2 a%b: 1
a>b && b>0: 1
a&b: 0 a<<1: 10
max: 5
sizeof(int): 4
```

## អានបន្ថែម

- [cppreference: operator precedence](https://en.cppreference.com/w/cpp/language/operator_precedence)
- [cppreference: operators](https://en.cppreference.com/w/cpp/language/operators)
