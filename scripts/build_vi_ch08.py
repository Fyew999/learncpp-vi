#!/usr/bin/env python3
"""
Generator for Chapter 07: Scope, Duration, and Linkage (15 lessons)
Location: docs/vi/ch08/
"""

import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DEST_DIR = os.path.join(BASE_DIR, "docs", "vi", "ch08")
os.makedirs(DEST_DIR, exist_ok=True)

def save_lesson(filename, content):
    path = os.path.join(DEST_DIR, filename)
    with open(path, "w", encoding="utf-8") as f:
        f.write(content.strip() + "\n")
    print(f"✅ Generated: docs/vi/ch08/{filename}")

# ==============================================================================
# Lesson 7.1
# ==============================================================================
lesson_7_1 = r"""# 7.1 — Câu Lệnh Phức Hợp: Khối Mã (Compound Statements / Blocks)

---

## 🎯 Mục Tiêu Bài Học
- Hiểu định nghĩa câu lệnh phức hợp (**Compound Statement**) hay còn gọi là **Khối mã (Block)**.
- Phân biệt câu lệnh đơn và khối lệnh được bao bọc bởi cặp ngoặc nhọn `{}`.
- Nắm vững khái niệm Khối lồng nhau (Nested Blocks).
- Hiểu cách các khối mã tạo ra ranh giới phạm vi (**Scope**) và điều khiển vòng đời biến trong ngăn xếp (Stack).

---

## 1. Khối Mã (Block) Là Gì?

Một **câu lệnh phức hợp (Compound Statement)**, thường được gọi ngắn gọn là một **khối mã (Block)**, là một nhóm gồm không hoặc nhiều câu lệnh được đặt bên trong cặp dấu ngoặc nhọn `{}`. Trình biên dịch C++ coi toàn bộ khối mã này như **một câu lệnh đơn nhất**.

```cpp
#include <iostream>

int main()
{ // Bắt đầu khối mã của hàm main
    std::cout << "Xin chao!\n";
    std::cout << "Tam biet!\n";
    return 0;
} // Kết thúc khối mã của hàm main
```

Lưu ý: Không có dấu chấm phẩy `;` ở sau dấu ngoặc nhọn đóng `}` của một khối mã thông thường.

---

## 2. Khối Mã Lồng Nhau (Nested Blocks)

Một khối mã có thể được đặt bên trong một khối mã khác. Khối bao bọc bên ngoài được gọi là **Outer Block**, khối nằm bên trong được gọi là **Inner Block** hoặc **Nested Block**:

```cpp
#include <iostream>

int main() // Outer block
{
    std::cout << "Bat dau outer block\n";

    { // Inner block 1
        int x { 10 };
        std::cout << "Inner block 1: x = " << x << '\n';
    } // x bi tieu huy tai day!

    { // Inner block 2
        int y { 20 };
        std::cout << "Inner block 2: y = " << y << '\n';
    } // y bi tieu huy tai day!

    std::cout << "Ket thuc outer block\n";
    return 0;
}
```

```mermaid
flowchart TD
    subgraph Outer ["Outer Block: main()"]
        O1["std::cout << Bat dau"]
        subgraph Inner1 ["Inner Block 1"]
            I1["int x = 10;"]
            I2["In x"]
            I3["x bị hủy ở cuối scope!"]
        end
        subgraph Inner2 ["Inner Block 2"]
            J1["int y = 20;"]
            J2["In y"]
            J3["y bị hủy ở cuối scope!"]
        end
        O2["std::cout << Ket thuc"]
    end
    O1 --> Inner1 --> Inner2 --> O2
```

---

## 3. Tác Động Của Khối Mã Lên Vòng Đời Biến Số

Một biến được khai báo bên trong một khối mã chỉ tồn tại từ điểm nó được khai báo cho đến dấu ngoặc nhọn đóng `}` của khối mã đó:
- **Phạm vi (Scope)**: Biến chỉ có thể được truy cập bên trong khối mã chứa nó (Block Scope).
- **Vòng đời (Lifetime / Duration)**: Biến được cấp phát trên Stack khi thực thi đến dòng khai báo, và **tự động bị giải phóng (destroyed)** ngay khi luồng chạy vượt qua dấu `}`.

::: warning ⚠️ Cạm Bẫy: Cố Gắng Truy Cập Biến Ngoài Scope
```cpp
int main()
{
    {
        int secret { 42 };
    }

    std::cout << secret; // 💥 LỖI BIÊN DỊCH: 'secret' was not declared in this scope!
    return 0;
}
```
:::

---

## 4. Thực Hành Tốt Nhất (Best Practices)

::: tip 💡 Lời Khuyên Chuyên Gia
1. **Luôn sử dụng khối mã `{}` cho các cấu trúc điều khiển**:
   Dù câu lệnh `if`, `for`, `while` chỉ có 1 dòng lệnh duy nhất, hãy luôn bọc nó trong cặp ngoặc `{}`. Điều này giúp ngăn ngừa 100% các lỗi nghiêm trọng kiểu *Apple Goto Fail bug* khi bổ sung thêm code sau này.
2. **Tận dụng khối mã để giải phóng tài nguyên sớm (RAII)**:
   Nếu bạn có một tài nguyên chiếm nhiều RAM hoặc một khóa đồng bộ luồng (Mutex lock), việc bọc nó trong một khối mã riêng biệt `{ ... }` sẽ khiến tài nguyên tự động được giải phóng ngay khi ra khỏi khối, giải tỏa bộ nhớ sớm cho hệ thống.
:::

---

## 📝 Hệ Thống Quiz & Bài Tập Tự Luyện

### Câu hỏi 1:
Đoạn mã sau có biên dịch thành công không? Nếu có, nó in ra gì?
```cpp
int main()
{
    int a { 5 };
    {
        int b { 10 };
        a = a + b;
    }
    std::cout << a;
    return 0;
}
```
::: details [Xem lời giải]
Biên dịch thành công!  
Khối bên trong (Inner block) có thể nhìn thấy và truy cập hợp lệ các biến của khối bên ngoài (Outer block). Biến `a` được cộng thêm 10 thành 15. Sau khi ra khỏi inner block, biến `b` bị hủy nhưng `a` vẫn tồn tại với giá trị mới. In ra màn hình: `15`.
:::
"""
save_lesson("7_1-compound-statements-blocks.md", lesson_7_1)

# ==============================================================================
# Lesson 7.2
# ==============================================================================
lesson_7_2 = r"""# 7.2 — Không Gian Tên Tự Định Nghĩa và Toán Tử Phân Giải Phạm Vi (User-Defined Namespaces)

---

## 🎯 Mục Tiêu Bài Học
- Hiểu vấn đề **Xung đột tên (Naming Collisions)** trong các dự án C++ lớn hoặc khi tích hợp thư viện bên thứ ba.
- Cách định nghĩa không gian tên riêng bằng từ khóa `namespace`.
- Sử dụng **Toán tử phân giải phạm vi (Scope Resolution Operator `::`)**.
- Phân biệt toán tử `::` không tên (Global Scope) và `::` có tiền tố namespace.
- Nắm vững khái niệm Không gian tên lồng nhau (Nested Namespaces) và cú pháp C++17.

---

## 1. Xung Đột Tên (Naming Collisions) Là Gì?

Khi một chương trình C++ phát triển với hàng nghìn tệp và liên kết nhiều thư viện khác nhau, việc hai lập trình viên (hoặc hai thư viện) vô tình đặt trùng tên hàm, biến hoặc class là điều không thể tránh khỏi:

```cpp
// Thu vien A:
void processData() { /* ... */ }

// Thu vien B:
void processData() { /* ... */ }
```

Khi tệp mã nguồn của bạn bao gồm cả hai thư viện, trình biên dịch sẽ báo lỗi:
`error: redefinition of 'void processData()'`!

Để giải quyết vấn đề sống còn này, chuẩn C++ cung cấp **Không gian tên (Namespace)**.

```mermaid
flowchart TD
    subgraph GlobalNamespace ["Toàn Cục (Global Scope)"]
        subgraph NS_A ["namespace AudioLib"]
            A1["init()"]
            A2["play()"]
        end
        subgraph NS_P ["namespace PhysicsLib"]
            P1["init()"]
            P2["update()"]
        end
    end
    App["Chương Trình Chính"] -->|Gọi AudioLib::init()| A1
    App -->|Gọi PhysicsLib::init()| P1
```

---

## 2. Định Nghĩa Không Gian Tên (User-Defined Namespace)

Bạn có thể tự định nghĩa một không gian tên bằng từ khóa `namespace`:

```cpp
#include <iostream>

namespace Foo
{
    // Tất cả các định danh bên trong đều thuộc phạm vi Foo
    int doSomething(int x, int y)
    {
        return x + y;
    }
}

namespace Goo
{
    int doSomething(int x, int y)
    {
        return x - y;
    }
}

int main()
{
    // Dùng toán tử phân giải phạm vi :: để chỉ định rõ namespace
    std::cout << Foo::doSomething(4, 3) << '\n'; // In ra 7
    std::cout << Goo::doSomething(4, 3) << '\n'; // In ra 1
    return 0;
}
```

---

## 3. Toán Tử Phân Giải Phạm Vi Toàn Cục (`::`)

Nếu bạn đặt toán tử `::` đứng trước một tên hàm hoặc biến mà **không có tên namespace nào phía trước**, nó báo cho trình biên dịch tìm kiếm định danh đó ở **Phạm vi toàn cục (Global Scope)**:

```cpp
#include <iostream>

int val { 100 }; // Biến toàn cục

int main()
{
    int val { 20 }; // Biến cục bộ trong main

    std::cout << val << '\n';   // In ra biến cục bộ: 20
    std::cout << ::val << '\n'; // Sử dụng :: để truy cập biến toàn cục: 100
    return 0;
}
```

---

## 4. Không Gian Tên Lồng Nhau (Nested Namespaces) và C++17

Một namespace có thể chứa các namespace con bên trong để phân cấp module:

```cpp
// Cú pháp cổ điển (trước C++17):
namespace GameEngine
{
    namespace Graphics
    {
        namespace Rendering
        {
            void renderFrame();
        }
    }
}

// 🚀 Cú pháp hiện đại từ C++17:
namespace GameEngine::Graphics::Rendering
{
    void renderFrame()
    {
        std::cout << "Rendering frame...\n";
    }
}
```

Bạn cũng có thể tạo **Bí danh không gian tên (Namespace Alias)** để rút ngắn các tên dài:
```cpp
namespace Render = GameEngine::Graphics::Rendering;

int main()
{
    Render::renderFrame(); // Siêu ngắn gọn!
}
```

---

## 📝 Hệ Thống Quiz & Bài Tập Tự Luyện

### Câu hỏi 1:
Có thể phân tách phần thân của cùng một namespace thành nhiều khối mã khác nhau hoặc nằm ở nhiều tệp header/source khác nhau được không?
::: details [Xem lời giải]
**HOÀN TOÀN ĐƯỢC!** Không gian tên trong C++ có tính chất "Mở" (Open-ended). Bạn có thể viết `namespace Foo { int x; }` ở tệp 1, và `namespace Foo { int y; }` ở tệp 2. Trình biên dịch sẽ tự động gộp tất cả các khai báo này vào chung không gian tên `Foo`. Thư viện chuẩn `std` cũng được xây dựng dựa trên nguyên lý này ở hàng trăm tệp header khác nhau (`<iostream>`, `<vector>`, `<string>`, v.v.).
:::
"""
save_lesson("7_2-user-defined-namespaces-and-the-scope-resolution-operator.md", lesson_7_2)

# ==============================================================================
# Lesson 7.3
# ==============================================================================
lesson_7_3 = r"""# 7.3 — Biến Cục Bộ: Phạm Vi và Vòng Đời Tự Động (Local Variables)

---

## 🎯 Mục Tiêu Bài Học
- Nắm vững định nghĩa **Biến cục bộ (Local Variables)** và tham số hàm.
- Hiểu rõ **Phạm vi khối mã (Block Scope)**: Thời điểm biến bắt đầu nhìn thấy và biến mất.
- Hiểu cơ chế **Vòng đời tự động (Automatic Storage Duration)** trên vùng nhớ Stack.
- Nguyên tắc vàng: Khai báo biến càng gần nơi sử dụng đầu tiên càng tốt (Declare near first use).

---

## 1. Biến Cục Bộ Có Block Scope

Một biến được định nghĩa bên trong một hàm (bao gồm cả các tham số của hàm) hoặc bên trong một khối mã `{}` được gọi là **Biến cục bộ (Local variable)**.

```cpp
void printValue(int x) // x là biến cục bộ (tham số) của hàm printValue
{
    int y { 10 };      // y là biến cục bộ
    std::cout << x + y << '\n';
} // x và y kết thúc phạm vi (out of scope) tại đây
```

Đặc điểm phạm vi:
- **Block Scope (hoặc Local Scope)**: Biến chỉ có thể nhìn thấy và truy cập được từ dòng nó được định nghĩa cho đến dấu ngoặc nhọn đóng `}` của khối chứa nó.
- Mã nguồn nằm bên ngoài khối hoàn toàn không biết đến sự tồn tại của biến đó.

---

## 2. Vòng Đời Tự Động (Automatic Storage Duration)

**Vòng đời (Lifetime / Duration)** là khoảng thời gian mà một đối tượng thực sự tồn tại trong bộ nhớ RAM của máy tính.

Biến cục bộ có thời gian lưu trữ tự động (**Automatic Duration**):
1. **Khởi tạo**: Biến được cấp phát trên Stack Frame của hàm khi luồng thực thi chạy tới câu lệnh định nghĩa.
2. **Tiêu hủy**: Khi luồng thực thi rời khỏi khối mã (chạm dấu `}`), biến sẽ được **tự động tiêu hủy (destroyed)**: vùng nhớ trên Stack được thu hồi, và hàm hủy (Destructor) của đối tượng được gọi nếu có.

```mermaid
sequenceDiagram
    autonumber
    participant Thread as Luồng Thực Thi
    participant Stack as Ngăn Xếp (Stack Memory)
    
    Thread->>Stack: Vào hàm -> Đẩy Stack Frame
    Thread->>Stack: Chạy đến 'int a = 5' -> Cấp phát 4 bytes cho a
    Thread->>Stack: Vào inner block -> Chạy 'int b = 10' -> Cấp phát 4 bytes cho b
    Note over Thread,Stack: Rời inner block '}'
    Thread->>Stack: Tiêu hủy b -> Thu hồi 4 bytes của b!
    Note over Thread,Stack: Rời hàm '}'
    Thread->>Stack: Tiêu hủy a -> Thu hồi toàn bộ Stack Frame!
```

---

## 3. Cạm Bẫy Thực Chiến: Tham Chiếu / Con Trỏ Lơ Lửng (Dangling Pointer)

::: danger ⚠️ Cực Kỳ Nguy Hiểm: Trả Về Con Trỏ / Tham Chiếu Tới Biến Cục Bộ!
Vì biến cục bộ bị tiêu hủy ngay khi ra khỏi hàm, việc trả về địa chỉ hoặc tham chiếu của nó là một lỗi thảm họa:

```cpp
int* getDanglingPointer()
{
    int val { 100 };
    return &val; // 💥 CẢNH BÁO: val sẽ bị hủy ngay lập tức khi hàm return!
}

int main()
{
    int* ptr = getDanglingPointer();
    // ptr đang trỏ vào vùng nhớ rác đã bị thu hồi (Dangling pointer)!
    std::cout << *ptr << '\n'; // ⚠️ UNDEFINED BEHAVIOR!
}
```
:::

---

## 4. Thực Hành Tốt Nhất: Khai Báo Biến Càng Gần Nơi Sử Dụng Càng Tốt

Trong ngôn ngữ C cổ điển (C89), mọi biến đều bắt buộc phải khai báo ở đầu hàm. **Trong Modern C++, điều này là một Anti-pattern (thói quen xấu)!**

::: tip 💡 Thực Hành Tốt Nhất (Best Practice)
1. **Định nghĩa biến gần nhất có thể với nơi nó được dùng lần đầu**: Giúp người đọc mã không phải cuộn trang lên đầu hàm để tìm kiểu dữ liệu, đồng thời thu hẹp phạm vi biến để tránh tái sử dụng biến sai mục đích.
2. **Luôn khởi tạo giá trị cho biến ngay khi định nghĩa**: Tuyệt đối không để biến ở trạng thái rác (`int x;`).
:::

---

## 📝 Hệ Thống Quiz & Bài Tập Tự Luyện

### Câu hỏi 1:
Giải thích sự khác nhau giữa **Scope (Phạm vi)** và **Lifetime (Vòng đời)** của một biến.
::: details [Xem lời giải]
- **Scope (Phạm vi)** là một khái niệm thuộc về **Mã Nguồn (Compile-time)**: Nó quy định vùng văn bản mã nguồn mà tên biến có thể được nhìn thấy và sử dụng bởi trình biên dịch.
- **Lifetime (Vòng đời)** là một khái niệm thuộc về **Thời Gian Chạy (Runtime)**: Nó là khoảng thời gian thực tế mà biến chiếm dụng bộ nhớ RAM (từ lúc được cấp phát đến khi bị giải phóng).
:::
"""
save_lesson("7_3-local-variables.md", lesson_7_3)

# ==============================================================================
# Lesson 7.4
# ==============================================================================
lesson_7_4 = r"""# 7.4 — Nhập Môn Biến Toàn Cục (Introduction to Global Variables)

---

## 🎯 Mục Tiêu Bài Học
- Hiểu định nghĩa **Biến toàn cục (Global Variables)**: Được khai báo bên ngoài mọi hàm.
- Nắm vững **Phạm vi tệp (File Scope / Global Namespace Scope)**.
- Hiểu cơ chế **Thời gian sống tĩnh (Static Storage Duration)**: Tồn tại trong suốt vòng đời của chương trình.
- Khởi tạo mặc định bằng 0 (Zero-initialization) của biến toàn cục.

---

## 1. Biến Toàn Cục Là Gì?

Trong C++, một biến được định nghĩa bên ngoài tất cả các khối mã, hàm hoặc class được gọi là **Biến toàn cục (Global Variable)**.

```cpp
#include <iostream>

// Biến toàn cục g_x được định nghĩa ngoài mọi hàm
int g_x { 5 }; 

void doSomething()
{
    std::cout << "Gia tri g_x trong doSomething: " << g_x << '\n';
    g_x = 10; // Thay đổi giá trị biến toàn cục
}

int main()
{
    std::cout << "Gia tri g_x trong main truoc do: " << g_x << '\n'; // 5
    doSomething();
    std::cout << "Gia tri g_x trong main sau do: " << g_x << '\n';   // 10
    return 0;
}
```

::: tip 💡 Quy Ước Đặt Tên (Naming Convention)
Nhiều kỹ sư C++ chuyên nghiệp sử dụng tiền tố `g_` (ví dụ: `g_x`, `g_mode`) cho các biến toàn cục để phân biệt rõ ràng ngay lập tức với các biến cục bộ trong thân hàm.
:::

---

## 2. Phạm Vi và Vòng Đời Của Biến Toàn Cục

```mermaid
flowchart LR
    subgraph RAM_Layout ["Bố Trí Bộ Nhớ Tiến Trình (RAM)"]
        DataSeg["Data Segment / BSS Segment\nChứa Biến Toàn Cục & Biến Static\nCấp phát khi nạp EXE -> Tồn tại đến khi tắt App"]
        StackSeg["Stack Segment\nChứa Biến Cục Bộ\nCấp phát & Hủy liên tục theo hàm"]
    end
```

| Tiêu chí | Biến Cục Bộ (Local) | Biến Toàn Cục (Global) |
| :--- | :--- | :--- |
| **Vị trí định nghĩa** | Bên trong hàm / khối mã `{}` | Bên ngoài mọi hàm |
| **Phạm vi (Scope)** | Block Scope (chỉ trong khối) | File Scope (toàn tệp từ dòng định nghĩa) |
| **Vòng đời (Duration)** | Automatic Duration (trên Stack) | **Static Duration** (trên Data Segment) |
| **Khởi tạo mặc định** | Giá trị rác (Không xác định) | **Tự động bằng 0 (Zero-initialized)** |

---

## 3. Khởi Tạo Tự Động Bằng 0 (Zero-initialization)

Không giống như các biến cục bộ (nếu không khởi tạo sẽ mang giá trị rác ngẫu nhiên), các biến có **Static Duration** luôn được đảm bảo khởi tạo bằng `0` trước khi hàm `main()` bắt đầu chạy:

```cpp
#include <iostream>

int g_uninitialized; // Tự động bằng 0!

int main()
{
    int local_uninitialized; // ⚠️ Giá trị rác ngẫu nhiên (UB nếu đọc)!
    
    std::cout << "Global: " << g_uninitialized << '\n'; // An toàn: In ra 0
    // std::cout << local_uninitialized; // Nguy hiểm!
    return 0;
}
```

---

## 📝 Hệ Thống Quiz & Bài Tập Tự Luyện

### Câu hỏi 1:
Biến toàn cục được lưu trữ tại phân vùng bộ nhớ nào của chương trình khi thực thi?
::: details [Xem lời giải]
Biến toàn cục không nằm trên Stack, cũng không nằm trên Heap. Chúng được lưu trữ trong phân vùng **Data Segment** (nếu đã được khởi tạo giá trị khác 0) hoặc **BSS Segment** (Block Started by Symbol - nếu chưa khởi tạo hoặc khởi tạo bằng 0). Vùng nhớ này được hệ điều hành nạp ngay khi chương trình bắt đầu và chỉ được giải phóng khi chương trình kết thúc hoàn toàn.
:::
"""
save_lesson("7_4-introduction-to-global-variables.md", lesson_7_4)

# ==============================================================================
# Lesson 7.5
# ==============================================================================
lesson_7_5 = r"""# 7.5 — Che Khuất Biến: Ẩn Tên Định Danh (Variable Shadowing / Name Hiding)

---

## 🎯 Mục Tiêu Bài Học
- Hiểu hiện tượng **Che khuất biến (Variable Shadowing)** hay **Ẩn tên (Name Hiding)**.
- Phân tích cơ chế trình biên dịch ưu tiên tìm kiếm định danh từ phạm vi hẹp nhất ra ngoài.
- Tác hại nguy hiểm của việc che khuất biến vô ý và cảnh báo từ compiler (`-Wshadow`).
- Cách dùng toán tử `::` để giải cứu biến toàn cục bị che khuất.

---

## 1. Hiện Tượng Che Khuất Biến Là Gì?

Khi một biến được khai báo bên trong một khối mã con (Inner scope) có **cùng tên** với một biến đã tồn tại ở khối cha (Outer scope) hoặc biến toàn cục, biến ở khối trong sẽ **che khuất (shadow/hide)** biến ở khối ngoài.

Mọi truy cập tên biến đó bên trong inner scope sẽ được ánh xạ tới biến cục bộ mới, khiến biến bên ngoài trở nên "vô hình":

```cpp
#include <iostream>

int main()
{
    int apples { 5 }; // apples của outer block

    {
        std::cout << "Apples outer: " << apples << '\n'; // 5

        // Định nghĩa biến trùng tên trong inner block!
        int apples { 10 }; // Biến này che khuất biến apples ở ngoài!

        std::cout << "Apples inner: " << apples << '\n'; // 10
    } // apples inner bị hủy tại đây!

    std::cout << "Apples outer sau do: " << apples << '\n'; // 5 (không hề bị thay đổi!)
    return 0;
}
```

```mermaid
flowchart TD
    subgraph Resolution ["Quy Tắc Tìm Kiếm Tên Của Trình Biên Dịch"]
        R1["Tìm trong Scope hiện tại"] -->|Tìm thấy| Found["Dừng lại và sử dụng ngay!"]
        R1 -->|Không thấy| R2["Tìm trong Outer Scope bao quanh"]
        R2 -->|Không thấy| R3["Tìm trong Global Scope"]
        R3 -->|Không thấy| Err["Báo lỗi biên dịch: undeclared identifier"]
    end
```

---

## 2. Che Khuất Biến Toàn Cục và Cách Dùng Toán Tử `::`

Một biến cục bộ có thể che khuất một biến toàn cục:

```cpp
#include <iostream>

int value { 7 }; // Biến toàn cục

int main()
{
    int value { 42 }; // Che khuất biến toàn cục value!

    std::cout << "Gia tri bien cuc bo: " << value << '\n';   // In ra 42
    std::cout << "Gia tri bien toan cuc: " << ::value << '\n'; // Dùng :: để vượt qua che khuất: In ra 7
    return 0;
}
```

---

## 3. Cạm Bẫy và Khuyến Cáo Thực Hành

::: warning ⚠️ Cực Kỳ Nguy Hiểm: Lỗi Logic Khó Gỡ Lỗi
Che khuất biến là thủ phạm số 1 gây ra các lỗi logic bí ẩn: Lập trình viên tưởng rằng mình đang thay đổi giá trị của biến bên ngoài, nhưng thực tế lại đang cập nhật biến tạm thời bên trong!

```cpp
int totalCount { 0 };

void calculate()
{
    for (int i = 0; i < 5; ++i)
    {
        int totalCount { 0 }; // 💥 LỖI: Vô tình khai báo biến mới thay vì cộng dồn!
        totalCount += i;
    }
    // Ra ngoài vòng lặp, totalCount toàn cục vẫn là 0!
}
```
:::

::: tip 💡 Thực Hành Tốt Nhất (Best Practice)
1. **Bật cờ cảnh báo của Compiler**: Luôn biên dịch với cờ `-Wshadow` trên GCC/Clang để trình biên dịch phát hiện và báo lỗi ngay khi có biến bị che khuất.
2. **Tránh đặt trùng tên biến**: Đặt tên biến rõ nghĩa theo ngữ cảnh cụ thể (ví dụ: `totalApples`, `currentApples`).
:::

---

## 📝 Hệ Thống Quiz & Bài Tập Tự Luyện

### Câu hỏi 1:
Đoạn mã sau in ra giá trị gì?
```cpp
int x { 1 };
{
    int x { 2 };
    {
        x = 3;
    }
    std::cout << x << ' ';
}
std::cout << x;
```
::: details [Xem lời giải]
- Biểu thức `x = 3` nằm trong khối sâu nhất, nơi không có khai báo `x` mới. Trình biên dịch tìm ra ngoài và thấy `int x { 2 }`, do đó gán `x` của khối giữa thành 3.
- Thoát khối trong cùng, dòng `std::cout << x` in ra `3`.
- Thoát khối giữa, biến `x` của khối giữa bị hủy. Dòng `std::cout << x` ngoài cùng truy cập biến `x { 1 }` ban đầu.
- In ra: `3 1`.
:::
"""
save_lesson("7_5-variable-shadowing-name-hiding.md", lesson_7_5)

# ==============================================================================
# Remaining Lessons 7.6 to 7.x
# ==============================================================================
lesson_7_6 = r"""# 7.6 — Liên Kết Nội Bộ (Internal Linkage)

---

## 🎯 Mục Tiêu Bài Học
- Hiểu khái niệm **Liên kết (Linkage)** và **Đơn vị biên dịch (Translation Unit)**.
- Phân biệt định danh có **Liên kết nội bộ (Internal Linkage)**: Chỉ có thể nhìn thấy trong phạm vi 1 tệp mã nguồn đơn lẻ.
- Sử dụng từ khóa `static` cho biến toàn cục và hàm để kích hoạt internal linkage.
- Tính chất internal linkage mặc định của hằng số `const` và `constexpr`.

---

## 1. Liên Kết (Linkage) Là Gì?

Một chương trình C++ thường bao gồm nhiều tệp mã nguồn `.cpp`. Mỗi tệp `.cpp` (kèm theo tất cả các tệp header mà nó `#include`) được trình biên dịch biên dịch hoàn toàn độc lập thành một tệp đối tượng nhị phân (`.obj` hoặc `.o`), gọi là một **Đơn vị biên dịch (Translation Unit - TU)**.

Sau đó, **Trình liên kết (Linker)** có nhiệm vụ kết nối các tệp đối tượng này lại với nhau để tạo thành tệp thực thi cuối cùng (`.exe` hoặc binary ELF).

**Liên kết (Linkage)** quy định xem một định danh (tên hàm, tên biến) có thể được Trình liên kết nhìn thấy và tham chiếu giữa các đơn vị biên dịch khác nhau hay không:
- **No Linkage**: Chỉ tồn tại trong khối mã cục bộ.
- **Internal Linkage**: Chỉ nhìn thấy bên trong đơn vị biên dịch hiện tại.
- **External Linkage**: Có thể được nhìn thấy và sử dụng từ các tệp `.cpp` khác!

```mermaid
flowchart LR
    subgraph TU1 ["file1.cpp (Translation Unit 1)"]
        S1["static int g_x = 10;\n(Internal Linkage)"]
        F1["void doWork()"]
    end
    subgraph TU2 ["file2.cpp (Translation Unit 2)"]
        S2["static int g_x = 20;\n(Internal Linkage)"]
        F2["void otherWork()"]
    end
    Linker["Trình Liên Kết (Linker)"]
    TU1 -.-> Linker
    TU2 -.-> Linker
    Note["Hai biến g_x hoàn toàn độc lập!\nKhông xảy ra xung đột ODR."]
```

---

## 2. Kích Hoạt Internal Linkage Bằng Từ Khóa `static`

Khi đặt từ khóa `static` trước một biến toàn cục hoặc một hàm ở phạm vi file, định danh đó sẽ có **Internal Linkage**:

```cpp
// a.cpp
static int g_secret { 42 }; // Internal linkage: Chỉ nhìn thấy trong a.cpp

static void helperFunction() // Internal linkage: Không thể gọi từ tệp khác
{
    // ...
}
```

Nếu một tệp `b.cpp` khác cũng định nghĩa `static int g_secret { 99 };`, hai biến này là **hoàn toàn độc lập** ở hai vùng nhớ khác nhau. Linker sẽ không bao giờ báo lỗi trùng tên!

---

## 3. Biến Hằng `const` và `constexpr` Toàn Cục Mặc Định Có Internal Linkage

Trong C++, các biến toàn cục không phải const (`int g_x`) mặc định có **External Linkage**.
Tuy nhiên, để tối ưu hóa và an toàn, chuẩn C++ quy định:
**Các biến toàn cục `const` và `constexpr` mặc định có Internal Linkage!**

```cpp
const int g_y { 1 };       // Mặc định có Internal Linkage!
constexpr int g_z { 2 };   // Mặc định có Internal Linkage!
```

---

## 📝 Hệ Thống Quiz & Bài Tập Tự Luyện

### Câu hỏi 1:
Tại sao việc sử dụng Internal Linkage cho các hàm trợ giúp (helper functions) bên trong tệp `.cpp` lại là một thói quen lập trình xuất sắc?
::: details [Xem lời giải]
1. **Đóng gói thông tin (Encapsulation)**: Ngăn chặn các tệp khác vô tình gọi trực tiếp các hàm nội bộ không thuộc về giao diện công khai (API).
2. **Tránh xung đột tên**: Bạn có thể đặt tên các hàm phụ trợ phổ biến (như `init()`, `clean()`, `helper()`) mà không lo bị trùng lặp với các thư viện hoặc tệp khác trong toàn bộ dự án.
:::
"""
save_lesson("7_6-internal-linkage.md", lesson_7_6)

lesson_7_7 = r"""# 7.7 — Liên Kết Ngoài và Khai Báo Báo Trước Biến (External Linkage and Variable Forward Declarations)

---

## 🎯 Mục Tiêu Bài Học
- Hiểu định nghĩa **Liên kết ngoài (External Linkage)**: Cho phép chia sẻ biến và hàm giữa nhiều tệp `.cpp`.
- Sử dụng từ khóa `extern` để tạo **Khai báo báo trước (Forward Declaration)** cho biến.
- Phân biệt rõ giữa **Khai báo biến (Declaration)** và **Định nghĩa biến (Definition)**.
- Biến hằng toàn cục với `extern const`.

---

## 1. Liên Kết Ngoài (External Linkage) Là Gì?

Một định danh có **External Linkage** có thể được nhìn thấy và sử dụng bởi bất kỳ đơn vị biên dịch (tệp `.cpp`) nào trong toàn bộ dự án.
- Các hàm thông thường mặc định có External Linkage.
- Các biến toàn cục không phải const (`int g_x { 5 };`) mặc định có External Linkage.

Để sử dụng một biến toàn cục được định nghĩa ở tệp này từ một tệp khác, bạn phải thông báo cho trình biên dịch biết sự tồn tại của biến đó qua một **Khai báo báo trước (Forward Declaration)** bằng từ khóa `extern`.

```mermaid
flowchart LR
    subgraph FileA ["globals.cpp"]
        Def["int g_score { 100 };\n(Định nghĩa thực tế: Cấp phát bộ nhớ)"]
    end
    subgraph FileB ["main.cpp"]
        Decl["extern int g_score;\n(Khai báo báo trước: Không cấp phát bộ nhớ)"]
        Use["std::cout << g_score;"]
        Decl --> Use
    end
    FileA <-->|Linker nối tham chiếu| FileB
```

---

## 2. Khai Báo (Declaration) vs Định Nghĩa (Definition) Với `extern`

- **Định nghĩa (Definition)**: Cấp phát bộ nhớ thực sự cho biến.
- **Khai báo (Declaration)**: Chỉ báo tên và kiểu, không cấp phát bộ nhớ.

```cpp
int g_x;             // ĐỊNH NGHĨA (không khởi tạo, tự động bằng 0)
int g_x { 5 };       // ĐỊNH NGHĨA (có khởi tạo)
extern int g_x { 5 };// ĐỊNH NGHĨA (có gán giá trị thì từ khóa extern bị vô hiệu hóa!)

extern int g_y;      // KHAI BÁO (Báo rằng g_y được định nghĩa ở đâu đó khác!)
```

### Ví dụ chia sẻ biến giữa 2 tệp:
::: code-group
```cpp [data.cpp]
// Định nghĩa biến toàn cục thực tế tại đây
int g_globalCounter { 42 };
```

```cpp [main.cpp]
#include <iostream>

// Khai báo báo trước cho trình biên dịch biết g_globalCounter tồn tại
extern int g_globalCounter; 

int main()
{
    std::cout << "Gia tri tu data.cpp: " << g_globalCounter << '\n'; // 42
    g_globalCounter = 100; // Thay đổi trực tiếp biến toàn cục
    return 0;
}
```
:::

---

## 3. Chia Sẻ Hằng Số Toàn Cục Với `extern const`

Vì biến `const` mặc định có Internal Linkage, nếu bạn muốn biến const có External Linkage để chia sẻ, bạn **bắt buộc phải thêm từ khóa `extern` ở cả nơi định nghĩa lẫn nơi khai báo**:

::: code-group
```cpp [constants.cpp]
// Phải có extern ở nơi định nghĩa để biến const có external linkage
extern const double g_pi { 3.14159 };
```

```cpp [main.cpp]
#include <iostream>

extern const double g_pi; // Khai báo

int main()
{
    std::cout << "Pi = " << g_pi << '\n';
    return 0;
}
```
:::

---

## 📝 Hệ Thống Quiz & Bài Tập Tự Luyện

### Câu hỏi 1:
Nếu bạn viết `extern int g_val;` trong `main.cpp` nhưng quên không định nghĩa `int g_val { 10 };` trong bất kỳ tệp `.cpp` nào, lỗi sẽ phát sinh ở giai đoạn nào?
::: details [Xem lời giải]
Lỗi sẽ phát sinh ở giai đoạn **Liên kết (Linking stage)**!  
Trình biên dịch (Compiler) xử lý `main.cpp` hoàn toàn trơn tru vì nó tin lời khai báo `extern`. Nhưng khi Linker gom các tệp lại, nó không tìm thấy địa chỉ bộ nhớ nào được cấp phát cho `g_val`, dẫn đến lỗi kinh điển:
`undefined reference to 'g_val'` hoặc `LNK2001: unresolved external symbol g_val`.
:::
"""
save_lesson("7_7-external-linkage-and-variable-forward-declarations.md", lesson_7_7)

lesson_7_8 = r"""# 7.8 — Tại Sao Biến Toàn Cục Không Phải Hằng Số Là "Ác Quỷ"? (Why Non-Const Globals Are Evil)

---

## 🎯 Mục Tiêu Bài Học
- Hiểu tại sao các kỹ sư phần mềm hàng đầu coi biến toàn cục không phải hằng (**Non-const global variables**) là "tội đồ" trong thiết kế phần mềm.
- Phân tích hiện tượng ô nhiễm trạng thái toàn cục (Global State Pollution) và mất tính cục bộ (Loss of locality).
- Nguy cơ xảy ra xung đột đa luồng (**Race Conditions** / Đua dữ liệu).
- Thứ tự khởi tạo biến toàn cục không xác định (Static Initialization Order Fiasco).
- Các giải pháp thay thế văn minh và an toàn.

---

## 1. Những Tác Hại Khủng Khiếp Của Biến Toàn Cục Non-Const

```mermaid
flowchart TD
    G["Biến Toàn Cục Non-Const\nint g_mode = 1;"] --> E1["Mất tính cục bộ:\nBất kỳ hàm nào cũng có thể sửa giá trị!"]
    G --> E2["Không thể kiểm thử (Untestable):\nCác Unit Test bị phụ thuộc lẫn nhau!"]
    G --> E3["Xung đột đa luồng (Data Race):\nNhiều luồng ghi đè bộ nhớ cùng lúc -> Crash!"]
    G --> E4["Static Initialization Fiasco:\nKhông biết biến nào được tạo trước giữa các file!"]
```

1. **Phá vỡ tính đóng gói và mất tính cục bộ**: Khi đọc một hàm, bạn chỉ cần nhìn vào các tham số truyền vào là hiểu hàm hoạt động ra sao. Nhưng nếu hàm đọc/ghi biến toàn cục, bạn buộc phải đọc toàn bộ mã nguồn của cả dự án để biết biến đó đã bị ai sửa đổi trước đó!
2. **Khó khăn tột cùng khi gỡ lỗi (Debugging)**: Biến `g_state` đột nhiên mang giá trị sai `-1`. Trong số 500 hàm của dự án, hàm nào đã gán `-1`? Bạn không thể đặt breakpoint hiệu quả.
3. **Cực kỳ nguy hiểm trong lập trình đa luồng (Multi-threading)**: Nếu hai luồng cùng đọc và ghi vào biến toàn cục mà không có cơ chế khóa (Mutex), chương trình sẽ bị Data Race và sập bất cứ lúc nào.

---

## 2. Vấn Nạn Trật Tự Khởi Tạo Tĩnh (Static Initialization Order Fiasco)

Nếu bạn có 2 biến toàn cục ở 2 tệp `.cpp` khác nhau, và biến này phụ thuộc vào giá trị của biến kia:

::: code-group
```cpp [a.cpp]
int initValue() { return 42; }
int g_a { initValue() }; // Khởi tạo động
```

```cpp [b.cpp]
extern int g_a;
int g_b { g_a + 10 }; // Phụ thuộc vào g_a!
```
:::

Chuẩn C++ **hoàn toàn không quy định** tệp `a.cpp` hay `b.cpp` được khởi tạo trước! Nếu `b.cpp` được khởi tạo trước `a.cpp`, `g_a` lúc này vẫn chỉ là `0`, dẫn đến `g_b` mang giá trị `10` thay vì `52`. Đây là một lỗi cực kỳ khó phát hiện.

---

## 3. Các Giải Pháp Thay Thế Văn Minh

::: tip 💡 Cách Thiết Kế Đúng Đắn
1. **Truyền dữ liệu qua tham số hàm**: Thay vì đọc biến toàn cục, hãy truyền biến đó vào hàm qua tham chiếu (`const Type&`).
2. **Đóng gói vào Class / Struct**: Biến dữ liệu thành thuộc tính của lớp, chỉ cho phép truy cập qua các phương thức được kiểm soát.
3. **Sử dụng Mẫu Thiết Kế Singleton Meyers (Meyers' Singleton)** nếu thực sự bắt buộc chỉ có 1 đối tượng duy nhất:
   ```cpp
   class GlobalConfig
   {
   public:
       static GlobalConfig& instance()
       {
           static GlobalConfig s_instance; // Khởi tạo an toàn luồng trong C++11
           return s_instance;
       }
   private:
       GlobalConfig() = default;
   };
   ```
:::
"""
save_lesson("7_8-why-non-const-global-variables-are-evil.md", lesson_7_8)

lesson_7_9 = r"""# 7.9 — Hàm Nội Tuyến và Biến Nội Tuyến (Inline Functions and Variables)

---

## 🎯 Mục Tiêu Bài Học
- Hiểu ý nghĩa lịch sử của từ khóa `inline`: Gợi ý thay thế lời gọi hàm bằng mã máy thực tế.
- Nắm vững ý nghĩa hiện đại chuẩn ISO C++ của `inline`: **Miễn trừ Quy tắc Một Định Nghĩa (One Definition Rule - ODR)**.
- Đặt định nghĩa hàm inline vào tệp Header an toàn mà không bị lỗi trùng lặp từ Linker.
- 🚀 Tính năng đột phá từ C++17: **Biến nội tuyến (`inline` variables)**.

---

## 1. Ý Nghĩa Lịch Sử vs Hiện Đại Của Từ Khóa `inline`

- **Thời kỳ đầu**: Mỗi khi gọi một hàm, CPU phải thực hiện nhảy địa chỉ, lưu thanh ghi, đẩy stack frame... Đối với các hàm siêu nhỏ (như `int min(int a, int b) { return a < b ? a : b; }`), chi phí gọi hàm còn tốn thời gian hơn cả phép so sánh! Từ khóa `inline` ra đời để gợi ý compiler chèn thẳng thân hàm vào nơi gọi.
- **Hiện đại**: Ngày nay, các trình biên dịch tối ưu hóa cực kỳ thông minh. Compiler tự quyết định hàm nào nên inline hay không dựa trên phân tích hiệu năng, **bất kể bạn có viết từ khóa `inline` hay không**!

Vậy từ khóa `inline` trong C++ hiện đại dùng để làm gì?
**Nó dùng để cho phép một hàm hoặc một biến được định nghĩa ở NHIỀU ĐƠN VỊ BIÊN DỊCH khác nhau mà không vi phạm Quy tắc Một Định Nghĩa (One Definition Rule - ODR)!**

```mermaid
flowchart TD
    subgraph Header ["math.h"]
        H["inline int add(int a, int b) { return a + b; }"]
    end
    H -->|#include| F1["file1.cpp"]
    H -->|#include| F2["file2.cpp"]
    F1 --> O1["file1.o (Có định nghĩa add)"]
    F2 --> O2["file2.o (Có định nghĩa add)"]
    O1 --> Linker["Linker"]
    O2 --> Linker
    Linker --> Res["Khử trùng lặp ODR:\nLinker tự động gom thành 1 định nghĩa duy nhất!"]
```

---

## 2. Biến Nội Tuyến (`inline` Variables) Từ C++17

Trước C++17, bạn chỉ có thể inline hàm, không thể inline biến. Muốn định nghĩa biến toàn cục, bạn phải tách: khai báo `extern` trong header, định nghĩa thực tế trong 1 tệp `.cpp`.

Từ **C++17**, bạn có thể thêm từ khóa `inline` trước biến toàn cục và **đặt trực tiếp định nghĩa của nó trong tệp header**:

```cpp
// constants.h (C++17)
#pragma once

namespace Constants
{
    inline constexpr double pi { 3.141592653589793 };
    inline constexpr double gravity { 9.80665 };
}
```

Bất kỳ tệp `.cpp` nào `#include "constants.h"` đều có thể truy cập `Constants::pi`. Linker sẽ tự động khử trùng lặp và đảm bảo chỉ có đúng một bản sao bộ nhớ duy nhất!

---

## 📝 Hệ Thống Quiz & Bài Tập Tự Luyện

### Câu hỏi 1:
Điều gì xảy ra nếu bạn định nghĩa một hàm thông thường (không có từ khóa `inline`) bên trong một tệp header, và tệp header đó được `#include` bởi 2 tệp `.cpp` khác nhau?
::: details [Xem lời giải]
Trình biên dịch sẽ biên dịch từng tệp `.cpp` thành công. Nhưng khi Linker gom các tệp lại, nó sẽ thấy 2 định nghĩa trùng lặp của cùng một hàm, và báo lỗi vi phạm ODR:
`fatal error LNK1169: one or more multiply defined symbols found` (hoặc `multiple definition of ...`).
Bổ sung từ khóa `inline` sẽ giải quyết dứt điểm lỗi này!
:::
"""
save_lesson("7_9-inline-functions-and-variables.md", lesson_7_9)

lesson_7_10 = r"""# 7.10 — Chia Sẻ Hằng Số Toàn Cục Bằng Biến Inline (Sharing Global Constants)

---

## 🎯 Mục Tiêu Bài Học
- So sánh các phương pháp chia sẻ hằng số toàn cục xuyên suốt lịch sử C++.
- Thấy rõ nhược điểm lãng phí bộ nhớ của phương pháp cổ điển (`const` trong header).
- Thấy rõ sự phiền toái của phương pháp `extern const` (tách header và cpp).
- Nắm vững giải pháp tối thượng chuẩn mực của C++17 trở đi: **`inline constexpr` trong header**.

---

## 1. Sự Tiến Hóa Của Việc Quản Lý Hằng Số Toàn Cục

Trong các dự án kỹ thuật hoặc game, chúng ta luôn có vô số hằng số vật lý, hằng số cấu hình (ví dụ: `pi`, `gravity`, `screen_width`, `max_connections`). Làm sao để định nghĩa chúng ở một nơi duy nhất và chia sẻ cho cả dự án?

```mermaid
flowchart TD
    subgraph OldWay ["C++ Cổ Điển: const trong Header"]
        O1["Header: const double pi = 3.14;"]
        O1 -->|Mỗi tệp .cpp include| O2["Mỗi file .cpp tự tạo 1 bản sao pi riêng trong RAM!\nLãng phí bộ nhớ!"]
    end
    subgraph ModernWay ["C++17 Hiện Đại: inline constexpr"]
        M1["Header: inline constexpr double pi = 3.14;"]
        M1 -->|Tất cả tệp include| M2["Chỉ duy nhất 1 bản sao bộ nhớ trong toàn app!\nTính toán tại Compile-time!"]
    end
```

---

## 2. Giải Pháp Chuẩn Mực Hiện Đại (C++17): Header-Only Constants

Chỉ cần một tệp header duy nhất, không cần tệp `.cpp` đi kèm:

```cpp
// Constants.h
#ifndef CONSTANTS_H
#define CONSTANTS_H

namespace Constants
{
    // C++17 inline constexpr: Siêu nhanh, an toàn, không trùng lặp ODR
    inline constexpr double pi { 3.141592653589793 };
    inline constexpr double avogadro { 6.0221413e23 };
    inline constexpr double myGravity { 9.2 }; // Trọng lực tùy chỉnh
    inline constexpr int maxPlayers { 64 };
}

#endif
```

Sử dụng ở bất kỳ đâu:
```cpp
// main.cpp
#include "Constants.h"
#include <iostream>

int main()
{
    std::cout << "Gia tri Pi: " << Constants::pi << '\n';
    return 0;
}
```

::: tip 💡 Vì Sao Đây Là Tiêu Chuẩn Vàng Hiện Nay?
1. **Header-only**: Cực kỳ dễ sử dụng và bảo trì, chỉ cần `#include`.
2. **Hiệu năng compile-time**: `constexpr` cho phép các hằng số này được dùng trong các biểu thức tính toán ngay lúc biên dịch (ví dụ: kích thước mảng tĩnh `int arr[Constants::maxPlayers];`).
3. **Tiết kiệm bộ nhớ**: `inline` đảm bảo Linker chỉ tạo 1 bản sao duy nhất trong tệp thực thi.
:::
"""
save_lesson("7_10-sharing-global-constants-across-multiple-files-using-inline-variables.md", lesson_7_10)

lesson_7_11 = r"""# 7.11 — Biến Cục Bộ Tĩnh (Static Local Variables)

---

## 🎯 Mục Tiêu Bài Học
- Hiểu khái niệm **Biến cục bộ tĩnh (Static Local Variable)** bằng từ khóa `static`.
- Nhận thức sự kết hợp độc đáo: **Phạm vi cục bộ (Block Scope)** nhưng **Vòng đời toàn cục (Static Duration)**.
- Phân tích cơ chế khởi tạo đúng 1 lần duy nhất trong lần gọi hàm đầu tiên.
- Tính năng an toàn đa luồng (**Thread-safe Initialization**) chuẩn C++11.

---

## 1. Biến Cục Bộ Tĩnh Là Gì?

Khi áp dụng từ khóa `static` cho một biến cục bộ bên trong hàm, biến đó sẽ thay đổi hoàn toàn vòng đời:
- **Scope (Phạm vi)**: Vẫn là **Block Scope** (chỉ có thể truy cập bên trong hàm đó).
- **Duration (Vòng đời)**: Trở thành **Static Duration** (tồn tại liên tục trong suốt thời gian chương trình chạy, không bị tiêu hủy khi hàm kết thúc!).

```cpp
#include <iostream>

void incrementAndPrint()
{
    static int s_counter { 0 }; // Chỉ khởi tạo DUY NHẤT 1 LẦN trong lần gọi đầu tiên!
    ++s_counter;
    std::cout << s_counter << ' ';
}

int main()
{
    incrementAndPrint(); // In ra: 1
    incrementAndPrint(); // In ra: 2
    incrementAndPrint(); // In ra: 3
    return 0;
}
```

```mermaid
sequenceDiagram
    autonumber
    participant Main as Hàm main()
    participant Func as Hàm incrementAndPrint()
    participant RAM as Vùng Nhớ Static (s_counter)
    
    Main->>Func: Gọi lần 1
    Note over Func,RAM: Khởi tạo s_counter = 0 (Chỉ làm 1 lần!)
    Func->>RAM: Tăng s_counter lên 1
    Func-->>Main: In ra 1, thoát hàm (s_counter KHÔNG bị hủy!)
    
    Main->>Func: Gọi lần 2
    Note over Func,RAM: Bỏ qua dòng khởi tạo!
    Func->>RAM: Tăng s_counter lên 2
    Func-->>Main: In ra 2
```

---

## 2. Ứng Dụng Đỉnh Cao: Bộ Sinh ID Tự Động (ID Generator)

```cpp
int generateUniqueID()
{
    static int s_id { 1000 };
    return ++s_id; // Mỗi lần gọi sinh ra 1 ID duy nhất không trùng lặp!
}
```

::: tip 💡 C++11 Magic: An Toàn Đa Luồng (Thread-Safety)
Từ chuẩn C++11, việc khởi tạo biến cục bộ tĩnh được đảm bảo **Thread-safe** bởi trình biên dịch. Nếu có 10 luồng cùng gọi hàm lần đầu tiên đồng thời, trình biên dịch sẽ tự động chèn khóa ngầm định để đảm bảo biến được khởi tạo chính xác 1 lần duy nhất mà không bị Data Race!
:::
"""
save_lesson("7_11-static-local-variables.md", lesson_7_11)

lesson_7_12 = r"""# 7.12 — Tổng Kết Toàn Diện Về Phạm Vi, Vòng Đời và Liên Kết (Summary)

---

## 🎯 Mục Tiêu Bài Học
- Hệ thống hóa bảng ma trận 3 chiều: **Scope**, **Duration**, và **Linkage**.
- Khắc sâu các quy tắc phân biệt loại biến trong C++.

---

## 1. Bảng Ma Trận Tổng Kết Toàn Diện

| Loại Biến | Vị trí định nghĩa | Scope (Phạm vi) | Duration (Vòng đời) | Linkage (Liên kết) |
| :--- | :--- | :--- | :--- | :--- |
| **Biến cục bộ thông thường** | Trong khối `{}` | Block scope | Automatic (trên Stack) | None |
| **Biến cục bộ tĩnh (`static`)** | Trong khối `{}` có `static` | Block scope | **Static** (suốt chương trình) | None |
| **Tham số hàm** | Danh sách tham số hàm | Block scope | Automatic | None |
| **Biến toàn cục nội bộ (`static`)** | Ngoài hàm có `static` | File / Global scope | Static | **Internal** (chỉ trong 1 file) |
| **Hằng toàn cục nội bộ (`const`)** | Ngoài hàm có `const` | File / Global scope | Static | **Internal** |
| **Biến toàn cục ngoài (thường)** | Ngoài hàm không `static` | File / Global scope | Static | **External** (toàn dự án) |
| **Biến toàn cục ngoài (`extern`)** | Ngoài hàm có `extern` | File / Global scope | Static | **External** |
| **Biến toàn cục inline (C++17)** | Header có `inline` | File / Global scope | Static | **External** (Khử trùng ODR) |

---

## 2. Sơ Đồ Cây Quyết Định (Decision Tree)

```mermaid
flowchart TD
    Q1{"Biến nằm ở đâu?"}
    Q1 -- "Trong hàm / khối {}" --> Q2{"Có từ khóa static không?"}
    Q2 -- Không --> Local["Biến Cục Bộ\nAutomatic Duration, No Linkage"]
    Q2 -- Có --> StaticLocal["Biến Cục Bộ Tĩnh\nStatic Duration, No Linkage"]
    
    Q1 -- "Ngoài mọi hàm" --> Q3{"Có từ khóa static hoặc const không?"}
    Q3 -- Có --> IntLink["Biến Toàn Cục Nội Bộ\nStatic Duration, Internal Linkage"]
    Q3 -- "Không (hoặc có extern/inline)" --> ExtLink["Biến Toàn Cục Ngoài\nStatic Duration, External Linkage"]
```
"""
save_lesson("7_12-scope-duration-and-linkage-summary.md", lesson_7_12)

lesson_7_13 = r"""# 7.13 — Khai Báo Using và Chỉ Thị Using (Using Declarations and Directives)

---

## 🎯 Mục Tiêu Bài Học
- Phân biệt rõ ràng giữa **Khai báo using (Using-declaration)** và **Chỉ thị using (Using-directive)**.
- Hiểu tại sao `using namespace std;` được coi là một thói quen xấu cần tránh.
- Phạm vi tác dụng của `using` trong các khối mã cục bộ.

---

## 1. Khai Báo Using (Using-declaration)

Khai báo using đưa **đúng một định danh cụ thể** từ namespace vào phạm vi hiện tại:

```cpp
#include <iostream>

int main()
{
    using std::cout; // Chỉ đưa duy nhất cout vào scope!

    cout << "Xin chao!\n"; // Hợp lệ!
    // cin >> x;           // Lỗi: cin vẫn cần std::cin!
    return 0;
}
```

---

## 2. Chỉ Thị Using (Using-directive)

Chỉ thị using đưa **TẤT CẢ mọi định danh** trong namespace vào phạm vi hiện tại:

```cpp
using namespace std; // Mở tung toàn bộ hàng trăm nghìn định danh của std!
```

::: danger ⚠️ Vì Sao Phải Tuyệt Đối Tránh `using namespace std;`?
1. **Xung đột tên bất ngờ (Ambiguity Errors)**: C++ chuẩn có sẵn các hàm phổ biến như `count`, `min`, `max`, `size`, `move`. Nếu bạn định nghĩa hàm `int count = 5;`, trình biên dịch sẽ không biết bạn muốn gọi `count` của bạn hay `std::count`, gây lỗi biên dịch ngay lập tức!
2. **Tuyệt đối cấm trong tệp Header (`.h`)**: Nếu bạn đặt `using namespace std;` trong header, mọi tệp `.cpp` `#include` header đó đều bị "nhiễm độc" namespace, không thể cứu vãn!
:::

::: tip 💡 Thực Hành Tốt Nhất (Best Practice)
1. **Ưu tiên gõ tiền tố tường minh**: Hãy viết `std::cout`, `std::string`, `std::vector`. Rất rõ ràng, trong sáng!
2. Nếu muốn ngắn gọn, chỉ dùng **Khai báo using cục bộ** bên trong hàm: `using std::cout;`.
:::
"""
save_lesson("7_13-using-declarations-and-using-directives.md", lesson_7_13)

lesson_7_14 = r"""# 7.14 — Không Gian Tên Không Tên và Inline (Unnamed and Inline Namespaces)

---

## 🎯 Mục Tiêu Bài Học
- Hiểu khái niệm **Không gian tên không tên (Unnamed / Anonymous Namespace)**: Giải pháp hiện đại thay thế cho `static` để kích hoạt Internal Linkage.
- Hiểu **Không gian tên nội tuyến (Inline Namespace)** và ứng dụng phiên bản hóa API không phá vỡ mã cũ.

---

## 1. Không Gian Tên Không Tên (Unnamed Namespace)

Khi bạn định nghĩa một `namespace` mà không đặt tên:

```cpp
#include <iostream>

namespace // Không có tên!
{
    void doSomethingInternal() // Hàm này tự động có Internal Linkage!
    {
        std::cout << "Ham noi bo\n";
    }
}

int main()
{
    doSomethingInternal(); // Gọi trực tiếp như thể nằm ở global scope
    return 0;
}
```

Trình biên dịch sẽ tự động gán cho nó một tên độc nhất vô nhị nội bộ. Tất cả các hàm, biến bên trong Unnamed Namespace đều có **Internal Linkage**.

::: tip 💡 Chuẩn ISO C++ Khuyến Nghị
Trong các tệp nguồn `.cpp`, **hãy ưu tiên sử dụng Unnamed Namespace thay cho từ khóa `static`** khi muốn tạo các hàm và biến nội bộ!
:::

---

## 2. Không Gian Tên Nội Tuyến (Inline Namespace) và Phiên Bản Hóa API

Từ khóa `inline namespace` biến toàn bộ thành viên của namespace con thành thành viên trực tiếp của namespace cha mà không cần gõ tên con:

```cpp
namespace App
{
    inline namespace V2 // Phiên bản mới nhất là mặc định!
    {
        void doWork() { std::cout << "Version 2.0\n"; }
    }

    namespace V1 // Phiên bản cũ giữ lại tương thích ngược
    {
        void doWork() { std::cout << "Version 1.0\n"; }
    }
}

int main()
{
    App::doWork();     // Tự động gọi V2 (Version 2.0)!
    App::V1::doWork(); // Ai muốn dùng bản cũ vẫn gọi được V1!
    return 0;
}
```
"""
save_lesson("7_14-unnamed-and-inline-namespaces.md", lesson_7_14)

lesson_7_x = r"""# 7.x — Tổng Kết Chương 07 & Bài Tập Toàn Diện (Chapter 7 Summary and Quiz)

---

## 🎯 Mục Tiêu Bài Học
- Hệ thống hóa toàn bộ kiến thức Chương 07: Scope, Lifetime, Duration, Linkage, Namespaces, Inline variables.
- Kiểm tra năng lực qua hệ thống bài tập thực chiến có lời giải chi tiết.

---

## 📝 Hệ Thống Bài Tập Thực Chiến

### Bài tập 1: Dự đoán kết quả in ra
```cpp
#include <iostream>

int g_x { 10 };

void foo()
{
    static int s_val { 1 };
    int local_val { 1 };
    
    ++s_val;
    ++local_val;
    
    std::cout << s_val << ':' << local_val << ' ';
}

int main()
{
    foo();
    foo();
    foo();
    return 0;
}
```
::: details [Xem lời giải]
- `local_val` có Automatic duration, mỗi lần gọi hàm đều được tạo mới thành 1, tăng lên thành 2, rồi bị hủy khi thoát hàm.
- `s_val` có Static duration, duy trì giá trị qua các lần gọi: lần 1 tăng lên 2, lần 2 tăng lên 3, lần 3 tăng lên 4.
- In ra: `2:2 3:2 4:2`.
:::

### Bài tập 2: Thiết kế module hằng số chuẩn C++17
Hãy tạo tệp header `MonsterConstants.h` định nghĩa các hằng số game bên trong namespace `Monster`:
- `maxHealth` kiểu int bằng 100
- `baseSpeed` kiểu double bằng 14.5
Đảm bảo tệp header có thể được include bởi nhiều tệp `.cpp` mà không gây lỗi ODR hay tốn bộ nhớ.

::: details [Xem lời giải]
```cpp
// MonsterConstants.h
#pragma once

namespace Monster
{
    inline constexpr int maxHealth { 100 };
    inline constexpr double baseSpeed { 14.5 };
}
```
:::
"""
save_lesson("7_x-chapter-7-summary-and-quiz.md", lesson_7_x)

print("🎉 Completed Chapter 07 (15 lessons) successfully!")
