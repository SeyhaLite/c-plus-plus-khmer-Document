// std: c++17
// ប្រមាណវិធីនព្វន្ធ ការចែកចំនួនគត់ និងប្រមាណវិធីតក្កវិជ្ជា។
#include <iostream>

int main() {
    int a = 7;
    int b = 2;

    std::cout << "a / b = " << a / b << '\n';
    std::cout << "a % b = " << a % b << '\n';
    std::cout << "a / b as double = " << static_cast<double>(a) / b << '\n';
    std::cout << "-7 / 2 = " << -7 / 2 << '\n';
    std::cout << "-7 % 2 = " << -7 % 2 << '\n';

    int total = 0;
    total += a;      // 7
    total *= b;      // 14
    std::cout << "total = " << total << '\n';

    std::cout << "comparison: " << (a > b) << '\n';
    std::cout << "ternary: " << (a > b ? a : b) << '\n';
    std::cout << "logical: " << (!(a > b) && (b == 2)) << '\n';
    return 0;
}

/* EXPECT
a / b = 3
a % b = 1
a / b as double = 3.5
-7 / 2 = -3
-7 % 2 = -1
total = 14
comparison: 1
ternary: 7
logical: 0
*/
