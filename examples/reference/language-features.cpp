// std: c++17
// លក្ខណៈភាសា៖ range-based for, lambda, structured binding, optional, constexpr។
#include <iostream>
#include <optional>
#include <utility>
#include <vector>

int main() {
    std::vector<int> values{1, 2, 3};

    auto sum = 0;
    for (int x : values) {
        sum += x;
    }
    auto square = [](int x) { return x * x; };
    std::cout << "sum: " << sum << " square(4): " << square(4) << '\n';

    auto pair = std::make_pair(10, 20);
    auto [a, b] = pair;
    (void)a;
    (void)b;
    std::cout << "structured binding ok\n";

    std::optional<int> value = 7;
    std::cout << "optional: " << *value << '\n';

    constexpr int computed = 5 * 5;
    std::cout << "constexpr: " << computed << '\n';
    return 0;
}

/* EXPECT
sum: 6 square(4): 16
structured binding ok
optional: 7
constexpr: 25
*/
