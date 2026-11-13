# 26.4 — Chuyên Biệt Hóa Toàn Phần Mẫu Lớp (Class Template Specialization)

---

## 🎯 Mục Tiêu Bài Học
- Nắm vững cú pháp chuyên biệt hóa toàn phần cho Class Template: `template <> class Storage<SpecificType>`.
- Phân tích ví dụ kinh điển: Tối ưu hóa bộ nhớ cho kiểu `bool` bằng kỹ thuật đóng gói Bitmask (8 bools trong 1 byte).
- Hiểu cấu trúc bên dưới của `std::vector<bool>` trong thư viện chuẩn C++.

---

## 1. Bài Toán Tối Ưu Hóa Bộ Nhớ Cực Hạn

Trong C++, kiểu `bool` chiếm tối thiểu 1 byte (8 bits) bộ nhớ vì CPU không thể định địa chỉ trực tiếp tới từng bit đơn lẻ. Nếu bạn có một lớp `Storage8<T>` lưu trữ 8 phần tử:
- Với `Storage8<int>`: Chiếm $8 \times 4 = 32$ bytes.
- Với `Storage8<bool>`: Chiếm $8 \times 1 = 8$ bytes (lãng phí 56 bits trống!).

Chúng ta có thể viết một **bản chuyên biệt hóa riêng cho `bool`** để đóng gói toàn bộ 8 giá trị boolean vào đúng **1 byte duy nhất** bằng các toán tử thao tác bit!

---

## 2. Cài Đặt Mã Nguồn Chuyên Biệt Hóa `Storage8<bool>`

```cpp
#include <iostream>
#include <cstdint>

// 1. Mẫu lớp tổng quát (Primary Class Template)
template <typename T>
class Storage8
{
private:
    T m_array[8];

public:
    void set(int index, const T& value) { m_array[index] = value; }
    const T& get(int index) const { return m_array[index]; }
};

// 2. CHUYÊN BIỆT HÓA TOÀN PHẦN CHO KIỂU bool
template <>
class Storage8<bool>
{
private:
    // Chỉ dùng DUY NHẤT 1 byte (8 bits) để lưu trữ cả 8 giá trị bool!
    std::uint8_t m_data{ 0 };

public:
    void set(int index, bool value)
    {
        if (value)
            m_data |= (1 << index);  // Bật bit thứ index lên 1
        else
            m_data &= ~(1 << index); // Tắt bit thứ index về 0
    }

    bool get(int index) const
    {
        return (m_data & (1 << index)) != 0; // Trích xuất giá trị bit
    }
};

int main()
{
    // Lớp thông thường
    Storage8<int> intStorage;
    std::cout << "sizeof(Storage8<int>):  " << sizeof(intStorage) << " bytes\n";

    // Lớp chuyên biệt hóa cho bool
    Storage8<bool> boolStorage;
    std::cout << "sizeof(Storage8<bool>): " << sizeof(boolStorage) << " byte! (Sieu tiet kiem!)\n";

    boolStorage.set(0, true);
    boolStorage.set(1, false);
    boolStorage.set(2, true);

    std::cout << "boolStorage[0] = " << boolStorage.get(0) << '\n';
    std::cout << "boolStorage[1] = " << boolStorage.get(1) << '\n';
    std::cout << "boolStorage[2] = " << boolStorage.get(2) << '\n';

    return 0;
}
```

### Kết quả xuất ra:
```text
sizeof(Storage8<int>):  32 bytes
sizeof(Storage8<bool>): 1 byte! (Sieu tiet kiem!)
boolStorage[0] = 1
boolStorage[1] = 0
boolStorage[2] = 1
```
