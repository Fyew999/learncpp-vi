# 7.2 — Không Gian Tên Tự Định Nghĩa và Toán Tử Phân Giải Phạm Vi (User-Defined Namespaces)

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
