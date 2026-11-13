// std: c++20
// std::ranges views និងអាល់ហ្គោរីត ranges។
#include <algorithm>
#include <iostream>
#include <ranges>
#include <vector>

int main() {
    std::vector<int> values{1, 2, 3, 4, 5, 6};

    auto even = values | std::views::filter([](int x) { return x % 2 == 0; });
    for (int x : even) {
        std::cout << x << ' ';
    }
    std::cout << '\n';

    auto doubled = values | std::views::transform([](int x) { return x * 2; })
                          | std::views::take(3);
    for (int x : doubled) {
        std::cout << x << ' ';
    }
    std::cout << '\n';

    std::cout << "count even: "
              << std::count_if(values.begin(), values.end(), [](int x) { return x % 2 == 0; })
              << '\n';
    return 0;
}

/* EXPECT
2 4 6 
2 4 6 
count even: 3
*/
