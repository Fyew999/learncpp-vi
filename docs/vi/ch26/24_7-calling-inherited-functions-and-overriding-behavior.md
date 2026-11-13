# 24.7 — Gọi Hàm Kế Thừa & Tái Định Nghĩa Hành Vi (Redefining Behavior)

---

## 🎯 Mục Tiêu Bài Học
- Biết cách tái định nghĩa (redefine / override tĩnh) hành vi của một hàm kế thừa từ lớp cha.
- Thành thạo việc gọi lại hàm của lớp cha bằng toán tử phạm vi `Base::function()`.
- Nhận biết cạm bẫy đệ quy vô tận dẫn đến sập chương trình vì tràn ngăn xếp (**Stack Overflow**).

---

## 1. Tái Định Nghĩa Hàm (Function Redefinition)

Khi lớp con kế thừa một hàm từ lớp cha nhưng muốn thay đổi cách hoạt động của hàm đó, nó có thể khai báo một hàm có cùng tên, cùng tham số và cùng kiểu trả về với lớp cha:

```cpp
#include <iostream>

class Base
{
public:
    void identify() const
    {
        std::cout << "Day la Base::identify()\n";
    }
};

class Derived : public Base
{
public:
    // Tai dinh nghia lai ham cua Base
    void identify() const
    {
        std::cout << "Day la Derived::identify() da duoc ghi de!\n";
    }
};

int main()
{
    Base b;
    b.identify(); // In ra: Day la Base::identify()

    Derived d;
    d.identify(); // In ra: Day la Derived::identify() da duoc ghi de!

    return 0;
}
```

---

## 2. Gọi Hàm Của Lớp Cha: Toán Tử Định Phạm Vi `Base::`

Trong nhiều trường hợp, lớp con không muốn xóa bỏ hoàn toàn công việc của lớp cha mà chỉ muốn **làm thêm** một số bước sau khi lớp cha hoàn tất. Bạn sử dụng cú pháp `Base::tenHam()`:

```cpp
class Derived : public Base
{
public:
    void identify() const
    {
        Base::identify(); // 1. Goi ham cua lop cha truoc
        std::cout << "-> Va Derived lam them cong viec bo sung tai day!\n";
    }
};
```

::: danger Cạm Bẫy Quên Toán Tử Phạm Vi `Base::`
Nếu bạn quên viết tiền tố `Base::` bên trong hàm trùng tên của `Derived`, hàm sẽ tự gọi lại chính nó:
```cpp
void identify() const
{
    identify(); // LỖI ĐỆ QUY VÔ TẬN! Tràn ngăn xếp (Stack Overflow) ngay lập tức!
}
```
:::

---

## 3. Quiz

### Câu hỏi:
Từ một đối tượng lớp con `Derived d;`, người dùng từ hàm `main()` có thể gọi tường minh hàm gốc của `Base` được không?
<details>
<summary><b>Xem lời giải</b></summary>

**Đáp án**: **HOÀN TOÀN ĐƯỢC!** Người dùng có thể chỉ định rõ toán tử phạm vi: `d.Base::identify();` để buộc trình biên dịch gọi phiên bản của lớp cha thay vì phiên bản bị ghi đè của lớp con.
</details>
