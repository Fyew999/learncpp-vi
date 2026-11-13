# 24.5 — Kế Thừa & Các Từ Khóa Truy Cập (Access Specifiers)

---

## 🎯 Mục Tiêu Bài Học
- Phân biệt phạm vi truy cập: `public`, `private`, và `protected`.
- Hiểu rõ ma trận kế thừa: Kế thừa công khai (`public`), Kế thừa bảo vệ (`protected`), và Kế thừa riêng tư (`private`).
- Đánh giá ưu nhược điểm của từ khóa `protected` trong thiết kế phần mềm.

---

## 1. Từ Khóa `protected` Trong C++

C++ cung cấp thêm phạm vi truy cập thứ ba: **`protected` (được bảo vệ)**:
- **`public`**: Bất kỳ ai, ở bất kỳ đâu cũng có thể truy cập trực tiếp.
- **`private`**: Chỉ chính các hàm thành viên và friend của lớp đó mới được truy cập. Lớp con cũng **KHÔNG THỂ** truy cập trực tiếp.
- **`protected`**: Các hàm bên ngoài không thể truy cập, nhưng **CÁC LỚP DẪN XUẤT ĐƯỢC PHÉP TRUY CẬP TRỰC TIẾP**.

```cpp
class Base
{
public:
    int m_public{ 1 };
protected:
    int m_protected{ 2 }; // Con truy cap duoc, ben ngoai cam!
private:
    int m_private{ 3 };   // Chi Base truy cap duoc!
};

class Derived : public Base
{
public:
    void test()
    {
        m_public = 10;    // HOP LE
        m_protected = 20; // HOP LE: Derived la con nen duoc phep
        // m_private = 30; // LOI BIEN DICH! Private khong the truy cap tu con
    }
};
```

---

## 2. Bảng Ma Trận Kế Thừa Toàn Diện

Kiểu kế thừa (`public`, `protected`, `private`) quy định mức độ quyền hạn tối đa của các thành viên kế thừa khi chuyển giao sang lớp con:

| Thành viên trong Base | Kế thừa `: public Base` | Kế thừa `: protected Base` | Kế thừa `: private Base` |
| :--- | :--- | :--- | :--- |
| **`public`** | Giữ nguyên là **`public`** | Trở thành **`protected`** | Trở thành **`private`** |
| **`protected`** | Giữ nguyên là **`protected`**| Trở thành **`protected`** | Trở thành **`private`** |
| **`private`** | **Không thể truy cập** | **Không thể truy cập** | **Không thể truy cập** |

::: tip Thực Tế Ngành Công Nghiệp
- Hơn **99%** trường hợp bạn sẽ sử dụng **`public inheritance`** vì nó duy trì đúng chuẩn quan hệ "is-a".
- `private inheritance` và `protected inheritance` rất hiếm khi được sử dụng, thường chỉ dùng trong các kỹ thuật chuyên sâu như *Policy-Based Design* hoặc mô phỏng quan hệ *implemented-in-terms-of*.
:::

---

## 3. Cảnh Báo Về Việc Sử Dụng Biến Thành Viên `protected`

::: warning Khuyến Cáo Thực Hành Tốt Nhất
Hạn chế tối đa việc đặt **biến thành viên** ở chế độ `protected`. Hãy giữ biến thành viên là `private` và cung cấp các hàm Getter/Setter ở chế độ `protected` cho lớp con sử dụng. 
Lý do: Nếu bạn cho phép lớp con truy cập trực tiếp vào biến, sau này khi bạn muốn thay đổi kiểu dữ liệu của biến ở lớp cha, bạn sẽ làm hỏng toàn bộ mã nguồn của tất cả các lớp con!
:::

---

## 4. Quiz

### Câu hỏi:
Nếu lớp `Child` kế thừa theo kiểu `private` từ `Parent` (`class Child : private Parent`), thì đối tượng `Child c;` có thể gọi được các hàm `public` của `Parent` từ hàm `main()` không?
`<details>`
`<summary>``<b>`Xem lời giải

**Đáp án**: **KHÔNG THỂ!** Vì qua kế thừa `private`, tất cả các thành viên `public` của `Parent` đã bị biến thành `private` bên trong `Child`. Do đó, người dùng từ bên ngoài `Child` hoàn toàn không thể nhìn thấy chúng.

