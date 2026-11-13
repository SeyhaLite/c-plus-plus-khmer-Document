// std: c++17
// dynamic binding, static binding និង object slicing។
#include <iostream>
#include <string>

class Base {
public:
    virtual ~Base() = default;

    virtual std::string speak() const {
        return "base";
    }

    std::string static_speak() const {
        return "base-static";
    }
};

class Derived : public Base {
public:
    std::string speak() const override {
        return "derived";
    }

    std::string static_speak() const {
        return "derived-static";
    }
};

int main() {
    Derived d;
    Base& ref = d;

    std::cout << "virtual: " << ref.speak() << '\n';
    std::cout << "non-virtual: " << ref.static_speak() << '\n';

    Base sliced = d;   // object slicing
    std::cout << "sliced: " << sliced.speak() << '\n';
    return 0;
}

/* EXPECT
virtual: derived
non-virtual: base-static
sliced: base
*/
