// std: c++17
// ប្រមាណវិធីគណិត ការប្រៀបធៀប តក្ក ប៊ីត និង ternary។
#include <iostream>

int main() {
    int a = 5, b = 2;
    std::cout << "a+b: " << a + b << '\n';
    std::cout << "a/b: " << a / b << " a%b: " << a % b << '\n';
    std::cout << "a>b && b>0: " << (a > b && b > 0) << '\n';
    std::cout << "a&b: " << (a & b) << " a<<1: " << (a << 1) << '\n';

    int maximum = (a > b) ? a : b;
    std::cout << "max: " << maximum << '\n';
    std::cout << "sizeof(int): " << sizeof(int) << '\n';
    return 0;
}

/* EXPECT
a+b: 7
a/b: 2 a%b: 1
a>b && b>0: 1
a&b: 0 a<<1: 10
max: 5
sizeof(int): 4
*/
