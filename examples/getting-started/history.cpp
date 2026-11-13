// std: c++17
// កម្មវិធីបង្ហាញថាកម្មវិធីបកប្រែកំពុងស្ថិតក្រោមស្តង់ដារណា
// តាមរយៈម៉ាក្រូ __cplusplus និងម៉ាក្រូលក្ខណៈ (feature test macro)។
#include <iostream>

int main() {
    std::cout << "__cplusplus = " << __cplusplus << '\n';

#if __cplusplus >= 201703L
    std::cout << "structured bindings and if constexpr are available\n";
#else
    std::cout << "C++17 features are not available\n";
#endif

#if defined(__cpp_concepts) && __cpp_concepts >= 201907L
    std::cout << "concepts (C++20) are available\n";
#endif
    return 0;
}

/* EXPECT
__cplusplus = 201703
structured bindings and if constexpr are available
*/
