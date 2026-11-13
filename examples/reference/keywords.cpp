// std: c++17
// ពាក្យគន្លឹះ៖ constexpr, auto, decltype, static_assert, noexcept។
#include <iostream>
#include <type_traits>

constexpr int square(int x) {
    return x * x;
}

int main() {
    constexpr int value = square(5);
    auto doubled = value * 2;
    decltype(doubled) tripled = value * 3;

    std::cout << "value: " << value << '\n';
    std::cout << "doubled: " << doubled << '\n';
    std::cout << "tripled: " << tripled << '\n';
    std::cout << "is int: " << std::is_same<decltype(value), const int>::value << '\n';

    static_assert(square(3) == 9, "square(3) must be 9");
    std::cout << "static_assert passed\n";
    return 0;
}

/* EXPECT
value: 25
doubled: 50
tripled: 75
is int: 1
static_assert passed
*/
