// std: c++20
// generator តូចមួយដែលសរសេរដោយប្រើ co_yield និង promise_type។
#include <coroutine>
#include <exception>
#include <iostream>

class Generator {
public:
    struct promise_type {
        int current{};

        Generator get_return_object() {
            return Generator{std::coroutine_handle<promise_type>::from_promise(*this)};
        }

        std::suspend_always initial_suspend() noexcept { return {}; }
        std::suspend_always final_suspend() noexcept { return {}; }
        void return_void() {}
        void unhandled_exception() { std::terminate(); }

        std::suspend_always yield_value(int value) {
            current = value;
            return {};
        }
    };

    explicit Generator(std::coroutine_handle<promise_type> handle) : handle_(handle) {}
    ~Generator() {
        if (handle_) {
            handle_.destroy();
        }
    }

    Generator(const Generator&) = delete;
    Generator& operator=(const Generator&) = delete;

    bool next() {
        handle_.resume();
        return !handle_.done();
    }

    int value() const { return handle_.promise().current; }

private:
    std::coroutine_handle<promise_type> handle_;
};

Generator count_to(int limit) {
    for (int i = 1; i <= limit; ++i) {
        co_yield i;
    }
}

int main() {
    auto generator = count_to(3);
    while (generator.next()) {
        std::cout << generator.value() << '\n';
    }
    std::cout << "done\n";
    return 0;
}

/* EXPECT
1
2
3
done
*/
