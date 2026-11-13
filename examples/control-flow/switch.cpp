// std: c++17
// switch លើ enum class និងលើចំនួនគត់។
#include <iostream>

enum class State { idle, running, stopped };

int main() {
    State state = State::running;

    switch (state) {
        case State::idle:
            std::cout << "state 0: idle\n";
            break;
        case State::running:
            std::cout << "state 2: running\n";
            break;
        case State::stopped:
            std::cout << "state 3: stopped\n";
            break;
    }

    int priority = 2;
    switch (priority) {
        case 1:
        case 2:
            std::cout << "priority: high\n";
            break;
        default:
            std::cout << "priority: normal\n";
            break;
    }
    return 0;
}

/* EXPECT
state 2: running
priority: high
*/
