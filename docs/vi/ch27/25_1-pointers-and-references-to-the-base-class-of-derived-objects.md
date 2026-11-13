# 25.1 — Con Trỏ & Tham Chiếu Trỏ Tới Lớp Cơ Sở

---

## 🎯 Mục Tiêu Bài Học
- Hiểu được khả năng độc đáo của C++: Một con trỏ hoặc tham chiếu kiểu lớp cơ sở (`Base*`, `Base&`) có thể trỏ tới bất kỳ đối tượng nào của lớp dẫn xuất (`Derived`).
- Nhận thức hạn chế của liên kết tĩnh (Compile-time Binding): Nếu không dùng hàm ảo, trình biên dịch chỉ gọi hàm của lớp cơ sở dựa trên kiểu của con trỏ, bỏ qua hoàn toàn hành vi của lớp con.
- Đặt nền móng cho sự ra đời của **Tính Đa Hình (Polymorphism)**.

---

## 1. Con Trỏ Lớp Cơ Sở Và Cơ Chế Upcasting

Trong C++, vì một đối tượng lớp dẫn xuất **LÀ MỘT** đối tượng lớp cơ sở (quan hệ "is-a"), bạn hoàn toàn có thể trỏ một con trỏ lớp cơ sở vào địa chỉ của đối tượng lớp con. Quá trình này được gọi là **Upcasting** (ép kiểu ngược lên cha) và diễn ra hoàn toàn tự động, an toàn 100%:

```cpp
#include <iostream>
#include <string_view>

class Base
{
public:
    std::string_view getName() const { return "Base"; }
};

class Derived : public Base
{
public:
    std::string_view getName() const { return "Derived"; }
};

int main()
{
    Derived derived;
    
    // 1. Tham chiếu lớp cơ sở trỏ tới đối tượng lớp con
    Base& ref{ derived };

    // 2. Con trỏ lớp cơ sở trỏ tới địa chỉ đối tượng lớp con
    Base* ptr{ &derived };

    // ĐIỀU BẤT NGỜ XẢY RA:
    std::cout << "derived.getName(): " << derived.getName() << '\n'; // In ra "Derived"
    std::cout << "ref.getName():     " << ref.getName() << '\n';     // In ra "Base" (!)
    std::cout << "ptr->getName():    " << ptr->getName() << '\n';    // In ra "Base" (!)

    return 0;
}
```

---

## 2. Vì Sao Lại In Ra "Base"? (Bản Chất Liên Kết Tĩnh)

Mặc định, trình biên dịch C++ giải quyết các lời gọi hàm dựa trên **kiểu dữ liệu tĩnh của con trỏ / tham chiếu tại thời điểm biên dịch (Compile-time Type)**, chứ không quan tâm đối tượng thực tế trong bộ nhớ RAM là gì:

```
VÙNG NHỚ CỦA ĐỐI TƯỢNG derived TRONG RAM:
+-------------------------------------------------------+ 0x2000
| [Base Subobject]  --> ptr trỏ vào đây (kiểu Base*)   |
+-------------------------------------------------------+ 0x2010
| [Derived Members]                                     |
+-------------------------------------------------------+
```

Khi bạn gọi `ptr->getName()`, trình biên dịch nhìn thấy `ptr` là kiểu `Base*`, do đó nó sinh mã máy trực tiếp gọi thẳng tới hàm `Base::getName()`!
Hành vi này gọi là **Liên kết tĩnh (Static Binding / Early Binding)**.

---

## 3. Bài Toán Thực Tế: Viết Hàm Xử Lý Đa Năng

Hãy tưởng tượng bạn có danh sách động vật gồm `Cat`, `Dog`, `Bird`. Chúng đều kế thừa từ `Animal`.
Nếu chỉ có liên kết tĩnh, bạn sẽ phải viết 3 mảng riêng biệt:
```cpp
std::vector<Cat> cats;
std::vector<Dog> dogs;
std::vector<Bird> birds;
```
Nhưng nếu con trỏ `Animal*` có thể thông minh tự biết đối tượng thực tế của nó là `Cat` để kêu "Meo meo", hay là `Dog` để sủa "Gâu gâu", bạn chỉ cần duy nhất một danh sách:
```cpp
std::vector<Animal*> animals; // Lưu trữ đồng nhất mọi loài vật!
```
Cơ chế thần kỳ đó được gọi là **Tính Đa Hình (Polymorphism)** thông qua **Hàm Ảo (Virtual Functions)** mà chúng ta sẽ khám phá ngay ở bài học tiếp theo!
