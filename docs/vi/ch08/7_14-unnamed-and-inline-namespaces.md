# 7.14 — Không Gian Tên Không Tên và Inline (Unnamed and Inline Namespaces)

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
