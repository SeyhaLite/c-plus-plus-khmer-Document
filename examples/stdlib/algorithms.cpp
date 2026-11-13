// std: c++17
// អាល់ហ្គោរីតស្តង់ដារ៖ sort, find, transform, accumulate, copy_if។
#include <algorithm>
#include <iostream>
#include <iterator>
#include <numeric>
#include <vector>

int main() {
    std::vector<int> values{5, 2, 8, 1, 9};
    std::sort(values.begin(), values.end());

    for (int x : values) {
        std::cout << x << ' ';
    }
    std::cout << '\n';

    auto it = std::find(values.begin(), values.end(), 8);
    std::cout << "found 8: " << (it != values.end() ? "yes" : "no") << '\n';

    std::transform(values.begin(), values.end(), values.begin(),
                   [](int x) { return x * 2; });
    std::cout << "sum: " << std::accumulate(values.begin(), values.end(), 0) << '\n';

    std::vector<int> out;
    std::copy_if(values.begin(), values.end(), std::back_inserter(out),
                 [](int x) { return x > 10; });
    std::cout << "gt10 count: " << out.size() << '\n';
    return 0;
}

/* EXPECT
1 2 5 8 9 
found 8: yes
sum: 50
gt10 count: 2
*/
