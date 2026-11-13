// std: c++17
#include <iostream>
#include <vector>
#include <algorithm>

int main() {
    std::vector<int> values = {3, 7, 2, 9, 4};
    auto largest = *std::max_element(values.begin(), values.end());
    std::cout << "max: " << largest << '\n';
    return 0;
}

/* EXPECT
max: 9
*/