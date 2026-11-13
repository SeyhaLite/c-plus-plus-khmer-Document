// std: c++17
// អ្នកសាងសង់លំនាំដើម អ្នកសាងសង់មានប៉ារ៉ាម៉ែត្រ និង delegating constructor។
#include <iostream>
#include <string>
#include <utility>

class Person {
public:
    Person() : name_("unknown"), age_(0) {}

    Person(std::string name, int age) : name_(std::move(name)), age_(age) {}

    Person(std::string name) : Person(std::move(name), 0) {}

    void print() const {
        std::cout << name_ << " (" << age_ << ")\n";
    }

private:
    std::string name_;
    int age_;
};

int main() {
    Person a;
    Person b("Sok", 21);
    Person c("Dara");

    a.print();
    b.print();
    c.print();
    return 0;
}

/* EXPECT
unknown (0)
Sok (21)
Dara (0)
*/
