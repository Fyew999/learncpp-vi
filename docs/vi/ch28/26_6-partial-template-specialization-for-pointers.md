# 26.6 — Chuyên Biệt Hóa Mẫu Cho Kiểu Con Trỏ (Specialization for Pointers)

---

## 🎯 Mục Tiêu Bài Học
- Hiểu cách thức áp dụng chuyên biệt hóa một phần cho mọi kiểu con trỏ: `template <typename T> class Storage<T*>`.
- Giải quyết vấn đề giải phóng bộ nhớ tự động (Deep clean) cho các con trỏ được truyền vào container.

---

## 1. Vấn Đề Khi Container Chứa Con Trỏ

Giả sử bạn có lớp mẫu `Storage<T>`. Khi người dùng tạo `Storage<int>`, biến `int` được giải phóng bình thường. Nhưng khi người dùng tạo `Storage<int*>`, biến thành viên là một con trỏ thô:
Khi `Storage` kết thúc vòng đời, Destructor mặc định chỉ hủy bản thân biến con trỏ, mà **KHÔNG GIẢI PHÓNG VÙNG NHỚ TRÊN HEAP MÀ CON TRỎ ĐANG TRỎ TỚI**, gây rò rỉ bộ nhớ nghiêm trọng!

---

## 2. Giải Pháp: Chuyên Biệt Hóa Cho Kiểu `T*`

```cpp
#include <iostream>

// 1. Mẫu tổng quát cho kiểu giá trị thông thường
template <typename T>
class Storage
{
private:
    T m_value;

public:
    Storage(T value) : m_value{ value } {}
    ~Storage() = default;

    void print() const { std::cout << "Gia tri: " << m_value << '\n'; }
};

// 2. CHUYÊN BIỆT HÓA MỘT PHẦN CHO MỌI KIỂU CON TRỎ T*
template <typename T>
class Storage<T*>
{
private:
    T* m_value{ nullptr };

public:
    Storage(T* value) : m_value{ value } {}

    // Destructor tự động dọn dẹp vùng nhớ Heap an toàn (RAII)
    ~Storage()
    {
        std::cout << "Storage<T*> tu dong delete vung nho con tro!\n";
        delete m_value;
    }

    void print() const
    {
        if (m_value)
            std::cout << "Gia tri tro toi: " << *m_value << '\n';
    }
};

int main()
{
    // Đối tượng giá trị thông thường
    Storage<int> s1{ 42 };
    s1.print();

    // Đối tượng con trỏ cấp phát động: Tự động delete khi rời scope!
    {
        Storage<int*> s2{ new int{ 999 } };
        s2.print();
    } // s2 giải phóng int* tại đây, không rò rỉ bộ nhớ!

    return 0;
}
```
