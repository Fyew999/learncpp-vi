# 8.14 — Sinh Số Ngẫu Nhiên Chuẩn Hiện Đại Với Mersenne Twister

---

## 🎯 Mục Tiêu Bài Học
- Sử dụng thuật toán sinh số ngẫu nhiên hàng đầu thế giới: **Mersenne Twister (`std::mt19937`)** trong header `<random>`.
- Lấy hạt giống từ phần cứng với `std::random_device`.
- Phân phối xác suất đều với `std::uniform_int_distribution` và `std::uniform_real_distribution`.
- Tách biệt rõ ràng giữa **Engine sinh số** và **Distribution (Phân phối xác suất)**.

---

## 1. Thiết Kế Chuẩn Mực Trong Header `<random>`

C++ hiện đại chia việc sinh số ngẫu nhiên thành 2 phần độc lập:
1. **Engine**: Bộ máy sinh chuỗi bit ngẫu nhiên (sử dụng `std::mt19937` - chu kỳ siêu dài $2^{19937} - 1$).
2. **Distribution**: Bộ phân phối định hình chuỗi bit thành khoảng giá trị mong muốn (ví dụ: xúc xắc từ 1 đến 6).

```cpp
#include <iostream>
#include <random>

int main()
{
    // 1. Khởi tạo nguồn hạt giống từ phần cứng
    std::random_device rd {};

    // 2. Khởi tạo engine Mersenne Twister với seed từ hardware
    std::mt19937 mt { rd() };

    // 3. Tạo phân phối đều từ 1 đến 6 (như tung xúc xắc)
    std::uniform_int_distribution die6 { 1, 6 };

    for (int i = 0; i < 5; ++i)
    {
        std::cout << die6(mt) << ' '; // Truyền engine vào distribution
    }
    std::cout << '\n';
    return 0;
}
```
