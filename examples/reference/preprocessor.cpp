// std: c++17
// ម៉ាក្រូ និងការ compile ដោយលក្ខខណ្ឌ។
#include <iostream>

#define PI 3.14159
#define SQUARE(x) ((x) * (x))
#define DEBUG 1

int main() {
    std::cout << "PI: " << PI << '\n';
    std::cout << "SQUARE(4): " << SQUARE(4) << '\n';

#if DEBUG
    std::cout << "debug on\n";
#endif

    std::cout << "cpp standard: " << __cplusplus << '\n';
    return 0;
}

/* EXPECT
PI: 3.14159
SQUARE(4): 16
debug on
cpp standard: 201703
*/
