// std: c++17
// ឧទាហរណ៍ I/O ដែលអាចធ្វើតេស្តស្វ័យប្រវត្តិបាន ដោយប្រើ istringstream ជំនួស cin។
#include <iostream>
#include <sstream>
#include <string>

int main() {
    std::istringstream input("Sok 21");
    std::string name;
    int age = 0;
    input >> name >> age;

    std::cout << "name: " << name << '\n';
    std::cout << "age: " << age << '\n';
    std::cout << "next year: " << age + 1 << '\n';

    std::istringstream lines("Phnom Penh\nSiem Reap");
    std::string line;
    while (std::getline(lines, line)) {
        std::cout << "city: " << line << '\n';
    }
    return 0;
}

/* EXPECT
name: Sok
age: 21
next year: 22
city: Phnom Penh
city: Siem Reap
*/
