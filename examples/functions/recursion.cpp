// std: c++17
// អនុគមន៍បែបហៅខ្លួនឯង ជាមួយករណីគោលច្បាស់លាស់។
#include <iostream>

long long factorial(int n) {
    if (n <= 1) {
        return 1;                   // ករណីគោល
    }
    return n * factorial(n - 1);    // ករណីហៅខ្លួនឯង
}

long long fib(int n) {
    if (n < 2) {
        return n;
    }
    return fib(n - 1) + fib(n - 2);
}

int main() {
    std::cout << "5! = " << factorial(5) << '\n';
    std::cout << "10! = " << factorial(10) << '\n';
    std::cout << "fib(10) = " << fib(10) << '\n';
    return 0;
}

/* EXPECT
5! = 120
10! = 3628800
fib(10) = 55
*/
