// std: c++17
// ថ្នាក់សាមញ្ញមួយ ជាមួយសមាជិកឯកជន និងអនុគមន៍សមាជិក const។
#include <iostream>

class Rectangle {
public:
    void set_size(int w, int h) {
        width_ = w;
        height_ = h;
    }

    int area() const {
        return width_ * height_;
    }

private:
    int width_ = 0;
    int height_ = 0;
};

int main() {
    Rectangle box;
    box.set_size(4, 5);
    std::cout << "area = " << box.area() << '\n';
    return 0;
}

/* EXPECT
area = 20
*/
