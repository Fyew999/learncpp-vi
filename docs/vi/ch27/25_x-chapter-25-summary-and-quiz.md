# 25.x — Tổng Kết Chương 25 & Bài Kiểm Tra Toàn Diện

---

## 🎯 Mục Tiêu
- Ôn tập toàn diện các trụ cột của Tính Đa Hình trong C++.
- Vượt qua bài kiểm tra trắc nghiệm và thử thách thiết kế hệ thống đồ họa đa hình.

---

## 1. Bảng Tóm Tắt Khái Niệm Chương 25

| Khái Niệm | Mục Đích | Lưu Ý Quan Trọng |
| :--- | :--- | :--- |
| **Virtual Function** | Kích hoạt liên kết động (Dynamic Dispatch) | Chi phí gọi gián tiếp qua vtable |
| **Virtual Destructor** | Đảm bảo dọn dẹp sạch lớp con khi xóa qua `Base*` | Bắt buộc phải có nếu lớp có bất kỳ hàm virtual nào |
| **override** | Bắt compiler đối chiếu chữ ký hàm | Luôn sử dụng trong C++ hiện đại |
| **Pure Virtual (`= 0`)** | Định nghĩa giao diện bắt buộc lớp con phải viết | Biến lớp thành Abstract Class |
| **Object Slicing** | Mất dữ liệu con khi truyền tham trị lớp cha | Luôn truyền `const Base&` hoặc `std::unique_ptr<Base>` |
| **dynamic_cast** | Downcast an toàn tại runtime | Yêu cầu lớp cha có ít nhất 1 hàm virtual (RTTI) |

---

## 2. Bài Tập Thực Chiến Toàn Diện: Hệ Thống Vẽ Hình Học (Vector Graphic Engine)

### Yêu cầu:
1. Định nghĩa lớp cơ sở trừu tượng `Shape` có:
   - Màu sắc (`std::string`).
   - Hàm ảo thuần ảo `virtual double getArea() const = 0;`.
   - Hàm ảo in thông tin `virtual void print() const = 0;`.
   - Hàm hủy ảo `virtual ~Shape() = default;`.
2. Tạo hai lớp con:
   - `Circle`: Có bán kính `double m_radius`.
   - `Rectangle`: Có chiều dài `m_width` và chiều rộng `m_height`.
3. Viết hàm `main()` khởi tạo một danh sách các hình học thông qua `std::vector<std::unique_ptr<Shape>>`, duyệt qua danh sách và tính tổng diện tích toàn bộ các hình.

`<details>`
`<summary>``<b>`Xem lời giải mã nguồn C++20 hoàn chỉnh

```cpp
#include <iostream>
#include <vector>
#include <memory>
#include <string>
#include <string_view>

class Shape
{
protected:
    std::string m_color;

public:
    Shape(std::string_view color) : m_color{ color } {}
    virtual ~Shape() = default; // Virtual Destructor chuan muc

    virtual double getArea() const = 0; // Pure virtual
    virtual void print() const = 0;    // Pure virtual
};

class Circle : public Shape
{
private:
    double m_radius{ 0.0 };

public:
    Circle(std::string_view color, double radius)
        : Shape{ color }, m_radius{ radius } {}

    double getArea() const override
    {
        return 3.1415926535 * m_radius * m_radius;
    }

    void print() const override
    {
        std::cout << "Hinh Tron [Mau: " << m_color << ", Ban kinh: " << m_radius 
                  << "] -> Dien tich: " << getArea() << '\n';
    }
};

class Rectangle : public Shape
{
private:
    double m_width{ 0.0 };
    double m_height{ 0.0 };

public:
    Rectangle(std::string_view color, double width, double height)
        : Shape{ color }, m_width{ width }, m_height{ height } {}

    double getArea() const override
    {
        return m_width * m_height;
    }

    void print() const override
    {
        std::cout << "Hinh Chu Nhat [Mau: " << m_color << ", Kich thuoc: " 
                  << m_width << "x" << m_height << "] -> Dien tich: " << getArea() << '\n';
    }
};

int main()
{
    // Quan ly danh sach da hinh an toan bang smart pointer (std::unique_ptr)
    std::vector<std::unique_ptr<Shape>> shapes;
    shapes.push_back(std::make_unique<Circle>("Do", 3.0));
    shapes.push_back(std::make_unique<Rectangle>("Xanh Duong", 4.0, 5.0));
    shapes.push_back(std::make_unique<Circle>("Vang", 2.5));

    double totalArea{ 0.0 };

    std::cout << "=== DANH SACH CAC HINH HOC ===\n";
    for (const auto& shape : shapes)
    {
        shape->print(); // Dynamic dispatch qua vtable!
        totalArea += shape->getArea();
    }

    std::cout << "--------------------------------\n";
    std::cout << "TONG DIEN TICH TOAN BO HE THONG: " << totalArea << '\n';

    return 0;
}
```

