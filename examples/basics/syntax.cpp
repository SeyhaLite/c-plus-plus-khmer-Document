// std: c++17
// រចនាសម្ព័ន្ធកម្មវិធី C++៖ directive, អនុគមន៍, អថេរ និងសេចក្តីថ្លែងការណ៍។
#include <iostream>

constexpr int width = 4;   // អថេរថេរនៅកម្រិតឯកសារ

int area(int w, int h) {   // អនុគមន៍ដែលត្រឡប់ int
    return w * h;
}

int main() {
    const int height = 3;              // អថេរនៅក្នុង main
    std::cout << "area = " << area(width, height) << '\n';
    return 0;
}

/* EXPECT
area = 12
*/
