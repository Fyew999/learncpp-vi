# 27.7 — Khối Try Của Hàm (Function Try Blocks)

---

## 🎯 Mục Tiêu Bài Học
- Hiểu hạn chế của khối `try` thông thường: Không thể bắt được ngoại lệ phát sinh từ **Member Initializer List** của Constructor.
- Nắm vững cú pháp và cơ chế của **Function Try Blocks**.
- Nhận thức quy tắc bắt buộc: Constructor function try block luôn tự động re-throw ngoại lệ.

---

## 1. Vấn Đề Ngoại Lệ Trong Member Initializer List

Nếu một lớp thành viên con ném ngoại lệ ngay trong danh sách khởi tạo của Constructor lớp cha, khối `try` thông thường bên trong thân hàm `{}` sẽ hoàn toàn bất lực vì đối tượng chưa kịp bước vào thân hàm:

```cpp
class A
{
public:
    A(int x) { throw std::runtime_error{ "Loi khoi tao A" }; }
};

class B
{
    A m_a;
public:
    B() : m_a{ 10 } // NẾU Ở ĐÂY NÉM NGOẠI LỆ THÌ BẮT THẾ NÀO?
    {
    }
};
```

---

## 2. Cú Pháp Function Try Block

Function try block bao bọc toàn bộ hàm, bao gồm cả danh sách khởi tạo:

```cpp
#include <iostream>
#include <stdexcept>

class Member
{
public:
    Member(int x)
    {
        if (x <= 0)
            throw std::runtime_error{ "Member: Gia tri phai > 0!" };
    }
};

class Container
{
private:
    Member m_member;

public:
    // FUNCTION TRY BLOCK BAO TRÙM CẢ INITIALIZER LIST
    Container(int x) try : m_member{ x }
    {
        std::cout << "Khoi tao Container thanh cong!\n";
    }
    catch (const std::exception& e)
    {
        std::cerr << "Container bat duoc loi tu Member: " << e.what() << '\n';
        // LƯU Ý BẮT BUỘC: Khi kết thúc catch, C++ sẽ TỰ ĐỘNG RE-THROW ngoại lệ!
        // Đối tượng Container coi như khởi tạo thất bại và bị hủy!
    }
};

int main()
{
    try
    {
        Container c{ -5 };
    }
    catch (const std::exception& e)
    {
        std::cerr << "main() bat ngoai le: " << e.what() << '\n';
    }
    return 0;
}
```
