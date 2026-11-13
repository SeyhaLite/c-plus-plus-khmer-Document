// std: c++17
#include <iostream>

int sum_formula(int n) {
    return n * (n + 1) / 2;
}

int main() {
    int n = 10;
    std::cout << "n: " << n << '\n';
    std::cout << "sum: " << sum_formula(n) << '\n';
    return 0;
}

/* EXPECT
n: 10
sum: 55
*/