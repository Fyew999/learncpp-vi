# 25.8 — Lớp Cơ Sở Ảo (Virtual Base Classes) Giải Quyết Vấn Đề Kim Cương

---

## 🎯 Mục Tiêu Bài Học
- Hiểu cách thức từ khóa `virtual` trong cú pháp kế thừa (`class Derived : virtual public Base`) giải quyết triệt để **Bài toán kim cương (The Diamond Problem)**.
- Trực quan hóa cấu trúc bộ nhớ RAM: Đối tượng con chỉ sở hữu duy nhất một Base Subobject dùng chung.
- Nắm bắt quy tắc khởi tạo đặc biệt: Lớp dẫn xuất cuối cùng (**Most-derived class**) chịu trách nhiệm khởi tạo Virtual Base.

---

## 1. Cú Pháp Kế Thừa Ảo (Virtual Inheritance)

Để đảm bảo các nhánh kế thừa không nhân bản đối tượng gốc, chúng ta thêm từ khóa `virtual` vào phát biểu kế thừa:

```cpp
#include <iostream>

class PoweredDevice
{
public:
    int m_power;
    PoweredDevice(int power) : m_power{ power }
    {
        std::cout << "PoweredDevice khoi tao voi cong suat: " << power << "W\n";
    }
};

// Kế thừa Ảo từ PoweredDevice
class Scanner : virtual public PoweredDevice
{
public:
    Scanner(int power) : PoweredDevice{ power } {}
};

// Kế thừa Ảo từ PoweredDevice
class Printer : virtual public PoweredDevice
{
public:
    Printer(int power) : PoweredDevice{ power } {}
};

// Copier kế thừa từ cả Scanner và Printer
class Copier : public Scanner, public Printer
{
public:
    // LƯU Ý ĐẶC BIỆT: Copier phải chịu trách nhiệm khởi tạo PoweredDevice trực tiếp!
    Copier(int power)
        : PoweredDevice{ power } // Khoi tao truc tiep Virtual Base
        , Scanner{ power }
        , Printer{ power }
    {
    }
};

int main()
{
    Copier copier{ 120 };
    // KHÔNG CÒN NHẬP NHẰNG! Chỉ có DUY NHẤT một m_power trong toàn bộ copier:
    std::cout << "Cong suat may in: " << copier.m_power << "W\n";

    return 0;
}
```

---

## 2. Trực Quan Hóa Cấu Trúc Bộ Nhớ RAM Của Virtual Inheritance

```
BỐ CỤC BỘ NHỚ RAM CỦA Copier KHI CÓ VIRTUAL INHERITANCE:
+-------------------------------------------------------------+
| [Scanner Subobject]                                         |
|   - Con trỏ virtual base pointer (vbptr)                    |
|   - Dữ liệu riêng của Scanner                               |
+-------------------------------------------------------------+
| [Printer Subobject]                                         |
|   - Con trỏ virtual base pointer (vbptr)                    |
|   - Dữ liệu riêng của Printer                               |
+-------------------------------------------------------------+
| [Copier Members]                                            |
|   - Dữ liệu riêng của Copier                                |
+-------------------------------------------------------------+
| [DUY NHẤT MỘT PoweredDevice Subobject DÙNG CHUNG]          |
|   - int m_power                                             |
+-------------------------------------------------------------+
```
Nhờ cơ chế này, `Scanner` và `Printer` không tự chứa `PoweredDevice` bên trong mình nữa, mà chúng lưu một con trỏ hoặc bảng offset trỏ tới vị trí của `PoweredDevice` dùng chung được đặt ở cuối đối tượng!
