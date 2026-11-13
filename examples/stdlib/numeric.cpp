// std: c++17
// ប្រតិបត្តិការលេខស្តង់ដារ៖ accumulate, iota, gcd, lcm។
#include <iostream>
#include <numeric>
#include <vector>

int main() {
    std::vector<int> values{1, 2, 3, 4};
    std::cout << "sum: " << std::accumulate(values.begin(), values.end(), 0) << '\n';

    std::iota(values.begin(), values.end(), 10);
    std::cout << "iota: ";
    for (int x : values) {
        std::cout << x << ' ';
    }
    std::cout << '\n';

    std::cout << "gcd(12,18): " << std::gcd(12, 18) << '\n';
    std::cout << "lcm(4,6): " << std::lcm(4, 6) << '\n';
    return 0;
}

/* EXPECT
sum: 10
iota: 10 11 12 13 
gcd(12,18): 6
lcm(4,6): 12
*/
