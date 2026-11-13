// std: c++17
// ប្រើកម្មវិធីនេះដើម្បីផ្ទៀងផ្ទាត់ថាកម្មវិធីបកប្រែរបស់អ្នកគាំទ្រ C++17។
#include <iostream>

int main() {
    std::cout << "standard macro: " << __cplusplus << '\n';
#if __cplusplus >= 201703L
    std::cout << "C++17 or newer: ok\n";
#else
    std::cout << "C++17 or newer: missing\n";
#endif
    return 0;
}

/* EXPECT
standard macro: 201703
C++17 or newer: ok
*/
