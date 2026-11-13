// std: c++17
// ការរួមបញ្ចូលឯកសារក្បាលស្តង់ដារជាច្រើន និងការប្រើវា។
#include <algorithm>
#include <filesystem>
#include <iostream>
#include <numeric>
#include <string>
#include <vector>

int main() {
    std::vector<int> values{3, 1, 2};
    std::sort(values.begin(), values.end());

    std::cout << "sorted: ";
    for (int x : values) {
        std::cout << x << ' ';
    }
    std::cout << '\n';

    std::cout << "sum: " << std::accumulate(values.begin(), values.end(), 0) << '\n';
    std::cout << "filesystem header ok\n";
    return 0;
}

/* EXPECT
sorted: 1 2 3 
sum: 6
filesystem header ok
*/
