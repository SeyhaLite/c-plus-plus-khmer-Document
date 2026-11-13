// std: c++17
// std::filesystem::path និងប្រតិបត្តិការឯកសារ/ថត។
#include <filesystem>
#include <iostream>

namespace fs = std::filesystem;

int main() {
    fs::path p = "a/b/c.txt";
    std::cout << "filename: " << p.filename().string() << '\n';
    std::cout << "extension: " << p.extension().string() << '\n';
    std::cout << "parent: " << p.parent_path().string() << '\n';

    fs::path dir = fs::temp_directory_path();
    std::cout << "temp exists: " << (fs::exists(dir) ? "yes" : "no") << '\n';
    std::cout << "is dir: " << (fs::is_directory(dir) ? "yes" : "no") << '\n';
    return 0;
}

/* EXPECT
filename: c.txt
extension: .txt
parent: a/b
temp exists: yes
is dir: yes
*/
