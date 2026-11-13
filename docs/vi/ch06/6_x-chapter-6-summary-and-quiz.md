# 6.x — Tổng Kết Chương 06 & Bài Tập Toàn Diện (Chapter 6 Summary and Quiz)

---

## 🎯 Mục Tiêu Bài Học
- Hệ thống hóa toàn bộ kiến thức cốt lõi của Chương 06: Toán tử, Thứ tự ưu tiên, Side effects, Phép chia, So sánh số thực và Logic.
- Rèn luyện kỹ năng phân tích biểu thức phức hợp và gỡ lỗi logic.
- Hoàn thành bộ bài tập thực chiến có lời giải chi tiết.

---

## 1. Bảng Khắc Cốt Ghi Tâm Của Chương 06

1. **Precedence vs Associativity**:
   - *Precedence* quyết định ai là toán hạng của ai.
   - *Associativity* quyết định hướng gom nhóm (L-&gt;R hay R-&gt;L) khi cùng cấp độ ưu tiên.
   - Cả hai đều **KHÔNG quyết định thứ tự thực thi (Order of Evaluation)** của các biểu thức con độc lập.
2. **Integer Division**: Phép chia 2 số nguyên luôn cắt bỏ phần thập phân. Muốn kết quả thực, ít nhất 1 toán hạng phải là `float` hoặc `double`.
3. **Division by Zero**: Chia số nguyên cho 0 là **Undefined Behavior (UB)** và gây crash.
4. **Modulo `%`**: Kết quả của `a % b` luôn cùng dấu với toán hạng trái `a`.
5. **Prefix vs Postfix**:
   - Luôn ưu tiên tiền tố `++x` (trả về lvalue, không tạo bản sao tạm).
   - Hậu tố `x++` tạo bản sao giá trị cũ rồi mới tăng.
6. **Side Effects**: Không bao giờ thay đổi và đọc cùng một biến nhiều lần trong 1 biểu thức (tránh UB).
7. **Floating Point Comparison**: Không bao giờ dùng `==` hay `!=` trực tiếp với `double`/`float`. Luôn dùng so sánh Epsilon.
8. **Short-circuit Evaluation**: `&&` và `||` sẽ dừng đánh giá ngay khi kết quả đã được ngã ngũ.

---

## 📝 Hệ Thống Bài Tập Thực Chiến Toàn Diện

### Bài tập 1: Dự đoán kết quả biểu thức
Hãy phân tích thứ tự gom nhóm và tính giá trị của các biểu thức sau:
```cpp
int a = 5;
int b = 3;
int c = 2;

int r1 = a + b * c;
int r2 = a / b + c;
int r3 = (a > b) ? a * 2 : b * 3;
int r4 = a - b - c;
```
::: details [Xem lời giải]
- `r1 = a + (b * c) = 5 + (3 * 2) = 11`.
- `r2 = (a / b) + c = (5 / 3) + 2 = 1 + 2 = 3` (phép chia nguyên 5/3 = 1).
- `r3 = (a > b) ? (a * 2) : (b * 3) = (5 > 3) ? 10 : 9 = 10`.
- `r4 = (a - b) - c = (5 - 3) - 2 = 2 - 2 = 0` (tính kết hợp Trái sang Phải).
:::

### Bài tập 2: Tự viết hàm kiểm tra số nguyên chẵn/lẻ an toàn
Viết một hàm `isEven(int n)` trả về `true` nếu `n` chẵn, `false` nếu `n` lẻ. Đảm bảo hàm hoạt động chính xác với cả số nguyên dương, số nguyên âm và số 0.

::: details [Xem lời giải]
```cpp
#include <iostream>

constexpr bool isEven(int n)
{
    // Dùng modulo: Số chẵn chia 2 dư 0 (đúng cho cả số âm, 0 và số dương)
    return (n % 2 == 0);
}

// Hoặc tối ưu bằng bitwise: Bit cuối cùng của số chẵn luôn là 0
constexpr bool isEvenBitwise(int n)
{
    return (n & 1) == 0;
}

int main()
{
    std::cout << std::boolalpha;
    std::cout << isEven(4) << '
';   // true
    std::cout << isEven(-4) << '
';  // true
    std::cout << isEven(0) << '
';   // true
    std::cout << isEven(-7) << '
';  // false
    return 0;
}
```
:::

### Bài tập 3: Mô phỏng bài toán rơi tự do
Viết chương trình yêu cầu người dùng nhập chiều cao ban đầu của một tòa tháp (đơn vị: mét). Sau đó, mô phỏng quả bóng rơi sau mỗi giây ($0, 1, 2, 3, 4, 5$ giây) cho đến khi bóng chạm đất.
Công thức quãng đường rơi: $s = rac{1}{2} 	imes g 	imes t^2$, với $g = 9.8 	ext{ m/s}^2$.

::: details [Xem lời giải]
```cpp
#include <iostream>

// Hằng số gia tốc trọng trường
constexpr double gravity { 9.8 };

// Hàm tính độ cao hiện tại của quả bóng
double calculateHeight(double initialHeight, int seconds)
{
    double distanceFallen { (gravity * seconds * seconds) / 2.0 };
    double currentHeight  { initialHeight - distanceFallen };
    return (currentHeight > 0.0) ? currentHeight : 0.0;
}

void printProgress(double initialHeight, int seconds)
{
    double height = calculateHeight(initialHeight, seconds);
    if (height > 0.0)
    {
        std::cout << "Sau " << seconds << " giay, qua bong dang o do cao: " << height << " met.
";
    }
    else
    {
        std::cout << "Sau " << seconds << " giay, qua bong da cham dat!
";
    }
}

int main()
{
    std::cout << "Nhap chieu cao toa thap (met): ";
    double towerHeight {};
    std::cin >> towerHeight;

    printProgress(towerHeight, 0);
    printProgress(towerHeight, 1);
    printProgress(towerHeight, 2);
    printProgress(towerHeight, 3);
    printProgress(towerHeight, 4);
    printProgress(towerHeight, 5);

    return 0;
}
```
:::
