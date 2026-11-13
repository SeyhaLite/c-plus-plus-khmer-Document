// std: c++17
// new/delete, new[]/delete[] និងការចាប់ផ្ដើមតម្លៃ។
#include <iostream>

int main() {
    int* single = new int(42);
    std::cout << "single: " << *single << '\n';
    delete single;

    int* array = new int[3]{1, 2, 3};
    int sum = 0;
    for (int i = 0; i < 3; ++i) {
        sum += array[i];
    }
    std::cout << "sum: " << sum << '\n';
    delete[] array;

    int* zeroed = new int[4]();   // value-initialized
    std::cout << "zeroed: " << zeroed[0] << '\n';
    delete[] zeroed;
    return 0;
}

/* EXPECT
single: 42
sum: 6
zeroed: 0
*/
