# 18.4 — Đo Thời Gian Thực Thi Bằng &lt;chrono&gt; (Timing Your Code)

---

## 🎯 Mục Tiêu Bài Học
- Hiểu tầm quan trọng của việc đo lường hiệu năng thực tế (Benchmarking).
- Phân biệt giữa `std::chrono::system_clock`, `steady_clock`, và `high_resolution_clock`.
- Xây dựng lớp đo thời gian tự động theo nguyên lý RAII (`Timer`).

---

## 1. Tại Sao Phải Dùng `std::chrono::steady_clock`?

Khi đo thời gian chạy của một đoạn mã:
- **`system_clock`**: Đồng hồ theo giờ hệ thống thực tế (Wall-clock time). **Không được dùng để benchmark** vì giờ hệ thống có thể bị thay đổi khi đồng bộ NTP hoặc người dùng đổi múi giờ, khiến thời gian đo được có thể bị âm!
- **`steady_clock`**: Đồng hồ đơn điệu (Monotonic clock), đảm bảo luôn luôn tăng đều đặn theo từng nhịp tick của phần cứng. **Đây là lựa chọn chuẩn xác nhất để đo hiệu năng**.

---

## 2. Xây Dựng Lớp `Timer` Tự Động Bằng RAII

```cpp
#include <iostream>
#include <chrono>
#include <vector>
#include <algorithm>

class Timer
{
private:
    using Clock = std::chrono::steady_clock;
    using Second = std::chrono::duration<double, std::ratio<1>>;

    std::chrono::time_point<Clock> m_beg{ Clock::now() };

public:
    void reset()
    {
        m_beg = Clock::now();
    }

    double elapsed() const
    {
        return std::chrono::duration_cast<Second>(Clock::now() - m_beg).count();
    }
};

int main()
{
    constexpr int size{ 100'000 };
    std::vector<int> v(size);
    for (int i{ 0 }; i < size; ++i)
        v[i] = size - i; // Dữ liệu ngược

    Timer t;
    std::sort(v.begin(), v.end());
    std::cout << "Thoi gian chay std::sort cho 100,000 phan tu: " 
              << t.elapsed() << " giay.
";

    return 0;
}
```

---

## 3. 📝 Hệ Thống Quiz & Bài Tập Tự Luyện

::: details Câu hỏi 1: Tại sao khi benchmark một hàm chạy quá nhanh (chỉ mất vài nano-giây), kết quả đo một lần duy nhất thường không chính xác?
**Lời giải chi tiết**:
Bởi vì ở thang đo cực nhỏ, kết quả đo bị chi phối bởi các yếu tố ngoại cảnh của hệ điều hành: chuyển ngữ cảnh tiến trình (Context Switching), độ trễ nạp code vào CPU Cache lần đầu (Warm-up / Cold Cache), và tần số xung nhịp CPU biến thiên. Để benchmark chính xác, ta cần chạy hàm đó trong một vòng lặp hàng triệu lần và lấy thời gian trung bình.
:::
