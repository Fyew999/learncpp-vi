# 6.3 — Phép Chia Lấy Dư và Lũy Thừa (Remainder and Exponentiation)

---

## 🎯 Mục Tiêu Bài Học
- Làm chủ toán tử chia lấy dư `%` (Remainder operator) và quy tắc dấu chuẩn C++11.
- Hiểu tại sao C++ không có toán tử lũy thừa tích hợp (và vì sao ký hiệu `^` KHÔNG PHẢI là lũy thừa!).
- Sử dụng hàm `std::pow` trong thư viện `<cmath>` và nhận diện các cạm bẫy sai số số thực.
- Tự cài đặt hàm tính lũy thừa số nguyên an toàn, hỗ trợ `constexpr` tại compile-time.

---

## 1. Toán Tử Chia Lấy Dư (`%`)

Toán tử chia lấy dư (thường gọi là toán tử modulo / remainder) chỉ hoạt động với **các số nguyên**:

```cpp
int remainder = 17 % 5; // 17 / 5 = 3 dư 2 -> remainder = 2
```

Nếu bạn cố tình dùng `%` với số thực (ví dụ `6.5 % 2`), trình biên dịch sẽ báo lỗi cú pháp. Để lấy dư số thực, bạn phải dùng hàm `std::fmod` trong `<cmath>`.

### Quy Tắc Dấu Của Phép Lấy Dư Trong Chuẩn C++11

Trước C++11, kết quả của `%` với số âm phụ thuộc vào trình biên dịch (Implementation-defined). Từ C++11 trở đi, chuẩn ISO C++ quy định rõ:
$$	ext{Kết quả của } a \% b 	ext{ luôn cùng dấu với toán hạng bên trái } a$$

| Biểu thức | Kết quả | Giải thích |
| :---: | :---: | :--- |
| `7 % 3` | `1` | $7 = 3 	imes 2 + 1$ |
| `-7 % 3` | `-1` | $-7 = 3 	imes (-2) + (-1)$ (Cùng dấu với -7) |
| `7 % -3` | `1` | $7 = (-3) 	imes (-2) + 1$ (Cùng dấu với 7) |
| `-7 % -3` | `-1` | $-7 = (-3) 	imes 2 + (-1)$ (Cùng dấu với -7) |

::: warning ⚠️ Cạm Bẫy: Hàm Kiểm Tra Số Lẻ Bị Sai Với Số Âm
Một lỗi kinh điển khi viết hàm kiểm tra số lẻ:
```cpp
bool isOdd(int n)
{
    return (n % 2 == 1); // 💥 LỖI: Với n = -5, -5 % 2 = -1 -> Hàm trả về false!
}
```
**Cách sửa đúng**:
```cpp
bool isOdd(int n)
{
    return (n % 2 != 0); // ✅ Đúng cho cả số âm và số dương!
}
```
:::

---

## 2. Vì Sao C++ Không Có Toán Tử Lũy Thừa?

Trong nhiều ngôn ngữ khác (như Python), toán tử `**` được dùng để tính lũy thừa ($2^3 = 8$). Một số người mới học C++ thường nhầm lẫn toán tử `^` là lũy thừa.

::: warning ⚠️ Ký hiệu `^` trong C++ là toán tử Bitwise XOR!
Nếu bạn viết:
```cpp
int result = 2 ^ 3;
```
Kết quả **KHÔNG PHẢI là 8**, mà là **1**! Vì:
- $2 = 0010_2$
- $3 = 0011_2$
- $2 \oplus 3 = 0001_2 = 1$.
:::

C++ không tích hợp toán tử lũy thừa vào cú pháp lõi vì:
1. Toán tử này rất ít khi được dùng trong lập trình hệ thống cơ bản so với các phép tính số học khác.
2. Lũy thừa có thể tính toán cho số nguyên, số thực, ma trận, số phức... Mỗi kiểu đòi hỏi thuật toán tối ưu hoàn toàn khác nhau.

---

## 3. Tính Lũy Thừa Bằng `std::pow` và Cạm Bẫy Sai Số Số Thực

Để tính lũy thừa, C++ cung cấp hàm `std::pow(base, exp)` nằm trong thư viện header `<cmath>`:

```cpp
#include <cmath>
#include <iostream>

int main()
{
    double res = std::pow(3.0, 4.0); // 3^4 = 81.0
    std::cout << res << '
';
}
```

::: warning ⚠️ Cạm bẫy chết người khi ép kiểu `std::pow` sang số nguyên!
Hàm `std::pow` nhận và trả về kiểu `double`. Do sai số biểu diễn số thực IEEE 754, giá trị $10^3 = 1000$ có thể được lưu trữ trong bộ nhớ dưới dạng `999.9999999999999`.

Nếu bạn ép kiểu trực tiếp về `int`:
```cpp
int val = static_cast<int>(std::pow(10, 3)); // Có thể bị cắt thành 999 thay vì 1000!
```
:::

---

## 4. Xây Dựng Hàm Tính Lũy Thừa Số Nguyên Chuẩn Hiện Đại (`constexpr`)

Dưới đây là hàm tính lũy thừa nguyên (Integer Exponentiation) sử dụng thuật toán **Lũy thừa nhị phân (Binary Exponentiation)** với độ phức tạp $O(\log n)$, có thể chạy ngay tại compile-time:

```cpp
#include <iostream>
#include <cstdint>

// Hàm constexpr tính lũy thừa số nguyên an toàn tại compile-time
constexpr std::int64_t powint(std::int64_t base, unsigned int exp)
{
    std::int64_t result { 1 };
    while (exp > 0)
    {
        if (exp & 1) // Nếu exp lẻ
            result *= base;
        base *= base;
        exp >>= 1;   // exp chia 2
    }
    return result;
}

int main()
{
    // Tính toán ngay lúc biên dịch!
    constexpr std::int64_t val { powint(2, 10) }; // 2^10 = 1024
    static_assert(val == 1024, "Lỗi tính toán lũy thừa!");

    std::cout << "2^10 = " << val << '
';
    return 0;
}
```

---

## 📝 Hệ Thống Quiz & Bài Tập Tự Luyện

### Câu hỏi 1:
Kết quả của đoạn mã sau là gì?
```cpp
std::cout << (-19 % 4) << " và " << (19 % -4);
```
::: details [Xem lời giải]
- `-19 % 4 = -3` (vì toán hạng trái là số âm `-19`).
- `19 % -4 = 3` (vì toán hạng trái là số dương `19`).
- In ra: `-3 và 3`.
:::

### Bài tập code 2:
Viết chương trình nhập vào một số nguyên dương $N$ và kiểm tra xem $N$ có phải là lũy thừa của 2 hay không (ví dụ: 1, 2, 4, 8, 16... là lũy thừa của 2) mà không dùng `std::pow`.

::: details [Xem lời giải]
Cách 1: Dùng vòng lặp chia 2 lấy dư `%`:
```cpp
#include <iostream>

bool isPowerOfTwo(int n)
{
    if (n <= 0) return false;
    while (n % 2 == 0)
    {
        n /= 2;
    }
    return (n == 1);
}
```
Cách 2 (Siêu tối ưu bằng bitwise): Một số là lũy thừa của 2 chỉ có đúng 1 bit `1` trong biểu diễn nhị phân!
```cpp
bool isPowerOfTwoBitwise(int n)
{
    return (n > 0) && ((n & (n - 1)) == 0);
}
```
:::
