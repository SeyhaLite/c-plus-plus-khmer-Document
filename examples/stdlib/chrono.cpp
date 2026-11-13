// std: c++17
// std::chrono::duration, steady_clock និងការវាស់រយៈពេល។
#include <chrono>
#include <iostream>
#include <thread>

int main() {
    using namespace std::chrono;

    auto start = steady_clock::now();
    std::this_thread::sleep_for(milliseconds(10));
    auto end = steady_clock::now();
    auto ms = duration_cast<milliseconds>(end - start).count();
    std::cout << "elapsed ms >= 10: " << (ms >= 10 ? "yes" : "no") << '\n';

    seconds s{2};
    minutes m{1};
    std::cout << "total seconds: " << (m + s).count() << '\n';
    return 0;
}

/* EXPECT
elapsed ms >= 10: yes
total seconds: 62
*/
