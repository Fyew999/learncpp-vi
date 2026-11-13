# 26.x — Tổng Kết Chương 26 & Bài Kiểm Tra Toàn Diện

---

## 🎯 Mục Tiêu
- Hệ thống hóa toàn bộ kiến thức về Class Templates và Kỹ thuật Chuyên biệt hóa (Specialization).
- Vượt qua bài kiểm tra lập trình thiết kế lớp Ma Trận Toán Học (`Matrix<T, Rows, Cols>`) tổng quát.

---

## 1. Bảng Tóm Tắt Khái Niệm

| Kỹ Thuật | Cú Pháp Minh Họa | Ứng Dụng Thực Chiến |
| :--- | :--- | :--- |
| **Class Template** | `template <typename T> class Foo` | Tạo các container tổng quát (`vector`, `list`) |
| **Non-Type Parameter** | `template <typename T, std::size_t N>` | Mảng cố định Stack (`std::array`), kích thước compile-time |
| **Full Specialization** | `template <> class Foo<int>` | Tối ưu hóa cực hạn cho kiểu cụ thể (`Storage8<bool>`) |
| **Partial Specialization** | `template <typename T> class Foo<T*>` | Xử lý chuyên biệt cho con trỏ, mảng, tham chiếu |

---

## 2. Bài Tập Thực Chiến: Thiết Kế Lớp `Matrix<T, Rows, Cols>`

### Yêu cầu:
Sử dụng Non-Type Template Parameter để xây dựng lớp Ma trận toán học `Matrix` với:
- Kiểu phần tử `T`, số hàng `Rows`, số cột `Cols`.
- Mảng 2 chiều trực tiếp trên Stack: `T m_data[Rows][Cols]`.
- Nạp chồng `operator()` để truy cập `matrix(row, col)`.
- Phương thức `fill(T value)` và `print()`.

`<details>`
`<summary>``<b>`Xem mã nguồn lời giải hoàn chỉnh

```cpp
#include <iostream>
#include <cassert>

template <typename T, std::size_t Rows, std::size_t Cols>
class Matrix
{
private:
    T m_data[Rows][Cols]{};

public:
    T& operator()(std::size_t row, std::size_t col)
    {
        assert(row < Rows && col < Cols && "Vuot qua gioi han ma tran!");
        return m_data[row][col];
    }

    const T& operator()(std::size_t row, std::size_t col) const
    {
        assert(row < Rows && col < Cols && "Vuot qua gioi han ma tran!");
        return m_data[row][col];
    }

    void fill(const T& value)
    {
        for (std::size_t r = 0; r < Rows; ++r)
            for (std::size_t c = 0; c < Cols; ++c)
                m_data[r][c] = value;
    }

    void print() const
    {
        std::cout << "Ma tran (" << Rows << "x" << Cols << "):\n";
        for (std::size_t r = 0; r < Rows; ++r)
        {
            for (std::size_t c = 0; c < Cols; ++c)
            {
                std::cout << m_data[r][c] << "\t";
            }
            std::cout << '\n';
        }
    }
};

int main()
{
    Matrix<int, 2, 3> mat;
    mat.fill(0);
    mat(0, 0) = 1;
    mat(0, 1) = 2;
    mat(0, 2) = 3;
    mat(1, 0) = 4;
    mat(1, 1) = 5;
    mat(1, 2) = 6;

    mat.print();

    return 0;
}
```

