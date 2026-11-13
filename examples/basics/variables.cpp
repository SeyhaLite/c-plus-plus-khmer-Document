// std: c++17
// ការប្រកាស និងការចាប់ផ្ដើមតម្លៃអថេរ។
#include <iostream>
#include <string>

int main() {
    int count{3};
    double price{8.5};
    auto total = count * price;          // double
    std::string label{"score"};

    std::cout << "count = " << count << '\n';
    std::cout << "total = " << total << '\n';
    std::cout << "label = " << label << '\n';
    return 0;
}

/* EXPECT
count = 3
total = 25.5
label = score
*/
