// std: c++17
// ការផ្ដល់តម្លៃដោយចម្លង ដោយយោង និងដោយយោងថេរ។
#include <iostream>
#include <string>

void by_value(int x) {
    x = 99;
}

void by_reference(int& x) {
    x = 99;
}

void print(const std::string& text) {
    std::cout << text << '\n';
}

int main() {
    int a = 1;
    by_value(a);
    std::cout << "after value: " << a << '\n';

    int b = 1;
    by_reference(b);
    std::cout << "after reference: " << b << '\n';

    print("hello from const reference");
    return 0;
}

/* EXPECT
after value: 1
after reference: 99
hello from const reference
*/
