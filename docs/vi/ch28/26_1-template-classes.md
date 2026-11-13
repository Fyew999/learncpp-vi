# 26.1 — Mẫu Lớp (Class Templates)

---

## 🎯 Mục Tiêu Bài Học
- Hiểu định nghĩa và cú pháp tạo **Mẫu Lớp (Class Template)** trong C++.
- Nắm vững cơ chế **Khởi tạo mẫu (Template Instantiation)** tại thời điểm biên dịch.
- Hiểu tại sao phần định nghĩa hàm thành viên của template bắt buộc phải đặt trong tệp Header (`.h`).

---

## 1. Class Template Là Gì?

Trong bài học về Container ở Chương 23, chúng ta đã viết lớp `IntArray` dành riêng cho kiểu số nguyên `int`. Nếu sau đó bạn cần một mảng chứa số thực `double`, chuỗi `std::string`, hay đối tượng `Point`, bạn sẽ phải viết lại toàn bộ mã nguồn của từng lớp tương ứng?

**Class Template (Mẫu Lớp)** giải quyết dứt điểm sự trùng lặp này bằng cách biến kiểu dữ liệu thành một tham số (`template <typename T>`):

```cpp
#include <iostream>
#include <cassert>

// Khai báo Class Template
template <typename T>
class Array
{
private:
    int m_length{ 0 };
    T* m_data{ nullptr }; // Mảng dữ liệu kiểu T tổng quát

public:
    Array(int length) : m_length{ length }
    {
        assert(length > 0 && "Kich thuoc phai > 0");
        m_data = new T[length]{};
    }

    ~Array()
    {
        delete[] m_data;
    }

    // Cấm sao chép đơn giản để bảo vệ bộ nhớ
    Array(const Array&) = delete;
    Array& operator=(const Array&) = delete;

    T& operator[](int index)
    {
        assert(index >= 0 && index < m_length);
        return m_data[index];
    }

    int getLength() const { return m_length; }
};

int main()
{
    // Khởi tạo mảng số nguyên
    Array<int> intArray{ 3 };
    intArray[0] = 10;
    intArray[1] = 20;
    intArray[2] = 30;

    // Khởi tạo mảng số thực
    Array<double> doubleArray{ 2 };
    doubleArray[0] = 3.14;
    doubleArray[1] = 2.71;

    std::cout << "intArray[1] = " << intArray[1] << '\n';
    std::cout << "doubleArray[0] = " << doubleArray[0] << '\n';

    return 0;
}
```

---

## 2. Bản Chất: Template Không Phải Là Mã Thực Thi!

Một hiểu lầm phổ biến là nghĩ rằng `Array<T>` là một lớp thực tế được tạo ra trong nhị phân. Thực tế:
- Template chỉ là một **bản thiết kế mẫu (Blueprint)** gửi cho trình biên dịch.
- Khi compiler bắt gặp dòng code `Array<int>`, nó sẽ tự động sinh mã nguồn nhị phân cho một lớp thực thụ mang tên `Array<int>`.
- Khi nó gặp `Array<double>`, nó sinh tiếp một lớp thứ hai hoàn toàn độc lập mang tên `Array<double>`.
- Nếu bạn không sử dụng template với kiểu nào, compiler sẽ **không sinh ra bất kỳ byte mã máy nào**!

---

## 3. Cạm Bẫy Phân Tách Header Và CPP

::: danger Lỗi Trình Liên Kết Kinh Điển (Linker Error LNK2019 / undefined reference)
Với các lớp thông thường, chúng ta đặt khai báo trong `.h` và định nghĩa thân hàm trong `.cpp`. Nhưng với **Class Template**, bạn **BẮT BUỘC PHẢI ĐẶT CẢ KHAI BÁO LẪN ĐỊNH NGHĨA TRONG CÙNG MỘT TỆP HEADER**!
:::

Lý do: Khi một file `.cpp` khác gọi `Array<int>`, compiler tại tệp đó bắt buộc phải nhìn thấy toàn bộ mã nguồn của template để có thể "nhân bản" và biên dịch ra lớp `Array<int>`. Nếu thân hàm nằm ở `.cpp` khác, compiler sẽ không thể sinh mã và Linker sẽ báo lỗi `undefined reference` khi kết nối chương trình!
