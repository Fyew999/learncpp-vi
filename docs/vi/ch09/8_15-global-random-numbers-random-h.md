# 8.15 — Quản Lý Bộ Sinh Số Ngẫu Nhiên Toàn Cục: Random.h

---

## 🎯 Mục Tiêu Bài Học
- Nhận thức cạm bẫy: Tạo lại `std::mt19937` liên tục trong hàm khiến các số sinh ra bị lặp lại.
- Thiết kế một thư viện header-only `Random.h` chuẩn C++17/C++20 dùng chung cho toàn bộ dự án.

---

## 1. Tệp Header Chuẩn Mực: `Random.h`

```cpp
// Random.h
#pragma once

#include <chrono>
#include <random>

namespace Random
{
    // Khởi tạo engine mt19937 an toàn dùng chung
    inline std::mt19937 generate()
    {
        std::random_device rd {};
        // Kết hợp cả phần cứng lẫn thời gian thực để tạo seed siêu mạnh
        std::seed_seq ss {
            rd(),
            static_cast<std::seed_seq::result_type>(std::chrono::steady_clock::now().time_since_epoch().count())
        };
        return std::mt19937 { ss };
    }

    inline std::mt19937 mt { generate() };

    // Hàm tiện ích sinh số nguyên trong đoạn [min, max]
    inline int get(int min, int max)
    {
        return std::uniform_int_distribution{ min, max }(mt);
    }
}
```

Sử dụng ở bất kỳ đâu chỉ với 1 dòng lệnh:
```cpp
#include "Random.h"
#include <iostream>

int main()
{
    std::cout << "Quay so may man: " << Random::get(1, 100) << '\n';
    return 0;
}
```
