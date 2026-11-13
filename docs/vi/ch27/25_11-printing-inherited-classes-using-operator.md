# 25.11 — Xuất Đối Tượng Đa Hình Với Toán Tử `<<`

---

## 🎯 Mục Tiêu Bài Học
- Hiểu vấn đề nan giải: Tại sao `friend std::ostream& operator<<` không thể khai báo là hàm ảo `virtual`.
- Nắm vững mẫu thiết kế (Idiom) kinh điển: Kết hợp `operator<<` thông thường với một hàm ảo hỗ trợ `print()`.

---

## 1. Vấn Đề: Toán Tử `<<` Không Thể Là Hàm Ảo

Toán tử xuất luồng `operator<<` bắt buộc phải nhận tham số đầu tiên là `std::ostream&`. Do đó, nó phải được cài đặt dưới dạng một hàm tự do (Friend function), không thể là một hàm thành viên của lớp.
Vì nó không phải hàm thành viên, **C++ không cho phép khai báo `virtual friend std::ostream& operator<<`**!

Nếu bạn chỉ nạp chồng `operator<<` thông thường cho `Base` và `Derived`, khi in qua con trỏ `Base*`, C++ sẽ chỉ gọi phiên bản của `Base`:

```cpp
Base* b = new Derived();
std::cout << *b; // Sẽ luôn gọi operator<<(ostream&, const Base&) bất kể b là gì!
```

---

## 2. Giải Pháp: Mẫu Thiết Kế Hàm Ảo `print()`

Để in đa hình, chúng ta áp dụng kỹ thuật 2 bước:
1. Khai báo một hàm ảo thành viên: `virtual std::ostream& print(std::ostream& out) const;` trong lớp cơ sở, và ghi đè nó ở các lớp con.
2. Nạp chồng duy nhất **MỘT** toán tử `operator<<` cho lớp `Base`, và bên trong nó chỉ việc ủy quyền cho hàm ảo `print()`!

```cpp
#include <iostream>

class Base
{
public:
    virtual ~Base() = default;

    // 1. Ham ao thanh vien chiu trach nhiem xuat du lieu
    virtual std::ostream& print(std::ostream& out) const
    {
        out << "Base";
        return out;
    }

    // 2. Nap chong operator<< duy nhat tai Base
    friend std::ostream& operator<<(std::ostream& out, const Base& b)
    {
        return b.print(out); // Goi ham ao print() tai runtime!
    }
};

class Derived : public Base
{
public:
    std::ostream& print(std::ostream& out) const override
    {
        out << "Derived da duoc in da hinh ruc ro!";
        return out;
    }
};

int main()
{
    Base b;
    Derived d;

    Base& ref1 = b;
    Base& ref2 = d;

    // In thong qua tham chieu lop co so:
    std::cout << ref1 << '\n'; // In ra: Base
    std::cout << ref2 << '\n'; // In ra: Derived da duoc in da hinh ruc ro!

    return 0;
}
```
