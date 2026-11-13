// std: c++17
// std::string និង std::string_view។
#include <iostream>
#include <string>
#include <string_view>

int main() {
    std::string text = "Hello";
    text += " World";

    std::cout << text << " (size " << text.size() << ")\n";
    std::cout << "substr: " << text.substr(6, 5) << '\n';

    std::string_view view = text;
    std::cout << "view: " << view << '\n';
    std::cout << "find 'World': " << text.find("World") << '\n';
    std::cout << "empty? " << (text.empty() ? "yes" : "no") << '\n';
    return 0;
}

/* EXPECT
Hello World (size 11)
substr: World
view: Hello World
find 'World': 6
empty? no
*/
