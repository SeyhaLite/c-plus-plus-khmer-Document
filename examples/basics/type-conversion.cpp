// std: c++17
// ការបំប្លែងប្រភេទដោយស្វ័យប្រវត្តិ និងដោយ static_cast។
#include <iostream>

int main() {
    int apples = 7;
    int people = 2;

    std::cout << "integer division: " << apples / people << '\n';
    std::cout << "double division: " << static_cast<double>(apples) / people << '\n';

    double price = 9.99;
    int truncated = static_cast<int>(price);
    std::cout << "truncated: " << truncated << '\n';

    bool flag = 42;  // តម្លៃមិនសូន្យបំប្លែងជា true
    std::cout << "bool from 42: " << flag << '\n';
    return 0;
}

/* EXPECT
integer division: 3
double division: 3.5
truncated: 9
bool from 42: 1
*/
