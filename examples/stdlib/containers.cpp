// std: c++17
// std::vector និង std::map ជាមួយប្រតិបត្តិការសំខាន់ៗ។
#include <iostream>
#include <map>
#include <string>
#include <vector>

int main() {
    std::vector<int> values{10, 20, 30};
    values.push_back(40);

    std::cout << "size: " << values.size() << '\n';
    std::cout << "front: " << values.front() << " back: " << values.back() << '\n';

    std::map<std::string, int> ages;
    ages["Alice"] = 30;
    ages["Bob"] = 25;

    for (const auto& [name, age] : ages) {
        std::cout << name << ": " << age << '\n';
    }
    std::cout << "count Alice: " << ages.count("Alice") << '\n';
    return 0;
}

/* EXPECT
size: 4
front: 10 back: 40
Alice: 30
Bob: 25
count Alice: 1
*/
