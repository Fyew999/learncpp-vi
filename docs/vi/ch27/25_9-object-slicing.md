# 25.9 — Cắt Gọt Đối Tượng (Object Slicing) — Cạm Bẫy Kinh Điển

---

## 🎯 Mục Tiêu Bài Học
- **MỔ XẺ BẢN CHẤT CẠM BẪY CẮT GỌT ĐỐI TƯỢNG (OBJECT SLICING) TRONG C++**.
- Trực quan hóa bộ nhớ: Tại sao truyền tham trị (`Pass-by-value`) lại cắt phăng toàn bộ phần dữ liệu chuyên biệt của lớp con và phá hủy con trỏ bảng ảo `__vptr`.
- Nắm vững các phương pháp phòng chống Object Slicing trong thực tế.

---

## 1. Hiện Tượng Object Slicing Là Gì?

Hãy quan sát đoạn code tưởng chừng vô hại sau:

```cpp
#include <iostream>
#include <string_view>

class Base
{
protected:
    int m_value{ 0 };

public:
    Base(int value) : m_value{ value } {}
    virtual ~Base() = default;

    virtual std::string_view getName() const { return "Base"; }
    int getValue() const { return m_value; }
};

class Derived : public Base
{
private:
    double m_extraData{ 99.99 };

public:
    Derived(int value, double extra)
        : Base{ value }, m_extraData{ extra } {}

    std::string_view getName() const override { return "Derived"; }
};

// CẠM BẪY CHÍ MẠNG: Hàm nhận tham trị (Pass-by-value) kiểu Base!
void printName(Base b)
{
    std::cout << "Toi la: " << b.getName() << '\n';
}

int main()
{
    Derived d{ 5, 3.14 };
    
    // GỌI HÀM VỚI THAM TRỊ:
    printName(d); // IN RA: "Toi la: Base" (!) TÍNH ĐA HÌNH BIẾN MẤT HOÀN TOÀN!

    return 0;
}
```

Tại sao `printName(d)` lại in ra `"Base"` trong khi `d` rõ ràng là `Derived` và `getName()` là hàm ảo `virtual`?

---

## 2. Trực Quan Hóa Quá Trình Cắt Gọt Trong RAM

Khi bạn truyền đối tượng `Derived d` vào tham số `Base b`, hàm khởi tạo sao chép của `Base` (`Base copy constructor`) được kích hoạt để sao chép dữ liệu từ `d` sang biến cục bộ `b`:

```
ĐỐI TƯỢNG BAN ĐẦU: Derived d                            BIẾN CỤC BỘ ĐƯỢC TẠO: Base b
+-----------------------------------+                   +-----------------------------------+
| __vptr (Trỏ tới vtable của D)     | === [BỊ CẮT!] ==> | __vptr (Trỏ tới vtable của Base!) |
+-----------------------------------+                   +-----------------------------------+
| int m_value = 5                   | === SAO CHÉP ===> | int m_value = 5                   |
+-----------------------------------+                   +-----------------------------------+
| double m_extraData = 3.14         | === [BỊ CẮT!] ==> | (Vùng nhớ không tồn tại trong b)  |
+-----------------------------------+                   +-----------------------------------+
(Kích thước: 24 bytes)                                  (Kích thước: 16 bytes)
```

### Diễn giải cơ chế:
1. Đối tượng `b` chỉ có kích thước của `Base`. Do đó, trình biên dịch **cắt bỏ hoàn toàn** trường `m_extraData` của `Derived` vì không có chỗ chứa!
2. Nguy hiểm hơn nữa: Con trỏ bảng ảo `__vptr` của `b` được thiết lập trỏ tới **bảng `vtable của Base`** (chứ không phải `Derived`).
3. Kết quả: Toàn bộ danh tính và tính đa hình của đối tượng con đã bị tước đoạt hoàn toàn!

---

## 3. Cách Phòng Tránh Triệt Để Object Slicing

### Quy tắc 1: Luôn truyền qua Tham Chiếu (`const Base&`) hoặc Con Trỏ (`Base*`)
```cpp
void printName(const Base& b) // An toàn tuyệt đối: Không copy, không slicing!
{
    std::cout << "Toi la: " << b.getName() << '\n'; // In ra "Derived" đúng chuẩn đa hình
}
```

### Quy tắc 2: Cấm sao chép lớp Base bằng cách khóa Copy Constructor
Nếu một lớp được thiết kế để làm lớp cha đa hình, hãy bảo vệ nó khỏi bị gán hoặc copy nhầm:
```cpp
class Base
{
public:
    Base(const Base&) = delete;            // Cấm copy
    Base& operator=(const Base&) = delete; // Cấm gán
};
```
