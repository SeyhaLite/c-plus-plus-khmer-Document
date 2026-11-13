// std: c++17
// copy constructor និង move constructor ជាមួយការរាយការណ៍។
#include <iostream>
#include <string>
#include <utility>
#include <vector>

class Tracker {
public:
    explicit Tracker(std::string name) : name_(std::move(name)) {}

    Tracker(const Tracker& other) : name_(other.name_) {
        std::cout << "copy " << name_ << '\n';
    }

    Tracker(Tracker&& other) noexcept : name_(std::move(other.name_)) {
        other.name_ = "(moved)";
        std::cout << "move " << name_ << '\n';
    }

    const std::string& name() const { return name_; }

private:
    std::string name_;
};

int main() {
    Tracker a("a");
    Tracker b = a;              // copy
    Tracker c = std::move(a);   // move

    std::cout << "a name: " << a.name() << '\n';
    std::cout << "c name: " << c.name() << '\n';

    std::vector<Tracker> items;
    items.reserve(2);
    items.push_back(Tracker("x"));   // ផ្លាស់ទីចូល vector
    std::cout << "size: " << items.size() << '\n';
    (void)b;
    return 0;
}

/* EXPECT
copy a
move a
a name: (moved)
c name: a
move x
size: 1
*/
