// std: c++17
// ពុម្ពអនុគមន៍ និងពុម្ពថ្នាក់។
#include <iostream>
#include <string>

template <typename T>
T maximum(T a, T b) {
    return a > b ? a : b;
}

template <typename T>
class Box {
public:
    explicit Box(T value) : value_(value) {}
    const T& get() const { return value_; }

private:
    T value_;
};

int main() {
    std::cout << "max int: " << maximum(3, 7) << '\n';
    std::cout << "max double: " << maximum(2.5, 1.5) << '\n';
    std::cout << "max string: "
              << maximum(std::string("apple"), std::string("pear")) << '\n';

    Box<int> numbers(42);
    Box<std::string> text("hello");
    std::cout << "box: " << numbers.get() << ", " << text.get() << '\n';
    return 0;
}

/* EXPECT
max int: 7
max double: 2.5
max string: pear
box: 42, hello
*/
