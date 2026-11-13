# 25.6 — Mổ Xẻ Bảng Hàm Ảo (vtable) & Con Trỏ Ảo (vptr) Trong Bộ Nhớ RAM

---

## 🎯 Mục Tiêu Bài Học
- **TRỰC QUAN HÓA TOÀN BỘ CƠ CHẾ BẢNG HÀM ẢO (VIRTUAL METHOD TABLE - VTABLE) TRONG RAM**.
- Hiểu cấu trúc con trỏ ẩn `__vptr` được compiler nhúng vào mỗi đối tượng như thế nào.
- Phân tích từng bước chu trình điều phối động (**Dynamic Dispatch**) ở cấp độ mã máy x86-64.
- Giải thích vì sao kích thước đối tượng tăng thêm đúng 8 bytes (trên kiến trúc 64-bit) khi xuất hiện hàm ảo.

---

## 1. Vtable và Vptr Là Gì?

Để thực hiện cơ chế liên kết muộn (Late Binding) với tốc độ nhanh nhất có thể, hầu hết các trình biên dịch C++ (GCC, Clang, MSVC) sử dụng cấu trúc dữ liệu gồm hai thành phần:

1. **Virtual Table (vtable)**: Một mảng tĩnh chứa các con trỏ hàm. Trình biên dịch tạo ra **duy nhất MỘT bảng vtable cho mỗi lớp** có chứa ít nhất một hàm ảo. Bảng này được đặt trong phân vùng bộ nhớ chỉ đọc (**Text / Read-only Data Segment**).
2. **Virtual Pointer (`__vptr`)**: Một con trỏ ẩn được trình biên dịch tự động chèn vào làm **thành viên đầu tiên** của bất kỳ đối tượng nào thuộc lớp có hàm ảo. Con trỏ này trỏ thẳng tới bảng `vtable` tương ứng của lớp đó.

---

## 2. Trực Quan Hóa Cấu Trúc Bộ Nhớ RAM Chi Tiết

Hãy xét phân cấp lớp sau:

```cpp
class Base
{
public:
    virtual void function1() { std::cout << "Base::func1\n"; }
    virtual void function2() { std::cout << "Base::func2\n"; }
    void nonVirtual() {}
};

class D1 : public Base
{
public:
    void function1() override { std::cout << "D1::func1\n"; }
};

class D2 : public Base
{
public:
    void function2() override { std::cout << "D2::func2\n"; }
};
```

### Sơ đồ liên kết bộ nhớ giữa Đối tượng trên Stack/Heap và Vtable trong Read-only Memory:

```
[VÙNG NHỚ ĐỐI TƯỢNG TRONG RAM]                          [PHÂN VÙNG READ-ONLY / TEXT SEGMENT]
                                                       
Đối tượng b (kiểu Base):                                BẢNG VTABLE CỦA Base:
+------------------------------+                        +------------------------------------+
| __vptr (8 bytes)             | ---------------------> | [0]: &Base::function1              |
+------------------------------+                        | [1]: &Base::function2              |
| Biến thành viên của Base...  |                        +------------------------------------+
+------------------------------+                       
                                                       
Đối tượng d1 (kiểu D1):                                 BẢNG VTABLE CỦA D1:
+------------------------------+                        +------------------------------------+
| __vptr (8 bytes)             | ---------------------> | [0]: &D1::function1  (Ghi đè!)     |
+------------------------------+                        | [1]: &Base::function2 (Kế thừa)    |
| Biến thành viên của D1...    |                        +------------------------------------+
+------------------------------+                       
                                                       
Đối tượng d2 (kiểu D2):                                 BẢNG VTABLE CỦA D2:
+------------------------------+                        +------------------------------------+
| __vptr (8 bytes)             | ---------------------> | [0]: &Base::function1 (Kế thừa)    |
+------------------------------+                        | [1]: &D2::function2  (Ghi đè!)     |
| Biến thành viên của D2...    |                        +------------------------------------+
+------------------------------+
```

::: tip Nhận Định Kỹ Thuật Quan Trọng
- Hàm không ảo `nonVirtual()` **KHÔNG** xuất hiện trong vtable. Nó được liên kết tĩnh trực tiếp!
- Dù bạn có tạo ra hàng triệu đối tượng `d1`, chúng đều dùng chung **duy nhất một bảng `vtable của D1`**. Mỗi đối tượng chỉ tốn đúng 8 bytes để lưu con trỏ `__vptr`.
:::

---

## 3. Mổ Xẻ Chu Trình Dynamic Dispatch (Thực Thi Mã Máy)

Khi bạn viết dòng code:
```cpp
Base* ptr = &d1;
ptr->function1();
```

Trình biên dịch dịch lời gọi hàm này thành chỉ thị tương đương mã máy giả lập:
```c
// 1. ptr->__vptr lấy địa chỉ bảng vtable của D1
// 2. Tra cứu ô index 0 (vị trí đã được cấp cho function1 khi biên dịch Base)
// 3. Gọi gián tiếp qua con trỏ hàm:
(*(ptr->__vptr[0]))(ptr);
```

Vì `ptr` trỏ tới `d1`, trường `ptr->__vptr` trỏ tới bảng `vtable của D1`. Tại ô `[0]`, địa chỉ được nạp chính là `&D1::function1`. Kết quả là hàm của lớp con được thực thi hoàn hảo!

---

## 4. Chứng Minh Thực Nghiệm Kích Thước Đối Tượng

```cpp
#include <iostream>

class EmptyWithoutVirtual
{
    int m_data;
};

class EmptyWithVirtual
{
    int m_data;
    virtual void dummy() {}
};

int main()
{
    std::cout << "sizeof(EmptyWithoutVirtual): " << sizeof(EmptyWithoutVirtual) << " bytes\n";
    std::cout << "sizeof(EmptyWithVirtual):    " << sizeof(EmptyWithVirtual) << " bytes\n";
    return 0;
}
```

### Kết quả trên hệ điều hành 64-bit:
```text
sizeof(EmptyWithoutVirtual): 4 bytes
sizeof(EmptyWithVirtual):    16 bytes (4 bytes int + 4 bytes padding + 8 bytes con trỏ __vptr!)
```
