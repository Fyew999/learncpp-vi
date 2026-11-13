# 24.6 — Bổ Sung Tính Năng Mới Cho Lớp Dẫn Xuất

---

## 🎯 Mục Tiêu Bài Học
- Nắm bắt cách mở rộng tính năng của lớp cơ sở bằng cách khai báo thêm các biến và hàm mới trong lớp dẫn xuất.
- Hiểu được sự khác biệt về quyền hạn giữa đối tượng lớp cha và đối tượng lớp con.

---

## 1. Mở Rộng Tính Năng

Một trong những sức mạnh lớn nhất của Kế thừa là bạn không cần đụng chạm hay biên dịch lại lớp cơ sở mà vẫn có thể mở rộng tính năng theo nhu cầu chuyên biệt.

```cpp
#include <iostream>

class Base
{
private:
    int m_value{};

public:
    Base(int value) : m_value{ value } {}

    void identify() const { std::cout << "Toi la Base, gia tri = " << m_value << '\n'; }
};

// Derived mo rong Base: them bien m_bonus va ham speak()
class Derived : public Base
{
private:
    double m_bonus{ 0.0 };

public:
    Derived(int value, double bonus)
        : Base{ value }, m_bonus{ bonus } {}

    // Ham moi bo sung hoan toan
    void speak() const
    {
        std::cout << "Derived co them gia tri thuong = " << m_bonus << '\n';
    }
};

int main()
{
    Base base{ 10 };
    base.identify();
    // base.speak(); // LOI BIEN DICH: Base khong co ham speak()!

    Derived derived{ 20, 99.5 };
    derived.identify(); // Ke thua tu Base
    derived.speak();    // Tinh nang rieng cua Derived

    return 0;
}
```

---

## 2. Quiz

### Câu hỏi:
Lớp cha có thể gọi được các hàm mới được định nghĩa trong lớp con không?
`<details>`
`<summary>``<b>`Xem lời giải</b></summary>

**Đáp án**: **HOÀN TOÀN KHÔNG!** Lớp cơ sở hoàn toàn không biết gì về sự tồn tại của các lớp con kế thừa từ nó. Quan hệ kế thừa là dòng chảy một chiều: Lớp con biết mọi thứ về lớp cha, nhưng lớp cha không biết lớp con có những tính năng gì.
</details>
