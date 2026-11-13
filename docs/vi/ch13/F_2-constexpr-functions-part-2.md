# F.2 — Biểu Thức Hằng & Giới Hạn Của Hàm Constexpr

---

## 🎯 Mục Tiêu Bài Học
- Phân biệt giữa ngữ cảnh bắt buộc compile-time và ngữ cảnh tùy chọn.
- Nắm bắt sự tiến hóa của hàm `constexpr` qua các chuẩn C++ (C++11 vs C++14/C++20).
- Các thao tác bị CẤM trong hàm `constexpr`.

---

## 1. Ngữ Cảnh Bắt Buộc Tính Compile-Time

Làm thế nào để bạn chắc chắn 100% một hàm `constexpr` được compiler tính toán lúc dịch chứ không phải lúc chạy?

Compiler **bắt buộc phải tính tại compile-time** khi kết quả của hàm được sử dụng ở nơi mà ngôn ngữ C++ đòi hỏi hằng số:
1. Khởi tạo một biến `constexpr`: `constexpr int x = func();`
2. Làm đối số Non-type template parameter: `std::array<int, func()>`
3. Khai báo kích thước mảng kiểu C: `int arr[func()];`
4. Dùng trong nhãn `case` của câu lệnh `switch`: `case func():`

Nếu trong các ngữ cảnh trên mà `func()` không thể tính toán được tại compile-time, **trình biên dịch sẽ lập tức báo lỗi!**

```cpp
constexpr int add(int x, int y)
{
    return x + y;
}

int main()
{
    int nonConstVal{ 10 };

    // constexpr int fail = add(nonConstVal, 5);
    // LỖI BIÊN DỊCH: the value of 'nonConstVal' is not usable in a constant expression

    return 0;
}
```

---

## 2. Sự Tiến Hóa Vượt Bậc Của `constexpr` Từ C++14

Trong C++11 thời kỳ đầu, thân hàm `constexpr` cực kỳ hạn chế (chỉ được chứa đúng 1 câu lệnh `return`, không được có vòng lặp hay biến cục bộ).

Từ C++14 và C++20, các rào cản đã bị dỡ bỏ. Bên trong hàm `constexpr` hiện đại, bạn có thể:
- Khai báo biến cục bộ (miễn là không phải `static` hoặc `thread_local`).
- Sử dụng các vòng lặp: `for`, `while`, `do-while`.
- Sử dụng rẽ nhánh phức tạp: `if`, `else`, `switch`.
- Thậm chí cấp phát bộ nhớ động tạm thời (`new`/`delete` - C++20) nếu được giải phóng trước khi hàm kết thúc!

```cpp
constexpr int factorial(int n)
{
    int result{ 1 };
    for (int i{ 2 }; i <= n; ++i) // Vòng lặp for hoàn toàn hợp lệ từ C++14
    {
        result *= i;
    }
    return result;
}

int main()
{
    constexpr int f5 = factorial(5); // Tính ra 120 ngay lúc biên dịch!
    return 0;
}
```

---

## ⚠️ Những Thứ Bị CẤM Tuyệt Đối Trong Hàm `constexpr`
1. Đọc/Ghi I/O (không được dùng `std::cout`, `std::cin`, đọc file).
2. Gọi các hàm thư viện hệ điều hành runtime (như `std::time`, `rand`, `malloc`).
3. Khai báo biến `static` hoặc `thread_local`.

---

## 📝 Bài Tập Tự Luyện & Quiz Củng Cố

### Bài tập code:
Hãy viết một hàm `constexpr int power(int base, int exp)` tính lũy thừa $base^{exp}$ sử dụng vòng lặp. Khởi tạo một biến `constexpr int val` nhận kết quả của `power(2, 8)` để chứng minh nó được tính lúc biên dịch.

::: details [Xem lời giải mẫu]
```cpp
#include <iostream>

constexpr int power(int base, int exp)
{
    int result{ 1 };
    for (int i{ 0 }; i < exp; ++i)
    {
        result *= base;
    }
    return result;
}

int main()
{
    // Bắt buộc tính tại compile-time
    constexpr int val = power(2, 8); // 2^8 = 256
    std::cout << "2^8 = " << val << '
';
    return 0;
}
```
:::
