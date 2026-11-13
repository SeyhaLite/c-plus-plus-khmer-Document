// std: c++17
// cin/cout និង string streams។
#include <iostream>
#include <sstream>

int main() {
    std::cout << "Hello, " << "world" << '\n';

    std::istringstream in("42");
    int n;
    in >> n;
    std::cout << "parsed: " << n << '\n';

    std::ostringstream out;
    out << "value=" << n;
    std::cout << out.str() << '\n';
    return 0;
}

/* EXPECT
Hello, world
parsed: 42
value=42
*/
