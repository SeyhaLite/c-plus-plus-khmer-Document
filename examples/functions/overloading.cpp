// std: c++17
// អនុគមន៍ឈ្មោះតែមួយជាមួយប៉ារ៉ាម៉ែត្រខុសគ្នា។
#include <iostream>
#include <string>

void show(int value) {
    std::cout << "int: " << value << '\n';
}

void show(double value) {
    std::cout << "double: " << value << '\n';
}

void show(const std::string& value) {
    std::cout << "string: " << value << '\n';
}

int main() {
    show(7);
    show(2.5);
    show("text");
    return 0;
}

/* EXPECT
int: 7
double: 2.5
string: text
*/
