# 25.4 — Hàm Hủy Ảo (Virtual Destructors) & Cạm Bẫy Quên Virtual Destructor

---

## 🎯 Mục Tiêu Bài Học
- Hiểu cặn kẽ cạm bẫy kinh hoàng: **Quên khai báo Virtual Destructor trong lớp cơ sở khi làm việc với đa hình**.
- Trực quan hóa cơ chế rò rỉ bộ nhớ (Memory Leak) khi gọi `delete` trên con trỏ lớp cơ sở.
- Nắm vững **Quy Tắc Vàng**: Bất kỳ lớp nào có ít nhất một hàm ảo BẮT BUỘC phải có Hàm Hủy Ảo (`virtual ~Base()`).

---

## 1. Kịch Bản Thảm Họa Khi Quên Virtual Destructor

Hãy xem đoạn mã nguy hiểm sau đây:

```cpp
#include <iostream>

class Base
{
public:
    Base() { std::cout << "Base constructor\n"; }
    // NGUY HIỂM CHÍ MẠNG: Destructor KHÔNG CÓ từ khóa virtual!
    ~Base() { std::cout << "Base destructor\n"; }
};

class Derived : public Base
{
private:
    int* m_largeBuffer{ nullptr };

public:
    Derived()
    {
        std::cout << "Derived constructor: Cap phat 1MB Heap\n";
        m_largeBuffer = new int[250000]; // 1 Megabyte
    }

    ~Derived()
    {
        std::cout << "Derived destructor: Giai phong Heap\n";
        delete[] m_largeBuffer;
    }
};

int main()
{
    // Cấp phát đối tượng Derived nhưng giữ bằng con trỏ Base*
    Base* ptr = new Derived();

    // XÓA ĐỐI TƯỢNG QUA CON TRỎ BASE*:
    delete ptr;

    return 0;
}
```

### Kết quả xuất hiện:
```text
Base constructor
Derived constructor: Cap phat 1MB Heap
Base destructor
```

::: danger Thảm Họa Rò Rỉ Bộ Nhớ (Undefined Behavior)
Nhìn vào kết quả: **`Derived destructor` HOÀN TOÀN KHÔNG ĐƯỢC GỌI!**
Bởi vì con trỏ `ptr` có kiểu tĩnh là `Base*`, và `~Base()` không phải là hàm ảo, lệnh `delete ptr` thực hiện liên kết tĩnh và chỉ gọi duy nhất Destructor của `Base`!
Hậu quả:
- Mảng `m_largeBuffer` (1MB) nằm lại vĩnh viễn trên Heap, gây **Rò rỉ bộ nhớ nghiêm trọng (Memory Leak)**!
- Chuẩn ISO C++ quy định: Việc `delete` một đối tượng dẫn xuất qua con trỏ lớp cơ sở không có virtual destructor là **Hành vi không xác định (Undefined Behavior)**!
:::

---

## 2. Giải Pháp Chuẩn Mực: Virtual Destructor

Chỉ cần thêm duy nhất từ khóa `virtual` vào trước hàm hủy của lớp cơ sở:

```cpp
class Base
{
public:
    Base() = default;
    // KHAI BÁO VIRTUAL DESTRUCTOR
    virtual ~Base()
    {
        std::cout << "Base destructor (Virtual: An toan 100%)\n";
    }
};
```

Khi có `virtual ~Base()`, quá trình hủy sẽ diễn ra đa hình:
1. Con trỏ `ptr` tra cứu bảng ảo và gọi `Derived::~Derived()`.
2. `Derived destructor` dọn dẹp sạch sẽ 1MB trên Heap.
3. Sau đó `Base destructor` tự động được kích hoạt để dọn phần còn lại.

---

## 3. Bỏ Qua Cơ Chế Ảo Bằng Toán Tử Phạm Vi

Đôi khi bạn muốn ép chương trình gọi đích danh phiên bản hàm của lớp cha thay vì chạy đa hình, hãy dùng toán tử phạm vi `Base::`:

```cpp
Base* ptr = new Derived();
ptr->Base::speak(); // Bỏ qua vtable, gọi thẳng Base::speak()
```
