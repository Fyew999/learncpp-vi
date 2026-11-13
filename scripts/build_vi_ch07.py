#!/usr/bin/env python3
"""
Generator for Chapter O: Thao Tác Bit (Bit Manipulation) (4 lessons)
Location: docs/vi/ch07/
"""

import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DEST_DIR = os.path.join(BASE_DIR, "docs", "vi", "ch07")
os.makedirs(DEST_DIR, exist_ok=True)

def save_lesson(filename, content):
    path = os.path.join(DEST_DIR, filename)
    with open(path, "w", encoding="utf-8") as f:
        f.write(content.strip() + "\n")
    print(f"✅ Generated: docs/vi/ch07/{filename}")

# ==============================================================================
# Lesson O.1
# ==============================================================================
lesson_O_1 = r"""# O.1 — Cờ Bit (Bit Flags) và Thao Tác Bit Với std::bitset

---

## 🎯 Mục Tiêu Bài Học
- Hiểu khái niệm Cờ Bit (**Bit Flags**) và lợi ích tối ưu hóa dung lượng bộ nhớ RAM trong hệ thống nhúng / game engine.
- Làm quen với lớp `std::bitset` trong thư viện chuẩn `<bitset>`.
- Sử dụng thành thạo các phương thức thao tác bit: `test()`, `set()`, `reset()`, `flip()`, `count()`, `any()`, `all()`, `none()`.
- Nắm vững quy ước đánh số bit: từ phải sang trái, bắt đầu từ bit 0 (Least Significant Bit - LSB).

---

## 1. Bài Toán Tối Ưu Hóa Bộ Nhớ: Tại Sao Cần Cờ Bit?

Trong C++, kiểu dữ liệu `bool` chỉ cần 1 bit để biểu diễn giá trị `true` (1) hoặc `false` (0). Tuy nhiên, vì kiến trúc phần cứng của máy tính chỉ có thể gán địa chỉ bộ nhớ cho từng **Byte (8 bits)**, nên biến `bool` thực tế phải chiếm trọn **1 byte (8 bits)** trong RAM!

Giả sử trong một trò chơi nhập vai (RPG), một nhân vật có 8 trạng thái khác nhau:
1. Đang đói (`isHungry`)
2. Đang khát (`isThirsty`)
3. Bị trúng độc (`isPoisoned`)
4. Bị choáng (`isStunned`)
5. Bị mù (`isBlinded`)
6. Bị câm lặng (`isSilenced`)
7. Bị trói chân (`isRooted`)
8. Bất tử (`isInvulnerable`)

Nếu dùng 8 biến `bool` riêng lẻ, bạn sẽ tiêu tốn $8 \times 1 = 8 \text{ bytes}$ bộ nhớ. Nếu trò chơi có 100,000 thực thể quái vật và NPC, bạn lãng phí tới 700 KB bộ nhớ chỉ cho các trạng thái boolean!

Thay vì vậy, chúng ta có thể nén toàn bộ 8 trạng thái này vào đúng **1 byte duy nhất**, trong đó mỗi bit đại diện cho một trạng thái độc lập. Kỹ thuật này gọi là **Cờ Bit (Bit Flags)**.

```mermaid
flowchart LR
    subgraph OneByte ["1 Byte Duy Nhất (8 Bits Trong RAM)"]
        direction RL
        B7["Bit 7\nBất tử\n(0)"]
        B6["Bit 6\nBị trói\n(0)"]
        B5["Bit 5\nBị câm\n(0)"]
        B4["Bit 4\nBị mù\n(0)"]
        B3["Bit 3\nBị choáng\n(1)"]
        B2["Bit 2\nTrúng độc\n(1)"]
        B1["Bit 1\nĐang khát\n(0)"]
        B0["Bit 0 (LSB)\nĐang đói\n(1)"]
    end
```

---

## 2. Quản Lý Cờ Bit Với `std::bitset`

Để làm việc với cờ bit một cách an toàn và trực quan, C++ cung cấp lớp `std::bitset<N>` nằm trong header `<bitset>`. Trong đó `N` là số lượng bit cố định tại thời điểm biên dịch.

```cpp
#include <bitset>
#include <iostream>

int main()
{
    // Khởi tạo một bitset gồm 8 bit, tất cả bit ban đầu là 0
    std::bitset<8> me {}; 

    // Các bit được đánh số từ PHẢI sang TRÁI (Bit 0 ở ngoài cùng bên phải)
    // Thiết lập bit 0, 2, 3 thành 1
    me.set(0); // Đang đói
    me.set(2); // Bị trúng độc
    me.set(3); // Bị choáng

    std::cout << "Trang thai bitset: " << me << '\n'; // In ra: 00001101

    return 0;
}
```

---

## 3. Các Phương Thức Cốt Lõi Của `std::bitset`

| Phương thức | Chức năng | Ví dụ minh họa |
| :--- | :--- | :--- |
| `test(n)` | Kiểm tra bit tại vị trí `n` có bật (1) hay không | `if (me.test(2)) ...` |
| `set(n)` | Bật bit tại vị trí `n` thành `1` | `me.set(4);` |
| `set()` | Bật **tất cả** các bit thành `1` | `me.set();` |
| `reset(n)` | Tắt bit tại vị trí `n` về `0` | `me.reset(2);` |
| `reset()` | Tắt **tất cả** các bit về `0` | `me.reset();` |
| `flip(n)` | Đảo bit tại vị trí `n` ($0 \to 1$ hoặc $1 \to 0$) | `me.flip(0);` |
| `flip()` | Đảo ngược **toàn bộ** các bit | `me.flip();` |
| `count()` | Đếm tổng số bit đang bật giá trị `1` | `std::cout << me.count();` |
| `size()` | Trả về tổng số bit của bitset (`N`) | `me.size();` |
| `all()` | Trả về `true` nếu TẤT CẢ các bit đều là `1` | `if (me.all()) ...` |
| `any()` | Trả về `true` nếu CÓ ÍT NHẤT một bit là `1` | `if (me.any()) ...` |
| `none()` | Trả về `true` nếu TẤT CẢ các bit đều là `0` | `if (me.none()) ...` |

---

## 4. Thực Hành Tốt Nhất: Đặt Tên Cho Vị Trí Bit Bằng Enum

::: tip 💡 Thực Hành Tốt Nhất (Best Practice)
Tránh dùng các con số ma thuật (magic numbers) như `me.set(3)`. Không ai nhớ nổi bit 3 là trạng thái gì! Hãy dùng một `enum` hoặc hằng số `constexpr` có tên gọi rõ ràng:

```cpp
#include <bitset>
#include <iostream>

namespace CharacterState
{
    enum State
    {
        isHungry,       // 0
        isThirsty,      // 1
        isPoisoned,     // 2
        isStunned,      // 3
        isBlinded,      // 4
        isSilenced,     // 5
        isRooted,       // 6
        isInvulnerable, // 7
        totalStates     // 8
    };
}

int main()
{
    std::bitset<CharacterState::totalStates> hero {};
    hero.set(CharacterState::isPoisoned);
    hero.set(CharacterState::isInvulnerable);

    if (hero.test(CharacterState::isPoisoned))
    {
        std::cout << "Anh hung dang bi trung doc!\n";
    }

    return 0;
}
```
:::

---

## 📝 Hệ Thống Quiz & Bài Tập Tự Luyện

### Câu hỏi 1:
Cho bitset `std::bitset<8> b { 0b0000'0101 };`. Sau khi gọi `b.flip(1);` và `b.reset(0);`, chuỗi nhị phân của `b` sẽ là bao nhiêu?
::: details [Xem lời giải]
- Ban đầu: `b = 00000101` (bit 0 = 1, bit 1 = 0, bit 2 = 1).
- `b.flip(1)`: Đảo bit 1 từ 0 thành 1 -> `00000111`.
- `b.reset(0)`: Tắt bit 0 về 0 -> `00000110`.
- Kết quả: `00000110`.
:::
"""
save_lesson("O_1-bit-flags-and-bit-manipulation-via-stdbitset.md", lesson_O_1)

# ==============================================================================
# Lesson O.2
# ==============================================================================
lesson_O_2 = r"""# O.2 — Các Toán Tử Trên Bit (Bitwise Operators)

---

## 🎯 Mục Tiêu Bài Học
- Nắm vững 6 toán tử thao tác trực tiếp trên từng bit:
  - Bitwise NOT (`~`)
  - Bitwise AND (`&`)
  - Bitwise OR (`|`)
  - Bitwise XOR (`^`)
  - Dịch trái (`<<`) và Dịch phải (`>>`)
- Phân biệt triệt để toán tử Bitwise (`&`, `|`) và toán tử Logic (`&&`, `||`).
- Hiểu cơ chế dịch bit số học (Arithmetic shift) vs dịch bit logic (Logical shift).
- Nhận thức nguy cơ Undefined Behavior khi dịch bit số nguyên có dấu âm hoặc vượt quá độ rộng bit.

---

## 1. Bản Chất Các Toán Tử Bitwise

Toán tử bitwise thao tác trực tiếp trên từng bit nhị phân trong bộ nhớ máy tính. Chúng chỉ áp dụng cho **các kiểu dữ liệu số nguyên** (`int`, `char`, `unsigned`, v.v.).

```mermaid
flowchart TD
    subgraph Ops ["6 Toán Tử Bitwise Trong C++"]
        direction TB
        N["NOT một ngôi: ~x\nĐảo toàn bộ bit (0 -> 1, 1 -> 0)"]
        A["AND hai ngôi: x & y\nBit 1 khi cả hai bit đều là 1"]
        O["OR hai ngôi: x | y\nBit 1 khi ít nhất một bit là 1"]
        X["XOR hai ngôi: x ^ y\nBit 1 khi đúng một trong hai bit là 1"]
        L["Left Shift: x << n\nDịch sang trái n bit (x nhân 2^n)"]
        R["Right Shift: x >> n\nDịch sang phải n bit (x chia 2^n)"]
    end
```

---

## 2. Chi Tiết Từng Toán Tử Bitwise

### 2.1. Toán tử Đảo Bit (Bitwise NOT `~`)
Đảo ngược từng bit của toán hạng: `0` thành `1`, `1` thành `0`.

Ví dụ với số nguyên không dấu 8-bit (`uint8_t`):
```
  ~ 0000 1100 (12)
  = 1111 0011 (243)
```

### 2.2. Toán tử Bitwise AND (`&`)
So sánh từng cặp bit tương ứng. Kết quả là `1` nếu và chỉ nếu **cả hai bit đều là 1**:
```
    0 1 0 1 (5)
  & 0 0 1 1 (3)
  ---------
  = 0 0 0 1 (1)
```

### 2.3. Toán tử Bitwise OR (`|`)
So sánh từng cặp bit. Kết quả là `1` nếu **ít nhất một trong hai bit là 1**:
```
    0 1 0 1 (5)
  | 0 0 1 1 (3)
  ---------
  = 0 1 1 1 (7)
```

### 2.4. Toán tử Bitwise XOR (`^` - Exclusive OR)
So sánh từng cặp bit. Kết quả là `1` nếu **hai bit khác nhau**:
```
    0 1 0 1 (5)
  ^ 0 0 1 1 (3)
  ---------
  = 0 1 1 0 (6)
```

::: tip 💡 Đặc tính siêu việt của phép XOR: Tự đảo ngược chính nó
$$A \oplus B \oplus B = A$$
Phép toán XOR thường được dùng để mã hóa đối xứng đơn giản, tìm phần tử xuất hiện lẻ trong mảng, hoặc hoán đổi giá trị hai biến mà không cần biến phụ:
```cpp
x = x ^ y;
y = x ^ y;
x = x ^ y;
```
:::

---

## 3. Toán Tử Dịch Bit: Dịch Trái (`<<`) và Dịch Phải (`>>`)

### 3.1. Dịch Trái (`<<`)
Khi thực hiện `x << n`:
- Toàn bộ các bit của `x` được dịch sang bên trái `n` vị trí.
- Các bit ngoài cùng bên trái bị rơi ra ngoài và biến mất.
- Các vị trí trống mới sinh ra ở ngoài cùng bên phải luôn được **lấp đầy bằng số 0**.
- **Ý nghĩa toán học**: Dịch trái $n$ bit tương đương với phép nhân số nguyên với $2^n$: $x \times 2^n$.

```
  0000 0101 (5) << 1
= 0000 1010 (10)
```

### 3.2. Dịch Phải (`>>`)
Khi thực hiện `x >> n`:
- Toàn bộ các bit dịch sang phải `n` vị trí. Các bit ngoài cùng bên phải bị rơi ra.
- Với số nguyên không dấu (**Unsigned** - Logical shift): Các vị trí trống bên trái luôn được điền số `0`.
- **Ý nghĩa toán học**: Dịch phải $n$ bit tương đương với phép chia nguyên cho $2^n$: $\lfloor x / 2^n \rfloor$.

---

## 4. Cạm Bẫy Thực Chiến & Undefined Behavior (UB)

::: danger ⚠️ Cạm Bẫy 1: Dịch Bit Với Số Âm và Dịch Quá Số Lượng Bit
1. Dịch số bit âm: `x << -2` hoặc `x >> -1` là **Undefined Behavior (UB)**!
2. Dịch số lượng bit lớn hơn hoặc bằng kích thước kiểu dữ liệu: Nếu `x` là `int` 32-bit, thì `x << 32` hoặc `x << 35` là **Undefined Behavior (UB)**!
3. Dịch trái một số nguyên có dấu làm tràn bit dấu (Signed Overflow) là **UB** trước C++20.
:::

::: warning ⚠️ Cạm Bẫy 2: Nhầm Lẫn Giữa Bitwise (`&`, `|`) và Logic (`&&`, `||`)
- `5 && 2`: Cả 5 và 2 đều khác 0 (là `true`), nên `true && true` cho ra `true` (`1`).
- `5 & 2`: Biểu diễn nhị phân $0101_2 \ \& \ 0010_2 = 0000_2 = 0$.
Hai kết quả hoàn toàn trái ngược nhau!
:::

---

## 5. 🚀 Cập Nhật C++20: Thư Viện `<bit>` Siêu Tối Ưu

C++20 bổ sung thư viện `<bit>` tận dụng trực tiếp các chỉ thị CPU tốc độ cao (như lệnh `POPCNT`, `BSF` trên x86):
```cpp
#include <bit>
#include <iostream>

int main()
{
    unsigned int x = 0b0000'1000'0000'0000;

    // Đếm số bit 1 (Population Count)
    std::cout << "So bit 1: " << std::popcount(x) << '\n'; // 1

    // Đếm số bit 0 liên tiếp từ bên trái (Leading Zeros)
    std::cout << "Leading zeros: " << std::countl_zero(x) << '\n';

    // Xoay bit vòng tròn (Bit rotation)
    unsigned char val = 0b1000'0001;
    std::cout << "Rotate left: " << (int)std::rotl(val, 1) << '\n'; // 00000011

    return 0;
}
```

---

## 📝 Hệ Thống Quiz & Bài Tập Tự Luyện

### Câu hỏi 1:
Giá trị của biểu thức `1u << 3` là bao nhiêu?
::: details [Xem lời giải]
`1u` là số 1 kiểu unsigned ($00000001_2$). Dịch trái 3 bit: $00001000_2 = 2^3 = 8$.
:::

### Câu hỏi 2:
Không dùng phép nhân `*`, hãy viết hàm nhân một số nguyên dương `x` với 10 bằng cách kết hợp dịch bit `<<` và phép cộng `+`.
::: details [Xem lời giải]
Ta có: $x \times 10 = x \times (8 + 2) = (x \times 8) + (x \times 2) = (x \ll 3) + (x \ll 1)$.
```cpp
constexpr unsigned int multiplyBy10(unsigned int x)
{
    return (x << 3) + (x << 1);
}
```
:::
"""
save_lesson("O_2-bitwise-operators.md", lesson_O_2)

# ==============================================================================
# Lesson O.3
# ==============================================================================
lesson_O_3 = r"""# O.3 — Kỹ Thuật Thao Tác Bit Với Mặt Nạ Bit (Bit Manipulation with Bit Masks)

---

## 🎯 Mục Tiêu Bài Học
- Hiểu khái niệm **Mặt nạ bit (Bit Mask)** và cách tạo mặt nạ bằng tiền tố nhị phân `0b` hoặc toán tử dịch bit `1u << n`.
- Làm chủ 4 thao tác kinh điển không thể thiếu trong lập trình hệ thống:
  1. **Kiểm tra bit (Test bit)**
  2. **Bật bit (Set bit)**
  3. **Tắt bit (Clear bit)**
  4. **Đảo bit (Toggle bit)**
- Ứng dụng thực tế: Đóng gói và giải nén màu sắc RGBA 32-bit (Color packing/unpacking).
- Cập nhật các hàm `std::bit_cast` (C++20) và `std::byteswap` (C++23).

---

## 1. Mặt Nạ Bit (Bit Mask) Là Gì?

Một **mặt nạ bit (Bit Mask)** là một hằng số nhị phân có các bit được thiết kế đặc biệt (thường chỉ có 1 bit duy nhất bật `1`, hoặc một cụm bit xác định) nhằm phục vụ việc đọc, sửa đổi hoặc xóa các bit cụ thể trên một biến số mục tiêu mà **không làm ảnh hưởng đến các bit còn lại**.

```mermaid
flowchart TD
    subgraph Masks ["Cách Định Nghĩa Bit Mask Trong C++"]
        M1["Hằng số nhị phân C++14:\nconstexpr uint8_t mask0 = 0b0000'0001;"]
        M2["Dịch bit tường minh:\nconstexpr uint8_t mask3 = (1u << 3);"]
        M3["Hằng số Hexa:\nconstexpr uint32_t redMask = 0xFF000000;"]
    end
```

---

## 2. Bốn Thao Tác Thần Thánh Với Mặt Nạ Bit

Dưới đây là 4 thao tác mà mọi kỹ sư lập trình nhúng, game engine, hệ điều hành và an ninh mạng bắt buộc phải thuộc lòng:

```mermaid
classDiagram
    class BitOperations {
        +Test Bit: (value & mask) != 0
        +Set Bit: value |= mask
        +Clear Bit: value &= ~mask
        +Toggle Bit: value ^= mask
    }
```

### 2.1. Kiểm Tra Bit (Testing a Bit)
Dùng toán tử **Bitwise AND (`&`)**:
```cpp
constexpr std::uint8_t mask2 { 1u << 2 }; // Mặt nạ bit 2: 0000 0100

if ((flags & mask2) != 0)
{
    // Bit 2 đang BẬT (1)
}
```

### 2.2. Bật Bit (Setting a Bit)
Dùng toán tử **Bitwise OR (`|=`)**:
Bất kỳ bit nào kết hợp OR với 1 đều biến thành 1; kết hợp OR với 0 giữ nguyên giá trị cũ.
```cpp
flags |= mask2; // Bật bit 2 thành 1 (các bit khác không đổi)
```

### 2.3. Tắt Bit (Clearing a Bit)
Dùng toán tử **Bitwise AND kết hợp NOT (`&= ~mask`)**:
`~mask` sẽ biến bit mục tiêu thành 0 và biến tất cả các bit còn lại thành 1!
```
  flags:  1101 1101
  mask2:  0000 0100
 ~mask2:  1111 1011
-------------------
  flags & ~mask2 = 1101 1001 (Bit 2 đã bị tắt về 0!)
```
```cpp
flags &= ~mask2; // Tắt bit 2 về 0
```

### 2.4. Đảo Bit (Toggling a Bit)
Dùng toán tử **Bitwise XOR (`^=`)**:
Bit nào XOR với 1 sẽ bị đảo ngược ($0 \to 1, 1 \to 0$); XOR với 0 giữ nguyên.
```cpp
flags ^= mask2; // Đảo trạng thái bit 2
```

---

## 3. Ứng Dụng Thực Chiến: Nén và Giải Nén Màu Sắc RGBA (32-bit Color)

Một pixel màu RGBA bao gồm 4 kênh: Đỏ (Red), Lục (Green), Lam (Blue) và Độ trong suốt (Alpha). Mỗi kênh là một giá trị 8-bit từ $0$ đến $255$.
Ta có thể nén cả 4 kênh vào đúng 1 số nguyên không dấu 32-bit `std::uint32_t`:

```cpp
#include <iostream>
#include <cstdint>

// Hàm đóng gói 4 kênh 8-bit thành 1 số 32-bit
std::uint32_t packRGBA(std::uint8_t r, std::uint8_t g, std::uint8_t b, std::uint8_t a)
{
    return (static_cast<std::uint32_t>(r) << 24) |
           (static_cast<std::uint32_t>(g) << 16) |
           (static_cast<std::uint32_t>(b) << 8)  |
           (static_cast<std::uint32_t>(a));
}

int main()
{
    // Màu cam rực rỡ với độ trong suốt 50%: R=255, G=128, B=0, A=128
    std::uint32_t pixel = packRGBA(255, 128, 0, 128);

    // Giải nén kênh Green (Lục) bằng Bit Mask và dịch bit
    constexpr std::uint32_t greenMask { 0x00FF0000 };
    std::uint8_t extractedGreen = static_cast<std::uint8_t>((pixel & greenMask) >> 16);

    std::cout << "Kenh Green duoc giai nen: " << static_cast<int>(extractedGreen) << '\n'; // 128
    return 0;
}
```

---

## 4. 🚀 Cập Nhật C++20 và C++23: An Toàn Bộ Nhớ

::: info 🚀 C++20: `std::bit_cast`
Trong C/C++ cũ, lập trình viên thường dùng ép kiểu con trỏ `*(int*)&float_var` để đọc biểu diễn nhị phân của số thực. Điều này vi phạm nghiêm trọng **Quy tắc biệt danh nghiêm ngặt (Strict Aliasing Rule)** và là Undefined Behavior!
C++20 mang đến `std::bit_cast` trong `<bit>`, cho phép sao chép bit trực tiếp an toàn tuyệt đối ngay tại compile-time:
```cpp
#include <bit>
#include <cstdint>

float f = 1.0f;
auto bits = std::bit_cast<std::uint32_t>(f); // An toàn chuẩn ISO!
```
:::

::: info 🚀 C++23: `std::byteswap`
C++23 bổ sung hàm `std::byteswap` trong `<bit>` giúp đảo ngược thứ tự các byte (Big Endian <-> Little Endian) siêu nhanh mà không cần viết hàm thủ công.
:::

---

## 📝 Hệ Thống Quiz & Bài Tập Tự Luyện

### Câu hỏi 1:
Nếu viết `flags &= mask;` thay vì `flags &= ~mask;`, điều gì thảm khốc sẽ xảy ra?
::: details [Xem lời giải]
`flags &= mask;` sẽ xóa sạch TẤT CẢ các bit khác về 0, và chỉ giữ lại bit được chỉ định trong mask! Trong khi ý đồ của "Clear bit" là chỉ xóa duy nhất bit mục tiêu và BẢO LƯU tất cả các bit còn lại. Quên dấu `~` là một trong những lỗi kinh hoàng nhất trong lập trình vi điều khiển.
:::
"""
save_lesson("O_3-bit-manipulation-with-bitwise-operators-and-bit-masks.md", lesson_O_3)

# ==============================================================================
# Lesson O.4
# ==============================================================================
lesson_O_4 = r"""# O.4 — Chuyển Đổi Số Nguyên Giữa Hệ Nhị Phân và Thập Phân (Binary and Decimal Conversion)

---

## 🎯 Mục Tiêu Bài Học
- Hiểu sâu sắc bản chất hệ cơ số 2 (Base-2 / Binary) và hệ cơ số 10 (Base-10 / Decimal).
- Nắm vững trọng số của từng bit nhị phân ($2^0, 2^1, 2^2, 2^3, ..., 2^7$).
- Thành thạo 2 thuật toán chuyển đổi:
  1. Thuật toán trừ dần lũy thừa của 2.
  2. Thuật toán chia liên tiếp cho 2 (Short division by 2).
- Tự tay viết chương trình C++ in ra chuỗi nhị phân của số nguyên bất kỳ.
- Sử dụng các tính năng hiện đại: `std::format` (C++20) và `std::println` (C++23).

---

## 1. Trọng Số Của Các Bit Nhị Phân

Trong hệ thập phân, mỗi chữ số có trọng số là lũy thừa của 10 ($10^0, 10^1, 10^2$). Trong hệ nhị phân, mỗi bit chỉ có thể nhận giá trị `0` hoặc `1`, và trọng số của nó là **lũy thừa của 2**:

| Vị trí bit | Bit 7 | Bit 6 | Bit 5 | Bit 4 | Bit 3 | Bit 2 | Bit 1 | Bit 0 |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **Trọng số ($2^n$)** | **128** | **64** | **32** | **16** | **8** | **4** | **2** | **1** |
| Giá trị bit | 1 | 0 | 1 | 0 | 1 | 1 | 0 | 1 |

Số trên tương đương:
$$1 \times 128 + 0 \times 64 + 1 \times 32 + 0 \times 16 + 1 \times 8 + 1 \times 4 + 0 \times 2 + 1 \times 1 = 173_{10}$$

---

## 2. Hai Thuật Toán Đổi Thập Phân Sang Nhị Phân

```mermaid
flowchart TD
    subgraph Method1 ["Cách 1: Trừ Lũy Thừa Của 2"]
        M1["Tìm lũy thừa 2 lớn nhất <= số cần đổi"] --> M2{"Số hiện tại >= lũy thừa 2?"}
        M2 -- Có --> M3["Ghi bit 1, trừ đi lũy thừa"]
        M2 -- Không --> M4["Ghi bit 0"]
        M3 --> M5["Xét lũy thừa kế tiếp nhỏ hơn"]
        M4 --> M5
    end
    
    subgraph Method2 ["Cách 2: Chia Liên Tiếp Cho 2"]
        D1["Lấy số chia cho 2"] --> D2["Ghi lại phần dư (0 hoặc 1)"]
        D2 --> D3["Tiếp tục lấy thương chia cho 2"]
        D3 --> D4["Đọc các số dư từ dưới lên trên"]
    end
```

---

## 3. Cài Đặt Chương Trình C++ Tự Động In Nhị Phân

Dưới đây là chương trình sử dụng toán tử dịch bit và bit mask để duyệt qua từng bit và in ra màn hình:

```cpp
#include <iostream>
#include <cstdint>

void printBinary8(std::uint8_t n)
{
    // Duyệt từ bit cao nhất (Bit 7) về bit thấp nhất (Bit 0)
    for (int i = 7; i >= 0; --i)
    {
        // Tạo mask: 1u << i
        if ((n & (1u << i)) != 0)
            std::cout << '1';
        else
            std::cout << '0';

        // In dấu phân tách cho dễ đọc ở giữa 4 bit
        if (i == 4)
            std::cout << '\'';
    }
    std::cout << '\n';
}

int main()
{
    std::cout << "173 sang nhi phan: ";
    printBinary8(173); // In ra: 1010'1101
    return 0;
}
```

---

## 4. 🚀 In Định Dạng Nhị Phân Trong C++ Hiện Đại (C++20 và C++23)

Nếu bạn sử dụng C++20 trở lên, bạn không cần phải tự viết vòng lặp in nhị phân nữa!

::: code-group
```cpp [C++20: std::format]
#include <format>
#include <iostream>

int main()
{
    int val = 173;
    // {:08b} nghĩa là: định dạng nhị phân, độ rộng tối thiểu 8 ký tự, điền số 0 phía trước
    std::string binStr = std::format("{:08b}", val);
    std::cout << binStr << '\n'; // 10101101
}
```

```cpp [C++23: std::println]
#include <print>

int main()
{
    int val = 173;
    std::println("Gia tri nhi phan: {:08b}", val);
}
```
:::

---

## 📝 Hệ Thống Quiz & Bài Tập Tự Luyện

### Câu hỏi 1:
Số nhị phân `1101'0010` đổi sang hệ thập phân là bao nhiêu?
::: details [Xem lời giải]
Tính tổng các trọng số có bit 1:
- Bit 7: 128
- Bit 6: 64
- Bit 4: 16
- Bit 1: 2
Tổng: $128 + 64 + 16 + 2 = 210_{10}$.
:::

### Câu hỏi 2:
Số thập phân `93` đổi sang nhị phân 8-bit là bao nhiêu?
::: details [Xem lời giải]
- $93 - 64 = 29$ (Bit 6 = 1)
- $29 - 16 = 13$ (Bit 4 = 1)
- $13 - 8 = 5$ (Bit 3 = 1)
- $5 - 4 = 1$ (Bit 2 = 1)
- $1 - 1 = 0$ (Bit 0 = 1)
Các bit còn lại (7, 5, 1) là 0.
Kết quả: `0101'1101`.
:::
"""
save_lesson("O_4-converting-integers-between-binary-and-decimal-representation.md", lesson_O_4)

print("🎉 Completed Chapter O (4 lessons) successfully!")
