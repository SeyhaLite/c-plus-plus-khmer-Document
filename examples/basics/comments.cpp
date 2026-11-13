// std: c++17
// មតិយោបល់បន្ទាត់តែមួយចាប់ផ្ដើមដោយ //។

/*
  មតិយោបល់ប្លុកអាចមានច្រើនបន្ទាត់។
  កម្មវិធីបកប្រែមិនអានអត្ថបទនេះទេ។
*/
#include <iostream>

/// មតិយោបល់បែបឯកសារ (documentation comment) សម្រាប់ឧបករណ៍បង្កើតឯកសារ។
int difference(int a, int b) {
    return a - b;
}

int main() {
    int result = difference(10, 4);  // ហៅអនុគមន៍ ហើយរក្សាលទ្ធផល
    std::cout << "difference = " << result << '\n';
    return 0;
}

/* EXPECT
difference = 6
*/
