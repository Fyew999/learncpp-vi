# 10.9 — Suy Luận Kiểu Trả Về Cho Hàm (`auto` Return Type)

---

## 🎯 Mục Tiêu Bài Học
- Nắm vững cú pháp suy luận kiểu trả về của hàm bằng `auto` (C++14).
- Hiểu cú pháp Trailing Return Type (`auto func() -> Type`) từ C++11.
- Nắm bắt quy tắc: Mọi nhánh câu lệnh `return` trong hàm bắt buộc phải trả về cùng một kiểu dữ liệu.

---

## 1. Suy Luận Kiểu Trả Về Của Hàm (C++14)

Từ C++14, bạn có thể đặt từ khóa `auto` ở vị trí kiểu trả về của hàm. Compiler sẽ tự động phân tích biểu thức trong câu lệnh `return` để xác định kiểu trả về thực tế:

```cpp
#include <iostream>

auto add(int x, int y)
{
    return x + y; // Compiler thấy x + y là int -> Suy luận kiểu trả về là int
}

int main()
{
    auto result = add(5, 7);
    std::cout << "Ket qua: " << result << '
';
    return 0;
}
```

---

## 2. Cạm Bẫy Sống Còn: Mọi Nhánh `return` Phải Đồng Nhất Kiểu!

Nếu một hàm có nhiều câu lệnh `return` ở các nhánh `if-else` khác nhau, tất cả các biểu thức `return` đó **bắt buộc phải có cùng kiểu dữ liệu**. Compiler sẽ không cố gắng tìm kiểu chung giữa chúng!

```cpp
// LỖI BIÊN DỊCH TRONG C++!
auto getNumber(bool condition)
{
    if (condition)
        return 5;    // int
    else
        return 6.7;  // double
    // error: inconsistent deduction for auto return type: 'int' and then 'double'
}
```

**Cách khắc phục**:
Hoặc sử dụng `static_cast` tường minh ở một nhánh, hoặc khai báo kiểu trả về cụ thể (ví dụ `double`).

---

## 3. Cú Pháp Trailing Return Type (C++11)

Trong C++11, `auto` còn được kết hợp với cú pháp **Kiểu trả về đặt sau (Trailing Return Type)** bằng dấu mũi tên `->`:

```cpp
auto divide(double x, double y) -> double
{
    return x / y;
}
```

### Tại sao lại cần cú pháp này?
Nó đặc biệt hữu ích khi kiểu trả về phụ thuộc vào tham số của hàm (sẽ học sâu hơn trong phần Mẫu hàm & `decltype` ở Chương 11 và 20). Ngoài ra, nó giúp căn chỉnh các tên hàm thẳng hàng nhau trong các giao diện header:

```cpp
auto getWidth()  -> int;
auto getHeight() -> int;
auto getName()   -> std::string;
```

---

## ⚠️ Giới Hạn Kiến Trúc Của Hàm Dùng `auto`

::: warning Khai báo trước (Forward Declaration) bị giới hạn!
Khi dùng `auto` cho hàm, compiler **bắt buộc phải nhìn thấy toàn bộ phần thân định nghĩa của hàm** trước khi hàm đó được gọi.  
Nếu bạn chỉ khai báo nguyên mẫu hàm:
```cpp
auto foo(); // Khai báo trước
```
Compiler không thể biết `foo()` trả về kiểu gì để cấp phát vùng nhớ stack cho nơi gọi nó -&gt; Báo lỗi biên dịch ngay lập tức!
:::

---

## 📝 Bài Tập Tự Luyện & Quiz Củng Cố

### Câu hỏi 1:
Đoạn mã sau có biên dịch thành công không?
```cpp
auto calculate(int a)
{
    if (a > 0)
        return a;
    return 0;
}
```
A) Lỗi biên dịch vì có 2 câu lệnh return.  
B) Biên dịch thành công vì cả 2 câu lệnh return đều trả về kiểu `int`.  
C) Lỗi vì thiếu kiểu trả về sau dấu `->`.

::: details [Xem lời giải]
**Đáp án đúng: B**  
Giải thích: Hàm có nhiều `return` vẫn hoàn toàn hợp lệ với `auto`, miễn là tất cả các nhánh đều trả về chính xác cùng một kiểu dữ liệu (ở đây cả `a` và `0` đều là `int`).
:::
