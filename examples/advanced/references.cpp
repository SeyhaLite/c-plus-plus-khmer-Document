// std: c++17
// យោងជាឈ្មោះផ្សេង យោងជាប៉ារ៉ាម៉ែត្រ និងយោងក្នុងរង្វិលជុំ។
#include <iostream>
#include <string>

void scale(int& value, int factor) {
    value *= factor;
}

int main() {
    int number = 10;
    int& alias = number;
    alias += 5;
    std::cout << "number: " << number << '\n';

    scale(number, 2);
    std::cout << "scaled: " << number << '\n';

    const std::string& text = std::string("hello");
    std::cout << "text: " << text << '\n';

    int values[] = {1, 2, 3};
    for (int& value : values) {
        value *= 2;
    }
    std::cout << "values: " << values[0] << values[1] << values[2] << '\n';
    return 0;
}

/* EXPECT
number: 15
scaled: 30
text: hello
values: 246
*/
