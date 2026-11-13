# 25.10 — Ép Kiểu Động (Dynamic Casting) & RTTI

---

## 🎯 Mục Tiêu Bài Học
- Hiểu mục đích của toán tử `dynamic_cast` trong việc chuyển đổi an toàn từ con trỏ lớp cơ sở xuống lớp dẫn xuất (**Downcasting**).
- Nắm vững cơ chế **RTTI (Run-Time Type Information)**.
- Phân biệt hành vi của `dynamic_cast` khi làm việc với con trỏ (trả về `nullptr`) so với tham chiếu (ném ngoại lệ `std::bad_cast`).

---

## 1. Downcasting Là Gì? Vì Sao Cần `dynamic_cast`?

Khi bạn đang nắm giữ một con trỏ `Base*`, nhưng bạn biết (hoặc nghi ngờ) rằng đối tượng thực tế đằng sau nó là một `Derived*`, bạn muốn chuyển đổi kiểu ngược xuống con để gọi một hàm chuyên biệt mà chỉ con mới có. Thao tác này gọi là **Downcasting**.

Sử dụng `static_cast` để downcast là cực kỳ nguy hiểm vì nó không kiểm tra tính hợp lệ tại runtime. Nếu con trỏ thực tế không phải là kiểu con đó, bạn sẽ gặp lỗi Undefined Behavior.
`dynamic_cast` sinh ra để thực hiện việc kiểm tra an toàn này tại thời điểm chạy:

```cpp
#include <iostream>
#include <string>

class Base
{
public:
    // dynamic_cast BẮT BUỘC lớp Base phải có ít nhất 1 hàm virtual để kích hoạt RTTI!
    virtual ~Base() = default;
};

class Derived : public Base
{
public:
    void doSomethingSpecial()
    {
        std::cout << "Goi tinh nang dac biet cua Derived!\n";
    }
};

class OtherDerived : public Base
{
};

int main()
{
    Base* b1 = new Derived();
    Base* b2 = new OtherDerived();

    // 1. ÉP KIỂU HỢP LỆ:
    Derived* d1 = dynamic_cast<Derived*>(b1);
    if (d1) // Kiểm tra nullptr
    {
        std::cout << "Cast b1 thanh cong!\n";
        d1->doSomethingSpecial();
    }

    // 2. ÉP KIỂU KHÔNG HỢP LỆ: b2 thực chất là OtherDerived, không phải Derived!
    Derived* d2 = dynamic_cast<Derived*>(b2);
    if (d2 == nullptr)
    {
        std::cout << "Cast b2 THAT BAI! dynamic_cast tra ve nullptr an toan.\n";
    }

    delete b1;
    delete b2;
    return 0;
}
```

---

## 2. Dynamic Cast Với Tham Chiếu (References)

Vì tham chiếu trong C++ không thể mang giá trị null, nếu `dynamic_cast` thất bại trên kiểu tham chiếu, nó sẽ **ném ra ngoại lệ `std::bad_cast`** (nằm trong thư viện `<typeinfo>`):

```cpp
#include <typeinfo>

void process(Base& b)
{
    try
    {
        Derived& d = dynamic_cast<Derived&>(b);
        d.doSomethingSpecial();
    }
    catch (const std::bad_cast& e)
    {
        std::cout << "Loi ep kieu tham chieu: " << e.what() << '\n';
    }
}
```

---

## 3. Lời Khuyên Về Phong Cách Thiết Kế

::: warning Cảnh Báo "Mùi Mã Nguồn" (Code Smell)
Nếu bạn nhận thấy mã nguồn của mình xuất hiện dày đặc các lệnh `if (dynamic_cast<TypeA*>(ptr)) ... else if (dynamic_cast<TypeB*>(ptr))`, bạn đang vi phạm nghiêm trọng nguyên lý thiết kế hướng đối tượng! 
Thay vì liên tục hỏi đối tượng "Bạn là ai?", hãy thêm một hàm ảo `virtual` vào lớp cha và để cơ chế đa hình tự động giải quyết.
:::
