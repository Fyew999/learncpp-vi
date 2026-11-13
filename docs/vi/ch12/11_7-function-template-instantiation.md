# 11.7 — Hiện Thực Hóa Mẫu Hàm (Template Instantiation)

---

## 🎯 Mục Tiêu Bài Học
- Hiểu quá trình Hiện thực hóa mẫu hàm (Template Instantiation) diễn ra tại thời điểm biên dịch.
- Nắm vững cơ chế Tự động suy luận đối số mẫu (Template Argument Deduction).
- Phân biệt giữa Hiện thực hóa ngầm định (Implicit Instantiation) và tường minh (Explicit Instantiation).

---

## 1. Bản Thân Template KHÔNG PHẢI Là Mã Máy!

Một hiểu lầm rất phổ biến của người mới học là nghĩ rằng `template` là một hàm vạn năng chạy được trong runtime.

**SỰ THẬT**:
- Bản thân Function Template không hề chiếm 1 byte mã máy nào trong tệp thực thi `.exe`!
- Khi bạn gọi template trong code, trình biên dịch sẽ đọc bản thiết kế đó, thay thế `T` bằng kiểu cụ thể (ví dụ `int`), và **tự tay sinh ra một hàm C++ thực thụ bằng mã máy**.
- Quá trình này được gọi là **Hiện thực hóa mẫu (Template Instantiation)**, và hàm được sinh ra gọi là **Hàm thể hiện (Template Instance / Instantiated Function)**.

---

## 2. Suy Luận Đối Số Mẫu Tự Động (Template Argument Deduction)

Trong hầu hết các trường hợp, bạn không cần phải viết `<int>` hay `<double>`. Compiler đủ thông minh để tự nhìn vào kiểu của các đối số truyền vào và suy luận ra `T`:

```cpp
#include <iostream>

template <typename T>
T max(T x, T y)
{
    return (x > y) ? x : y;
}

int main()
{
    // Không cần viết max<int>(5, 6)
    std::cout << max(5, 6) << '
';     // Compiler tự suy luận T là int!
    std::cout << max(3.14, 2.71) << '
'; // Compiler tự suy luận T là double!
    return 0;
}
```

---

## ⚠️ Cạm Bẫy: Xung Đột Suy Luận Kiểu (Deduction Ambiguity)

```cpp
int main()
{
    // max(5, 6.7); // LỖI BIÊN DỊCH!
    // error: no matching function for call to 'max(int, double)'
    // note: template parameter 'T' deduced as 'int' and then 'double'
    return 0;
}
```
Tại sao lại lỗi? Vì trong định nghĩa mẫu `T max(T x, T y)`, cả hai tham số đều có cùng kiểu `T`.  
Compiler thấy tham số thứ nhất là `int` -> suy ra `T = int`.  
Nhưng tham số thứ hai lại là `double` -> suy ra `T = double`.  
Hai kết luận mâu thuẫn nhau, compiler sẽ từ chối tự ý ép kiểu và báo lỗi!

### Cách giải quyết:
1. **Ép kiểu tường minh bằng góc ngoặc**: `max<double>(5, 6.7);` -> Ép `5` thành `double 5.0`.
2. **Dùng `static_cast`**: `max(static_cast<double>(5), 6.7);`
3. **Thiết kế mẫu với nhiều kiểu tham số**: Học ngay ở bài 11.8 tiếp theo!

---

## 📝 Bài Tập Tự Luyện & Quiz Củng Cố

### Câu hỏi 1:
Hiện thực hóa mẫu hàm (Template Instantiation) diễn ra vào thời điểm nào?
A) Thời điểm chạy chương trình (Runtime)  
B) Thời điểm tiền xử lý (Preprocessor)  
C) Thời điểm biên dịch (Compile-time)  
D) Thời điểm nạp chương trình vào RAM (Loading time)

::: details [Xem lời giải]
**Đáp án đúng: C**  
Giải thích: Toàn bộ quá trình kiểm tra kiểu và sinh mã thực thi cho template đều diễn ra 100% tại compile-time bởi trình biên dịch.
:::
