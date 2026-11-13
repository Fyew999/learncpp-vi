# 17.5 — Mảng Các Tham Chiếu Qua std::reference_wrapper

---

## 🎯 Mục Tiêu Bài Học
- Hiểu tại sao C++ **nghiêm cấm** việc tạo mảng chứa các tham chiếu thuần túy (`T& arr[]`).
- Giới thiệu **`std::reference_wrapper`** trong thư viện `<functional>`.
- Tạo và thao tác mảng chứa các tham chiếu có thể gán lại và sắp xếp được.

---

## 1. Tại Sao Không Thể Tạo Mảng Các Tham Chiếu?

Trong C++, câu lệnh sau là **BẤT HỢP PHÁP**:
```cpp
int a{ 10 }, b{ 20 };
int& arr[2]{ a, b }; // LỖI BIÊN DỊCH: cannot declare array of references
```

Lý do:
- Tham chiếu trong C++ không phải là một đối tượng độc lập. Nó không có kích thước riêng (`sizeof` tham chiếu thực chất là `sizeof` đối tượng nó trỏ tới) và không thể lấy địa chỉ của chính nó.
- Một mảng yêu cầu các phần tử phải là các đối tượng độc lập có kích thước xác định và có thể đánh địa chỉ bộ nhớ liên tục.

---

## 2. Giải Pháp: `std::reference_wrapper`

Chuẩn C++11 bổ sung **`std::reference_wrapper<T>`** nằm trong `<functional>`. Đây là một class bọc con trỏ bên trong nhưng hành xử giống hệt như một tham chiếu thông thường:

```cpp
#include <iostream>
#include <array>
#include <functional> // for std::reference_wrapper, std::ref

int main()
{
    int x{ 100 };
    int y{ 200 };
    int z{ 300 };

    // Tạo std::array chứa các tham chiếu tới x, y, z!
    std::array<std::reference_wrapper<int>, 3> refArr{ x, y, z };

    // Sửa đổi thông qua mảng tham chiếu:
    refArr[0].get() = 999; // Hoặc refArr[0] = 999;

    std::cout << "Gia tri goc cua x: " << x << '
'; // In ra 999!

    return 0;
}
```

---

## 3. 💡 Hộp Thực Hành Tốt Nhất (Best Practice)

::: tip Khi nào dùng std::reference_wrapper?
Khi bạn muốn tạo một danh sách hoặc một mảng liên kết trỏ tới các biến có sẵn mà không muốn sao chép dữ liệu của chúng, đồng thời không muốn dùng con trỏ thô (`T*`) dễ gây lỗi null pointer.
:::

---

## 4. 📝 Hệ Thống Quiz & Bài Tập Tự Luyện

::: details Câu hỏi 1: Hàm `std::ref()` có vai trò gì khi làm việc với `std::reference_wrapper`?
**Lời giải chi tiết**:
`std::ref(var)` là một hàm tiện ích trợ giúp (helper function) giúp tạo nhanh một đối tượng `std::reference_wrapper<T>` từ biến `var` mà không cần phải gõ tên kiểu dài dòng `std::reference_wrapper<int>(var)`. Tương tự, `std::cref(var)` dùng để tạo một `std::reference_wrapper<const T>` cho tham chiếu hằng.
:::
