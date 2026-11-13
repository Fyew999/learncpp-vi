# 27.10 — `std::move_if_noexcept` & Đảm Bảo An Toàn Ngoại Lệ

---

## 🎯 Mục Tiêu Bài Học
- Hiểu 4 cấp độ **Đảm bảo an toàn ngoại lệ (Exception Safety Guarantees)**.
- Phân tích cơ chế hoạt động của hàm tiện ích `std::move_if_noexcept` trong C++11.
- Hiểu cách thức `std::vector` tự động cân bằng giữa hiệu năng tối đa và tính toàn vẹn dữ liệu.

---

## 1. Bốn Cấp Độ Đảm Bảo An Toàn Ngoại Lệ

1. **No-throw / Nothrow guarantee**: Hàm đảm bảo không bao giờ ném ngoại lệ (đánh dấu `noexcept`).
2. **Strong guarantee (Đảm bảo mạnh)**: Nếu có ngoại lệ xảy ra, trạng thái toàn bộ chương trình được giữ nguyên như trước khi gọi hàm (Tương tự như cơ chế *Rollback* của giao dịch Database).
3. **Basic guarantee (Đảm bảo cơ bản)**: Không bị rò rỉ bộ nhớ, nhưng dữ liệu có thể bị biến đổi về một trạng thái hợp lệ nào đó.
4. **No guarantee (Không đảm bảo)**: Nếu xảy ra ngoại lệ, rò rỉ tài nguyên hoặc dữ liệu bị phá hủy hoàn toàn.

---

## 2. Cơ Chế Hoạt Động Của `std::move_if_noexcept`

Để đạt được **Strong Exception Guarantee**, hàm `std::move_if_noexcept(x)` hoạt động thông minh:
- Nếu kiểu của `x` có Move Constructor được đánh dấu là `noexcept`: Nó trả về một rvalue reference (`std::move`), kích hoạt cơ chế di chuyển siêu tốc.
- Ngược lại, nếu Move Constructor có nguy cơ ném lỗi: Nó trả về một lvalue reference thông thường, ép trình biên dịch phải dùng **Sao chép (Copy)** an toàn!

```cpp
#include <iostream>
#include <utility> // std::move_if_noexcept

class SafeMove
{
public:
    SafeMove() = default;
    SafeMove(const SafeMove&) { std::cout << "Copy SafeMove\n"; }
    // Khẳng định noexcept: Kích hoạt Move!
    SafeMove(SafeMove&&) noexcept { std::cout << "Move SafeMove (Sieu toc!)\n"; }
};

class RiskyMove
{
public:
    RiskyMove() = default;
    RiskyMove(const RiskyMove&) { std::cout << "Copy RiskyMove (An toan)\n"; }
    // Không có noexcept: Sẽ bị hạ cấp về Copy!
    RiskyMove(RiskyMove&&) { std::cout << "Move RiskyMove\n"; }
};

int main()
{
    SafeMove s;
    RiskyMove r;

    std::cout << "Goi move_if_noexcept voi SafeMove:\n";
    SafeMove s2 = std::move_if_noexcept(s); // In ra: Move SafeMove

    std::cout << "\nGoi move_if_noexcept voi RiskyMove:\n";
    RiskyMove r2 = std::move_if_noexcept(r); // In ra: Copy RiskyMove (Tránh rủi ro ném lỗi)

    return 0;
}
```
