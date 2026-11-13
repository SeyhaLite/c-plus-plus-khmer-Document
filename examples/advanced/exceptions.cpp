// std: c++17
// ការបោះ និងការចាប់ករណីលើកលែង ជាមួយថ្នាក់ផ្ទាល់ខ្លួន។
#include <exception>
#include <iostream>
#include <stdexcept>
#include <string>

class ValidationError : public std::runtime_error {
public:
    explicit ValidationError(const std::string& message)
        : std::runtime_error(message) {}
};

int parse_positive(int value) {
    if (value <= 0) {
        throw ValidationError("value must be positive");
    }
    return value;
}

int main() {
    try {
        std::cout << "parsed: " << parse_positive(5) << '\n';
    } catch (const ValidationError&) {
        std::cout << "error: validation\n";
    }

    try {
        parse_positive(-1);
    } catch (const std::exception& error) {
        const bool matched = std::string(error.what()) == "value must be positive";
        std::cout << "caught base: " << (matched ? "yes" : "no") << '\n';
    }
    return 0;
}

/* EXPECT
parsed: 5
caught base: yes
*/
