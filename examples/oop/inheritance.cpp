// std: c++17
// មរតក ជាមួយលំដាប់នៃការបង្កើត និងការបំផ្លាញ។
#include <iostream>
#include <string>
#include <utility>

class Animal {
public:
    explicit Animal(std::string name) : name_(std::move(name)) {
        std::cout << "Animal(" << name_ << ")\n";
    }

    virtual ~Animal() {
        std::cout << "~Animal(" << name_ << ")\n";
    }

    void eat() const {
        std::cout << name_ << " eats\n";
    }

    const std::string& name() const { return name_; }

protected:
    std::string name_;
};

class Dog : public Animal {
public:
    explicit Dog(std::string name) : Animal(std::move(name)) {
        std::cout << "Dog()\n";
    }

    ~Dog() override {
        std::cout << "~Dog()\n";
    }

    void bark() const {
        std::cout << name_ << " barks\n";
    }
};

int main() {
    Dog dog("Rex");
    dog.eat();
    dog.bark();
    std::cout << "name: " << dog.name() << '\n';
    return 0;
}

/* EXPECT
Animal(Rex)
Dog()
Rex eats
Rex barks
name: Rex
~Dog()
~Animal(Rex)
*/
