# 26.3 — Chuyên Biệt Hóa Mẫu Hàm (Function Template Specialization)

---

## 🎯 Mục Tiêu Bài Học
- Hiểu khái niệm **Chuyên biệt hóa mẫu (Template Specialization)**.
- Cú pháp chuyên biệt hóa toàn phần cho mẫu hàm: `template <> void func<Type>(...)`.
- Ứng dụng: Xử lý định dạng đặc biệt cho kiểu số thực khoa học hoặc chuỗi ký tự.

---

## 1. Khi Nào Cần Chuyên Biệt Hóa?

Đôi khi một mẫu hàm tổng quát hoạt động tốt cho hầu hết các kiểu dữ liệu, nhưng lại hoạt động không tối ưu hoặc không đúng mong muốn đối với một kiểu dữ liệu cụ thể.

Ví dụ: Bạn muốn in dữ liệu thông thường, nhưng khi gặp kiểu `double`, bạn muốn xuất theo ký hiệu khoa học (`std::scientific`):

```cpp
#include <iostream>
#include <iomanip>

// 1. Mẫu hàm tổng quát (Primary Template)
template <typename T>
void printStorage(const T& value)
{
    std::cout << "Gia tri: " << value << '\n';
}

// 2. Chuyên biệt hóa toàn phần cho kiểu double
template <>
void printStorage<double>(const double& value)
{
    std::cout << "Gia tri (Khoa hoc): " << std::scientific << std::setprecision(4) << value << '\n';
}

int main()
{
    printStorage(100);       // Gọi mẫu hàm tổng quát (int)
    printStorage("Xin chao");// Gọi mẫu hàm tổng quát (const char*)
    printStorage(12345.6789);// Tự động chọn bản CHUYÊN BIỆT HÓA cho double!

    return 0;
}
```

### Kết quả xuất ra:
```text
Gia tri: 100
Gia tri: Xin chao
Gia tri (Khoa hoc): 1.2346e+04
```
