// std: c++17
// វត្ថុនីមួយៗមានទិន្នន័យរៀងៗខ្លួន និងការចម្លងវត្ថុ។
#include <iostream>

class Counter {
public:
    void increment() { ++value_; }
    int value() const { return value_; }

private:
    int value_ = 0;
};

int main() {
    Counter a;
    Counter b;
    a.increment();
    a.increment();
    b.increment();

    std::cout << "a = " << a.value() << '\n';
    std::cout << "b = " << b.value() << '\n';

    Counter copy = a;   // ចម្លងវត្ថុ
    copy.increment();
    std::cout << "copy = " << copy.value() << '\n';
    std::cout << "a after copy = " << a.value() << '\n';
    return 0;
}

/* EXPECT
a = 2
b = 1
copy = 3
a after copy = 2
*/
