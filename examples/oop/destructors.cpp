// std: c++17
// លំដាប់នៃការហៅ constructor និង destructor។
#include <iostream>

class Tracked {
public:
    explicit Tracked(const char* name) : name_(name) {
        std::cout << "construct " << name_ << '\n';
    }

    ~Tracked() {
        std::cout << "destroy " << name_ << '\n';
    }

private:
    const char* name_;
};

int main() {
    std::cout << "begin\n";
    {
        Tracked inner("inner");
    }
    std::cout << "after block\n";

    Tracked outer("outer");
    std::cout << "end of main\n";
    return 0;
}

/* EXPECT
begin
construct inner
destroy inner
after block
construct outer
end of main
destroy outer
*/
