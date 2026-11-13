// std: c++17
// អ្នកដើរកាត់ និងប្រតិបត្តិការសំខាន់ៗ។
#include <algorithm>
#include <iostream>
#include <iterator>
#include <vector>

int main() {
    std::vector<int> values{1, 2, 3, 4};

    for (auto it = values.begin(); it != values.end(); ++it) {
        std::cout << *it << ' ';
    }
    std::cout << '\n';

    for (auto it = values.rbegin(); it != values.rend(); ++it) {
        std::cout << *it << ' ';
    }
    std::cout << '\n';

    auto found = std::find(values.begin(), values.end(), 3);
    std::cout << "found: " << *found
              << " at offset " << (found - values.begin()) << '\n';
    std::cout << "distance begin-end: "
              << std::distance(values.begin(), values.end()) << '\n';
    return 0;
}

/* EXPECT
1 2 3 4 
4 3 2 1 
found: 3 at offset 2
distance begin-end: 4
*/
