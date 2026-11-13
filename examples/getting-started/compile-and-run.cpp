// std: c++17
// កម្មវិធីបង្ហាញភាពខុសគ្នារវាងការគណនានៅពេលបកប្រែ និងនៅពេលដំណើរការ។
#include <iostream>

int add(int a, int b) {
    return a + b;
}

int main() {
    constexpr int compile_time = 2 + 3;  // គណនាដោយកម្មវិធីបកប្រែ
    int runtime = add(4, 5);             // គណនានៅពេលដំណើរការ

    std::cout << "compile-time: " << compile_time << '\n';
    std::cout << "runtime: " << runtime << '\n';
    return 0;
}

/* EXPECT
compile-time: 5
runtime: 9
*/
