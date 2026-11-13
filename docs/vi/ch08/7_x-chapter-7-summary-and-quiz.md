# 7.x — Tổng Kết Chương 07 & Bài Tập Toàn Diện (Chapter 7 Summary and Quiz)

---

## 🎯 Mục Tiêu Bài Học
- Hệ thống hóa toàn bộ kiến thức Chương 07: Scope, Lifetime, Duration, Linkage, Namespaces, Inline variables.
- Kiểm tra năng lực qua hệ thống bài tập thực chiến có lời giải chi tiết.

---

## 📝 Hệ Thống Bài Tập Thực Chiến

### Bài tập 1: Dự đoán kết quả in ra
```cpp
#include <iostream>

int g_x { 10 };

void foo()
{
    static int s_val { 1 };
    int local_val { 1 };
    
    ++s_val;
    ++local_val;
    
    std::cout << s_val << ':' << local_val << ' ';
}

int main()
{
    foo();
    foo();
    foo();
    return 0;
}
```
::: details [Xem lời giải]
- `local_val` có Automatic duration, mỗi lần gọi hàm đều được tạo mới thành 1, tăng lên thành 2, rồi bị hủy khi thoát hàm.
- `s_val` có Static duration, duy trì giá trị qua các lần gọi: lần 1 tăng lên 2, lần 2 tăng lên 3, lần 3 tăng lên 4.
- In ra: `2:2 3:2 4:2`.
:::

### Bài tập 2: Thiết kế module hằng số chuẩn C++17
Hãy tạo tệp header `MonsterConstants.h` định nghĩa các hằng số game bên trong namespace `Monster`:
- `maxHealth` kiểu int bằng 100
- `baseSpeed` kiểu double bằng 14.5
Đảm bảo tệp header có thể được include bởi nhiều tệp `.cpp` mà không gây lỗi ODR hay tốn bộ nhớ.

::: details [Xem lời giải]
```cpp
// MonsterConstants.h
#pragma once

namespace Monster
{
    inline constexpr int maxHealth { 100 };
    inline constexpr double baseSpeed { 14.5 };
}
```
:::
