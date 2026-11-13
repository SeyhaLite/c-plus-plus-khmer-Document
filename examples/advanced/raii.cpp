// std: c++17
// វត្ថុដែលកាន់កាប់អង្គចងចាំ និងដោះលែងវានៅ destructor។
#include <iostream>

class Buffer {
public:
    explicit Buffer(int size) : size_(size), data_(new int[size]) {
        std::cout << "allocate " << size_ << '\n';
    }

    ~Buffer() {
        delete[] data_;
        std::cout << "release " << size_ << '\n';
    }

    Buffer(const Buffer&) = delete;
    Buffer& operator=(const Buffer&) = delete;

    int& at(int index) { return data_[index]; }
    int size() const { return size_; }

private:
    int size_;
    int* data_;
};

int main() {
    {
        Buffer buffer(4);
        buffer.at(0) = 42;
        std::cout << "value: " << buffer.at(0) << '\n';
    }   // destructor ដោះលែងអង្គចងចាំ
    std::cout << "done\n";
    return 0;
}

/* EXPECT
allocate 4
value: 42
release 4
done
*/
