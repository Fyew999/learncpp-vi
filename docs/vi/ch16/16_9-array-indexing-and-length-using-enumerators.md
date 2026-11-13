# 16.9 — Đánh Chỉ Số Mảng Bằng Enum (Array Indexing Using Enumerators)

---

## 🎯 Mục Tiêu Bài Học
- Sử dụng `enum` và `enum class` để đặt tên có ý nghĩa cho các chỉ số mảng, loại bỏ "ma thuật số" (Magic Numbers).
- Áp dụng kỹ thuật đếm phần tử bằng phần tử `max_items` hoặc `count` trong enum.
- Xử lý ép kiểu an toàn khi dùng Scoped Enumerations (`enum class`).

---

## 1. Vấn Đề "Magic Numbers" Khi Đánh Chỉ Số Mảng

Hãy xem xét một mảng lưu trữ số lượng sinh viên theo từng khối lớp:
```cpp
std::vector<int> students(4);
students[0] = 120; // 0 là lớp nào? Năm 1?
students[1] = 115; // 1 là gì?
students[2] = 105;
students[3] = 98;
```
Việc dùng các số `0, 1, 2, 3` trần trụi (Magic Numbers) khiến mã nguồn cực kỳ khó đọc và rất dễ nhầm lẫn.

---

## 2. Giải Pháp: Sử Dụng Enum Làm Chỉ Số

```cpp
#include <iostream>
#include <vector>

namespace StudentClass
{
    enum Type
    {
        freshman,  // 0
        sophomore, // 1
        junior,    // 2
        senior,    // 3
        max_classes // 4 - Kỹ thuật tự động đếm tổng số lớp!
    };
}

int main()
{
    // Tự động khởi tạo vector với số lượng phần tử đúng bằng max_classes
    std::vector<int> students(StudentClass::max_classes);

    students[StudentClass::freshman] = 120;
    students[StudentClass::sophomore] = 115;
    students[StudentClass::junior] = 105;
    students[StudentClass::senior] = 98;

    std::cout << "So sinh vien nam nhat: " << students[StudentClass::freshman] << '
';

    return 0;
}
```

---

## 3. Sử Dụng Scoped Enumerations (`enum class`)

Trong C++ hiện đại, `enum class` được khuyến khích hơn unscoped enum vì tính an toàn kiểu. Tuy nhiên, `enum class` không tự động chuyển đổi ngầm định sang số nguyên, do đó ta cần ép kiểu qua `static_cast` hoặc viết một hàm trợ giúp:

```cpp
#include <iostream>
#include <vector>
#include <type_traits>

enum class Monster
{
    goblin,
    orc,
    troll,
    dragon,
    max_monsters
};

// Hàm chuyển đổi enum class sang size_t tiện dụng
constexpr auto toIndex(Monster m) noexcept
{
    return static_cast<std::size_t>(m);
}

int main()
{
    std::vector<int> monsterCounts(toIndex(Monster::max_monsters));

    monsterCounts[toIndex(Monster::dragon)] = 3;
    std::cout << "So luong rong: " << monsterCounts[toIndex(Monster::dragon)] << '
';

    return 0;
}
```

---

## 4. 💡 Hộp Thực Hành Tốt Nhất (Best Practice)

::: tip Thực hành tốt nhất với Enum Indexing
1. Đặt một enumerator cuối cùng có tên như `max_items` hoặc `count` để tự động đại diện cho tổng số lượng phần tử.
2. Nếu thêm một mục mới vào enum trước `max_items`, kích thước mảng sẽ tự động co giãn theo ở lần biên dịch tiếp theo mà không cần sửa đổi thủ công!
:::

---

## 5. 📝 Hệ Thống Quiz & Bài Tập Tự Luyện

::: details Câu hỏi 1: Kỹ thuật đặt enumerator `max_items` ở cuối enum có ưu điểm vượt trội gì so với việc dùng một hằng số `#define NUM_ITEMS 4`?
**Lời giải chi tiết**:
Khi bạn thêm hoặc bớt một phần tử trong danh sách enum (ví dụ thêm `super_senior`), giá trị số của `max_items` sẽ tự động tăng/giảm tương ứng nhờ cơ chế tự động đánh số tăng dần của enum trong C++. Nếu dùng `#define` hoặc biến `const` rời rạc, lập trình viên rất dễ quên cập nhật số lượng, dẫn đến lỗi mảng bị thiếu phần tử hoặc lãng phí bộ nhớ.
:::
