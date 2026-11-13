// std: c++17
// អាយុកាលនៃទិន្នន័យលើ static, stack និង heap។
#include <iostream>

int global_counter = 0;   // static storage duration

int next_id() {
    return ++global_counter;
}

int main() {
    std::cout << "id: " << next_id() << '\n';
    std::cout << "id: " << next_id() << '\n';

    {
        int local = 5;    // stack: បំផ្លាញនៅចុងប្លុក
        std::cout << "local: " << local << '\n';
    }

    int* heap_value = new int(7);   // heap: រស់រហូតដល់ delete
    std::cout << "heap: " << *heap_value << '\n';
    delete heap_value;
    heap_value = nullptr;
    return 0;
}

/* EXPECT
id: 1
id: 2
local: 5
heap: 7
*/
