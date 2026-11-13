// std: c++17
// ការប្រកាសអនុគមន៍មុនការហៅ និងការកំណត់នៅក្រោយ។
#include <iostream>

int square(int x);   // prototype

int main() {
    std::cout << "square(5) = " << square(5) << '\n';
    return 0;
}

int square(int x) {
    return x * x;
}

/* EXPECT
square(5) = 25
*/
