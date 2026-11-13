// std: c++17
// auto, trailing return type, std::pair, structured bindings និង [[nodiscard]]។
#include <iostream>
#include <utility>

auto add(int a, int b) -> int {
    return a + b;
}

std::pair<int, int> minmax(int a, int b) {
    if (a < b) {
        return {a, b};
    }
    return {b, a};
}

[[nodiscard]] int important() {
    return 42;
}

int main() {
    std::cout << "add = " << add(2, 3) << '\n';

    auto [lo, hi] = minmax(9, 4);
    std::cout << "lo = " << lo << ", hi = " << hi << '\n';
    std::cout << "important = " << important() << '\n';
    return 0;
}

/* EXPECT
add = 5
lo = 4, hi = 9
important = 42
*/
