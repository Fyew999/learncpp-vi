# 9.x — Tổng Kết Chương 09 & Bài Tập Toàn Diện (Chapter 9 Summary and Quiz)

---

## 🎯 Mục Tiêu Bài Học
- Hệ thống hóa toàn bộ kiến thức Chương 09: Kiểm thử đơn vị, Độ bao phủ mã nguồn, Lỗi ngữ nghĩa, `std::cin` xử lý nhập liệu, và `assert`/`static_assert`.
- Hoàn thành bài tập thiết kế hệ thống nhập và tính toán phân số an toàn.

---

## 📝 Dự Án Thực Chiến: Lớp Phân Số An Toàn Bộ Nhớ

Viết chương trình tính toán và rút gọn phân số thỏa mãn:
1. Có cấu trúc `Fraction` gồm tử số và mẫu số.
2. Kiểm tra mẫu số khác 0 bằng `assert` trong hàm tạo.
3. Có hàm nhập liệu an toàn `getFraction()` chống mọi lỗi nhập ký tự từ `std::cin`.
4. Rút gọn phân số bằng thuật toán tìm ước chung lớn nhất (GCD).

::: details [Xem lời giải hoàn chỉnh]
```cpp
#include <iostream>
#include <numeric>
#include <limits>
#include <cassert>

struct Fraction
{
    int numerator { 0 };
    int denominator { 1 };

    Fraction(int num, int den) : numerator{ num }, denominator{ den }
    {
        // Khẳng định mẫu số không được bằng 0
        assert(den != 0 && "Mau so khong the bang 0!");
        simplify();
    }

    void simplify()
    {
        int gcd = std::gcd(numerator, denominator);
        if (gcd != 0)
        {
            numerator /= gcd;
            denominator /= gcd;
        }
        if (denominator < 0)
        {
            numerator = -numerator;
            denominator = -denominator;
        }
    }

    void print() const
    {
        std::cout << numerator << '/' << denominator << '\n';
    }
};

int getValidInt(const char* prompt)
{
    while (true)
    {
        std::cout << prompt;
        int val {};
        std::cin >> val;

        if (std::cin.fail())
        {
            std::cin.clear();
            std::cin.ignore(std::numeric_limits<std::streamsize>::max(), '\n');
            std::cout << "Gia tri khong hop le, vui long nhap lai!\n";
            continue;
        }

        std::cin.ignore(std::numeric_limits<std::streamsize>::max(), '\n');
        return val;
    }
}

int main()
{
    int num = getValidInt("Nhap tu so: ");
    int den {};
    do
    {
        den = getValidInt("Nhap mau so (khac 0): ");
        if (den == 0)
            std::cout << "Mau so phai khac 0!\n";
    } while (den == 0);

    Fraction f { num, den };
    std::cout << "Phan so da rut gon: ";
    f.print();

    return 0;
}
```
:::
