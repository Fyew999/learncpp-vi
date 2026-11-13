# 23.5 — Quan Hệ Phụ Thuộc (Dependencies)

---

## 🎯 Mục Tiêu Bài Học
- Hiểu định nghĩa của quan hệ **Dependency (depends-on)** trong C++.
- Phân biệt giữa quan hệ phụ thuộc tạm thời và quan hệ sở hữu thuộc tính.
- Nắm bắt nguyên lý thiết kế: Giảm thiểu độ kết dính (Loose Coupling) để code dễ bảo trì và test.

---

## 1. Bản Chất Quan Hệ Dependency

Một lớp A được gọi là **phụ thuộc (depends-on)** vào lớp B nếu một thay đổi trong định nghĩa của B có thể làm ảnh hưởng hoặc buộc phải thay đổi mã nguồn của A, **nhưng A không lưu trữ B làm biến thành viên**.

Thông thường, đối tượng B chỉ xuất hiện thoáng qua bên trong lớp A dưới dạng:
- Tham số truyền vào một hàm thành viên (`void doSomething(const B& b)`).
- Biến cục bộ được khởi tạo bên trong một hàm thành viên.
- Kiểu dữ liệu trả về của một hàm (`B createB()`).

```mermaid
flowchart LR
    Point["Lớp Point"] -->|"phụ thuộc qua tham số hàm
operator<<(std::ostream&, Point)"| Stream["Thư viện std::ostream"]
```

---

## 2. Ví Dụ Thực Tế Trong Mã Nguồn C++

Toán tử xuất dữ liệu `operator<<` kinh điển là ví dụ hoàn hảo về quan hệ Dependency:

```cpp
#include <iostream>

class Point
{
private:
    double m_x{ 0.0 };
    double m_y{ 0.0 };

public:
    Point(double x, double y) : m_x{ x }, m_y{ y } {}

    // Lớp Point PHỤ THUỘC vào std::ostream để xuất dữ liệu ra màn hình
    // nhưng Point KHÔNG SỞ HỮU std::ostream
    friend std::ostream& operator<<(std::ostream& out, const Point& point)
    {
        out << "Point(" << point.m_x << ", " << point.m_y << ')';
        return out;
    }
};

int main()
{
    Point p{ 3.14, 2.71 };
    std::cout << "Gia tri toa do: " << p << '\n';
    return 0;
}
```

Trong ví dụ trên:
- `Point` không lưu biến `std::ostream` nào trong bộ nhớ của nó.
- `Point` chỉ phụ thuộc vào giao diện (interface) của `std::ostream` khi hàm `operator<<` được thực thi.

---

## 3. Tight Coupling vs Loose Coupling (Độ Kết Dính)

```
+--------------------------+       Phụ thuộc chặt      +--------------------------+
|       Lớp Order          | ------------------------> |    Lớp MySQLDatabase     |
| (Tight Coupling - Xấu)   |  (Khó đổi sang Oracle/DB) |                          |
+--------------------------+                           +--------------------------+

+--------------------------+       Phụ thuộc lỏng      +--------------------------+
|       Lớp Order          | ------------------------> |  Interface IDatabase     |
| (Loose Coupling - Tốt)   |   (Linh hoạt tuyệt đối)   |                          |
+--------------------------+                           +--------------------------+
```

::: tip Lời Khuyên Thiết Kế (Clean Architecture)
Hạn chế tối đa việc các lớp cấp cao phụ thuộc trực tiếp vào các lớp cấp thấp cụ thể. Hãy áp dụng nguyên lý **Đảo ngược phụ thuộc (Dependency Inversion Principle - chữ D trong SOLID)** thông qua các lớp trừu tượng (Abstract Classes / Interfaces).
:::

---

## 4. Quiz

### Câu hỏi:
Nếu hàm `printData(const User& u)` nhận một đối tượng `User` làm tham số và in ra màn hình, thì hàm này có quan hệ gì với `User`?
`<details>`
`<summary>``<b>`Xem lời giải

**Đáp án**: Quan hệ **Dependency (Phụ thuộc)**. Hàm chỉ mượn tạm `User` để đọc dữ liệu trong quá trình thực thi, không chịu trách nhiệm cấp phát hay hủy bỏ `User`.

