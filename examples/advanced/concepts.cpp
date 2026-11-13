// std: c++20
// concepts ស្តង់ដារ ជាមួយ requires clause និង abbreviated template។
#include <concepts>
#include <iostream>

template <typename T>
    requires std::integral<T>
T twice(T value) {
    return value * 2;
}

void print(const std::integral auto& value) {
    std::cout << "int-like: " << value << '\n';
}

void print(const std::floating_point auto& value) {
    std::cout << "float-like: " << value << '\n';
}

int main() {
    std::cout << "twice: " << twice(21) << '\n';
    print(7);
    print(2.5);

    static_assert(std::integral<int>);
    static_assert(!std::integral<double>);
    std::cout << "static asserts passed\n";
    return 0;
}

/* EXPECT
twice: 42
int-like: 7
float-like: 2.5
static asserts passed
*/
