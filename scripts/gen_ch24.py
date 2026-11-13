#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import os

BASE_DIR = "/home/nam/Documents/learncpp"
OUT_DIR = os.path.join(BASE_DIR, "docs", "vi", "ch26")
os.makedirs(OUT_DIR, exist_ok=True)

lessons = {}

# 24.1
lessons["24_1-introduction-to-inheritance.md"] = """# 24.1 — Giới Thiệu Về Tính Kế Thừa (Introduction to Inheritance)

---

## 🎯 Mục Tiêu Bài Học
- Hiểu rõ bản chất quan hệ **Kế thừa (Inheritance)** và khái niệm **"is-a"** (Con LÀ một dạng của Cha).
- Phân biệt giữa quan hệ Kế thừa và quan hệ Thành phần sở hữu (Composition).
- Nhận thức giá trị tối thượng của Kế thừa: Tái sử dụng mã nguồn (Code reuse) và thiết lập hệ thống phân cấp logic.

---

## 1. Kế Thừa Là Gì?

Trong lập trình hướng đối tượng, **Kế thừa (Inheritance)** là cơ chế cho phép một lớp mới (gọi là **Lớp dẫn xuất / Derived Class** hoặc **Lớp con / Subclass**) tiếp nhận và tái sử dụng toàn bộ các thuộc tính và hành vi của một lớp đã có sẵn (gọi là **Lớp cơ sở / Base Class** hoặc **Lớp cha / Superclass**), đồng thời có thể mở rộng thêm các tính năng chuyên biệt của riêng mình.

Mối quan hệ kế thừa luôn thể hiện quan hệ **"is-a" (Là một dạng của)**:
- Táo (*Apple*) **là một** Trái cây (*Fruit*).
- Lập trình viên (*Programmer*) **là một** Nhân viên (*Employee*).
- Hình chữ nhật (*Rectangle*) **là một** Hình học (*Shape*).

```mermaid
classDiagram
    class Person {
        +std::string m_name
        +int m_age
        +getName()
    }
    class Employee {
        +double m_hourlySalary
        +long m_employeeId
        +printInfo()
    }
    class Supervisor {
        +std::vector~long~ m_overseenEmployeeIds
    }
    Person <|-- Employee : is-a (Kế thừa)
    Employee <|-- Supervisor : is-a (Kế thừa chuyên biệt)
```

---

## 2. Tại Sao Cần Kế Thừa? (Giải Quyết Vấn Đề Dư Thừa Mã)

Giả sử bạn phải xây dựng phần mềm quản lý nhân sự. Ban đầu bạn viết lớp `Person` để quản lý thông tin công dân. Sau đó công ty cần quản lý `Employee`.
Nếu không có kế thừa, bạn sẽ phải sao chép toàn bộ code của `Person` sang `Employee`:

```cpp
// THIẾT KẾ XẤU: Trùng lặp mã nguồn (Code Duplication)
class Person
{
    std::string m_name;
    int m_age;
};

class Employee
{
    std::string m_name;  // Trùng lặp!
    int m_age;           // Trùng lặp!
    double m_salary;
    long m_id;
};
```

Hậu quả:
- Nếu bạn cần sửa lỗi hoặc thêm trường dữ liệu (ví dụ: `email`), bạn phải sửa ở cả 2 nơi!
- Vi phạm nguyên lý **DRY (Don't Repeat Yourself)**.

Với **Kế thừa**, `Employee` chỉ cần kế thừa `Person` và chỉ tập trung khai báo những gì chuyên biệt của nhân viên: lương và mã nhân viên.

---

## 3. Quiz Kiểm Tra Hiểu Biết

### Câu hỏi:
Xác định xem các cặp thực thể sau đây có mối quan hệ **Kế thừa ("is-a")** hay **Thành phần ("has-a")**:
1. Xe hơi và Bánh xe.
2. Tam giác và Hình đa giác.
3. Bệnh viện và Bác sĩ.
4. Chó và Động vật có vú.

<details>
<summary><b>Xem lời giải</b></summary>

1. **has-a (Composition/Aggregation)**: Xe hơi *có* bánh xe (không phải Xe hơi là một bánh xe).
2. **is-a (Inheritance)**: Tam giác *là một* Hình đa giác.
3. **has-a (Aggregation)**: Bệnh viện *có* bác sĩ làm việc.
4. **is-a (Inheritance)**: Chó *là một* loài Động vật có vú.
</details>
"""

# 24.2
lessons["24_2-basic-inheritance-in-c.md"] = """# 24.2 — Kế Thừa Cơ Bản Trong C++ (Basic Inheritance)

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
        std::cout << "Nhan vien: " << m_name << " (" << m_age << " tuoi)\\n"
                  << "Ma NV: " << m_employeeId << " | Luong/h: " << m_hourlySalary << "$\\n";
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
"""

# 24.3
lessons["24_3-order-of-construction-of-derived-classes.md"] = """# 24.3 — Thứ Tự Khởi Tạo & Hủy Bỏ Lớp Dẫn Xuất (Order of Construction)

---

## 🎯 Mục Tiêu Bài Học
- Hiểu quy tắc bất biến: **Lớp cơ sở luôn được khởi tạo TRƯỚC lớp dẫn xuất**.
- Nắm rõ thứ tự gọi Constructor và Destructor trong chuỗi kế thừa nhiều tầng.
- Hiểu lý do tại sao C++ bắt buộc phải tuân theo thứ tự này để đảm bảo an toàn bộ nhớ.

---

## 1. Quy Tắc Khởi Tạo: Base Trước, Derived Sau

Hãy tưởng tượng bạn xây dựng một ngôi nhà 3 tầng: bạn không thể nào đổ mái tầng 2 khi chưa xây xong móng và tường tầng 1.
Trong C++, lớp dẫn xuất phụ thuộc vào các biến thành viên của lớp cơ sở. Do đó, **Lớp cơ sở bắt buộc phải được tạo lập hoàn tất trước khi lớp dẫn xuất bắt đầu chạy Constructor**.

```mermaid
sequenceDiagram
    participant Program as Chương trình (main)
    participant Derived as Constructor Lớp Con (Derived)
    participant Base as Constructor Lớp Cha (Base)

    Program->>Derived: Khởi tạo Derived d;
    Derived->>Base: Tự động gọi Constructor Base TRƯỚC
    Base-->>Derived: Hoàn thành khởi tạo Base
    Note over Derived: Thực thi thân hàm Constructor Derived
    Derived-->>Program: Đối tượng d sẵn sàng sử dụng
```

---

## 2. Minh Họa Bằng Mã Nguồn Thực Tế

```cpp
#include <iostream>

class A
{
public:
    A() { std::cout << "1. Constructor A (Base)\\n"; }
    ~A() { std::cout << "4. Destructor A (Base)\\n"; }
};

class B : public A
{
public:
    B() { std::cout << "2. Constructor B (Derived tu A)\\n"; }
    ~B() { std::cout << "3. Destructor B (Derived tu A)\\n"; }
};

class C : public B
{
public:
    C() { std::cout << "3. Constructor C (Derived tu B)\\n"; }
    ~C() { std::cout << "2. Destructor C (Derived tu B)\\n"; }
};

int main()
{
    std::cout << "=== KHOI TAO DOI TUONG C ===\\n";
    {
        C c;
    } // c roi scope va bi huy
    std::cout << "=== KET THUC CHUONG TRINH ===\\n";

    return 0;
}
```

### Kết quả xuất ra màn hình:
```text
=== KHOI TAO DOI TUONG C ===
1. Constructor A (Base)
2. Constructor B (Derived tu A)
3. Constructor C (Derived tu B)
2. Destructor C (Derived tu B)
3. Destructor B (Derived tu A)
4. Destructor A (Base)
=== KET THUC CHUONG TRINH ===
```

::: warning Quy Tắc Đối Xứng Bất Biến
- **Thứ tự Khởi tạo (Construction)**: Từ **Gốc đến Ngọn** (Cha $\\rightarrow$ Con $\\rightarrow$ Cháu).
- **Thứ tự Hủy diệt (Destruction)**: Từ **Ngọn về Gốc** (Cháu $\\rightarrow$ Con $\\rightarrow$ Cha) — hoàn toàn tương tự nguyên lý LIFO (Last In First Out) của ngăn xếp Stack.
:::

---

## 3. Quiz

### Câu hỏi:
Tại sao Destructor của lớp con phải chạy trước Destructor của lớp cha?
<details>
<summary><b>Xem lời giải</b></summary>

**Đáp án**: Nếu Destructor của lớp cha chạy trước, các biến thành viên của lớp cha sẽ bị giải phóng. Khi đó, nếu Destructor của lớp con cần truy cập dữ liệu của lớp cha để dọn dẹp, nó sẽ truy cập vào vùng nhớ đã chết, gây lỗi nghiêm trọng (Undefined Behavior / Crash).
</details>
"""

# 24.4
lessons["24_4-constructors-and-initialization-of-derived-classes.md"] = """# 24.4 — Khởi Tạo Lớp Dẫn Xuất Với Constructor Lớp Cơ Sở

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
                  << " | Luong: " << m_hourlySalary << "$ | ID: " << m_employeeId << '\\n';
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
<details>
<summary><b>Xem lời giải</b></summary>

**Đáp án**: Theo chuẩn C++, lớp cơ sở luôn được khởi tạo **trước** bất kỳ biến thành viên nào của lớp con, bất kể bạn viết nó ở vị trí nào trong danh sách. Tuy nhiên, quy tắc phong cách (Best Practice) là luôn luôn đặt lệnh gọi lớp cơ sở ở **vị trí đầu tiên** của Member Initializer List để code phản ánh đúng thực tế thực thi.
</details>
"""

# 24.5
lessons["24_5-inheritance-and-access-specifiers.md"] = """# 24.5 — Kế Thừa & Các Từ Khóa Truy Cập (Access Specifiers)

---

## 🎯 Mục Tiêu Bài Học
- Phân biệt phạm vi truy cập: `public`, `private`, và `protected`.
- Hiểu rõ ma trận kế thừa: Kế thừa công khai (`public`), Kế thừa bảo vệ (`protected`), và Kế thừa riêng tư (`private`).
- Đánh giá ưu nhược điểm của từ khóa `protected` trong thiết kế phần mềm.

---

## 1. Từ Khóa `protected` Trong C++

C++ cung cấp thêm phạm vi truy cập thứ ba: **`protected` (được bảo vệ)**:
- **`public`**: Bất kỳ ai, ở bất kỳ đâu cũng có thể truy cập trực tiếp.
- **`private`**: Chỉ chính các hàm thành viên và friend của lớp đó mới được truy cập. Lớp con cũng **KHÔNG THỂ** truy cập trực tiếp.
- **`protected`**: Các hàm bên ngoài không thể truy cập, nhưng **CÁC LỚP DẪN XUẤT ĐƯỢC PHÉP TRUY CẬP TRỰC TIẾP**.

```cpp
class Base
{
public:
    int m_public{ 1 };
protected:
    int m_protected{ 2 }; // Con truy cap duoc, ben ngoai cam!
private:
    int m_private{ 3 };   // Chi Base truy cap duoc!
};

class Derived : public Base
{
public:
    void test()
    {
        m_public = 10;    // HOP LE
        m_protected = 20; // HOP LE: Derived la con nen duoc phep
        // m_private = 30; // LOI BIEN DICH! Private khong the truy cap tu con
    }
};
```

---

## 2. Bảng Ma Trận Kế Thừa Toàn Diện

Kiểu kế thừa (`public`, `protected`, `private`) quy định mức độ quyền hạn tối đa của các thành viên kế thừa khi chuyển giao sang lớp con:

| Thành viên trong Base | Kế thừa `: public Base` | Kế thừa `: protected Base` | Kế thừa `: private Base` |
| :--- | :--- | :--- | :--- |
| **`public`** | Giữ nguyên là **`public`** | Trở thành **`protected`** | Trở thành **`private`** |
| **`protected`** | Giữ nguyên là **`protected`**| Trở thành **`protected`** | Trở thành **`private`** |
| **`private`** | **Không thể truy cập** | **Không thể truy cập** | **Không thể truy cập** |

::: tip Thực Tế Ngành Công Nghiệp
- Hơn **99%** trường hợp bạn sẽ sử dụng **`public inheritance`** vì nó duy trì đúng chuẩn quan hệ "is-a".
- `private inheritance` và `protected inheritance` rất hiếm khi được sử dụng, thường chỉ dùng trong các kỹ thuật chuyên sâu như *Policy-Based Design* hoặc mô phỏng quan hệ *implemented-in-terms-of*.
:::

---

## 3. Cảnh Báo Về Việc Sử Dụng Biến Thành Viên `protected`

::: warning Khuyến Cáo Thực Hành Tốt Nhất
Hạn chế tối đa việc đặt **biến thành viên** ở chế độ `protected`. Hãy giữ biến thành viên là `private` và cung cấp các hàm Getter/Setter ở chế độ `protected` cho lớp con sử dụng. 
Lý do: Nếu bạn cho phép lớp con truy cập trực tiếp vào biến, sau này khi bạn muốn thay đổi kiểu dữ liệu của biến ở lớp cha, bạn sẽ làm hỏng toàn bộ mã nguồn của tất cả các lớp con!
:::

---

## 4. Quiz

### Câu hỏi:
Nếu lớp `Child` kế thừa theo kiểu `private` từ `Parent` (`class Child : private Parent`), thì đối tượng `Child c;` có thể gọi được các hàm `public` của `Parent` từ hàm `main()` không?
<details>
<summary><b>Xem lời giải</b></summary>

**Đáp án**: **KHÔNG THỂ!** Vì qua kế thừa `private`, tất cả các thành viên `public` của `Parent` đã bị biến thành `private` bên trong `Child`. Do đó, người dùng từ bên ngoài `Child` hoàn toàn không thể nhìn thấy chúng.
</details>
"""

# 24.6
lessons["24_6-adding-new-functionality-to-a-derived-class.md"] = """# 24.6 — Bổ Sung Tính Năng Mới Cho Lớp Dẫn Xuất

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

    void identify() const { std::cout << "Toi la Base, gia tri = " << m_value << '\\n'; }
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
        std::cout << "Derived co them gia tri thuong = " << m_bonus << '\\n';
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
<details>
<summary><b>Xem lời giải</b></summary>

**Đáp án**: **HOÀN TOÀN KHÔNG!** Lớp cơ sở hoàn toàn không biết gì về sự tồn tại của các lớp con kế thừa từ nó. Quan hệ kế thừa là dòng chảy một chiều: Lớp con biết mọi thứ về lớp cha, nhưng lớp cha không biết lớp con có những tính năng gì.
</details>
"""

# 24.7
lessons["24_7-calling-inherited-functions-and-overriding-behavior.md"] = """# 24.7 — Gọi Hàm Kế Thừa & Tái Định Nghĩa Hành Vi (Redefining Behavior)

---

## 🎯 Mục Tiêu Bài Học
- Biết cách tái định nghĩa (redefine / override tĩnh) hành vi của một hàm kế thừa từ lớp cha.
- Thành thạo việc gọi lại hàm của lớp cha bằng toán tử phạm vi `Base::function()`.
- Nhận biết cạm bẫy đệ quy vô tận dẫn đến sập chương trình vì tràn ngăn xếp (**Stack Overflow**).

---

## 1. Tái Định Nghĩa Hàm (Function Redefinition)

Khi lớp con kế thừa một hàm từ lớp cha nhưng muốn thay đổi cách hoạt động của hàm đó, nó có thể khai báo một hàm có cùng tên, cùng tham số và cùng kiểu trả về với lớp cha:

```cpp
#include <iostream>

class Base
{
public:
    void identify() const
    {
        std::cout << "Day la Base::identify()\\n";
    }
};

class Derived : public Base
{
public:
    // Tai dinh nghia lai ham cua Base
    void identify() const
    {
        std::cout << "Day la Derived::identify() da duoc ghi de!\\n";
    }
};

int main()
{
    Base b;
    b.identify(); // In ra: Day la Base::identify()

    Derived d;
    d.identify(); // In ra: Day la Derived::identify() da duoc ghi de!

    return 0;
}
```

---

## 2. Gọi Hàm Của Lớp Cha: Toán Tử Định Phạm Vi `Base::`

Trong nhiều trường hợp, lớp con không muốn xóa bỏ hoàn toàn công việc của lớp cha mà chỉ muốn **làm thêm** một số bước sau khi lớp cha hoàn tất. Bạn sử dụng cú pháp `Base::tenHam()`:

```cpp
class Derived : public Base
{
public:
    void identify() const
    {
        Base::identify(); // 1. Goi ham cua lop cha truoc
        std::cout << "-> Va Derived lam them cong viec bo sung tai day!\\n";
    }
};
```

::: danger Cạm Bẫy Quên Toán Tử Phạm Vi `Base::`
Nếu bạn quên viết tiền tố `Base::` bên trong hàm trùng tên của `Derived`, hàm sẽ tự gọi lại chính nó:
```cpp
void identify() const
{
    identify(); // LỖI ĐỆ QUY VÔ TẬN! Tràn ngăn xếp (Stack Overflow) ngay lập tức!
}
```
:::

---

## 3. Quiz

### Câu hỏi:
Từ một đối tượng lớp con `Derived d;`, người dùng từ hàm `main()` có thể gọi tường minh hàm gốc của `Base` được không?
<details>
<summary><b>Xem lời giải</b></summary>

**Đáp án**: **HOÀN TOÀN ĐƯỢC!** Người dùng có thể chỉ định rõ toán tử phạm vi: `d.Base::identify();` để buộc trình biên dịch gọi phiên bản của lớp cha thay vì phiên bản bị ghi đè của lớp con.
</details>
"""

# 24.8
lessons["24_8-hiding-inherited-functionality.md"] = """# 24.8 — Ẩn & Vô Hiệu Hóa Tính Năng Kế Thừa

---

## 🎯 Mục Tiêu Bài Học
- Biết cách thay đổi quyền truy cập của một hàm kế thừa bằng từ khóa `using`.
- Nắm vững cách vô hiệu hóa hoàn toàn một hàm kế thừa bằng `= delete` trong C++11.
- Hiểu được cạm bẫy che khuất hàm nạp chồng (Overload Hiding) trong C++.

---

## 1. Thay Đổi Phạm Vi Truy Cập Bằng `using`

Nếu một hàm là `protected` trong lớp cha, bạn có thể đưa nó thành `public` trong lớp con (hoặc ngược lại) bằng cách sử dụng phát biểu `using`:

```cpp
#include <iostream>

class Base
{
protected:
    void printValue(int x) const
    {
        std::cout << "Gia tri: " << x << '\\n';
    }
};

class Derived : public Base
{
public:
    // Cong khai hoa ham printValue de nguoi dung ngoai co the goi duoc
    using Base::printValue;
};

int main()
{
    Derived d;
    d.printValue(42); // Hop le!
    return 0;
}
```

---

## 2. Xóa Bỏ Tính Năng Bằng `= delete` (C++11)

Nếu một lớp con không muốn cho phép người dùng sử dụng một tính năng của lớp cha, cách chuẩn mực nhất trong C++ hiện đại là đánh dấu `= delete`:

```cpp
class Base
{
public:
    void dangerousOperation() { std::cout << "Thao tac nguy hiem!\\n"; }
};

class SecureDerived : public Base
{
public:
    // Cam nguoi dung goi ham nay tu SecureDerived
    void dangerousOperation() = delete;
};

int main()
{
    SecureDerived s;
    // s.dangerousOperation(); // LOI BIEN DICH: Ham da bi xoa (deleted function)!
    return 0;
}
```

---

## 3. Cạm Bẫy Ẩn Hàm Nạp Chồng (Name Hiding)

::: danger Cạm Bẫy Kinh Điển Của Trình Biên Dịch C++
Nếu lớp cha có nhiều phiên bản nạp chồng của một hàm (ví dụ: `func(int)` và `func(double)`), mà lớp con chỉ định nghĩa lại ĐÚNG MỘT phiên bản `func(int)`, thì **TẤT CẢ các phiên bản nạp chồng còn lại của lớp cha sẽ bị ẩn hoàn toàn**!
:::

Để khắc phục, bạn phải khai báo `using Base::func;` trong lớp con để kéo toàn bộ các bản nạp chồng của lớp cha vào phạm vi tìm kiếm.
"""

# 24.9
lessons["24_9-multiple-inheritance.md"] = """# 24.9 — Đa Kế Thừa (Multiple Inheritance) & Vấn Đề Kim Cương

---

## 🎯 Mục Tiêu Bài Học
- Hiểu cú pháp và cách thức hoạt động của **Đa kế thừa (Multiple Inheritance)** trong C++.
- Nhận thức sâu sắc cạm bẫy kinh điển: **Bài toán kim cương (The Diamond Problem)**.
- Trực quan hóa cấu trúc bộ nhớ RAM khi đa kế thừa gây dư thừa và xung đột dữ liệu.
- Giới thiệu giải pháp Kế thừa ảo (**Virtual Inheritance**).

---

## 1. Đa Kế Thừa Là Gì?

C++ là một trong số ít các ngôn ngữ mạnh mẽ cho phép một lớp con kế thừa trực tiếp từ **nhiều hơn một lớp cha**.

```cpp
#include <iostream>

class USBDevice
{
public:
    void plugUSB() { std::cout << "Cam cong USB.\\n"; }
};

class WirelessDevice
{
public:
    void connectWifi() { std::cout << "Ket noi Wifi.\\n"; }
};

// Smartphone ke thua ca 2 lop cha
class Smartphone : public USBDevice, public WirelessDevice
{
};

int main()
{
    Smartphone phone;
    phone.plugUSB();     // Tu USBDevice
    phone.connectWifi(); // Tu WirelessDevice
    return 0;
}
```

---

## 2. Cạm Bẫy Chí Mạng: The Diamond Problem (Bài Toán Kim Cương)

Bài toán kim cương xảy ra khi hai lớp con cùng kế thừa từ một lớp gốc, và sau đó có một lớp thứ tư kế thừa từ cả hai lớp con đó:

```mermaid
classDiagram
    PoweredDevice <|-- Scanner
    PoweredDevice <|-- Printer
    Scanner <|-- Copier
    Printer <|-- Copier
    class PoweredDevice {
        +int m_power
    }
```

### Trực quan hóa cấu trúc bộ nhớ RAM của `Copier`:

```
BỐ CỤC BỘ NHỚ RAM CỦA ĐỐI TƯỢNG Copier:
+-------------------------------------------------------------+
| [PHẦN KẾ THỪA TỪ Scanner]                                   |
|   +-------------------------------------------------------+ |
|   | PoweredDevice subobject (BẢN SAO SỐ 1: m_power)       | |
|   +-------------------------------------------------------+ |
|   | Scanner members                                       | |
+-------------------------------------------------------------+
| [PHẦN KẾ THỪA TỪ Printer]                                   |
|   +-------------------------------------------------------+ |
|   | PoweredDevice subobject (BẢN SAO SỐ 2: m_power)       | |
|   +-------------------------------------------------------+ |
|   | Printer members                                       | |
+-------------------------------------------------------------+
| [PHẦN THÀNH VIÊN RIÊNG CỦA Copier]                          |
+-------------------------------------------------------------+
```

Hậu quả:
1. **Lãng phí bộ nhớ**: `Copier` mang trong mình **2 bản sao độc lập** của `PoweredDevice`!
2. **Nhập nhằng định danh (Ambiguity)**: Khi gọi `copier.m_power`, trình biên dịch lập tức báo lỗi vì không biết bạn muốn truy cập `m_power` của nhánh `Scanner` hay nhánh `Printer`!

---

## 3. Lời Giải: Virtual Base Classes (Kế Thừa Ảo)

Để giải quyết triệt để vấn đề này, C++ cung cấp cơ chế **`virtual inheritance`** (sẽ được đào sâu chi tiết ở bài 25.8). Khi khai báo `class Scanner : virtual public PoweredDevice`, C++ sẽ đảm bảo trong toàn bộ đối tượng `Copier` chỉ tồn tại duy nhất một bản sao chung của `PoweredDevice`.

---

## 4. Quiz

### Câu hỏi:
Tại sao nhiều ngôn ngữ hiện đại như Java hay C# lại cấm đa kế thừa lớp?
<details>
<summary><b>Xem lời giải</b></summary>

**Đáp án**: Đa kế thừa làm tăng vọt độ phức tạp của mã nguồn, dễ tạo ra nhập nhằng xung đột tên hàm và phát sinh lỗi bài toán kim cương. Java và C# chỉ cho phép kế thừa 1 lớp và thực thi nhiều Interface để tránh hoàn toàn các rủi ro kiến trúc này.
</details>
"""

# 24.x
lessons["24_x-chapter-24-summary-and-quiz.md"] = """# 24.x — Tổng Kết Chương 24 & Bài Kiểm Tra Toàn Diện

---

## 🎯 Mục Tiêu
- Hệ thống hóa toàn bộ kiến thức về Tính Kế Thừa (Inheritance) trong C++.
- Đánh giá khả năng vận dụng qua bài tập lập trình hướng đối tượng thực chiến.

---

## 1. Tóm Tắt Các Khái Niệm Trọng Tâm

1. **Quan hệ "is-a"**: Lớp con là một phiên bản mở rộng chuyên biệt của lớp cha.
2. **Thứ tự Construction/Destruction**: Cha sinh trước Con, Con chết trước Cha.
3. **Gọi Constructor Cha**: Luôn gọi tường minh trong Member Initializer List của lớp con.
4. **Phạm vi truy cập**: `protected` cho phép lớp con truy cập nhưng giấu với bên ngoài.
5. **Đa kế thừa**: Cẩn trọng tuyệt đối với bài toán kim cương (The Diamond Problem).

---

## 2. Bài Tập Thực Chiến Toàn Diện: Hệ Thống Game Nhập Vai (RPG)

### Yêu cầu:
1. Xây dựng lớp cơ sở `Creature` có:
   - Tên (`std::string`), Lượng máu tối đa (`int`), Sát thương cơ bản (`int`).
   - Các phương thức: `getName()`, `getHp()`, `getDamage()`, `reduceHp(int damage)`, `isDead()`.
2. Xây dựng lớp dẫn xuất `Player` kế thừa từ `Creature`:
   - Bổ sung cấp độ `m_level{ 1 }`.
   - Phương thức `levelUp()`: Tăng cấp độ và tăng máu, sát thương.
3. Xây dựng lớp dẫn xuất `Monster` kế thừa từ `Creature`:
   - Bổ sung loại quái vật `enum class Type { Dragon, Orc, Slime }`.
4. Viết hàm `main()` mô phỏng một hiệp chiến đấu giữa Player và Dragon.

<details>
<summary><b>Xem lời giải mã nguồn hoàn chỉnh</b></summary>

```cpp
#include <iostream>
#include <string>
#include <string_view>

class Creature
{
protected:
    std::string m_name;
    int m_hp;
    int m_damage;

public:
    Creature(std::string_view name, int hp, int damage)
        : m_name{ name }, m_hp{ hp }, m_damage{ damage }
    {
    }

    const std::string& getName() const { return m_name; }
    int getHp() const { return m_hp; }
    int getDamage() const { return m_damage; }

    void reduceHp(int damage)
    {
        m_hp -= damage;
        if (m_hp < 0) m_hp = 0;
    }

    bool isDead() const { return m_hp <= 0; }
};

class Player : public Creature
{
private:
    int m_level{ 1 };

public:
    Player(std::string_view name)
        : Creature{ name, 100, 20 } // Khoi tao Base: 100 HP, 20 Damage
    {
    }

    int getLevel() const { return m_level; }

    void levelUp()
    {
        ++m_level;
        m_hp += 30;
        m_damage += 10;
        std::cout << m_name << " da len CAP DO " << m_level << "! (HP: " << m_hp << ", DMG: " << m_damage << ")\\n";
    }
};

class Monster : public Creature
{
public:
    enum class Type { Dragon, Orc, Slime };

private:
    Type m_type;

public:
    Monster(Type type)
        : Creature{ "", 0, 0 }, m_type{ type }
    {
        switch (m_type)
        {
        case Type::Dragon:
            m_name = "Rong Co Dai";
            m_hp = 150;
            m_damage = 35;
            break;
        case Type::Orc:
            m_name = "Chien Binh Orc";
            m_hp = 60;
            m_damage = 15;
            break;
        case Type::Slime:
            m_name = "Quai Chat Nhon";
            m_hp = 20;
            m_damage = 5;
            break;
        }
    }
};

int main()
{
    Player hero{ "Hiep Si Arthur" };
    Monster boss{ Monster::Type::Dragon };

    std::cout << "--- TRAN CHIEN BAT DAU ---\\n";
    std::cout << hero.getName() << " (HP: " << hero.getHp() << ") VS " 
              << boss.getName() << " (HP: " << boss.getHp() << ")\\n\\n";

    // Hiep Si danh Boss
    boss.reduceHp(hero.getDamage());
    std::cout << hero.getName() << " chem " << boss.getName() << " mat " << hero.getDamage() << " HP!\\n";
    std::cout << boss.getName() << " con lai " << boss.getHp() << " HP.\\n\\n";

    // Boss phan cong
    hero.reduceHp(boss.getDamage());
    std::cout << boss.getName() << " phun lua thieu dot " << hero.getName() << " mat " << boss.getDamage() << " HP!\\n";
    std::cout << hero.getName() << " con lai " << hero.getHp() << " HP.\\n\\n";

    // Hiep si len cap
    hero.levelUp();

    return 0;
}
```
</details>

---

## 3. Bước Tiếp Theo
Kế thừa giúp tái sử dụng mã, nhưng sức mạnh thực sự của lập trình hướng đối tượng chỉ bùng nổ khi kết hợp với **Hàm Ảo và Tính Đa Hình (Virtual Functions & Polymorphism)** trong Chương 25!
"""

for fname, content in lessons.items():
    fpath = os.path.join(OUT_DIR, fname)
    with open(fpath, "w", encoding="utf-8") as f:
        f.write(content.strip() + "\n")
    print(f" -> Đã tạo ch26: {fname}")

print("HOÀN THÀNH CHƯƠNG 24 (10 bài trong docs/vi/ch26)")
