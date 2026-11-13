# 24.2 — Kế Thừa Cơ Bản Trong C++ (Basic Inheritance)

---

## 🎯 Mục Tiêu Bài Học
- Nắm vững cú pháp kế thừa chuẩn trong C++: `class Derived : public Base`.
- Trực quan hóa cấu trúc bộ nhớ RAM: Đối tượng lớp dẫn xuất chứa một đối tượng con lớp cơ sở (**Base Subobject**).
- Biết cách truy cập các hàm và biến thành viên kế thừa từ lớp cha.

---

## 1. Cú Pháp Kế Thừa Trong C++

Để cho phép một lớp dẫn xuất kế thừa từ lớp cơ sở, chúng ta sử dụng dấu hai chấm `:` theo sau là từ khóa phạm vi truy cập (thông dụng nhất là `public`) và tên lớp cha.

```cpp
#include <iostream>
#include <string>
#include <string_view>

// Lớp cơ sở (Base Class)
class Person
{
public:
    std::string m_name{};
    int m_age{ 0 };

    Person(std::string_view name = "", int age = 0)
        : m_name{ name }, m_age{ age }
    {
    }

    const std::string& getName() const { return m_name; }
    int getAge() const { return m_age; }
};

// Lớp dẫn xuất (Derived Class) kế thừa công khai từ Person
class Employee : public Person
{
public:
    double m_hourlySalary{ 0.0 };
    long m_employeeId{ 0 };

    Employee(double salary = 0.0, long id = 0)
        : m_hourlySalary{ salary }, m_employeeId{ id }
    {
    }

    void printInfo() const
    {
        // Truy cập trực tiếp các thành viên kế thừa từ Person
        std::cout << "Nhan vien: " << m_name << " (" << m_age << " tuoi)\n"
                  << "Ma NV: " << m_employeeId << " | Luong/h: " << m_hourlySalary << "$\n";
    }
};

int main()
{
    Employee dev{ 45.5, 1001 };
    
    // Gán dữ liệu cho các trường kế thừa từ Person
    dev.m_name = "Nguyen Van Dev";
    dev.m_age = 28;

    dev.printInfo();

    return 0;
}
```

---

## 2. Trực Quan Hóa Cấu Trúc Bộ Nhớ RAM Của Đối Tượng Dẫn Xuất

Một đối tượng `Employee` trong bộ nhớ thực chất là một khối dữ liệu kép:
Nó bao gồm **Đối tượng con lớp cơ sở (Base Subobject)** được đặt ở đầu, tiếp nối ngay sau đó là các biến thành viên của chính lớp dẫn xuất.

```
BỐ CỤC BỘ NHỚ RAM CỦA ĐỐI TƯỢNG Employee:
+-------------------------------------------------------------+ 0x1000 (Địa chỉ bắt đầu)
| [PHẦN SUB-OBJECT LỚP CƠ SỞ: Person]                        |
|   - std::string m_name  (32 bytes)                          |
|   - int m_age           (4 bytes)                           |
|   - padding             (4 bytes để align 8-byte)           |
+-------------------------------------------------------------+ 0x1028
| [PHẦN THÀNH VIÊN LỚP DẪN XUẤT: Employee]                    |
|   - double m_hourlySalary (8 bytes)                         |
|   - long m_employeeId     (8 bytes)                         |
+-------------------------------------------------------------+ 0x1038
Tổng kích thước = sizeof(Person) + các thành viên của Employee = 56 bytes.
```

::: tip Nhận Định Cốt Lõi
Do phần đầu của đối tượng `Employee` hoàn toàn trùng khớp với cấu trúc bộ nhớ của một đối tượng `Person`, trình biên dịch có thể dễ dàng chuyển đổi con trỏ `Employee*` thành con trỏ `Person*` chỉ bằng cách giữ nguyên địa chỉ bộ nhớ!
:::

---

## 3. Quiz

### Câu hỏi:
Kích thước `sizeof(Employee)` có bằng tổng `sizeof(Person) + sizeof(double) + sizeof(long)` không?
<details>
<summary><b>Xem lời giải</b></summary>

**Đáp án**: Thông thường sẽ bằng hoặc lớn hơn một chút do quy tắc căn chỉnh bộ nhớ (Data Structure Padding/Alignment). Tuy nhiên, chắc chắn kích thước của đối tượng con luôn bao hàm toàn bộ dung lượng của đối tượng cha.
</details>
