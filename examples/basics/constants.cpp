// std: c++17
// const និង constexpr។
#include <iostream>

constexpr double pi = 3.14159265358979323846;

constexpr double circle_area(double radius) {
    return pi * radius * radius;
}

int main() {
    constexpr double area = circle_area(5.0);  // គណនានៅពេលបកប្រែ
    const int max_attempts = 3;                // ថេរនៅពេលដំណើរការ

    std::cout << "circle area = " << area << '\n';
    std::cout << "max attempts = " << max_attempts << '\n';
    return 0;
}

/* EXPECT
circle area = 78.5398
max attempts = 3
*/
