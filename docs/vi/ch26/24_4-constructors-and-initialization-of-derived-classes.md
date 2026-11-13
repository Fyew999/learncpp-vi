# 24.4 — Khởi Tạo Lớp Dẫn Xuất Với Constructor Lớp Cơ Sở

---

## 🎯 Mục Tiêu Bài Học
- Biết cách truyền tham số tường minh từ Constructor của lớp dẫn xuất lên Constructor của lớp cơ sở.
- Cú pháp sử dụng **Member Initializer List** để khởi tạo lớp cha.
- Tránh lỗi biên dịch phổ biến khi lớp cha không có Constructor mặc định (Default Constructor).

---

## 1. Vấn Đề Khi Lớp Cha Có Constructor Có Tham Số

Mặc định, trình biên dịch sẽ cố gắng gọi Constructor mặc định (không tham số) của lớp cơ sở. Nhưng điều gì xảy ra nếu lớp cha chỉ có Constructor nhận tham số?

```cpp
class Base
{
private:
    int m_id;
public:
    Base(int id) : m_id{ id } {} // Không có Default Constructor!
};

class Derived : public Base
{
public:
    Derived() // LỖI BIÊN DỊCH: Compiler không tìm thấy Base::Base()!
    {
    }
};
```

---

## 2. Giải Pháp: Gọi Tường Minh Constructor Lớp Cơ Sở

Để giải quyết, Constructor của lớp dẫn xuất phải gọi tường minh Constructor tương ứng của lớp cha ngay trong **Danh sách khởi tạo thành viên (Member Initializer List)**:

```cpp
#include <iostream>
#include <string>
#include <string_view>

class Person
{
private:
    std::string m_name;
    int m_age;

public:
    Person(std::string_view name, int age)
        : m_name{ name }, m_age{ age }
    {
    }

    const std::string& getName() const { return m_name; }
    int getAge() const { return m_age; }
};

class Employee : public Person
{
private:
    double m_hourlySalary;
    long m_employeeId;

public:
    // GOI TUONG MINH Person(name, age) TRONG INITIALIZER LIST
    Employee(std::string_view name, int age, double salary, long id)
        : Person{ name, age }          // 1. Khoi tao Base subobject truoc
        , m_hourlySalary{ salary }     // 2. Khoi tao cac bien cua Derived
        , m_employeeId{ id }
    {
    }

    void print() const
    {
        std::cout << "NV: " << getName() << " | Tuoi: " << getAge()
                  << " | Luong: " << m_hourlySalary << "$ | ID: " << m_employeeId << '\n';
    }
};

int main()
{
    Employee dev{ "Pham Van Minh", 25, 35.0, 9999 };
    dev.print();

    return 0;
}
```

::: danger Sai Lầm Nghiêm Trọng Cần Tránh
Tuyệt đối **KHÔNG** cố gắng gán giá trị cho các biến của lớp cha bên trong thân `{}` của Constructor lớp con:
```cpp
Employee(std::string_view name, int age)
{
    m_name = name; // LỖI NẾU m_name LÀ PRIVATE TRONG PERSON!
}
```
Ngay cả khi `m_name` là public, việc gán trong thân constructor cũng khiến `m_name` bị khởi tạo mặc định 2 lần (một lần khi gọi Base constructor, một lần bị ghi đè), làm suy giảm hiệu năng!
:::

---

## 3. Quiz

### Câu hỏi:
Tên lớp cơ sở `Person{ name, age }` trong danh sách khởi tạo của `Employee` bắt buộc phải đặt ở vị trí nào?
`<details>`
`<summary>``<b>`Xem lời giải

**Đáp án**: Theo chuẩn C++, lớp cơ sở luôn được khởi tạo **trước** bất kỳ biến thành viên nào của lớp con, bất kể bạn viết nó ở vị trí nào trong danh sách. Tuy nhiên, quy tắc phong cách (Best Practice) là luôn luôn đặt lệnh gọi lớp cơ sở ở **vị trí đầu tiên** của Member Initializer List để code phản ánh đúng thực tế thực thi.

