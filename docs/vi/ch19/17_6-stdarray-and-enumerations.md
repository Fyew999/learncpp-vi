# 17.6 — Kết Hợp std::array và Enumerations

---

## 🎯 Mục Tiêu Bài Học
- Sử dụng `std::array` kết hợp với `enum` để tạo các bảng tra cứu tĩnh (Static Lookup Tables).
- Đảm bảo an toàn kiểu tuyệt đối tại compile-time với `enum class`.
- Khởi tạo bảng dữ liệu với số phần tử tự động khớp kích thước của enum.

---

## 1. Xây Dựng Bảng Tra Cứu Tĩnh Bằng `std::array`

Trong lập trình game hoặc các ứng dụng thực tế, ta thường có một danh sách các loại đối tượng cố định kèm theo thuộc tính của chúng:

```cpp
#include <iostream>
#include <string_view>
#include <array>

namespace Weapon
{
    enum Type
    {
        sword,
        bow,
        axe,
        staff,
        max_weapons // 4
    };
}

// Bảng tra cứu tên vũ khí
constexpr std::array<std::string_view, Weapon::max_weapons> weaponNames{
    "Thanh Kiem",
    "Cay Cung",
    "Chiec Riu",
    "Quyen Truong"
};

// Bảng tra cứu sát thương tương ứng
constexpr std::array<int, Weapon::max_weapons> weaponDamages{
    25,
    18,
    35,
    12
};

int main()
{
    Weapon::Type currentWeapon{ Weapon::axe };

    std::cout << "Vu khi hien tai: " << weaponNames[currentWeapon]
              << " | Sat thuong: " << weaponDamages[currentWeapon] << '
';

    return 0;
}
```

---

## 2. Lợi Ích Tuyệt Vời Của Cách Tiếp Cận Này

1. **Khớp kích thước 100% tại compile-time**: Nếu lập trình viên thêm một loại vũ khí mới vào enum (ví dụ `dagger`), trình biên dịch sẽ lập tức báo lỗi thiếu giá trị khởi tạo trong `weaponNames` và `weaponDamages`, ngăn chặn triệt để lỗi quên cập nhật bảng dữ liệu!
2. **Hiệu năng Compile-time (constexpr)**: Bảng dữ liệu có thể được tính toán và lưu trực tiếp trong phân vùng dữ liệu tĩnh (Read-only data segment) của chương trình, chi phí truy cập là $O(1)$ mà không tốn một chu kỳ CPU nào tại runtime.

---

## 3. 📝 Hệ Thống Quiz & Bài Tập Tự Luyện

::: details Câu hỏi 1: Tại sao việc sử dụng `constexpr std::array` làm bảng tra cứu lại vượt trội hơn việc dùng câu lệnh `switch-case` truyền thống?
**Lời giải chi tiết**:
- Bảng tra cứu `std::array` truy cập phần tử qua chỉ số với độ phức tạp $O(1)$ trực tiếp thông qua một phép tính địa chỉ bộ nhớ đơn giản (`base + index * sizeof(T)`), trong khi `switch-case` lớn có thể phải so sánh tuần tự hoặc cần bảng nhảy (jump table).
- Bảng tra cứu cho phép duyệt qua toàn bộ các thuộc tính bằng vòng lặp `for (const auto& w : weaponNames)` cực kỳ dễ dàng, điều mà khối lệnh `switch-case` hoàn toàn không làm được.
:::
