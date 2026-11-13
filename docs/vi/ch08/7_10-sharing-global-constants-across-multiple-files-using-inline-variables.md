# 7.10 — Chia Sẻ Hằng Số Toàn Cục Bằng Biến Inline (Sharing Global Constants)

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
