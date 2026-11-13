#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import os

BASE_DIR = "/home/nam/Documents/learncpp"
OUT_DIR = os.path.join(BASE_DIR, "docs", "vi", "ch29")
os.makedirs(OUT_DIR, exist_ok=True)

lessons = {}

# 27.1
lessons["27_1-the-need-for-exceptions.md"] = """# 27.1 — Nhu Cầu Cần Ngoại Lệ (The Need for Exceptions)

---

## 🎯 Mục Tiêu Bài Học
- Nhận thức những hạn chế nghiêm trọng của cơ chế xử lý lỗi truyền thống qua Mã Lỗi (Return / Error Codes).
- Hiểu tại sao Constructor không thể dùng mã lỗi và nguy cơ tạo ra "Đối tượng xác sống" (**Zombie Objects**).
- Thấy được sự thanh lịch của Ngoại Lệ (**Exceptions**) trong việc tách rời luồng logic chính khỏi luồng xử lý lỗi.

---

## 1. Hạn Chế Của Cơ Chế Báo Lỗi Truyền Thống

Trong ngôn ngữ C và C++ thời kỳ đầu, cách thông dụng nhất để báo lỗi là trả về một giá trị đặc biệt (ví dụ `-1`, `nullptr` hoặc mã lỗi `enum`):

```cpp
// Cách tiếp cận truyền thống
int divide(int a, int b, int& result)
{
    if (b == 0)
        return -1; // Mã lỗi: Chia cho 0
    result = a / b;
    return 0;      // Thành công
}
```

Cách làm này bộc lộ 3 nhược điểm chí tử:
1. **Dễ bị lập trình viên bỏ qua**: Không có cơ chế nào ép buộc người gọi hàm phải kiểm tra giá trị trả về. Nếu họ lờ đi, chương trình sẽ tiếp tục chạy với dữ liệu sai lệch.
2. **Làm ô nhiễm luồng logic chính**: Mã nguồn bị phân mảnh bởi hàng loạt câu lệnh `if (err != 0) return err;`, khiến code cực kỳ rối rắm và khó đọc.
3. **Constructor hoàn toàn bất lực!**: Constructor **không có kiểu dữ liệu trả về**. Nếu Constructor của một đối tượng bị lỗi (ví dụ: không mở được file hoặc không kết nối được Database), nó không thể trả về mã lỗi. Kết quả là đối tượng vẫn được tạo ra ở trạng thái lỗi hỏng — một đối tượng "xác sống" (**Zombie Object**)!

---

## 2. Giải Pháp Ngoại Lệ (Exceptions)

Cơ chế ngoại lệ giải quyết triệt để vấn đề:
- Khi một hàm gặp sự cố không thể tự giải quyết, nó **ném ngoại lệ (`throw`)**.
- Luồng thực thi lập tức dừng lại, ngăn chặn việc sử dụng dữ liệu rác.
- Ngoại lệ được chuyển ngược lên ngăn xếp cho tới khi gặp một khối xử lý phù hợp (`catch`).

```mermaid
flowchart TD
    Normal["Luồng Logic Chính (Thực thi thuận lợi)"]
    Normal -->|"Gặp lỗi chí mạng: b == 0"| Throw["throw std::runtime_error()"]
    Throw -->|"Nhảy vọt qua các lệnh tiếp theo"| Catch["Khối catch: Xử lý sự cố tập trung"]
```
"""

# 27.2
lessons["27_2-basic-exception-handling.md"] = """# 27.2 — Cơ Chế Xử Lý Ngoại Lệ Cơ Bản (try, throw, catch)

---

## 🎯 Mục Tiêu Bài Học
- Nắm vững 3 từ khóa nền tảng: **`throw`**, **`try`**, và **`catch`**.
- Hiểu luồng chuyển giao quyền điều khiển khi một ngoại lệ được kích hoạt.
- Thực hành bắt các ngoại lệ với nhiều kiểu dữ liệu khác nhau.

---

## 1. Cấu Trúc Khối `try - catch` Và Lệnh `throw`

Xử lý ngoại lệ trong C++ dựa trên bộ ba từ khóa:
1. **`throw`**: Dùng để ném ra một đối tượng ngoại lệ khi phát hiện sự cố.
2. **`try`**: Bao bọc một khối lệnh có thể phát sinh ngoại lệ.
3. **`catch`**: Bắt và xử lý ngoại lệ có kiểu dữ liệu tương ứng.

```cpp
#include <iostream>
#include <string_view>

double divide(double a, double b)
{
    if (b == 0.0)
    {
        // 1. Ném ngoại lệ kiểu const char*
        throw "Loi chia cho so 0!";
    }
    return a / b;
}

int main()
{
    std::cout << "Nhap hai so: ";
    double x{ 10.0 };
    double y{ 0.0 };

    // 2. Bao bọc mã nguồn rủi ro trong khối try
    try
    {
        double result = divide(x, y);
        // Dòng lệnh dưới đây SẼ BỊ BỎ QUA nếu có ngoại lệ ném ra!
        std::cout << "Ket qua: " << result << '\\n';
    }
    // 3. Bắt ngoại lệ kiểu const char*
    catch (const char* errorMessage)
    {
        std::cerr << "Phat hien su co: " << errorMessage << '\\n';
    }

    std::cout << "Chuong trinh tiep tuc thuc thi an toan!\\n";
    return 0;
}
```

### Kết quả xuất ra màn hình:
```text
Phat hien su co: Loi chia cho so 0!
Chuong trinh tiep tuc thuc thi an toan!
```

---

## 2. Luồng Điều Khiển Khi Ném Ngoại Lệ

1. Khi lệnh `throw` được thực thi, C++ **lập tức tạm dừng hàm hiện tại**.
2. Nó kiểm tra xem lệnh `throw` có nằm bên trong một khối `try` hay không.
3. Nếu có, nó so khớp kiểu của đối tượng được ném với danh sách các khối `catch` bên dưới theo thứ tự từ trên xuống dưới.
4. Khi tìm thấy khối `catch` phù hợp, luồng điều khiển nhảy thẳng vào khối đó. Sau khi khối `catch` chạy xong, chương trình tiếp tục chạy các lệnh bình thường phía sau khối `catch` đó!
"""

# 27.3
lessons["27_3-exceptions-functions-and-stack-unwinding.md"] = """# 27.3 — Ngoại Lệ, Hàm & Cơ Chế Cuộn Ngược Ngăn Xếp (Stack Unwinding)

---

## 🎯 Mục Tiêu Bài Học
- **TRỰC QUAN HÓA TOÀN BỘ CƠ CHẾ CUỘN NGƯỢC NGĂN XẾP (STACK UNWINDING) TRONG RAM**.
- Hiểu cách C++ tự động dọn dẹp biến cục bộ và gọi Destructor theo triết lý RAII khi ngoại lệ bay xuyên qua các tầng hàm.
- **CẠM BẪY SỐNG CÒN**: Con trỏ thô (Raw Pointer) bị rò rỉ bộ nhớ khi Stack Unwind và lý do bắt buộc dùng Smart Pointer.

---

## 1. Cơ Chế Stack Unwinding Là Gì?

Khi một ngoại lệ được ném ra từ một hàm ở rất sâu bên dưới cây gọi hàm (`main -> funcA -> funcB -> funcC`), nếu hàm hiện tại không có khối `try-catch`, C++ sẽ **thoát khỏi hàm đó và cuộn ngược lên hàm cha đã gọi nó**.

Quá trình này lặp lại liên tục ngược lên đỉnh ngăn xếp cho tới khi tìm thấy một khối `catch` phù hợp. Quá trình đó được gọi là **Cuộn ngược ngăn xếp (Stack Unwinding)**.

::: tip Sức Mạnh Vô Song Của RAII Trong Stack Unwinding
Mỗi khi C++ thoát khỏi một hàm trong quá trình cuộn ngược ngăn xếp, **tất cả các đối tượng cục bộ trong Stack Frame của hàm đó BẮT BUỘC ĐƯỢC GỌI DESTRUCTOR ĐỂ GIẢI PHÓNG TÀI NGUYÊN HOÀN TOÀN TỰ ĐỘNG!**
:::

---

## 2. Trực Quan Hóa Quá Trình Stack Unwinding Trong Bộ Nhớ RAM

```mermaid
sequenceDiagram
    participant Main as main() [Có khối try/catch]
    participant FuncA as funcA() [Không có catch]
    participant FuncB as funcB() [Không có catch]
    participant Throw as Nơi xảy ra lỗi

    Main->>FuncA: Gọi funcA() (Tạo stack frame A)
    FuncA->>FuncB: Gọi funcB() (Tạo stack frame B)
    FuncB->>Throw: Phát hiện lỗi! THROW EXCEPTION!
    Note over FuncB: 1. Hủy đối tượng cục bộ trong B (Destructor)<br/>2. Xóa Stack Frame của B
    Note over FuncA: 3. Unwind về A: Hủy đối tượng cục bộ trong A<br/>4. Xóa Stack Frame của A
    FuncA-->>Main: 5. Tìm thấy catch trong main()!
    Note over Main: 6. Thực thi khối catch, phục hồi tiến trình
```

---

## 3. Mã Nguồn Thực Nghiệm Chứng Minh Thứ Tự Hủy Biến

```cpp
#include <iostream>

class Tracker
{
private:
    std::string m_name;

public:
    Tracker(std::string_view name) : m_name{ name }
    {
        std::cout << " [Khoi tao] " << m_name << '\\n';
    }

    ~Tracker()
    {
        std::cout << " [Huy bo]   " << m_name << " (Tu dong don dep boi Stack Unwinding!)\\n";
    }
};

void funcC()
{
    Tracker tC{ "Bien cuc bo tai funcC" };
    std::cout << "funcC: Nem ngoai le!\\n";
    throw 404; // Nem ngoai le so nguyen
}

void funcB()
{
    Tracker tB{ "Bien cuc bo tai funcB" };
    funcC();
    std::cout << "Dong nay trong funcB KHONG BAO GIO duoc in!\\n";
}

void funcA()
{
    Tracker tA{ "Bien cuc bo tai funcA" };
    funcB();
}

int main()
{
    try
    {
        funcA();
    }
    catch (int errorCode)
    {
        std::cout << "-> main() da bat ngoai le ma: " << errorCode << '\\n';
    }

    return 0;
}
```

### Kết quả xuất ra:
```text
 [Khoi tao] Bien cuc bo tai funcA
 [Khoi tao] Bien cuc bo tai funcB
 [Khoi tao] Bien cuc bo tai funcC
funcC: Nem ngoai le!
 [Huy bo]   Bien cuc bo tai funcC (Tu dong don dep boi Stack Unwinding!)
 [Huy bo]   Bien cuc bo tai funcB (Tu dong don dep boi Stack Unwinding!)
 [Huy bo]   Bien cuc bo tai funcA (Tu dong don dep boi Stack Unwinding!)
-> main() da bat ngoai le ma: 404
```

---

## 4. Cạm Bẫy Sống Còn: Con Trỏ Thô & Rò Rỉ Bộ Nhớ (Memory Leak)

::: danger Cạm Bẫy Kinh Điển Của Lập Trình Viên C++ Cũ
Nếu bạn sử dụng **con trỏ thô (Raw Pointers)** và cấp phát Heap thủ công:
```cpp
void badFunction()
{
    int* data = new int[1000]; // Cấp phát Heap
    doSomethingRisky();        // NẾU HÀM NÀY NÉM NGOẠI LỆ...
    delete[] data;             // DÒNG NÀY SẼ BỊ BỎ QUA VĨNH VIỄN!
}
```
Khi `doSomethingRisky()` ném ngoại lệ, Stack Unwinding diễn ra: biến con trỏ `data` trên Stack bị xóa, nhưng **vùng nhớ 1000 số int trên Heap KHÔNG AI GIẢI PHÓNG** $\\rightarrow$ **RÒ RỈ BỘ NHỚ!**

**GIẢI PHÁP HIỆN ĐẠI**: Luôn sử dụng Smart Pointer (`std::unique_ptr<int[]> data = std::make_unique<int[]>(1000);`). Vì `unique_ptr` là một đối tượng có Destructor, nó sẽ tự động dọn dẹp Heap khi Stack Unwind!
:::
"""

# 27.4
lessons["27_4-uncaught-exceptions-catch-all-handlers.md"] = """# 27.4 — Ngoại Lệ Chưa Được Bắt & Trình Bắt Tất Cả `catch (...)`

---

## 🎯 Mục Tiêu Bài Học
- Hiểu số phận của chương trình khi một ngoại lệ không có khối `catch` nào khớp: **`std::terminate()`**.
- Sử dụng khối **Trình bắt tất cả (Catch-all handler: `catch (...)`)** để làm chốt chặn an toàn cuối cùng.
- Tùy chỉnh hàm xử lý khi sập chương trình với `std::set_terminate()`.

---

## 1. Ngoại Lệ Chưa Được Bắt (Uncaught Exception)

Nếu một ngoại lệ được ném ra mà cuộn ngược lên tận hàm `main()` vẫn không tìm thấy bất kỳ khối `catch` nào tương ứng, chương trình sẽ rơi vào trạng thái **Uncaught Exception**:
- Hệ thống runtime lập tức kích hoạt hàm **`std::terminate()`**.
- Hàm này mặc định sẽ gọi tiếp `std::abort()` để **hủy diệt tiến trình ngay lập tức (Crash)**.
- Khi bị crash bởi `std::terminate()`, trình biên dịch có thể **không bảo đảm thực hiện việc cuộn ngược ngăn xếp**, khiến các tài nguyên, file đang mở hoặc kết nối database bị đóng đột ngột mà không kịp lưu!

---

## 2. Khối Trình Bắt Tất Cả: `catch (...)`

Để ngăn chặn chương trình bị crash bất ngờ, C++ cung cấp cú pháp dấu ba chấm `...` trong mệnh đề `catch`, cho phép **bắt bất kỳ kiểu ngoại lệ nào**, bất kể đó là số nguyên, chuỗi, hay đối tượng ngoại lệ phức tạp:

```cpp
#include <iostream>

void riskyFunction()
{
    throw 404; // Ném một kiểu bất kỳ
}

int main()
{
    try
    {
        riskyFunction();
    }
    catch (double d)
    {
        std::cout << "Bat kieu double\\n";
    }
    // CHỐT CHẶN CUỐI CÙNG: Bắt tất cả mọi ngoại lệ còn lại!
    catch (...)
    {
        std::cerr << "Da bat mot ngoai le khong xac dinh! Ngan chan crash thanh cong.\\n";
    }

    return 0;
}
```

::: warning Vị Trí Của Khối `catch (...)`
Khối `catch (...)` **BẮT BUỘC PHẢI ĐẶT Ở VỊ TRÍ CUỐI CÙNG** trong danh sách các khối catch. Nếu bạn đặt nó lên đầu, nó sẽ nuốt chửng mọi ngoại lệ và khiến tất cả các khối `catch` cụ thể bên dưới trở thành mã chết (Dead code)!
:::
"""

# 27.5
lessons["27_5-exceptions-classes-and-inheritance.md"] = """# 27.5 — Ngoại Lệ, Lớp & Tính Kế Thừa (Exceptions and Inheritance)

---

## 🎯 Mục Tiêu Bài Học
- Sử dụng thư viện chuẩn `<stdexcept>` và lớp nền tảng **`std::exception`**.
- **CẠM BẪY CHÍ MẠNG**: Bắt ngoại lệ bằng giá trị gây Object Slicing. Bắt buộc luôn dùng tham chiếu hằng: `catch (const std::exception& e)`.
- Quy tắc thứ tự khối `catch` khi có kế thừa: **Lớp con bắt trước, Lớp cha bắt sau**.

---

## 1. Hệ Thống Phân Cấp Ngoại Lệ Trong Thư Viện Chuẩn STL

Trong thực tế, chúng ta không ném các kiểu nguyên thủy (`int`, `char*`) mà luôn sử dụng các lớp ngoại lệ kế thừa từ **`std::exception`** (trong header `<stdexcept>`):

```mermaid
classDiagram
    class exception {
        +what() const char*
    }
    class runtime_error
    class logic_error
    class out_of_range
    class invalid_argument

    exception <|-- runtime_error
    exception <|-- logic_error
    logic_error <|-- out_of_range
    logic_error <|-- invalid_argument
```

Hàm ảo `virtual const char* what() const noexcept;` trả về chuỗi thông báo lỗi chi tiết.

---

## 2. Cạm Bẫy Slicing: Luôn Bắt Ngoại Lệ Bằng Tham Chiếu Hằng

::: danger Cạm Bẫy Phổ Biến (Object Slicing Khi Catch)
Nếu bạn bắt ngoại lệ theo giá trị:
```cpp
catch (std::exception e) // NGUY HIỂM: Truyền tham trị!
{
    std::cout << e.what(); // BỊ CẮT GỌT! Mất thông tin của lớp con!
}
```
Toàn bộ phần thông tin chuyên biệt của ngoại lệ con (ví dụ `out_of_range`) sẽ bị cắt phăng đi do hiện tượng **Object Slicing**!

**QUY TẮC BẤT BIẾN**: Luôn luôn bắt ngoại lệ bằng **Tham Chiếu Hằng (`const Base&`)**:
```cpp
catch (const std::exception& e) // CHUẨN XÁC: Bảo toàn đa hình qua hàm what()!
{
    std::cout << e.what();
}
```
:::

---

## 3. Thứ Tự Bắt Ngoại Lệ Kế Thừa

Quy tắc so khớp của C++ là: Khối `catch` nào nằm trước sẽ được kiểm tra trước. Nếu một con trỏ hoặc tham chiếu lớp cha nằm ở trên, nó sẽ bắt luôn cả lớp con!

```cpp
#include <iostream>
#include <stdexcept>

int main()
{
    try
    {
        throw std::out_of_range{ "Chi so mang vuot qua gioi han!" };
    }
    // 1. KHỐI CON PHẢI ĐẶT TRƯỚC:
    catch (const std::out_of_range& e)
    {
        std::cerr << "Bat cu the out_of_range: " << e.what() << '\\n';
    }
    // 2. KHỐI CHA ĐẶT SAU:
    catch (const std::exception& e)
    {
        std::cerr << "Bat tong quat std::exception: " << e.what() << '\\n';
    }

    return 0;
}
```
"""

# 27.6
lessons["27_6-rethrowing-exceptions.md"] = """# 27.6 — Ném Lại Ngoại Lệ (Rethrowing Exceptions)

---

## 🎯 Mục Tiêu Bài Học
- Hiểu mục đích của việc ném lại ngoại lệ (**Rethrow**): Khi một hàm chỉ muốn ghi log sự cố rồi chuyển tiếp lỗi lên cấp cao hơn xử lý.
- Phân biệt sự khác nhau sống còn giữa cú pháp **`throw;`** và **`throw e;`**.
- Tránh cạm bẫy cắt gọt đối tượng (Object Slicing) khi ném lại ngoại lệ.

---

## 1. Khi Nào Cần Rethrow Ngoại Lệ?

Đôi khi một hàm ở tầng giữa bắt được ngoại lệ, nó cần làm một số thao tác cục bộ (ví dụ: ghi log lỗi vào file, giải phóng tài nguyên tạm thời), nhưng nó **không thể khắc phục hoàn toàn sự cố**. Lúc này nó cần chuyển tiếp chính ngoại lệ đó lên tầng trên bằng cách **ném lại (Rethrow)**.

---

## 2. Cạm Bẫy Chết Người: `throw;` vs `throw e;`

```cpp
#include <iostream>
#include <stdexcept>

class CustomDerivedException : public std::runtime_error
{
public:
    CustomDerivedException() : std::runtime_error{ "Loi tuy bien dac biet cua Derived!" } {}
};

void handleProcess()
{
    try
    {
        throw CustomDerivedException{};
    }
    catch (const std::exception& e)
    {
        std::cout << "Ghi log su co tai handleProcess...\\n";

        // CÁCH 1 (SAI LẦM): throw e;
        // throw e; // NGUY HIỂM: Tạo ra bản sao mới kiểu std::exception -> GÂY OBJECT SLICING!

        // CÁCH 2 (ĐÚNG CHUẨN): throw;
        throw; // Ném lại CHÍNH XÁC đối tượng ngoại lệ ban đầu, giữ nguyên kiểu Derived!
    }
}

int main()
{
    try
    {
        handleProcess();
    }
    catch (const CustomDerivedException& e)
    {
        std::cout << "main() bat dung kieu CustomDerivedException: " << e.what() << '\\n';
    }
    catch (const std::exception& e)
    {
        std::cout << "main() bat std::exception (neu bi slicing se roi vao day!)\\n";
    }

    return 0;
}
```

::: tip Quy Tắc Vàng
Để ném lại ngoại lệ đang bắt, **LUÔN LUÔN DÙNG TỪ KHÓA `throw;` ĐỨNG ĐỘC LẬP KHÔNG CÓ THAM SỐ!**
:::
"""

# 27.7
lessons["27_7-function-try-blocks.md"] = """# 27.7 — Khối Try Của Hàm (Function Try Blocks)

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
        std::cout << "Khoi tao Container thanh cong!\\n";
    }
    catch (const std::exception& e)
    {
        std::cerr << "Container bat duoc loi tu Member: " << e.what() << '\\n';
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
        std::cerr << "main() bat ngoai le: " << e.what() << '\\n';
    }
    return 0;
}
```
"""

# 27.8
lessons["27_8-exception-dangers-and-downsides.md"] = """# 27.8 — Cạm Bẫy Sống Còn: Ngoại Lệ Trong Destructor & Mặt Trái Của Ngoại Lệ

---

## 🎯 Mục Tiêu Bài Học
- **CẠM BẪY CHÍ MẠNG BẬC NHẤT C++: NÉM NGOẠI LỆ TỪ DESTRUCTOR DẪN ĐẾN SẬP CHƯƠNG TRÌNH NGAY LẬP TỨC!**
- Hiểu quy định mặc định từ C++11: Mọi Destructor đều có thuộc tính **`noexcept(true)`**.
- Đánh giá mặt trái của ngoại lệ: Phình to kích thước file nhị phân (Unwind Tables) và chi phí khi xảy ra lỗi.

---

## 1. Cạm Bẫy Chí Mạng: Ngoại Lệ Trong Destructor

Hãy hình dung kịch bản kinh hoàng sau:
1. Hàm `foo()` phát hiện lỗi và ném ra Ngoại lệ số 1.
2. Trình biên dịch bắt đầu quá trình **Stack Unwinding** để dọn dẹp các biến cục bộ trong `foo()`.
3. Trong khi đang dọn dẹp, Destructor của một đối tượng cục bộ được gọi.
4. **Bên trong Destructor đó lại ném ra Ngoại lệ số 2!**

```mermaid
flowchart TD
    E1["Ngoại lệ 1 đang bay... (Stack Unwinding)"] --> Unwind["Gọi Destructor biến cục bộ"]
    Unwind -->|"Destructor ném tiếp Ngoại lệ 2!"| Crash["HAI NGOẠI LỆ ĐỒNG THỜI!\nstd::terminate() ĐƯỢC GỌI NGAY LẬP TỨC!\nCHƯƠNG TRÌNH CRASH CHÍ MẠNG!"]
```

::: danger Quy Tắc Bất Biến Của Chuẩn ISO C++
C++ không cho phép tồn tại đồng thời 2 ngoại lệ đang được xử lý trong cùng một luồng. Nếu một Destructor ném ra ngoại lệ trong khi Stack Unwind đang diễn ra, C++ sẽ kích hoạt ngay hàm **`std::terminate()`** để bắn sập chương trình ngay lập tức!
:::

Vì lý do này, từ C++11 trở đi, **tất cả Destructor mặc định được ngầm định coi là `noexcept`**. Nếu một Destructor muốn ném ngoại lệ, nó bắt buộc phải tự bắt và giải quyết triệt để bên trong chính nó, không bao giờ được để ngoại lệ thoát ra ngoài!

---

## 2. Chi Phí Hiệu Năng Của Ngoại Lệ (Zero-Cost Exceptions)

Các trình biên dịch hiện đại (GCC/Clang/MSVC) sử dụng mô hình **Table-driven Zero-Cost Exceptions**:
- **Khi chương trình chạy bình thường (Happy path)**: Tốc độ thực thi nhanh ngang bằng mã không dùng ngoại lệ (Zero runtime overhead), không tốn chu kỳ CPU để kiểm tra cờ lỗi.
- **Mặt trái**: 
  - Kích thước tệp thực thi (`.exe` / ELF binary) tăng từ 15% - 30% do phải chứa các bảng tra cứu cấu trúc cuộn ngược ngăn xếp (**Exception Handling Tables / `.eh_frame`**).
  - Khi có lỗi thực sự xảy ra (Unhappy path), việc tra cứu bảng và cuộn ngược ngăn xếp diễn ra rất chậm, tốn hàng ngàn chu kỳ CPU. Do đó, **ngoại lệ chỉ dành cho các tình huống thực sự bất thường (exceptional), không dùng để điều khiển luồng logic thông thường!**
"""

# 27.9
lessons["27_9-exception-specifications-and-noexcept.md"] = """# 27.9 — Từ Khóa `noexcept` Trong C++11

---

## 🎯 Mục Tiêu Bài Học
- Hiểu ý nghĩa của chỉ định đặc tả **`noexcept`** trong C++11.
- Nắm vững toán tử kiểm tra tại compile-time: `noexcept(biểu_thức)`.
- Hiểu tại sao `noexcept` là điều kiện tiên quyết để các container như `std::vector` kích hoạt Move Semantics siêu tốc.

---

## 1. Từ Khóa `noexcept` Là Gì?

Trong C++11, từ khóa `noexcept` được dùng để thông báo cho trình biên dịch và lập trình viên biết rằng: **Hàm này đảm bảo 100% sẽ không bao giờ ném ra bất kỳ ngoại lệ nào**.

```cpp
void doSomethingFast() noexcept // Cam ket khong nem ngoai le
{
    // ...
}
```

Nếu một hàm được đánh dấu `noexcept` mà bên trong nó vẫn ném ra ngoại lệ mà không tự bắt, `std::terminate()` sẽ được gọi ngay lập tức để ngắt chương trình.

---

## 2. Lợi Ích Khổng Lồ Của `noexcept` Với Hiệu Năng

Khi trình biên dịch biết một hàm là `noexcept`, nó có thể áp dụng các tối ưu hóa cực kỳ mạnh tay:
1. Compiler không cần sinh các mã bảo vệ cuộn ngược ngăn xếp cho hàm đó, giúp kích thước code nhỏ gọn hơn.
2. **Kích hoạt Move Semantics trong Thư viện chuẩn**:
   Khi một `std::vector` cần mở rộng dung lượng, nó phải chuyển các phần tử từ vùng nhớ cũ sang vùng nhớ mới. 
   - Nếu Move Constructor của đối tượng là `noexcept`, vector sẽ dùng **Move** (nhanh gấp hàng trăm lần).
   - Nếu Move Constructor có thể ném ngoại lệ, vector sẽ buộc phải chuyển về dùng **Copy** chậm chạp để đảm bảo an toàn dữ liệu!
"""

# 27.10
lessons["27_10-stdmove_if_noexcept.md"] = """# 27.10 — `std::move_if_noexcept` & Đảm Bảo An Toàn Ngoại Lệ

---

## 🎯 Mục Tiêu Bài Học
- Hiểu 4 cấp độ **Đảm bảo an toàn ngoại lệ (Exception Safety Guarantees)**.
- Phân tích cơ chế hoạt động của hàm tiện ích `std::move_if_noexcept` trong C++11.
- Hiểu cách thức `std::vector` tự động cân bằng giữa hiệu năng tối đa và tính toàn vẹn dữ liệu.

---

## 1. Bốn Cấp Độ Đảm Bảo An Toàn Ngoại Lệ

1. **No-throw / Nothrow guarantee**: Hàm đảm bảo không bao giờ ném ngoại lệ (đánh dấu `noexcept`).
2. **Strong guarantee (Đảm bảo mạnh)**: Nếu có ngoại lệ xảy ra, trạng thái toàn bộ chương trình được giữ nguyên như trước khi gọi hàm (Tương tự như cơ chế *Rollback* của giao dịch Database).
3. **Basic guarantee (Đảm bảo cơ bản)**: Không bị rò rỉ bộ nhớ, nhưng dữ liệu có thể bị biến đổi về một trạng thái hợp lệ nào đó.
4. **No guarantee (Không đảm bảo)**: Nếu xảy ra ngoại lệ, rò rỉ tài nguyên hoặc dữ liệu bị phá hủy hoàn toàn.

---

## 2. Cơ Chế Hoạt Động Của `std::move_if_noexcept`

Để đạt được **Strong Exception Guarantee**, hàm `std::move_if_noexcept(x)` hoạt động thông minh:
- Nếu kiểu của `x` có Move Constructor được đánh dấu là `noexcept`: Nó trả về một rvalue reference (`std::move`), kích hoạt cơ chế di chuyển siêu tốc.
- Ngược lại, nếu Move Constructor có nguy cơ ném lỗi: Nó trả về một lvalue reference thông thường, ép trình biên dịch phải dùng **Sao chép (Copy)** an toàn!

```cpp
#include <iostream>
#include <utility> // std::move_if_noexcept

class SafeMove
{
public:
    SafeMove() = default;
    SafeMove(const SafeMove&) { std::cout << "Copy SafeMove\\n"; }
    // Khẳng định noexcept: Kích hoạt Move!
    SafeMove(SafeMove&&) noexcept { std::cout << "Move SafeMove (Sieu toc!)\\n"; }
};

class RiskyMove
{
public:
    RiskyMove() = default;
    RiskyMove(const RiskyMove&) { std::cout << "Copy RiskyMove (An toan)\\n"; }
    // Không có noexcept: Sẽ bị hạ cấp về Copy!
    RiskyMove(RiskyMove&&) { std::cout << "Move RiskyMove\\n"; }
};

int main()
{
    SafeMove s;
    RiskyMove r;

    std::cout << "Goi move_if_noexcept voi SafeMove:\\n";
    SafeMove s2 = std::move_if_noexcept(s); // In ra: Move SafeMove

    std::cout << "\\nGoi move_if_noexcept voi RiskyMove:\\n";
    RiskyMove r2 = std::move_if_noexcept(r); // In ra: Copy RiskyMove (Tránh rủi ro ném lỗi)

    return 0;
}
```
"""

# 27.x
lessons["27_x-chapter-27-summary-and-quiz.md"] = """# 27.x — Tổng Kết Chương 27 & Bài Kiểm Tra Toàn Diện

---

## 🎯 Mục Tiêu
- Hệ thống hóa toàn bộ bức tranh về Xử Lý Ngoại Lệ trong C++.
- Vượt qua bài kiểm tra trắc nghiệm và thử thách lập trình hệ thống Tài Khoản Ngân Hàng an toàn giao dịch.

---

## 1. Bảng Tóm Tắt Các Quy Tắc Ngoại Lệ Sống Còn

1. **Tách rời xử lý lỗi**: Dùng `throw` để báo lỗi, `try-catch` để xử lý tập trung.
2. **Stack Unwinding**: Biến cục bộ được hủy tự động, nhưng con trỏ thô sẽ rò rỉ nếu không dùng Smart Pointer.
3. **Bắt bằng tham chiếu**: Luôn dùng `catch (const std::exception& e)` để tránh Object Slicing.
4. **Thứ tự khối catch**: Lớp dẫn xuất con bắt trước, lớp cơ sở cha bắt sau.
5. **Ném lại ngoại lệ**: Luôn dùng `throw;` độc lập để bảo toàn kiểu đối tượng gốc.
6. **Destructor an toàn**: Tuyệt đối **KHÔNG BAO GIỜ** ném ngoại lệ từ Destructor!

---

## 2. Bài Tập Thực Chiến: Hệ Thống Giao Dịch Ngân Hàng (Transactional Bank)

### Yêu cầu:
Xây dựng lớp `BankAccount` với:
- Số tài khoản (`std::string`), Số dư (`double`).
- Lớp ngoại lệ tự tạo `InsufficientFundsException` kế thừa từ `std::runtime_error`.
- Phương thức `withdraw(double amount)`: Nếu số tiền rút lớn hơn số dư, ném ngoại lệ `InsufficientFundsException`.
- Hàm thực hiện giao dịch chuyển tiền giữa 2 tài khoản đảm bảo an toàn ngoại lệ (Nếu rút tiền từ tài khoản nguồn thất bại, tài khoản đích không bị ảnh hưởng).

<details>
<summary><b>Xem lời giải mã nguồn C++ hoàn chỉnh</b></summary>

```cpp
#include <iostream>
#include <string>
#include <stdexcept>

// Lớp ngoại lệ chuyên biệt
class InsufficientFundsException : public std::runtime_error
{
private:
    double m_attemptedAmount;
    double m_currentBalance;

public:
    InsufficientFundsException(double attempted, double balance)
        : std::runtime_error{ "Loi: So du khong du de thuc hien giao dich!" }
        , m_attemptedAmount{ attempted }
        , m_currentBalance{ balance }
    {
    }

    double getAttempted() const { return m_attemptedAmount; }
    double getBalance() const { return m_currentBalance; }
};

class BankAccount
{
private:
    std::string m_accountNumber;
    double m_balance{ 0.0 };

public:
    BankAccount(std::string_view accNum, double initialBalance)
        : m_accountNumber{ accNum }, m_balance{ initialBalance }
    {
        if (initialBalance < 0.0)
            throw std::invalid_argument{ "So du khoi tao khong duoc am!" };
    }

    void deposit(double amount)
    {
        if (amount <= 0.0)
            throw std::invalid_argument{ "So tien nap phai lon hon 0!" };
        m_balance += amount;
    }

    void withdraw(double amount)
    {
        if (amount <= 0.0)
            throw std::invalid_argument{ "So tien rut phai lon hon 0!" };
        if (amount > m_balance)
            throw InsufficientFundsException{ amount, m_balance };

        m_balance -= amount;
    }

    double getBalance() const { return m_balance; }
    const std::string& getAccountNumber() const { return m_accountNumber; }
};

// Hàm chuyển tiền bảo đảm an toàn giao dịch
void transferMoney(BankAccount& from, BankAccount& to, double amount)
{
    std::cout << "Dang chuyen " << amount << "$ tu " << from.getAccountNumber() 
              << " sang " << to.getAccountNumber() << "...\\n";

    // 1. Rút từ tài khoản nguồn trước (nếu lỗi sẽ ném ngoại lệ và dừng tại đây)
    from.withdraw(amount);

    // 2. Nạp vào tài khoản đích
    to.deposit(amount);

    std::cout << "-> Giao dich thanh cong hoan hao!\\n";
}

int main()
{
    BankAccount accA{ "ACC_VIETCOMBANK_01", 1000.0 };
    BankAccount accB{ "ACC_TECHCOMBANK_02", 200.0 };

    try
    {
        // Giao dịch 1: Hợp lệ
        transferMoney(accA, accB, 300.0);

        // Giao dịch 2: Rút vượt quá số dư
        transferMoney(accA, accB, 1500.0);
    }
    catch (const InsufficientFundsException& e)
    {
        std::cerr << "[NGOAI LE NGAN HANG]: " << e.what() << '\\n';
        std::cerr << " -> So tien yeu cau rut: " << e.getAttempted() << "$\\n";
        std::cerr << " -> So du hien tai:      " << e.getBalance() << "$\\n";
    }
    catch (const std::exception& e)
    {
        std::cerr << "[NGOAI LE HE THONG]: " << e.what() << '\\n';
    }

    std::cout << "\\nSo du cuoi cung cua " << accA.getAccountNumber() << ": " << accA.getBalance() << "$\\n";
    std::cout << "So du cuoi cung cua " << accB.getAccountNumber() << ": " << accB.getBalance() << "$\\n";

    return 0;
}
```
</details>
"""

for fname, content in lessons.items():
    fpath = os.path.join(OUT_DIR, fname)
    with open(fpath, "w", encoding="utf-8") as f:
        f.write(content.strip() + "\n")
    print(f" -> Đã tạo ch29: {fname}")

print("HOÀN THÀNH CHƯƠNG 27 (11 bài trong docs/vi/ch29)")
