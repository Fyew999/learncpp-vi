# 27.x — Tổng Kết Chương 27 & Bài Kiểm Tra Toàn Diện

---

## 🎯 Mục Tiêu
- Hệ thống hóa toàn bộ bức tranh về Xử Lý Ngoại Lệ trong C++.
- Vượt qua bài kiểm tra trắc nghiệm và thử thách lập trình hệ thống Tài Khoản Ngân Hàng an toàn giao dịch.

---

## 1. Bảng Tóm Tắt Các Quy Tắc Ngoại Lệ Sống Còn

1. **Tách rời xử lý lỗi**: Dùng `throw` để báo lỗi, `try-catch` để xử lý tập trung.
2. **Stack Unwinding**: Biến cục bộ được hủy tự động, nhưng con trỏ thô sẽ rò rỉ nếu không dùng Smart Pointer.
3. **Bắt bằng tham chiếu**: Luôn dùng `catch (const std::exception& e)` để tránh Object Slicing.
4. **Thứ tự khối catch**: Lớp dẫn xuất con bắt trước, lớp cơ sở cha bắt sau.
5. **Ném lại ngoại lệ**: Luôn dùng `throw;` độc lập để bảo toàn kiểu đối tượng gốc.
6. **Destructor an toàn**: Tuyệt đối **KHÔNG BAO GIỜ** ném ngoại lệ từ Destructor!

---

## 2. Bài Tập Thực Chiến: Hệ Thống Giao Dịch Ngân Hàng (Transactional Bank)

### Yêu cầu:
Xây dựng lớp `BankAccount` với:
- Số tài khoản (`std::string`), Số dư (`double`).
- Lớp ngoại lệ tự tạo `InsufficientFundsException` kế thừa từ `std::runtime_error`.
- Phương thức `withdraw(double amount)`: Nếu số tiền rút lớn hơn số dư, ném ngoại lệ `InsufficientFundsException`.
- Hàm thực hiện giao dịch chuyển tiền giữa 2 tài khoản đảm bảo an toàn ngoại lệ (Nếu rút tiền từ tài khoản nguồn thất bại, tài khoản đích không bị ảnh hưởng).

`<details>`
`<summary>``<b>`Xem lời giải mã nguồn C++ hoàn chỉnh

```cpp
#include <iostream>
#include <string>
#include <stdexcept>

// Lớp ngoại lệ chuyên biệt
class InsufficientFundsException : public std::runtime_error
{
private:
    double m_attemptedAmount;
    double m_currentBalance;

public:
    InsufficientFundsException(double attempted, double balance)
        : std::runtime_error{ "Loi: So du khong du de thuc hien giao dich!" }
        , m_attemptedAmount{ attempted }
        , m_currentBalance{ balance }
    {
    }

    double getAttempted() const { return m_attemptedAmount; }
    double getBalance() const { return m_currentBalance; }
};

class BankAccount
{
private:
    std::string m_accountNumber;
    double m_balance{ 0.0 };

public:
    BankAccount(std::string_view accNum, double initialBalance)
        : m_accountNumber{ accNum }, m_balance{ initialBalance }
    {
        if (initialBalance < 0.0)
            throw std::invalid_argument{ "So du khoi tao khong duoc am!" };
    }

    void deposit(double amount)
    {
        if (amount <= 0.0)
            throw std::invalid_argument{ "So tien nap phai lon hon 0!" };
        m_balance += amount;
    }

    void withdraw(double amount)
    {
        if (amount <= 0.0)
            throw std::invalid_argument{ "So tien rut phai lon hon 0!" };
        if (amount > m_balance)
            throw InsufficientFundsException{ amount, m_balance };

        m_balance -= amount;
    }

    double getBalance() const { return m_balance; }
    const std::string& getAccountNumber() const { return m_accountNumber; }
};

// Hàm chuyển tiền bảo đảm an toàn giao dịch
void transferMoney(BankAccount& from, BankAccount& to, double amount)
{
    std::cout << "Dang chuyen " << amount << "$ tu " << from.getAccountNumber() 
              << " sang " << to.getAccountNumber() << "...\n";

    // 1. Rút từ tài khoản nguồn trước (nếu lỗi sẽ ném ngoại lệ và dừng tại đây)
    from.withdraw(amount);

    // 2. Nạp vào tài khoản đích
    to.deposit(amount);

    std::cout << "-> Giao dich thanh cong hoan hao!\n";
}

int main()
{
    BankAccount accA{ "ACC_VIETCOMBANK_01", 1000.0 };
    BankAccount accB{ "ACC_TECHCOMBANK_02", 200.0 };

    try
    {
        // Giao dịch 1: Hợp lệ
        transferMoney(accA, accB, 300.0);

        // Giao dịch 2: Rút vượt quá số dư
        transferMoney(accA, accB, 1500.0);
    }
    catch (const InsufficientFundsException& e)
    {
        std::cerr << "[NGOAI LE NGAN HANG]: " << e.what() << '\n';
        std::cerr << " -> So tien yeu cau rut: " << e.getAttempted() << "$\n";
        std::cerr << " -> So du hien tai:      " << e.getBalance() << "$\n";
    }
    catch (const std::exception& e)
    {
        std::cerr << "[NGOAI LE HE THONG]: " << e.what() << '\n';
    }

    std::cout << "\nSo du cuoi cung cua " << accA.getAccountNumber() << ": " << accA.getBalance() << "$\n";
    std::cout << "So du cuoi cung cua " << accB.getAccountNumber() << ": " << accB.getBalance() << "$\n";

    return 0;
}
```

