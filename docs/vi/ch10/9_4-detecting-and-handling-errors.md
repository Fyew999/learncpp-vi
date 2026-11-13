# 9.4 — Phát Hiện và Xử Lý Lỗi (Detecting and Handling Errors)

---

## 🎯 Mục Tiêu Bài Học
- Hiểu chiến lược 3 bước: **Phát hiện lỗi (Detect) $\to$ Báo hiệu lỗi (Signal) $\to$ Xử lý lỗi (Handle)**.
- Các phương pháp báo hiệu lỗi:
  - Giá trị lính canh / Mã lỗi trả về (Sentinel values / Error codes).
  - Đối số đầu ra (Out parameters) và `bool` thành công.
  - 🚀 Giải pháp hiện đại C++17: `std::optional`.
  - 🚀 Đột phá C++23: `std::expected`.

---

## 1. Báo Lỗi Bằng Mã Lỗi vs `std::optional` (C++17)

Cách cổ điển thường dùng một giá trị đặc biệt (như `-1` hoặc `nullptr`) để báo lỗi, nhưng điều này dễ bị lập trình viên bỏ qua không kiểm tra:

```cpp
// Cách cổ điển: Dễ sinh bug nếu người gọi quên kiểm tra nullptr
const char* findUser(int id);
```

### 🚀 Giải Pháp Hiện Đại: `std::optional` (C++17)
`std::optional` trong header `<optional>` thể hiện rõ ràng rằng hàm có thể trả về một giá trị hoặc **không có gì cả (`std::nullopt`)**:

```cpp
#include <iostream>
#include <optional>

std::optional<double> divide(double a, double b)
{
    if (b == 0.0)
        return std::nullopt; // Báo hiệu thất bại!

    return a / b; // Báo hiệu thành công kèm giá trị
}

int main()
{
    auto result = divide(10.0, 2.0);
    if (result.has_value())
    {
        std::cout << "Ket qua: " << result.value() << '\n'; // 5
    }
    else
    {
        std::cout << "Loi: Chia cho 0!\n";
    }
    return 0;
}
```
