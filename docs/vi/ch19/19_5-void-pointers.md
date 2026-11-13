# 19.5 — Con Trỏ Vô Kiểu (Void Pointers)

---

## 🎯 Mục Tiêu Bài Học
- Hiểu khái niệm con trỏ vô kiểu (`void*`).
- Nắm vững các hạn chế: Không thể giải tham chiếu trực tiếp, không thể thực hiện số học con trỏ.
- Sử dụng `static_cast` để chuyển đổi kiểu an toàn.
- Hiểu lý do C++ hiện đại thay thế `void*` bằng Templates, `std::any` và `std::variant`.

---

## 1. Con Trỏ Vô Kiểu (`void*`) Là Gì?

**Con trỏ vô kiểu (Void Pointer)** là một con trỏ đặc biệt có thể trỏ tới bất kỳ kiểu dữ liệu nào (từ `int`, `double` cho tới các struct phức tạp):

```cpp
int n{ 10 };
double d{ 3.14 };

void* ptr{ &n }; // Hợp lệ! Trỏ tới int
ptr = &d;        // Cũng hợp lệ! Giờ trỏ tới double
```

---

## 2. Hai Hạn Chế Sống Còn Của `void*`

Vì `void*` không biết đối tượng mà nó trỏ tới có kiểu dữ liệu là gì (chiếm bao nhiêu byte trong bộ nhớ):
1. **Không thể giải tham chiếu trực tiếp**: `*ptr` là lỗi biên dịch vì compiler không biết cần đọc 1 byte, 4 bytes hay 8 bytes!
2. **Không thể làm toán số học con trỏ**: `ptr + 1` là lỗi biên dịch vì compiler không biết bước nhảy là bao nhiêu byte!

Để sử dụng dữ liệu, bạn **bắt buộc phải ép kiểu về con trỏ cụ thể bằng `static_cast`**:

```cpp
#include <iostream>

int main()
{
    int value{ 42 };
    void* vPtr{ &value };

    // Ép kiểu tường minh về int* trước khi giải tham chiếu:
    int* intPtr{ static_cast<int*>(vPtr) };
    std::cout << *intPtr << '
'; // 42

    return 0;
}
```

::: danger Hiểm họa ép nhầm kiểu
Nếu bạn ép nhầm `vPtr` (đang trỏ tới `int`) thành `double*`, trình biên dịch vẫn tin tưởng và cho phép chạy. Khi giải tham chiếu, chương trình sẽ đọc 8 bytes thay vì 4 bytes, gây ra lỗi đọc rác hoặc crash bộ nhớ!
:::

---

## 3. Thay Thế `void*` Trong C++ Hiện Đại

Trong C++ hiện đại, `void*` hầu như chỉ còn tồn tại trong các API cấp thấp của hệ điều hành. Hãy thay thế nó bằng:
- **Function Templates**: Đảm bảo an toàn kiểu 100% tại compile-time.
- **`std::any` (C++17)**: Chứa bất kỳ kiểu nào nhưng có cơ chế kiểm tra kiểu an toàn (Type-safe).
- **`std::variant` (C++17)**: Kiểu tập hợp an toàn cho một danh sách các kiểu cụ thể.

---

## 4. 📝 Hệ Thống Quiz & Bài Tập Tự Luyện

::: details Câu hỏi 1: Tại sao việc gọi `delete vPtr;` trên một con trỏ `void*` lại là một lỗi nguy hiểm nghiêm trọng?
**Lời giải chi tiết**:
Vì `vPtr` không có thông tin về kiểu dữ liệu gốc, toán tử `delete` sẽ không thể biết được đối tượng đó có hàm hủy (Destructor) hay không. Do đó, **hàm hủy của đối tượng sẽ KHÔNG ĐƯỢC GỌI**. Nếu đối tượng đó bên trong có sở hữu tài nguyên (như vector, file handle, socket), toàn bộ tài nguyên đó sẽ bị rò rỉ vĩnh viễn!
:::
