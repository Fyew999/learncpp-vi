# 0.13 — Kiểm Tra Tiêu Chuẩn C++ Đang Sử Dụng

---

## 🎯 Mục Tiêu Bài Học
- Hiểu cách Macro chuẩn `__cplusplus` lưu trữ mã định danh phiên bản C++.
- Tự viết chương trình kiểm tra phiên bản C++ đang hoạt động trên máy bạn.

---

## 1. Macro `__cplusplus` Là Gì?

Mỗi trình biên dịch tuân thủ chuẩn ISO đều định nghĩa sẵn một hằng số đặc biệt có tên là **`__cplusplus`**. Giá trị của macro này là một số nguyên đại diện cho năm và tháng mà tiêu chuẩn đó được phê chuẩn:

| Tiêu Chuẩn C++ | Giá Trị Macro `__cplusplus` | Ý Nghĩa (Năm/Tháng) |
| :--- | :--- | :--- |
| **C++98** | `199711L` | Tháng 11 năm 1997 |
| **C++11** | `201103L` | Tháng 03 năm 2011 |
| **C++14** | `201402L` | Tháng 02 năm 2014 |
| **C++17** | `201703L` | Tháng 03 năm 2017 |
| **C++20** | `202002L` | Tháng 02 năm 2020 |
| **C++23** | `202302L` | Tháng 02 năm 2023 |

---

## 2. Chương Trình Tự Động Nhận Diện Phiên Bản C++

Hãy tạo một tệp `check_version.cpp` và chạy đoạn mã sau để biết chính xác trình biên dịch của bạn đang ở phiên bản nào:

```cpp
#include <iostream>

int main()
{
    std::cout << "Gia tri macro __cplusplus la: " << __cplusplus << "

";

    if (__cplusplus == 202302L)
        std::cout << "Chuc mung! Trinh bien dich dang hoat dong o che do: C++23!
";
    else if (__cplusplus == 202002L)
        std::cout << "Tuyet voi! Ban dang su dung chuan: C++20!
";
    else if (__cplusplus == 201703L)
        std::cout << "Ban dang su dung chuan: C++17.
";
    else if (__cplusplus == 201402L)
        std::cout << "Ban dang su dung chuan: C++14.
";
    else if (__cplusplus == 201103L)
        std::cout << "Ban dang su dung chuan cu: C++11.
";
    else if (__cplusplus == 199711L)
        std::cout << "Canh bao: Trinh bien dich dang o chuan co dien C++98!
";
    else
        std::cout << "Che do dac biet hoac phien ban thu nghiem C++26 (Ma: " << __cplusplus << ")
";

    return 0;
}
```

::: info Lưu ý đối với Visual Studio
Trên Visual Studio, theo mặc định giá trị macro `__cplusplus` có thể bị giữ ở mức `199711L` để tương thích ngược. Để Visual Studio trả về giá trị chuẩn, bạn cần thêm cờ `/Zc:__cplusplus` vào phần cấu hình `Additional Options` của trình biên dịch!
:::
