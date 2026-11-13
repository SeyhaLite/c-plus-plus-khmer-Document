// std: c++17
// std::thread, join និង joinable។
#include <iostream>
#include <numeric>
#include <thread>
#include <vector>

int main() {
    std::vector<int> data(1000);
    std::iota(data.begin(), data.end(), 0);   // 0..999

    long long total = 0;
    std::thread worker([&data, &total] {
        total = std::accumulate(data.begin(), data.end(), 0LL);
    });

    std::cout << "thread id valid: "
              << (worker.get_id() != std::thread::id() ? "yes" : "no") << '\n';

    worker.join();   // រង់ចាំឱ្យការគណនាបញ្ចប់ មុនអាន total
    std::cout << "total: " << total << '\n';
    std::cout << "joinable after join: " << (worker.joinable() ? "yes" : "no") << '\n';
    return 0;
}

/* EXPECT
thread id valid: yes
total: 499500
joinable after join: no
*/
