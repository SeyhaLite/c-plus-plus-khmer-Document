// std: c++17
// break, continue និង return ក្នុងរង្វិលជុំ។
#include <iostream>

int first_negative(const int values[], int count) {
    for (int i = 0; i < count; ++i) {
        if (values[i] < 0) {
            return i;   // ចេញពីអនុគមន៍ភ្លាម
        }
    }
    return -1;
}

int main() {
    for (int i = 0; i < 5; ++i) {
        if (i == 2) {
            continue;   // រំលង 2
        }
        if (i == 4) {
            break;      // ឈប់មុន 4
        }
        std::cout << "i=" << i << '\n';
    }

    int data[] = {3, 8, -1, 6};
    std::cout << "first negative index = " << first_negative(data, 4) << '\n';
    return 0;
}

/* EXPECT
i=0
i=1
i=3
first negative index = 2
*/
