// std: c++17
// unique_ptr, shared_ptr និងការរាប់ម្ចាស់។
#include <iostream>
#include <memory>
#include <string>
#include <utility>

class Resource {
public:
    explicit Resource(std::string name) : name_(std::move(name)) {
        std::cout << "acquire " << name_ << '\n';
    }

    ~Resource() {
        std::cout << "release " << name_ << '\n';
    }

    const std::string& name() const { return name_; }

private:
    std::string name_;
};

void use(std::unique_ptr<Resource> resource) {
    std::cout << "using " << resource->name() << '\n';
}   // ដោះលែងនៅទីនេះ

int main() {
    auto first = std::make_unique<Resource>("unique");
    std::cout << "unique_ptr ready\n";
    use(std::move(first));
    std::cout << "first is null: " << (first == nullptr ? "yes" : "no") << '\n';

    auto shared = std::make_shared<Resource>("shared");
    {
        auto copy = shared;
        std::cout << "count: " << shared.use_count() << '\n';
    }
    std::cout << "count after scope: " << shared.use_count() << '\n';
    return 0;
}

/* EXPECT
acquire unique
unique_ptr ready
using unique
release unique
first is null: yes
acquire shared
count: 2
count after scope: 1
release shared
*/
