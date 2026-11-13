// std: c++17
// រង្វិលជុំបុរាណ រង្វិលជុំលើជួរ និងរង្វិលជុំជាន់គ្នា។
#include <iostream>
#include <vector>

int main() {
    int sum = 0;
    for (int i = 1; i <= 5; ++i) {
        sum += i;
    }
    std::cout << "sum = " << sum << '\n';

    std::vector<int> values{10, 20, 30};
    for (int value : values) {
        std::cout << "v=" << value << '\n';
    }

    for (int row = 1; row <= 2; ++row) {
        for (int col = 1; col <= 2; ++col) {
            std::cout << row << ',' << col << '\n';
        }
    }
    return 0;
}

/* EXPECT
sum = 15
v=10
v=20
v=30
1,1
1,2
2,1
2,2
*/
