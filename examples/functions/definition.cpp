// std: c++17
// ការកំណត់អនុគមន៍ inline និងការហៅវា។
#include <iostream>

inline int cube(int x) {
    return x * x * x;
}

int main() {
    std::cout << "cube(3) = " << cube(3) << '\n';
    return 0;
}

/* EXPECT
cube(3) = 27
*/
