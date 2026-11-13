// std: c++17
// while សម្រាប់លក្ខខណ្ឌដែលមិនដឹងចំនួនជុំ និង while(true) ជាមួយ break។
#include <iostream>

int main() {
    int n = 987;
    int digits = 0;
    while (n > 0) {
        n /= 10;
        ++digits;
    }
    std::cout << "digits = " << digits << '\n';

    int attempts = 0;
    while (true) {
        ++attempts;
        if (attempts == 3) {
            break;
        }
    }
    std::cout << "attempts = " << attempts << '\n';
    return 0;
}

/* EXPECT
digits = 3
attempts = 3
*/
