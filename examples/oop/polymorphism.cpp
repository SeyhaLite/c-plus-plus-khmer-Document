// std: c++17
// ពហុរូបភាពតាមរយៈអនុគមន៍និម្មិត និង std::unique_ptr។
#include <iostream>
#include <memory>
#include <vector>

class Shape {
public:
    virtual ~Shape() = default;
    virtual double area() const = 0;
    virtual const char* name() const = 0;
};

class Square : public Shape {
public:
    explicit Square(double side) : side_(side) {}

    double area() const override { return side_ * side_; }
    const char* name() const override { return "square"; }

private:
    double side_;
};

class Circle : public Shape {
public:
    explicit Circle(double radius) : radius_(radius) {}

    double area() const override { return 3.141592653589793 * radius_ * radius_; }
    const char* name() const override { return "circle"; }

private:
    double radius_;
};

int main() {
    std::vector<std::unique_ptr<Shape>> shapes;
    shapes.push_back(std::make_unique<Square>(3.0));
    shapes.push_back(std::make_unique<Circle>(1.0));

    for (const auto& shape : shapes) {
        std::cout << shape->name() << ": " << shape->area() << '\n';
    }
    return 0;
}

/* EXPECT
square: 9
circle: 3.14159
*/
