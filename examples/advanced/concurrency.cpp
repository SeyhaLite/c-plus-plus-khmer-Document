// std: c++17
// std::atomic សម្រាប់ការរាប់ និង std::mutex សម្រាប់ការបញ្ចេញអត្ថបទ។
#include <atomic>
#include <iostream>
#include <mutex>
#include <thread>
#include <vector>

int main() {
    std::atomic<int> counter{0};
    std::mutex log_mutex;
    std::vector<std::thread> threads;

    for (int i = 0; i < 4; ++i) {
        threads.emplace_back([&counter, &log_mutex] {
            for (int n = 0; n < 1000; ++n) {
                counter.fetch_add(1, std::memory_order_relaxed);
            }
            std::lock_guard<std::mutex> lock(log_mutex);
            std::cout << "worker done\n";
        });
    }

    for (auto& thread : threads) {
        thread.join();
    }
    std::cout << "counter: " << counter.load() << '\n';
    return 0;
}

/* EXPECT
worker done
worker done
worker done
worker done
counter: 4000
*/
