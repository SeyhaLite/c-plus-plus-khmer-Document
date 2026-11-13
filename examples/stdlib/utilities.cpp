// std: c++17
// std::pair, structured bindings, std::optional, std::variant។
#include <iostream>
#include <optional>
#include <tuple>
#include <utility>
#include <variant>

int main() {
    std::pair<int, std::string> p{1, "one"};
    std::cout << p.first << " " << p.second << '\n';

    auto [a, b] = p;
    std::cout << "bound: " << a << ' ' << b << '\n';

    std::optional<int> value = 42;
    std::cout << "optional: " << (value ? *value : -1) << '\n';

    std::optional<int> empty;
    std::cout << "empty has value: " << (empty.has_value() ? "yes" : "no") << '\n';

    std::variant<int, std::string> v = "hello";
    std::cout << "variant holds string: "
              << (std::holds_alternative<std::string>(v) ? "1" : "0") << '\n';
    return 0;
}

/* EXPECT
1 one
bound: 1 one
optional: 42
empty has value: no
variant holds string: 1
*/
