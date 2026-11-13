// std: c++17
// អាសយដ្ឋាន ការ dereference និងពោយន្ត័រ nullptr។
#include <iostream>

void add_one(int* value) {
    if (value != nullptr) {
        *value += 1;
    }
}

int main() {
    int number = 41;
    int* ptr = &number;

    std::cout << "value: " << *ptr << '\n';
    add_one(ptr);
    std::cout << "after: " << number << '\n';

    int values[] = {10, 20, 30};
    int* cursor = values;   // អារេរលាយទៅពោយន្ត័រទៅធាតុដំបូង
    std::cout << "second: " << *(cursor + 1) << '\n';

    int* nothing = nullptr;
    std::cout << "nullptr check: " << (nothing == nullptr ? "yes" : "no") << '\n';
    return 0;
}

/* EXPECT
value: 41
after: 42
second: 20
nullptr check: yes
*/
