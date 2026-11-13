// std: c++17
// if, else if, else និង if ជាមួយការចាប់ផ្ដើមតម្លៃ (C++17)។
#include <iostream>

int main() {
    int score = 78;

    std::cout << "grade: ";
    if (score >= 90) {
        std::cout << "A\n";
    } else if (score >= 80) {
        std::cout << "B\n";
    } else if (score >= 70) {
        std::cout << "C\n";
    } else {
        std::cout << "F\n";
    }

    int age = 20;
    if (const int voting_age = 18; age >= voting_age) {
        std::cout << "category: adult\n";
    } else {
        std::cout << "category: minor\n";
    }
    return 0;
}

/* EXPECT
grade: C
category: adult
*/
