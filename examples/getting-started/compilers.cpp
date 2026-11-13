// std: c++17
// កម្មវិធីបង្ហាញរបៀបស្គាល់គ្រួសារកម្មវិធីបកប្រែដោយប្រើម៉ាក្រូដែលវាកំណត់ដោយខ្លួនឯង។
#include <iostream>

int main() {
#if defined(__clang__)
    const char* family = "Clang";
#elif defined(__GNUC__)
    const char* family = "GCC";
#elif defined(_MSC_VER)
    const char* family = "MSVC";
#else
    const char* family = "unknown";
#endif

    std::cout << "compiler family: " << family << '\n';
    std::cout << "standard: " << __cplusplus << '\n';
    return 0;
}

/* EXPECT
compiler family: GCC
standard: 201703
*/
