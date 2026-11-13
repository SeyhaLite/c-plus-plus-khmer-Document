// std: c++17
// អនុគមន៍បណ្ណាល័យស្តង់ដារទូទៅ៖ max, min, clamp, swap, to_string, size។
#include <algorithm>
#include <iostream>
#include <iterator>
#include <string>

int main() {
    std::cout << "max(3,7): " << std::max(3, 7) << '\n';
    std::cout << "min(3,7): " << std::min(3, 7) << '\n';
    std::cout << "clamp(10,0,5): " << std::clamp(10, 0, 5) << '\n';

    int a = 1, b = 2;
    std::swap(a, b);
    std::cout << "swapped: " << a << ' ' << b << '\n';

    std::cout << "to_string: " << std::to_string(42) << '\n';

    std::string text = "hello";
    std::cout << "size: " << std::size(text) << '\n';
    return 0;
}

/* EXPECT
max(3,7): 7
min(3,7): 3
clamp(10,0,5): 5
swapped: 2 1
to_string: 42
size: 5
*/
