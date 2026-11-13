// std: c++17
#include <iostream>

int sum_to(int n) {
    int total = 0;
    for (int i = 1; i <= n; ++i) total += i;
    return total;
}

int main() {
    int n = 5;
    std::cout << "n: " << n << '\n';
    std::cout << "sum: " << sum_to(n) << '\n';
    return 0;
}

/* EXPECT
n: 5
sum: 15
*/