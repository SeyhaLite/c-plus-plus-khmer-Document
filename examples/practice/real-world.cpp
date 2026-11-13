// std: c++17
#include <iostream>
#include <sstream>
#include <string>
#include <vector>

int main() {
    std::string line = "Alice,30,Engineer";
    std::vector<std::string> fields;
    std::stringstream stream(line);
    std::string item;
    while (std::getline(stream, item, ',')) {
        fields.push_back(item);
    }
    for (const auto& field : fields) {
        std::cout << field << '\n';
    }
    return 0;
}

/* EXPECT
Alice
30
Engineer
*/