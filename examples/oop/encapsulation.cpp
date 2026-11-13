// std: c++17
// សមាជិក private និងការត្រួតពិនិត្យ invariant ក្នុងអនុគមន៍សាធារណៈ។
#include <iostream>
#include <stdexcept>

class BankAccount {
public:
    explicit BankAccount(int balance) : balance_(balance) {}

    void deposit(int amount) {
        if (amount <= 0) {
            throw std::invalid_argument("amount must be positive");
        }
        balance_ += amount;
    }

    int balance() const { return balance_; }

private:
    int balance_;
};

int main() {
    BankAccount account(100);
    account.deposit(50);
    std::cout << "balance = " << account.balance() << '\n';

    try {
        account.deposit(-10);
    } catch (const std::invalid_argument&) {
        std::cout << "rejected: invalid amount\n";
    }
    std::cout << "balance = " << account.balance() << '\n';
    return 0;
}

/* EXPECT
balance = 150
rejected: invalid amount
balance = 150
*/
