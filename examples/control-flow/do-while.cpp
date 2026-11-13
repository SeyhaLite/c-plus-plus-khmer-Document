// std: c++17
// do-while ប្រតិបត្តិយ៉ាងតិចម្តង មុនពេលពិនិត្យលក្ខខណ្ឌ។
#include <iostream>
#include <sstream>

int main() {
    std::istringstream input("0 -2 5");
    int value = 0;
    do {
        input >> value;
    } while (value <= 0);
    std::cout << "accepted = " << value << '\n';

    int i = 0;
    do {
        ++i;
    } while (i < 3);
    std::cout << "i = " << i << '\n';
    return 0;
}

/* EXPECT
accepted = 5
i = 3
*/
