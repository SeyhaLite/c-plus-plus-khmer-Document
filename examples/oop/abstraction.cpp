// std: c++17
// ថ្នាក់អរូបីជាចំណុចប្រទាក់ និងការអនុវត្តពីរផ្សេងគ្នា។
#include <iostream>
#include <string>

class Logger {
public:
    virtual ~Logger() = default;
    virtual void log(const std::string& message) = 0;
};

class ConsoleLogger : public Logger {
public:
    void log(const std::string& message) override {
        std::cout << "[console] " << message << '\n';
    }
};

class FileLogger : public Logger {
public:
    void log(const std::string& message) override {
        std::cout << "[file] " << message << '\n';
    }
};

void run(Logger& logger) {
    logger.log("started");
}

int main() {
    ConsoleLogger console;
    FileLogger file;
    run(console);
    run(file);
    return 0;
}

/* EXPECT
[console] started
[file] started
*/
