#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import os

BASE_DIR = "/home/nam/Documents/learncpp"
OUT_DIR = os.path.join(BASE_DIR, "docs", "vi", "ch25")
os.makedirs(OUT_DIR, exist_ok=True)

lessons = {}

# -------------------------------------------------------------
# 23.1
# -------------------------------------------------------------
lessons["23_1-object-relationships.md"] = """# 23.1 — Tổng Quan Về Mối Quan Hệ Giữa Các Đối Tượng (Object Relationships)

---

## 🎯 Mục Tiêu Bài Học
- Hiểu được tầm quan trọng của việc mô hình hóa mối quan hệ giữa các đối tượng trong lập trình hướng đối tượng (OOP).
- Phân biệt 5 loại quan hệ cốt lõi: **Thành phần sở hữu (Composition)**, **Tổng hợp (Aggregation)**, **Liên kết (Association)**, **Phụ thuộc (Dependency)**, và **Kế thừa (Inheritance)**.
- Nắm vững các thuật ngữ chuẩn quốc tế: *part-of*, *has-a*, *uses-a*, *depends-on*, *is-a*.
- Định hướng kiến trúc phần mềm linh hoạt, dễ mở rộng và tái sử dụng mã nguồn.

---

## 1. Mối Quan Hệ Giữa Các Đối Tượng Trong Thế Giới Thực Và Lập Trình

Thế giới tự nhiên xung quanh chúng ta là một mạng lưới phức tạp gồm các thực thể liên kết với nhau theo các quy tắc và thứ bậc chặt chẽ. Khi bạn quan sát một chiếc xe hơi, bạn nhận thấy nó được cấu thành từ động cơ, bánh xe và khung gầm. Bạn biết rằng nếu chiếc xe bị nghiền nát thành phế liệu, động cơ gắn trong nó cũng bị hủy hoại. Nhưng người lái xe thì khác: người lái xe chỉ tạm thời điều khiển chiếc xe, và khi chiếc xe dừng hoạt động, người lái xe vẫn tồn tại độc lập.

Trong lập trình hướng đối tượng (C++ OOP), các lớp (classes) và đối tượng (objects) không hoạt động đơn độc. Giá trị thực sự của phần mềm xuất hiện khi các đối tượng tương tác, chứa đựng hoặc kế thừa lẫn nhau.

```mermaid
flowchart TD
    Rel["Mối Quan Hệ Giữa Các Đối Tượng (Object Relationships)"]
    Rel --> Comp["1. Composition (part-of)\nThành phần sở hữu sống còn"]
    Rel --> Agg["2. Aggregation (has-a)\nTổng hợp độc lập vòng đời"]
    Rel --> Assoc["3. Association (uses-a)\nLiên kết bình đẳng"]
    Rel --> Dep["4. Dependency (depends-on)\nPhụ thuộc tạm thời qua hàm"]
    Rel --> Inh["5. Inheritance (is-a)\nKế thừa bản chất chuyên biệt"]
```

---

## 2. Bảng Phân Loại Các Mối Quan Hệ Trong C++

Dưới đây là ma trận phân biệt chi tiết 5 mối quan hệ nền tảng:

| Loại Quan Hệ | Thuật Ngữ Gốc | Kiểu Quan Hệ | Ràng Buộc Vòng Đời (Lifetime) | Cơ Chế Cài Đặt Trong C++ |
| :--- | :--- | :--- | :--- | :--- |
| **Composition** | Thành phần sở hữu | **part-of** | Chặt chẽ (Cha hủy $\\rightarrow$ Con hủy) | Thành viên kiểu giá trị trực tiếp (`Member m;`) |
| **Aggregation** | Tổng hợp | **has-a** | Độc lập (Con tồn tại ngoài Cha) | Con trỏ hoặc tham chiếu (`Member*`, `std::reference_wrapper`) |
| **Association** | Liên kết | **uses-a** | Độc lập hoàn toàn (Hai bên ngang hàng) | Con trỏ, tham chiếu hoặc mã định danh ID |
| **Dependency** | Phụ thuộc | **depends-on** | Tạm thời (Chỉ trong phạm vi gọi hàm) | Tham số truyền vào hàm, biến cục bộ |
| **Inheritance** | Kế thừa | **is-a** | Tuyệt đối (Con LÀ một dạng của Cha) | Cú pháp kế thừa `: public Base` |

---

## 3. Ý Nghĩa Kỹ Thuật Khi Lựa Chọn Quan Hệ

Việc lựa chọn sai mối quan hệ là nguyên nhân hàng đầu dẫn đến kiến trúc "mì ăn liền" (spaghetti code), thắt chặt liên kết không cần thiết (tight coupling), gây khó khăn cho việc viết Unit Test và bảo trì mã nguồn.

::: tip Nguyên Tắc Thiết Kế Vàng (Gang of Four)
**"Favor object composition over class inheritance"** (Hãy ưu tiên sử dụng Thành phần sở hữu hơn là Kế thừa). 
Kế thừa tạo ra mối liên kết rất cứng nhắc giữa lớp cha và lớp con. Trong khi đó, việc kết hợp các đối tượng độc lập (Composition/Aggregation) giúp mã nguồn mềm dẻo, dễ thay thế và giảm thiểu rủi ro lan truyền lỗi.
:::

---

## 4. Câu Hỏi Kiểm Tra Hiểu Biết (Quiz)

### Câu hỏi 1:
Mối quan hệ giữa "Một cuốn sách" và "Các trang sách" thuộc loại nào? Nếu cuốn sách bị đốt cháy, các trang sách có còn tồn tại không?
<details>
<summary><b>Xem lời giải</b></summary>

**Đáp án**: Đây là quan hệ **Composition (part-of)**. Các trang sách là một phần không thể tách rời của cuốn sách. Khi cuốn sách bị tiêu hủy, các trang sách cấu thành nó cũng bị tiêu hủy theo.
</details>

### Câu hỏi 2:
Mối quan hệ giữa "Giáo viên" và "Khoa/Bộ môn trường đại học" là gì?
<details>
<summary><b>Xem lời giải</b></summary>

**Đáp án**: Đây là quan hệ **Aggregation (has-a)**. Khoa đại học *có* các giáo viên, nhưng giáo viên tồn tại độc lập với khoa. Nếu khoa đó giải thể, giáo viên vẫn tồn tại và có thể chuyển sang khoa khác hoặc trường khác công tác.
</details>

---

## 5. Tổng Kết
Trong các bài tiếp theo của Chương 23, chúng ta sẽ lần lượt mổ xẻ mã nguồn, kiến trúc bộ nhớ RAM và các cạm bẫy thực tế của từng loại quan hệ này.
"""

# -------------------------------------------------------------
# 23.2
# -------------------------------------------------------------
lessons["23_2-composition.md"] = """# 23.2 — Thành Phần Sở Hữu (Composition)

---

## 🎯 Mục Tiêu Bài Học
- Hiểu rõ bản chất quan hệ **Composition (part-of)** trong C++.
- Nắm vững cơ chế cấp phát bộ nhớ liền kề (Contiguous Memory Layout) khi một đối tượng chứa trực tiếp đối tượng khác.
- Thành thạo việc sử dụng **Danh sách khởi tạo thành viên (Member Initializer List)** để khởi tạo các đối tượng con.
- Hiểu quy tắc vòng đời sống còn (Lifetime Dependency): Đối tượng con sinh ra cùng cha và chết cùng cha.

---

## 1. Bản Chất Của Quan Hệ Composition

Quan hệ **Composition (Thành phần sở hữu)** là mối quan hệ phức hợp chặt chẽ nhất giữa hai đối tượng. Để một mối quan hệ được coi là Composition, nó phải thỏa mãn 3 tiêu chí bắt buộc:

1. **Quan hệ bộ phận (part-of)**: Đối tượng con là một thành phần không thể tách rời của đối tượng cha.
2. **Một chủ sở hữu duy nhất (Exclusive ownership)**: Đối tượng con tại một thời điểm chỉ thuộc về đúng một đối tượng cha.
3. **Vòng đời đồng nhất (Coincident lifetime)**: Đối tượng con được tạo ra khi đối tượng cha được tạo ra, và đối tượng con tự động bị hủy diệt khi đối tượng cha kết thúc vòng đời.

```mermaid
classDiagram
    class Creature {
        -std::string m_name
        -Point2D m_location
        +moveTo(int x, int y)
    }
    class Point2D {
        -int m_x
        -int m_y
        +setPoint(int x, int y)
    }
    Creature *-- Point2D : Composition (part-of)
```

---

## 2. Trực Quan Hóa Cấu Trúc Bộ Nhớ RAM

Khi một lớp chứa trực tiếp một thành viên kiểu lớp khác (không dùng con trỏ hay tham chiếu), trình biên dịch sẽ nhúng trực tiếp toàn bộ dữ liệu của đối tượng con vào bên trong không gian bộ nhớ của đối tượng cha.

```
VÙNG NHỚ CỦA ĐỐI TƯỢNG Creature TRÊN STACK:
+-------------------------------------------------------------+
| Creature::m_name (std::string: 32 bytes)                   |
+-------------------------------------------------------------+
| Creature::m_location (Point2D: 8 bytes)                     |
|   +-----------------------+-----------------------+         |
|   | int m_x (4 bytes)     | int m_y (4 bytes)     |         |
|   +-----------------------+-----------------------+         |
+-------------------------------------------------------------+
Tổng kích thước = sizeof(std::string) + sizeof(Point2D) (+ padding nếu có)
```

::: tip Ưu Điểm Tuyệt Đối Về Hiệu Năng
Do các biến thành viên nằm liền kề nhau trong bộ nhớ (Cache locality cực cao), CPU khi nạp đối tượng cha vào L1/L2 Cache sẽ nạp luôn cả đối tượng con. Không phát sinh chi phí phân mảnh bộ nhớ Heap hay trỏ gián tiếp qua con trỏ!
:::

---

## 3. Cài Đặt Mã Nguồn Hoàn Chỉnh

Hãy xem xét ví dụ một sinh vật `Creature` sở hữu tọa độ `Point2D`:

```cpp
#include <iostream>
#include <string>
#include <string_view>

class Point2D
{
private:
    int m_x{ 0 };
    int m_y{ 0 };

public:
    Point2D() = default;
    Point2D(int x, int y) : m_x{ x }, m_y{ y }
    {
        std::cout << "Point2D (" << m_x << ", " << m_y << ") duoc tao.\\n";
    }

    ~Point2D()
    {
        std::cout << "Point2D (" << m_x << ", " << m_y << ") bi huy.\\n";
    }

    void setPoint(int x, int y)
    {
        m_x = x;
        m_y = y;
    }

    int getX() const { return m_x; }
    int getY() const { return m_y; }
};

class Creature
{
private:
    std::string m_name;
    Point2D m_location; // Composition: Point2D la mot phan cua Creature

public:
    Creature(std::string_view name, const Point2D& location)
        : m_name{ name }, m_location{ location }
    {
        std::cout << "Sinh vat " << m_name << " xuat hien tai toa do!\\n";
    }

    ~Creature()
    {
        std::cout << "Sinh vat " << m_name << " bi tieu diet!\\n";
    }

    void moveTo(int newX, int newY)
    {
        m_location.setPoint(newX, newY);
    }

    void report() const
    {
        std::cout << m_name << " dang o toa do: (" 
                  << m_location.getX() << ", " << m_location.getY() << ")\\n";
    }
};

int main()
{
    std::cout << "=== BAT DAU KHOI LENH ===\\n";
    {
        Creature monster{ "Rong Lua", Point2D{ 10, 25 } };
        monster.report();
        monster.moveTo(50, 100);
        monster.report();
    } // Tai day monster roi scope, bi huy tu dong
    std::cout << "=== KET THUC KHOI LENH ===\\n";

    return 0;
}
```

### Kết quả thực thi:
```text
=== BAT DAU KHOI LENH ===
Point2D (10, 25) duoc tao.
Sinh vat Rong Lua xuat hien tai toa do!
Point2D (10, 25) bi huy.
Rong Lua dang o toa do: (10, 25)
Rong Lua dang o toa do: (50, 100)
Sinh vat Rong Lua bi tieu diet!
Point2D (50, 100) bi huy.
=== KET THUC KHOI LENH ===
```

::: warning Thứ Tự Khởi Tạo Và Hủy Bỏ
1. **Khởi tạo**: Các đối tượng thành phần con (`m_location`) luôn được khởi tạo **TRƯỚC**, sau đó mới thực thi thân Constructor của đối tượng cha (`Creature`).
2. **Hủy diệt**: Đối tượng cha (`Creature`) thực thi Destructor **TRƯỚC**, sau đó các đối tượng thành phần con (`m_location`) mới bị hủy theo thứ tự ngược lại.
:::

---

## 4. Khi Nào Nên Sử Dụng Composition?

Hãy áp dụng quan hệ Composition khi:
- Thành phần con không có ý nghĩa tồn tại độc lập nếu thiếu đối tượng cha.
- Bạn muốn quản lý tài nguyên tự động theo triết lý **RAII**: Khi cha bị hủy, toàn bộ con tự động giải phóng sạch sẽ mà không bao giờ sợ rò rỉ bộ nhớ (Memory Leak).
- Thiết kế hệ thống đơn giản, an toàn và trực quan.

---

## 5. Quiz & Bài Tập

### Câu hỏi:
Lớp `Car` sở hữu 4 đối tượng kiểu `Tire`. Nếu đối tượng `Car` được cấp phát động trên Heap (`Car* car = new Car;`), thì 4 đối tượng `Tire` nằm trên vùng nhớ nào (Stack hay Heap)?
<details>
<summary><b>Xem lời giải</b></summary>

**Đáp án**: Chúng nằm trên **Heap**! Vì trong Composition, đối tượng con được nhúng trực tiếp vào không gian bộ nhớ của đối tượng cha. Nếu đối tượng cha nằm trên Heap, thì toàn bộ các thành viên của nó cũng nằm trên Heap cùng một khối bộ nhớ liền mạch.
</details>
"""

# -------------------------------------------------------------
# 23.3
# -------------------------------------------------------------
lessons["23_3-aggregation.md"] = """# 23.3 — Quan Hệ Tổng Hợp (Aggregation)

---

## 🎯 Mục Tiêu Bài Học
- Hiểu rõ bản chất quan hệ **Aggregation (has-a)** và sự khác biệt then chốt so với Composition.
- Nắm vững cách quản lý đối tượng thành viên tồn tại độc lập thông qua con trỏ thô, con trỏ thông minh, hoặc `std::reference_wrapper`.
- Nhận diện và phòng tránh cạm bẫy **Con trỏ lơ lửng (Dangling Pointer)** khi đối tượng thành viên bị hủy trước lớp chứa nó.

---

## 1. Bản Chất Của Quan Hệ Aggregation

**Aggregation (Tổng hợp)** là mối quan hệ yếu hơn Composition. Để một mối quan hệ là Aggregation, nó phải thỏa mãn các điều kiện:

1. **Quan hệ sở hữu lỏng lẻo (has-a)**: Đối tượng A có đối tượng B, nhưng B không phải là một phần thể xác của A.
2. **Vòng đời độc lập (Independent lifetime)**: Đối tượng con được tạo ra **trước** đối tượng cha, và khi đối tượng cha bị hủy, đối tượng con **vẫn tiếp tục tồn tại bình thường**.
3. **Có thể chia sẻ quyền sở hữu (Shared)**: Nhiều đối tượng cha có thể cùng tham chiếu tới một đối tượng con.

```mermaid
classDiagram
    class Department {
        -std::string m_name
        -const Teacher* m_teacher
        +addTeacher(const Teacher& t)
    }
    class Teacher {
        -std::string m_name
        +getName()
    }
    Department o-- Teacher : Aggregation (has-a)
```

---

## 2. So Sánh Chi Tiết: Composition vs Aggregation

| Đặc Tính | Composition (Thành Phần Sở Hữu) | Aggregation (Tổng Hợp) |
| :--- | :--- | :--- |
| **Bản chất** | *part-of* (một phần thể xác) | *has-a* (sở hữu/liên kết độc lập) |
| **Vòng đời** | Phụ thuộc tuyệt đối (Cùng sinh cùng tử) | Độc lập (Con sống sót khi Cha chết) |
| **Quyền sở hữu** | Độc quyền (Exclusive) | Không sở hữu hoặc chia sẻ (Shared) |
| **Cài đặt C++** | Biến giá trị thông thường (`Type m_var;`) | Con trỏ hoặc tham chiếu (`Type*`, `Type&`) |
| **Quản lý hủy** | Cha tự động giải phóng con | Cha **KHÔNG ĐƯỢC** delete con |

---

## 3. Cài Đặt Mã Nguồn C++ Chuẩn Xác

Trong C++, vì tham chiếu (`&`) không thể gán lại sau khi khởi tạo và không thể lưu trực tiếp trong các container như `std::vector`, giải pháp hiện đại chuẩn C++11 trở lên là sử dụng **con trỏ** hoặc **`std::reference_wrapper`** (trong thư viện `<functional>`).

```cpp
#include <iostream>
#include <string>
#include <string_view>
#include <vector>
#include <functional> // std::reference_wrapper

class Teacher
{
private:
    std::string m_name;

public:
    Teacher(std::string_view name) : m_name{ name }
    {
        std::cout << "Giao vien " << m_name << " duoc tao.\\n";
    }

    ~Teacher()
    {
        std::cout << "Giao vien " << m_name << " bi huy.\\n";
    }

    std::string_view getName() const { return m_name; }
};

class Department
{
private:
    std::string m_name;
    // Dung std::reference_wrapper de luu danh sach tham chieu an toan
    std::vector<std::reference_wrapper<const Teacher>> m_teachers;

public:
    Department(std::string_view name) : m_name{ name } {}

    ~Department()
    {
        std::cout << "Khoa " << m_name << " bi giai the! (Nhung giao vien van an toan)\\n";
    }

    void addTeacher(const Teacher& teacher)
    {
        m_teachers.push_back(teacher);
    }

    void showTeachers() const
    {
        std::cout << "Danh sach giang vien Khoa " << m_name << ":\\n";
        for (const auto& teacherRef : m_teachers)
        {
            std::cout << " - " << teacherRef.get().getName() << '\\n';
        }
    }
};

int main()
{
    // 1. Giao vien duoc tao truoc, doc lap voi Khoa
    Teacher t1{ "Thay Ba - Toan Cao Cap" };
    Teacher t2{ "Co Hoa - Lap Trinh C++" };

    std::cout << "--- Mo Khoa Cong Nghe Thong Tin ---\\n";
    {
        Department cntt{ "Cong Nghe Thong Tin" };
        cntt.addTeacher(t1);
        cntt.addTeacher(t2);
        cntt.showTeachers();
    } // Tai day Khoa cntt bi huy

    std::cout << "--- Sau khi Khoa giai the ---\\n";
    std::cout << "Giao vien van con song: " << t1.getName() << " va " << t2.getName() << '\\n';

    return 0;
}
```

### Kết quả thực thi:
```text
Giao vien Thay Ba - Toan Cao Cap duoc tao.
Giao vien Co Hoa - Lap Trinh C++ duoc tao.
--- Mo Khoa Cong Nghe Thong Tin ---
Danh sach giang vien Khoa Cong Nghe Thong Tin:
 - Thay Ba - Toan Cao Cap
 - Co Hoa - Lap Trinh C++
Khoa Cong Nghe Thong Tin bi giai the! (Nhung giao vien van an toan)
--- Sau khi Khoa giai the ---
Giao vien van con song: Thay Ba - Toan Cao Cap va Co Hoa - Lap Trinh C++
Giao vien Co Hoa - Lap Trinh C++ bi huy.
Giao vien Thay Ba - Toan Cao Cap bi huy.
```

---

## 4. Cạm Bẫy Chết Người: Dangling Pointer / Dangling Reference

::: danger Nguy Hiểm Cực Kỳ (Undefined Behavior)
Nếu đối tượng thành viên bị hủy **TRƯỚC** khi đối tượng chứa nó kết thúc vòng đời, con trỏ hoặc tham chiếu bên trong lớp chứa sẽ trỏ vào vùng nhớ rác!
:::

```cpp
Department* dept = new Department{ "Ngoai Ngu" };
{
    Teacher tempTeacher{ "Thay Tam Thoi" };
    dept->addTeacher(tempTeacher);
} // tempTeacher bi huy tai day!

// NGUY HIEM: dept van con giu tham chieu den tempTeacher da chet!
dept->showTeachers(); // UNDEFINED BEHAVIOR! Crash hoac in ky tu rac!
```

---

## 5. Quiz Kiểm Tra Kiến Thức

### Câu hỏi:
Khi nào Destructor của lớp `Department` có quyền gọi lệnh `delete` lên con trỏ giáo viên?
<details>
<summary><b>Xem lời giải</b></summary>

**Đáp án**: **KHÔNG BAO GIỜ!** Trong quan hệ Aggregation, lớp cha không sở hữu vòng đời của đối tượng con. Nếu Destructor của `Department` tự ý `delete` giáo viên, sẽ xảy ra lỗi **Double Free** hoặc làm sập chương trình khi các đối tượng khác đang sử dụng chung giáo viên đó.
</details>
"""

# -------------------------------------------------------------
# 23.4
# -------------------------------------------------------------
lessons["23_4-association.md"] = """# 23.4 — Quan Hệ Liên Kết (Association)

---

## 🎯 Mục Tiêu Bài Học
- Hiểu rõ bản chất quan hệ **Association (uses-a)** giữa các đối tượng ngang hàng.
- Phân biệt giữa liên kết **Một chiều (Unidirectional)** và **Hai chiều (Bidirectional)**.
- Nắm bắt giải pháp xử lý **Phụ thuộc vòng (Circular Dependency)** bằng Khai báo tiền tiến (**Forward Declaration**).

---

## 1. Bản Chất Quan Hệ Association

Quan hệ **Association (Liên kết)** mô tả mối quan hệ giữa hai lớp độc lập hoàn toàn, trong đó không có bên nào sở hữu hay làm cha của bên nào.
- Chúng là các thực thể ngang hàng (*peer-to-peer*).
- Cả hai đều có vòng đời riêng biệt do bên ngoài quản lý.
- Mối quan hệ này biểu thị động từ "sử dụng", "làm việc cùng" (*uses-a* hoặc *works-with*).

Ví dụ kinh điển: Mối quan hệ giữa **Bác sĩ (Doctor)** và **Bệnh nhân (Patient)**.
- Một bác sĩ có thể khám cho nhiều bệnh nhân.
- Một bệnh nhân có thể có nhiều bác sĩ phụ trách.
- Bác sĩ nghỉ việc không làm bệnh nhân chết. Bệnh nhân xuất viện không làm bác sĩ bị sa thải.

```mermaid
classDiagram
    class Doctor {
        -std::string m_name
        -std::vector<Patient*> m_patients
        +addPatient(Patient& p)
    }
    class Patient {
        -std::string m_name
        -std::vector<Doctor*> m_doctors
        +addDoctor(Doctor& d)
    }
    Doctor <--> Patient : Association Hai Chiều (Bidirectional)
```

---

## 2. Thách Thức Kỹ Thuật: Circular Dependency

Khi Bác sĩ cần biết thông tin Bệnh nhân, và Bệnh nhân cũng cần biết thông tin Bác sĩ, hai tệp header sẽ nảy sinh tình trạng phụ thuộc lẫn nhau:

```cpp
// Doctor.h include Patient.h
// Patient.h include Doctor.h --> LOI BIEN DICH VO TAN!
```

### Giải pháp chuẩn mực: Forward Declaration
Chúng ta khai báo trước tên lớp `class Patient;` trong `Doctor.h`, và chỉ định nghĩa chi tiết trong tệp `.cpp`.

```cpp
#include <iostream>
#include <string>
#include <string_view>
#include <vector>

// Forward declaration
class Patient;

class Doctor
{
private:
    std::string m_name;
    std::vector<std::reference_wrapper<const Patient>> m_patients;

public:
    Doctor(std::string_view name) : m_name{ name } {}

    std::string_view getName() const { return m_name; }

    void addPatient(const Patient& patient);
    void showPatients() const;
};

class Patient
{
private:
    std::string m_name;
    std::vector<std::reference_wrapper<const Doctor>> m_doctors;

public:
    Patient(std::string_view name) : m_name{ name } {}

    std::string_view getName() const { return m_name; }

    void addDoctor(const Doctor& doctor)
    {
        m_doctors.push_back(doctor);
    }

    void showDoctors() const
    {
        std::cout << "Benh nhan " << m_name << " dang duoc dieu tri boi:\\n";
        for (const auto& docRef : m_doctors)
        {
            std::cout << " - Bac si: " << docRef.get().getName() << '\\n';
        }
    }
};

// Trien khai phuong thuc cua Doctor sau khi Patient da duoc dinh nghia day du
void Doctor::addPatient(const Patient& patient)
{
    m_patients.push_back(patient);
}

void Doctor::showPatients() const
{
    std::cout << "Bac si " << m_name << " dang theo doi danh sach benh nhan:\\n";
    for (const auto& patientRef : m_patients)
    {
        std::cout << " - Benh nhan: " << patientRef.get().getName() << '\\n';
    }
}

int main()
{
    Doctor docMinh{ "BS. Nguyen Van Minh" };
    Doctor docLan{ "BS. Tran Thi Lan" };

    Patient benhNhanAn{ "Nguyen Van An" };
    Patient benhNhanBinh{ "Le Van Binh" };

    // Thiet lap lien ket 2 chieu
    docMinh.addPatient(benhNhanAn);
    benhNhanAn.addDoctor(docMinh);

    docMinh.addPatient(benhNhanBinh);
    benhNhanBinh.addDoctor(docMinh);

    docLan.addPatient(benhNhanAn);
    benhNhanAn.addDoctor(docLan);

    std::cout << "================================\\n";
    docMinh.showPatients();
    std::cout << "================================\\n";
    benhNhanAn.showDoctors();

    return 0;
}
```

---

## 3. Quản Lý Liên Kết Gián Tiếp Qua ID (Id-based Association)

Trong các ứng dụng cơ sở dữ liệu lớn (Database), việc lưu trữ con trỏ trực tiếp giữa hai đối tượng rất dễ gây lỗi đồng bộ khi dữ liệu thay đổi. Cách tiếp cận chuyên nghiệp hơn là sử dụng **Mã định danh duy nhất (ID)**:

```cpp
class Patient
{
private:
    int m_id;
    std::string m_name;
    std::vector<int> m_doctorIds; // Luu ID thay vi con tro
};
```
Mô hình này giúp tách rời hoàn toàn liên kết bộ nhớ, cực kỳ thích hợp cho lập trình mạng (Networking) và lưu trữ dữ liệu (Persistence).

---

## 4. Quiz

### Câu hỏi:
Sự khác biệt căn bản giữa Aggregation và Association là gì?
<details>
<summary><b>Xem lời giải</b></summary>

**Đáp án**: 
- **Aggregation** thể hiện mối quan hệ "sở hữu không chặt chẽ" (*whole/part* hay *has-a*), tức có một thực thể đóng vai trò là "vỏ chứa" hoặc "chủ quản" của thực thể kia (như Khoa và Giáo viên).
- **Association** thể hiện mối quan hệ liên kết ngang hàng bình đẳng (*peer-to-peer*), không bên nào chứa hay quản lý bên nào (như Bác sĩ và Bệnh nhân).
</details>
"""

# -------------------------------------------------------------
# 23.5
# -------------------------------------------------------------
lessons["23_5-dependencies.md"] = """# 23.5 — Quan Hệ Phụ Thuộc (Dependencies)

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
    Point["Lớp Point"] -->|"phụ thuộc qua tham số hàm\noperator<<(std::ostream&, Point)"| Stream["Thư viện std::ostream"]
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
    std::cout << "Gia tri toa do: " << p << '\\n';
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
<details>
<summary><b>Xem lời giải</b></summary>

**Đáp án**: Quan hệ **Dependency (Phụ thuộc)**. Hàm chỉ mượn tạm `User` để đọc dữ liệu trong quá trình thực thi, không chịu trách nhiệm cấp phát hay hủy bỏ `User`.
</details>
"""

# -------------------------------------------------------------
# 23.6
# -------------------------------------------------------------
lessons["23_6-container-classes.md"] = """# 23.6 — Các Lớp Vỏ Chứa (Container Classes)

---

## 🎯 Mục Tiêu Bài Học
- Hiểu định nghĩa và vai trò của **Lớp vỏ chứa (Container Class)** trong C++.
- Tự tay cài đặt hoàn chỉnh lớp mảng động `IntArray` an toàn từ số 0.
- Nắm vững các thao tác: Cấp phát lại (`reallocate`), Thay đổi kích thước (`resize`), Chèn phần tử (`insertAt`), Xóa phần tử (`remove`).
- Tuân thủ nguyên lý **RAII (Resource Acquisition Is Initialization)** để ngăn chặn tuyệt đối rò rỉ bộ nhớ (Memory Leak).

---

## 1. Container Class Là Gì?

Một **Container Class** là một lớp được thiết kế với mục đích duy nhất: tổ chức, lưu trữ và quản lý một tập hợp các phần tử khác. Trong Thư viện chuẩn STL của C++, các container kinh điển bao gồm `std::vector`, `std::array`, `std::list`, `std::map`.

Container Class thường được chia làm 2 loại:
1. **Value Containers**: Chứa trực tiếp các bản sao của dữ liệu (Composition).
2. **Reference Containers**: Chứa các con trỏ hoặc tham chiếu tới dữ liệu bên ngoài (Aggregation).

---

## 2. Tự Cài Đặt Lớp Mảng Động `IntArray` Hoàn Chỉnh

Hãy cùng mổ xẻ mã nguồn xây dựng lớp `IntArray` chuyên nghiệp:

```cpp
#include <iostream>
#include <cassert> // Cho phep kiem tra assert

class IntArray
{
private:
    int m_length{ 0 };
    int* m_data{ nullptr };

public:
    // 1. Constructor mac dinh
    IntArray() = default;

    // 2. Constructor tao mang co do dai length
    explicit IntArray(int length) : m_length{ length }
    {
        assert(length >= 0 && "Do dai mang phai lon hon hoac bang 0!");
        if (length > 0)
            m_data = new int[length]{}; // Khoi tao tat ca phan tu bang 0
    }

    // 3. Destructor giai phong Heap tu dong (RAII)
    ~IntArray()
    {
        delete[] m_data;
    }

    // Cam copy ngam dinh de tranh loi Double Free (o bai sau se hoc Rule of 5)
    IntArray(const IntArray&) = delete;
    IntArray& operator=(const IntArray&) = delete;

    // Xoa sach mang
    void erase()
    {
        delete[] m_data;
        m_data = nullptr;
        m_length = 0;
    }

    // Truy cap phan tu voi kiem tra chi so hop le
    int& operator[](int index)
    {
        assert(index >= 0 && index < m_length && "Chi so vuot qua gioi han mang!");
        return m_data[index];
    }

    int operator[](int index) const
    {
        assert(index >= 0 && index < m_length && "Chi so vuot qua gioi han mang!");
        return m_data[index];
    }

    int getLength() const { return m_length; }

    // Cap phat lai vung nho moi (xoa bo du lieu cu)
    void reallocate(int newLength)
    {
        erase();
        if (newLength <= 0)
            return;

        m_data = new int[newLength];
        m_length = newLength;
    }

    // Thay doi kich thuoc mang (GIU LAI DU LIEU CU)
    void resize(int newLength)
    {
        if (newLength == m_length)
            return;

        if (newLength <= 0)
        {
            erase();
            return;
        }

        // Cap phat vung nho moi
        int* data = new int[newLength];

        // Sao chep cac phan tu cu sang vung nho moi
        if (m_length > 0)
        {
            int elementsToCopy = (newLength > m_length) ? m_length : newLength;
            for (int i = 0; i < elementsToCopy; ++i)
                data[i] = m_data[i];
        }

        // Xoa vung nho cu va gan vung nho moi
        delete[] m_data;
        m_data = data;
        m_length = newLength;
    }

    // Chen phan tu tai mot vi tri chi dinh
    void insertAt(int value, int index)
    {
        assert(index >= 0 && index <= m_length && "Vi tri chen khong hop le!");

        int* data = new int[m_length + 1];

        // Sao chep phan tu truoc index
        for (int before = 0; before < index; ++before)
            data[before] = m_data[before];

        // Chen gia tri moi vao index
        data[index] = value;

        // Sao chep cac phan tu con lai
        for (int after = index; after < m_length; ++after)
            data[after + 1] = m_data[after];

        delete[] m_data;
        m_data = data;
        ++m_length;
    }

    // Xoa phan tu tai vi tri index
    void remove(int index)
    {
        assert(index >= 0 && index < m_length && "Vi tri xoa khong hop le!");

        if (m_length == 1)
        {
            erase();
            return;
        }

        int* data = new int[m_length - 1];

        for (int before = 0; before < index; ++before)
            data[before] = m_data[before];

        for (int after = index + 1; after < m_length; ++after)
            data[after - 1] = m_data[after];

        delete[] m_data;
        m_data = data;
        --m_length;
    }
};

int main()
{
    IntArray array{ 5 };

    for (int i = 0; i < array.getLength(); ++i)
        array[i] = (i + 1) * 10;

    std::cout << "Mang ban dau: ";
    for (int i = 0; i < array.getLength(); ++i)
        std::cout << array[i] << ' ';
    std::cout << '\\n';

    // Chen phan tu 99 vao vi tri index 2
    array.insertAt(99, 2);

    std::cout << "Sau khi chen 99 vao index 2: ";
    for (int i = 0; i < array.getLength(); ++i)
        std::cout << array[i] << ' ';
    std::cout << '\\n';

    // Xoa phan tu tai vi tri index 0
    array.remove(0);

    std::cout << "Sau khi xoa index 0: ";
    for (int i = 0; i < array.getLength(); ++i)
        std::cout << array[i] << ' ';
    std::cout << '\\n';

    return 0;
}
```

---

## 3. Quiz & Bài Tập

### Câu hỏi:
Tại sao trong hàm `resize()`, chúng ta phải cấp phát con trỏ mới `int* data = new int[newLength];` trước khi gọi `delete[] m_data;`?
<details>
<summary><b>Xem lời giải</b></summary>

**Đáp án**: Nếu bạn gọi `delete[] m_data;` trước, toàn bộ dữ liệu cũ sẽ bị giải phóng ngay lập tức trên Heap! Khi đó, bạn không còn dữ liệu để sao chép sang mảng mới. Ngoài ra, việc cấp phát trước còn đảm bảo tính an toàn ngoại lệ (Exception Safety): nếu `new` bị lỗi ném ra ngoại lệ `std::bad_alloc`, dữ liệu cũ của đối tượng vẫn còn nguyên vẹn.
</details>
"""

# -------------------------------------------------------------
# 23.7
# -------------------------------------------------------------
lessons["23_7-stdinitializer_list.md"] = """# 23.7 — Khởi Tạo Danh Sách Với `std::initializer_list` (C++11)

---

## 🎯 Mục Tiêu Bài Học
- Hiểu cơ chế hoạt động bên dưới của `std::initializer_list` trong C++11.
- Tích hợp Constructor nhận `std::initializer_list` vào lớp Container tự tạo.
- Nắm vững cạm bẫy: Trình biên dịch ưu tiên tối thượng `std::initializer_list` khi dùng cặp ngoặc nhọn `{}`.

---

## 1. Sự Cần Thiết Của `std::initializer_list`

Trước C++11, việc khởi tạo một container với các giá trị ban đầu rất cồng kềnh:
```cpp
// Thoi ky C++03: Phai chen tung phan tu mot
IntArray arr(3);
arr[0] = 10;
arr[1] = 20;
arr[2] = 30;
```

C++11 giới thiệu lớp mẫu `std::initializer_list<T>` trong header `<initializer_list>`, cho phép chúng ta khởi tạo trực quan và thanh lịch:
```cpp
IntArray arr{ 10, 20, 30, 40, 50 }; // C++11 Uniform Initialization
```

---

## 2. Bản Chất Bộ Nhớ Của `std::initializer_list`

Khi trình biên dịch nhìn thấy danh sách `{ 10, 20, 30 }`, nó thực hiện:
1. Tạo một mảng ẩn các phần tử kiểu `const T` trên Stack hoặc vùng dữ liệu chỉ đọc (Read-only data segment).
2. Tạo một đối tượng `std::initializer_list<T>` bọc lấy hai con trỏ: `begin()` trỏ tới phần tử đầu tiên và `end()` trỏ tới vị trí sau phần tử cuối cùng.
3. Truyền đối tượng nhỏ gọn này (thường chỉ 16 bytes gồm 2 con trỏ) vào Constructor.

```mermaid
flowchart LR
    List["std::initializer_list<int>\n(kich thuoc 16 bytes)"]
    List -->|".begin()"| E0["Mảng ẩn trong RAM\nPhần tử 0: 10"]
    E0 --> E1["Phần tử 1: 20"]
    E1 --> E2["Phần tử 2: 30"]
    List -->|".end()"| E3["Vị trí sau phần tử 2"]
```

---

## 3. Tích Hợp Vào Lớp `IntArray`

```cpp
#include <iostream>
#include <initializer_list>
#include <algorithm> // std::copy

class IntArray
{
private:
    int m_length{ 0 };
    int* m_data{ nullptr };

public:
    IntArray() = default;

    explicit IntArray(int length) : m_length{ length }
    {
        if (length > 0)
            m_data = new int[length]{};
    }

    // CONSTRUCTOR NHAN std::initializer_list
    IntArray(std::initializer_list<int> list)
        : IntArray(static_cast<int>(list.size())) // Goi constructor uy quyen (Delegating constructor)
    {
        int count{ 0 };
        for (auto element : list)
        {
            m_data[count] = element;
            ++count;
        }
    }

    ~IntArray()
    {
        delete[] m_data;
    }

    int getLength() const { return m_length; }
    int operator[](int index) const { return m_data[index]; }
};

int main()
{
    // Khoi tao mang de dang nhu cac kieu nguyen thuy!
    IntArray array{ 5, 4, 3, 2, 1, 99, 100 };

    std::cout << "Cac phan tu trong array: ";
    for (int i = 0; i < array.getLength(); ++i)
    {
        std::cout << array[i] << ' ';
    }
    std::cout << '\\n';

    return 0;
}
```

---

## 4. Cạm Bẫy Kinh Điển: `v{5}` vs `v(5)` Trong `std::vector`

::: danger Cạm Bẫy Cực Kỳ Phổ Biến Của Lập Trình Viên C++
Khi một lớp có cả Constructor nhận tham số thông thường và Constructor nhận `std::initializer_list`, việc dùng ngoặc nhọn `{}` sẽ luôn được compiler **ƯU TIÊN TUYỆT ĐỐI** nếu các phần tử có thể chuyển đổi kiểu về kiểu của initializer_list!
:::

```cpp
#include <vector>
#include <iostream>

int main()
{
    // Goi Constructor (int size): Tao vector co 5 phan tu, tat ca bang 0
    std::vector<int> a(5);
    std::cout << "a.size() = " << a.size() << " | a[0] = " << a[0] << '\\n'; 
    // Output: size = 5, a[0] = 0

    // Goi Constructor (initializer_list<int>): Tao vector co dung 1 phan tu la so 5!
    std::vector<int> b{5};
    std::cout << "b.size() = " << b.size() << " | b[0] = " << b[0] << '\\n'; 
    // Output: size = 1, b[0] = 5

    return 0;
}
```

---

## 5. Quiz

### Câu hỏi:
Có thể sửa đổi các phần tử bên trong `std::initializer_list<T>` được không (ví dụ: `*list.begin() = 10;`)?
<details>
<summary><b>Xem lời giải</b></summary>

**Đáp án**: **HOÀN TOÀN KHÔNG!** Các phần tử trong `std::initializer_list<T>` luôn có thuộc tính `const`. Trình biên dịch cấm tuyệt đối mọi hành vi sửa đổi giá trị bên trong danh sách này để đảm bảo tính an toàn và cho phép đặt mảng dữ liệu vào vùng nhớ chỉ đọc (Read-only memory).
</details>
"""

# -------------------------------------------------------------
# 23.x
# -------------------------------------------------------------
lessons["23_x-chapter-23-summary-and-quiz.md"] = """# 23.x — Tổng Kết Chương 23 & Bài Kiểm Tra Toàn Diện

---

## 🎯 Mục Tiêu
- Khái quát toàn bộ bức tranh về mối quan hệ giữa các đối tượng trong C++.
- Hệ thống hóa bảng tra cứu nhanh giúp bạn ra quyết định thiết kế kiến trúc phần mềm chuẩn xác.
- Vượt qua bộ câu hỏi trắc nghiệm và bài tập thực hành thiết kế OOP hoàn chỉnh.

---

## 1. Bảng Tổng Hợp Các Mối Quan Hệ Đối Tượng

```mermaid
flowchart TD
    Q1{"Đối tượng B có phải là một phần thể xác của A?"}
    Q1 -->|Có| Q2{"Vòng đời của B có phụ thuộc hoàn toàn vào A?"}
    Q1 -->|Không| Q3{"A có sở hữu B không hay ngang hàng?"}
    
    Q2 -->|Có: A chết B chết| C["COMPOSITION (part-of)\nVí dụ: Xe và Động cơ"]
    Q2 -->|Không: B sống độc lập| A["AGGREGATION (has-a)\nVí dụ: Khoa và Giáo viên"]
    
    Q3 -->|Ngang hàng: uses-a| AS["ASSOCIATION (uses-a)\nVí dụ: Bác sĩ và Bệnh nhân"]
    Q3 -->|Chỉ dùng tạm trong hàm| D["DEPENDENCY (depends-on)\nVí dụ: In ra std::ostream"]
```

---

## 2. Bài Kiểm Tra Toàn Diện (Comprehensive Quiz)

### Câu hỏi 1:
Mỗi trường hợp sau đây tương ứng với mối quan hệ nào (Composition, Aggregation, Association, Dependency)?
1. Một chiếc máy tính xách tay và bo mạch chủ (Motherboard) gắn chặt bên trong nó.
2. Một thư viện và các cuốn sách có thể mượn đem về nhà.
3. Một người lập trình viên và bàn phím máy tính anh ấy đang gõ.
4. Một hàm tính căn bậc hai `Math::sqrt` nhận vào một số `double`.

<details>
<summary><b>Xem lời giải</b></summary>

1. **Composition (part-of)**: Bo mạch chủ là thành phần sống còn của máy tính.
2. **Aggregation (has-a)**: Thư viện chứa sách, nhưng sách mượn ra ngoài vẫn tồn tại độc lập.
3. **Association (uses-a)**: Lập trình viên và bàn phím là 2 thực thể độc lập tương tác với nhau.
4. **Dependency (depends-on)**: Hàm toán học chỉ nhận dữ liệu tham số để tính toán tạm thời.
</details>

### Câu hỏi 2:
Hãy viết một chương trình C++ hoàn chỉnh mô phỏng mối quan hệ:
- Một lớp `Monster` (Quái vật) có tên (`std::string`) và máu (`int`).
- Một lớp `Weapon` (Vũ khí) có tên và sát thương (`int`).
- Quái vật có thể nhặt một vũ khí và sử dụng nó để tấn công. Vũ khí tồn tại độc lập với quái vật (Khi quái vật chết, vũ khí rơi ra đất và không bị hủy).
- Xác định đây là mối quan hệ gì và viết code minh họa.

<details>
<summary><b>Xem lời giải</b></summary>

Đây là quan hệ **Aggregation (has-a)**: Quái vật *có* vũ khí, nhưng không sở hữu vòng đời của vũ khí.

```cpp
#include <iostream>
#include <string>
#include <string_view>

class Weapon
{
private:
    std::string m_name;
    int m_damage{ 0 };

public:
    Weapon(std::string_view name, int damage)
        : m_name{ name }, m_damage{ damage } {}

    std::string_view getName() const { return m_name; }
    int getDamage() const { return m_damage; }
};

class Monster
{
private:
    std::string m_name;
    int m_hp{ 100 };
    const Weapon* m_weapon{ nullptr }; // Aggregation qua con trỏ

public:
    Monster(std::string_view name, int hp)
        : m_name{ name }, m_hp{ hp } {}

    void equipWeapon(const Weapon& weapon)
    {
        m_weapon = &weapon;
    }

    void attack() const
    {
        if (m_weapon)
        {
            std::cout << m_name << " tan cong bang " << m_weapon->getName() 
                      << " gay " << m_weapon->getDamage() << " sat thuong!\\n";
        }
        else
        {
            std::cout << m_name << " tan cong bang tay khong gay 1 sat thuong!\\n";
        }
    }
};

int main()
{
    // Vu khi ton tai doc lap
    Weapon legendarySword{ "Thanh Guom Diet Quy", 999 };

    {
        Monster orc{ "Chua Te Orc", 500 };
        orc.equipWeapon(legendarySword);
        orc.attack();
    } // Quai vat orc bi tieu diet tai day

    // Vu khi van nguyen ven sau khi quai vat chet!
    std::cout << "Vu khi van con tren mat dat: " << legendarySword.getName() 
              << " voi sat thuong: " << legendarySword.getDamage() << '\\n';

    return 0;
}
```
</details>

---

## 3. Lời Kết Chương 23
Bạn đã làm chủ toàn bộ các mối quan hệ cấu thành hướng đối tượng. Ở Chương 24 và Chương 25 tiếp theo, chúng ta sẽ bước vào đỉnh cao của lập trình hướng đối tượng: **Tính Kế Thừa (Inheritance)** và **Hàm Ảo & Tính Đa Hình (Virtual Functions & Polymorphism)**!
"""

for fname, content in lessons.items():
    fpath = os.path.join(OUT_DIR, fname)
    with open(fpath, "w", encoding="utf-8") as f:
        f.write(content.strip() + "\n")
    print(f" -> Đã tạo ch25: {fname}")

print("HOÀN THÀNH CHƯƠNG 23 (8 bài trong docs/vi/ch25)")
