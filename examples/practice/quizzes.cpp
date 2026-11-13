// std: c++17
#include <iostream>

int main() {
    int correct = 3;
    int total = 5;
    std::cout << "score: " << correct << "/" << total << '\n';
    std::cout << "percent: " << (correct * 100 / total) << "%\n";
    return 0;
}

/* EXPECT
score: 3/5
percent: 60%
*/