# 10.8 — Suy Luận Kiểu Cho Biến Với Từ Khóa `auto`

---

## 🎯 Mục Tiêu Bài Học
- Hiểu cơ chế Suy luận kiểu (Type Deduction) trong C++11 thông qua từ khóa `auto`.
- Nắm rõ nguyên lý: `auto` hoạt động 100% tại thời điểm biên dịch (Compile-time), hoàn toàn KHÔNG có chi phí thời gian chạy (Zero Runtime Overhead).
- Tránh các cạm bẫy: `auto` tự động loại bỏ tính bất biến (`const`) và tham chiếu (`&`).

---

## 1. `auto` Là Gì? Tại Sao Nên Dùng?

Trong các phiên bản C++ cũ, bạn luôn phải khai báo kiểu dữ liệu tường minh lặp đi lặp lại:
```cpp
int a = 5;
double b = 3.14;
```
Nhưng hãy nhìn vào dòng code: Giá trị khởi tạo `5` rõ ràng là kiểu `int`, giá trị `3.14` rõ ràng là kiểu `double`. Tại sao ta phải gõ lại một điều mà compiler thừa sức biết?

Từ C++11, từ khóa **`auto`** cho phép trình biên dịch tự động suy luận kiểu dữ liệu của biến dựa vào **kiểu của giá trị khởi tạo (Initializer)**.

```cpp
int main()
{
    auto a{ 5 };       // Suy luận ra int
    auto b{ 3.14 };    // Suy luận ra double
    auto c{ 10.0f };   // Suy luận ra float
    auto d{ 'Z' };     // Suy luận ra char
    auto e{ true };    // Suy luận ra bool
    return 0;
}
```

```mermaid
flowchart LR
    Init["Giá trị khởi tạo: 5 (kiểu int)"] -->|Compiler Phân Tích Lúc Dịch| Auto["auto x { 5 }"]
    Auto --> CodeGen["Sinh mã máy: int x { 5 }"]
    CodeGen --> Binary["Binary hoàn hảo - 0% chi phí runtime"]
```

---

## 2. Quy Tắc Bắt Buộc: Phải Có Giá Trị Khởi Tạo

Compiler chỉ có thể suy luận kiểu nếu bạn cung cấp giá trị khởi tạo ngay khi khai báo:
```cpp
// auto x; // LỖI BIÊN DỊCH: error: declaration of 'auto x' has no initializer
```

---

## 3. Cạm Bẫy Lớn Nhất: `auto` Vứt Bỏ `const` Và `&`

Theo quy tắc suy luận chuẩn của C++, khi một biến được khởi tạo bằng `auto`:
1. Mọi tham chiếu (`&`) của giá trị khởi tạo sẽ bị loại bỏ.
2. Mọi `const` ở cấp cao nhất (Top-level const) sẽ bị vứt bỏ!

```cpp
#include <iostream>

int main()
{
    const int x{ 10 };
    auto y = x; // y có kiểu là 'int', KHÔNG PHẢI 'const int'!

    y = 20; // Hợp lệ! y có thể sửa đổi thoải mái!

    // Nếu muốn giữ const, bạn phải thêm const tường minh:
    const auto z = x; // z có kiểu 'const int'
    // z = 30; // Lỗi biên dịch!

    return 0;
}
```

---

## 4. Lợi Ích Của `auto` Trong Thực Chiến

1. **Không bao giờ có biến rác chưa khởi tạo**: Vì `auto` bắt buộc phải có giá trị khởi tạo.
2. **Tránh lỗi chuyển đổi thu hẹp vô tình**:
   ```cpp
   // Nếu viết: int len = str.length(); // Nguy cơ lỗi vì length() trả về size_t (unsigned 64-bit)
   auto len = str.length(); // Tuyệt đối chính xác 100% kiểu size_t!
   ```
3. **Mã nguồn ngắn gọn, thanh thoát**: Đặc biệt khi làm việc với các kiểu phức tạp của STL như `std::vector<int>::const_iterator`.

---

## 📝 Bài Tập Tự Luyện & Quiz Củng Cố

### Câu hỏi 1:
Kiểu dữ liệu thực sự của biến `val` sau khi biên dịch là gì?
```cpp
const double d{ 9.99 };
auto val{ d };
```
A) `const double`  
B) `double`  
C) `float`  
D) Lỗi biên dịch

::: details [Xem lời giải]
**Đáp án đúng: B**  
Giải thích: `auto` tự động loại bỏ `const` cấp cao nhất khi khởi tạo theo giá trị (copy). Do đó `val` trở thành một biến `double` bình thường độc lập với `d`.
:::
