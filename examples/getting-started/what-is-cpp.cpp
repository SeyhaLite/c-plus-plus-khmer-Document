// std: c++11
// គំរូតូចមួយបង្ហាញលក្ខណៈមូលដ្ឋានរបស់ C++៖
// ប្រភេទទិន្នន័យ ធុងទិន្នន័យ (container) និងរង្វិលជុំលើជួរ។
#include <iostream>
#include <string>
#include <vector>

int main() {
    std::vector<std::string> standards{"C++98", "C++11", "C++17", "C++20"};

    std::cout << "Known standards:";
    for (const auto& name : standards) {
        std::cout << ' ' << name;
    }
    std::cout << '\n';
    std::cout << "Count: " << standards.size() << '\n';
    return 0;
}

/* EXPECT
Known standards: C++98 C++11 C++17 C++20
Count: 4
*/
