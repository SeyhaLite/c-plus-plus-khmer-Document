// std: c++17
// lambda ជាមួយការចាប់ដោយចម្លង ការចាប់ដោយយោង និងការប្រើជាមួយអាល់ហ្គោរីត។
#include <algorithm>
#include <iostream>
#include <vector>

int main() {
    int factor = 3;
    auto times = [factor](int x) { return x * factor; };
    std::cout << "times(4) = " << times(4) << '\n';

    int total = 0;
    auto add_to_total = [&total](int x) { total += x; };
    std::vector<int> values{1, 2, 3};
    for (int value : values) {
        add_to_total(value);
    }
    std::cout << "total = " << total << '\n';

    auto is_even = [](int x) { return x % 2 == 0; };
    std::cout << "even count = "
              << std::count_if(values.begin(), values.end(), is_even) << '\n';
    return 0;
}

/* EXPECT
times(4) = 12
total = 6
even count = 1
*/
