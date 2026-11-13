# 7.13 — Khai Báo Using và Chỉ Thị Using (Using Declarations and Directives)

---

## 🎯 Mục Tiêu Bài Học
- Phân biệt rõ ràng giữa **Khai báo using (Using-declaration)** và **Chỉ thị using (Using-directive)**.
- Hiểu tại sao `using namespace std;` được coi là một thói quen xấu cần tránh.
- Phạm vi tác dụng của `using` trong các khối mã cục bộ.

---

## 1. Khai Báo Using (Using-declaration)

Khai báo using đưa **đúng một định danh cụ thể** từ namespace vào phạm vi hiện tại:

```cpp
#include <iostream>

int main()
{
    using std::cout; // Chỉ đưa duy nhất cout vào scope!

    cout << "Xin chao!\n"; // Hợp lệ!
    // cin >> x;           // Lỗi: cin vẫn cần std::cin!
    return 0;
}
```

---

## 2. Chỉ Thị Using (Using-directive)

Chỉ thị using đưa **TẤT CẢ mọi định danh** trong namespace vào phạm vi hiện tại:

```cpp
using namespace std; // Mở tung toàn bộ hàng trăm nghìn định danh của std!
```

::: danger ⚠️ Vì Sao Phải Tuyệt Đối Tránh `using namespace std;`?
1. **Xung đột tên bất ngờ (Ambiguity Errors)**: C++ chuẩn có sẵn các hàm phổ biến như `count`, `min`, `max`, `size`, `move`. Nếu bạn định nghĩa hàm `int count = 5;`, trình biên dịch sẽ không biết bạn muốn gọi `count` của bạn hay `std::count`, gây lỗi biên dịch ngay lập tức!
2. **Tuyệt đối cấm trong tệp Header (`.h`)**: Nếu bạn đặt `using namespace std;` trong header, mọi tệp `.cpp` `#include` header đó đều bị "nhiễm độc" namespace, không thể cứu vãn!
:::

::: tip 💡 Thực Hành Tốt Nhất (Best Practice)
1. **Ưu tiên gõ tiền tố tường minh**: Hãy viết `std::cout`, `std::string`, `std::vector`. Rất rõ ràng, trong sáng!
2. Nếu muốn ngắn gọn, chỉ dùng **Khai báo using cục bộ** bên trong hàm: `using std::cout;`.
:::
