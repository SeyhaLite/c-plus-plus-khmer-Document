// std: c++17
// ការពិនិត្យទំហំប្រភេទទិន្នន័យដោយ sizeof។
// លទ្ធផលពិតអាចខុសគ្នាតាមប្រព័ន្ធ។
#include <iostream>

int main() {
    std::cout << "sizeof(bool) = " << sizeof(bool) << '\n';
    std::cout << "sizeof(char) = " << sizeof(char) << '\n';
    std::cout << "sizeof(int) = " << sizeof(int) << '\n';
    std::cout << "sizeof(double) = " << sizeof(double) << '\n';
    std::cout << "sizeof(long) = " << sizeof(long) << '\n';
    return 0;
}

/* EXPECT
sizeof(bool) = 1
sizeof(char) = 1
sizeof(int) = 4
sizeof(double) = 8
sizeof(long) = 8
*/
