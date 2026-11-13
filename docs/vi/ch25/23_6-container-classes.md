# 23.6 — Các Lớp Vỏ Chứa (Container Classes)

---

## 🎯 Mục Tiêu Bài Học
- Hiểu định nghĩa và vai trò của **Lớp vỏ chứa (Container Class)** trong C++.
- Tự tay cài đặt hoàn chỉnh lớp mảng động `IntArray` an toàn từ số 0.
- Nắm vững các thao tác: Cấp phát lại (`reallocate`), Thay đổi kích thước (`resize`), Chèn phần tử (`insertAt`), Xóa phần tử (`remove`).
- Tuân thủ nguyên lý **RAII (Resource Acquisition Is Initialization)** để ngăn chặn tuyệt đối rò rỉ bộ nhớ (Memory Leak).

---

## 1. Container Class Là Gì?

Một **Container Class** là một lớp được thiết kế với mục đích duy nhất: tổ chức, lưu trữ và quản lý một tập hợp các phần tử khác. Trong Thư viện chuẩn STL của C++, các container kinh điển bao gồm `std::vector`, `std::array`, `std::list`, `std::map`.

Container Class thường được chia làm 2 loại:
1. **Value Containers**: Chứa trực tiếp các bản sao của dữ liệu (Composition).
2. **Reference Containers**: Chứa các con trỏ hoặc tham chiếu tới dữ liệu bên ngoài (Aggregation).

---

## 2. Tự Cài Đặt Lớp Mảng Động `IntArray` Hoàn Chỉnh

Hãy cùng mổ xẻ mã nguồn xây dựng lớp `IntArray` chuyên nghiệp:

```cpp
#include <iostream>
#include <cassert> // Cho phep kiem tra assert

class IntArray
{
private:
    int m_length{ 0 };
    int* m_data{ nullptr };

public:
    // 1. Constructor mac dinh
    IntArray() = default;

    // 2. Constructor tao mang co do dai length
    explicit IntArray(int length) : m_length{ length }
    {
        assert(length >= 0 && "Do dai mang phai lon hon hoac bang 0!");
        if (length > 0)
            m_data = new int[length]{}; // Khoi tao tat ca phan tu bang 0
    }

    // 3. Destructor giai phong Heap tu dong (RAII)
    ~IntArray()
    {
        delete[] m_data;
    }

    // Cam copy ngam dinh de tranh loi Double Free (o bai sau se hoc Rule of 5)
    IntArray(const IntArray&) = delete;
    IntArray& operator=(const IntArray&) = delete;

    // Xoa sach mang
    void erase()
    {
        delete[] m_data;
        m_data = nullptr;
        m_length = 0;
    }

    // Truy cap phan tu voi kiem tra chi so hop le
    int& operator[](int index)
    {
        assert(index >= 0 && index < m_length && "Chi so vuot qua gioi han mang!");
        return m_data[index];
    }

    int operator[](int index) const
    {
        assert(index >= 0 && index < m_length && "Chi so vuot qua gioi han mang!");
        return m_data[index];
    }

    int getLength() const { return m_length; }

    // Cap phat lai vung nho moi (xoa bo du lieu cu)
    void reallocate(int newLength)
    {
        erase();
        if (newLength <= 0)
            return;

        m_data = new int[newLength];
        m_length = newLength;
    }

    // Thay doi kich thuoc mang (GIU LAI DU LIEU CU)
    void resize(int newLength)
    {
        if (newLength == m_length)
            return;

        if (newLength <= 0)
        {
            erase();
            return;
        }

        // Cap phat vung nho moi
        int* data = new int[newLength];

        // Sao chep cac phan tu cu sang vung nho moi
        if (m_length > 0)
        {
            int elementsToCopy = (newLength > m_length) ? m_length : newLength;
            for (int i = 0; i < elementsToCopy; ++i)
                data[i] = m_data[i];
        }

        // Xoa vung nho cu va gan vung nho moi
        delete[] m_data;
        m_data = data;
        m_length = newLength;
    }

    // Chen phan tu tai mot vi tri chi dinh
    void insertAt(int value, int index)
    {
        assert(index >= 0 && index <= m_length && "Vi tri chen khong hop le!");

        int* data = new int[m_length + 1];

        // Sao chep phan tu truoc index
        for (int before = 0; before < index; ++before)
            data[before] = m_data[before];

        // Chen gia tri moi vao index
        data[index] = value;

        // Sao chep cac phan tu con lai
        for (int after = index; after < m_length; ++after)
            data[after + 1] = m_data[after];

        delete[] m_data;
        m_data = data;
        ++m_length;
    }

    // Xoa phan tu tai vi tri index
    void remove(int index)
    {
        assert(index >= 0 && index < m_length && "Vi tri xoa khong hop le!");

        if (m_length == 1)
        {
            erase();
            return;
        }

        int* data = new int[m_length - 1];

        for (int before = 0; before < index; ++before)
            data[before] = m_data[before];

        for (int after = index + 1; after < m_length; ++after)
            data[after - 1] = m_data[after];

        delete[] m_data;
        m_data = data;
        --m_length;
    }
};

int main()
{
    IntArray array{ 5 };

    for (int i = 0; i < array.getLength(); ++i)
        array[i] = (i + 1) * 10;

    std::cout << "Mang ban dau: ";
    for (int i = 0; i < array.getLength(); ++i)
        std::cout << array[i] << ' ';
    std::cout << '\n';

    // Chen phan tu 99 vao vi tri index 2
    array.insertAt(99, 2);

    std::cout << "Sau khi chen 99 vao index 2: ";
    for (int i = 0; i < array.getLength(); ++i)
        std::cout << array[i] << ' ';
    std::cout << '\n';

    // Xoa phan tu tai vi tri index 0
    array.remove(0);

    std::cout << "Sau khi xoa index 0: ";
    for (int i = 0; i < array.getLength(); ++i)
        std::cout << array[i] << ' ';
    std::cout << '\n';

    return 0;
}
```

---

## 3. Quiz & Bài Tập

### Câu hỏi:
Tại sao trong hàm `resize()`, chúng ta phải cấp phát con trỏ mới `int* data = new int[newLength];` trước khi gọi `delete[] m_data;`?
<details>
<summary><b>Xem lời giải</b></summary>

**Đáp án**: Nếu bạn gọi `delete[] m_data;` trước, toàn bộ dữ liệu cũ sẽ bị giải phóng ngay lập tức trên Heap! Khi đó, bạn không còn dữ liệu để sao chép sang mảng mới. Ngoài ra, việc cấp phát trước còn đảm bảo tính an toàn ngoại lệ (Exception Safety): nếu `new` bị lỗi ném ra ngoại lệ `std::bad_alloc`, dữ liệu cũ của đối tượng vẫn còn nguyên vẹn.
</details>
