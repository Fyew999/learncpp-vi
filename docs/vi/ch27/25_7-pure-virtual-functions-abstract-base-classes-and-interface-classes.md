# 25.7 — Hàm Thuần Ảo, Lớp Trừu Tượng & Interface

---

## 🎯 Mục Tiêu Bài Học
- Hiểu định nghĩa của **Hàm thuần ảo (Pure Virtual Function)** với cú pháp `= 0`.
- Nắm vững đặc tính của **Lớp cơ sở trừu tượng (Abstract Base Class)**: Không thể khởi tạo đối tượng trực tiếp.
- Khái niệm và phương pháp thiết kế **Lớp giao diện (Interface Class)** trong C++.

---

## 1. Hàm Thuần Ảo (Pure Virtual Function) Là Gì?

Hàm thuần ảo là một hàm ảo được khai báo trong lớp cơ sở nhưng **không bắt buộc phải có định nghĩa phần thân hàm** tại lớp cơ sở đó. Cú pháp kết thúc bằng `= 0`:

```cpp
virtual void render() = 0; // Hàm thuần ảo
```

Ý nghĩa: Lớp cơ sở tuyên bố: *"Tôi quy định mọi lớp con kế thừa từ tôi BẮT BUỘC phải tự viết mã cho hàm này, nếu không lớp con cũng sẽ trở thành trừu tượng và không thể tạo đối tượng!"*.

---

## 2. Lớp Cơ Sở Trừu Tượng (Abstract Base Class)

Bất kỳ lớp nào có **chứa ít nhất một hàm thuần ảo** thì tự động được trình biên dịch xếp vào loại **Lớp trừu tượng (Abstract Class)**.
- Bạn **KHÔNG THỂ** tạo đối tượng trực tiếp từ lớp trừu tượng (ví dụ: `Shape s;` sẽ báo lỗi biên dịch).
- Nhưng bạn **CÓ THỂ** tạo con trỏ và tham chiếu kiểu lớp trừu tượng để quản lý các lớp con đa hình (`Shape* ptr = new Circle();`).

```cpp
#include <iostream>

// Lớp trừu tượng Shape
class Shape
{
public:
    virtual ~Shape() = default; // Luôn cần virtual destructor

    // Hàm thuần ảo: Định nghĩa giao diện
    virtual double getArea() const = 0;
    virtual void draw() const = 0;
};

class Circle : public Shape
{
private:
    double m_radius;

public:
    Circle(double r) : m_radius{ r } {}

    // Bắt buộc phải ghi đè toàn bộ các hàm thuần ảo
    double getArea() const override { return 3.14159 * m_radius * m_radius; }
    void draw() const override { std::cout << "Ve hinh tron ban kinh " << m_radius << '\n'; }
};

int main()
{
    // Shape s; // LỖI BIÊN DỊCH: Không thể khởi tạo đối tượng của lớp trừu tượng!
    
    Circle c{ 5.0 };
    Shape* shape = &c;
    shape->draw();
    std::cout << "Dien tich: " << shape->getArea() << '\n';

    return 0;
}
```

---

## 3. Lớp Giao Diện (Interface Class) Trong C++

Trong C++, không có từ khóa `interface` riêng biệt như Java hay C#. Một lớp được coi là một **Interface** thuần túy nếu nó thỏa mãn:
1. Tất cả các hàm thành viên đều là **hàm thuần ảo** (`= 0`).
2. **Không có bất kỳ biến thành viên dữ liệu nào** (trừ các hằng số static).
3. Có một **Hàm hủy ảo mặc định** (`virtual ~Interface() = default;`).

Quy ước đặt tên phổ biến trong các dự án lớn là bắt đầu bằng tiền tố `I`: ví dụ `ILogger`, `IDatabaseConnection`, `IRenderer`.
