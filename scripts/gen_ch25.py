#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import os

BASE_DIR = "/home/nam/Documents/learncpp"
OUT_DIR = os.path.join(BASE_DIR, "docs", "vi", "ch27")
os.makedirs(OUT_DIR, exist_ok=True)

lessons = {}

# 25.1
lessons["25_1-pointers-and-references-to-the-base-class-of-derived-objects.md"] = """# 25.1 — Con Trỏ & Tham Chiếu Trỏ Tới Lớp Cơ Sở

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
    std::cout << "derived.getName(): " << derived.getName() << '\\n'; // In ra "Derived"
    std::cout << "ref.getName():     " << ref.getName() << '\\n';     // In ra "Base" (!)
    std::cout << "ptr->getName():    " << ptr->getName() << '\\n';    // In ra "Base" (!)

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
"""

# 25.2
lessons["25_2-virtual-functions.md"] = """# 25.2 — Hàm Ảo & Tính Đa Hình (Virtual Functions & Polymorphism)

---

## 🎯 Mục Tiêu Bài Học
- Hiểu định nghĩa của **Hàm ảo (Virtual Function)** thông qua từ khóa `virtual`.
- Nắm vững khái niệm **Tính đa hình runtime (Runtime Polymorphism / Dynamic Dispatch)**.
- Biết cách sử dụng con trỏ hoặc tham chiếu lớp cơ sở để thực thi đa hình các hành vi chuyên biệt của lớp con.

---

## 1. Hàm Ảo (Virtual Function) Là Gì?

**Hàm ảo** là một hàm thành viên đặc biệt được khai báo với từ khóa `virtual` trong lớp cơ sở, cho phép trình biên dịch hoãn việc quyết định gọi hàm nào cho tới khi chương trình đang chạy thực tế (**Runtime / Dynamic Binding**). 

Khi một hàm ảo được gọi thông qua con trỏ hoặc tham chiếu lớp cơ sở, C++ sẽ tự động tra cứu loại đối tượng thực tế đang được trỏ tới và gọi phiên bản được ghi đè tương ứng của lớp con đó!

```mermaid
flowchart TD
    Ptr["Con trỏ: Animal* ptr"] -->|"Tại Runtime: Kiểm tra đối tượng thực tế"| Dispatch{Đối tượng là ai?}
    Dispatch -->|"Là Cat"| CatCall["Gọi Cat::speak() -> 'Meo meo'"]
    Dispatch -->|"Là Dog"| DogCall["Gọi Dog::speak() -> 'Gau gau'"]
    Dispatch -->|"Là Cow"| CowCall["Gọi Cow::speak() -> 'Um bo'"]
```

---

## 2. Mã Nguồn Minh Họa Tính Đa Hình Chuẩn Mực

```cpp
#include <iostream>
#include <string_view>
#include <vector>

class Animal
{
protected:
    std::string_view m_name;

public:
    Animal(std::string_view name) : m_name{ name } {}

    // KHAI BÁO HÀM ẢO BẰNG TỪ KHÓA virtual
    virtual std::string_view speak() const
    {
        return "???";
    }

    std::string_view getName() const { return m_name; }
};

class Cat : public Animal
{
public:
    Cat(std::string_view name) : Animal{ name } {}

    // Ghi đè (override) hàm ảo của lớp cha
    virtual std::string_view speak() const
    {
        return "Meo meo";
    }
};

class Dog : public Animal
{
public:
    Dog(std::string_view name) : Animal{ name } {}

    virtual std::string_view speak() const
    {
        return "Gau gau";
    }
};

// Hàm nhận tham chiếu lớp cơ sở nhưng hoạt động ĐA HÌNH tuyệt đối!
void report(const Animal& animal)
{
    std::cout << animal.getName() << " keu tieng: " << animal.speak() << '\\n';
}

int main()
{
    Cat meo{ "Mimi" };
    Dog cho{ "Milu" };

    // Gọi hàm thông qua tham chiếu lớp cơ sở
    report(meo); // In ra: Mimi keu tieng: Meo meo
    report(cho); // In ra: Milu keu tieng: Gau gau

    // Lưu trữ danh sách đa hình bằng mảng con trỏ
    std::vector<const Animal*> zoo{ &meo, &cho };
    std::cout << "\\n--- TIENG KEU TRONG SO THU ---\\n";
    for (const auto* animal : zoo)
    {
        std::cout << animal->getName() << ": " << animal->speak() << '\\n';
    }

    return 0;
}
```

---

## 3. Các Quy Tắc Quan Trọng Về Hàm Ảo

1. **Tính lan truyền tự động**: Nếu một hàm được đánh dấu là `virtual` trong lớp cơ sở, nó sẽ tự động là hàm ảo trong tất cả các lớp dẫn xuất sau này, dù bạn có viết từ khóa `virtual` ở lớp con hay không.
2. **Chữ ký hàm phải giống hệt nhau**: Hàm ở lớp con bắt buộc phải có cùng tên, cùng số lượng kiểu tham số, và cùng tính chất `const` với hàm lớp cha. Nếu sai khác dù chỉ một chi tiết nhỏ, trình biên dịch sẽ coi đó là một hàm mới độc lập (Function Overloading) chứ không phải ghi đè!
3. **Chỉ hoạt động qua con trỏ hoặc tham chiếu**: Nếu bạn truyền theo giá trị (Pass-by-value), hiện tượng **Object Slicing** sẽ xảy ra và làm mất hoàn toàn tính đa hình (chi tiết tại bài 25.9).
"""

# 25.3
lessons["25_3-the-override-and-final-specifiers-and-covariant-return-types.md"] = """# 25.3 — Từ Khóa `override`, `final` & Kiểu Trả Về Đồng Biến

---

## 🎯 Mục Tiêu Bài Học
- Hiểu tại sao C++11 bổ sung từ khóa **`override`** để bảo vệ lập trình viên khỏi các lỗi gõ sai chữ ký hàm ngớ ngẩn.
- Sử dụng từ khóa **`final`** (C++11) để cấm kế thừa hoặc cấm ghi đè hàm.
- Nắm bắt cơ chế **Kiểu trả về đồng biến (Covariant Return Types)**.

---

## 1. Cứu Cánh C++11: Từ Khóa `override`

Trước C++11, nếu bạn muốn ghi đè hàm ảo của lớp cha nhưng vô tình gõ sai tên hoặc quên từ khóa `const`, trình biên dịch sẽ âm thầm coi đó là một hàm hoàn toàn mới:

```cpp
class Base
{
public:
    virtual void show(int x) const;
};

class Derived : public Base
{
public:
    // Quên const hoặc nhầm kiểu: Compiler KHÔNG BÁO LỖI!
    // Nhưng tính đa hình runtime BỊ HỎNG HOÀN TOÀN!
    void show(short x); 
};
```

C++11 đưa ra giải pháp triệt để: **luôn gắn từ khóa `override` vào cuối khai báo hàm ở lớp con**:

```cpp
class Derived : public Base
{
public:
    // Trình biên dịch sẽ kiểm tra: Nếu Base không có hàm virtual void show(short)
    // COMPILER SẼ BÁO LỖI BIÊN DỊCH NGAY LẬP TỨC!
    void show(short x) override; // ERROR: show does not override any base member!
    
    // ĐÚNG CHUẨN:
    void show(int x) const override; // COMPILES OK!
};
```

::: tip Quy Tắc Bắt Buộc Trong C++ Hiện Đại
Luôn luôn sử dụng từ khóa `override` cho mọi hàm ảo trong lớp dẫn xuất! Không bao giờ viết hàm ghi đè mà thiếu `override`.
:::

---

## 2. Từ Khóa `final` Trong C++11

Từ khóa `final` phục vụ 2 mục đích ngăn chặn:

### 2.1. Cấm ghi đè tiếp một hàm ảo:
```cpp
class B : public A
{
public:
    void doWork() override final; // Các lớp con kế thừa từ B KHÔNG ĐƯỢC PHÉP ghi đè doWork() nữa!
};
```

### 2.2. Cấm một lớp bị kế thừa:
```cpp
class SecureEngine final // Không ai có thể kế thừa từ SecureEngine
{
};

// class CustomEngine : public SecureEngine {}; // LỖI BIÊN DỊCH!
```

---

## 3. Kiểu Trả Về Đồng Biến (Covariant Return Types)

Thông thường, hàm ghi đè phải có cùng kiểu trả về với hàm ở lớp cha. Ngoại lệ duy nhất là: **Nếu hàm cha trả về con trỏ hoặc tham chiếu tới lớp `Base*`, thì hàm ghi đè ở lớp con có thể trả về con trỏ hoặc tham chiếu tới lớp `Derived*`**:

```cpp
#include <iostream>

class Base
{
public:
    virtual Base* clone() const { return new Base(*this); }
};

class Derived : public Base
{
public:
    // Kiểu trả về đồng biến: Derived* thay vì Base*
    Derived* clone() const override { return new Derived(*this); }
};

int main()
{
    Derived d;
    // Nhờ covariant return type, người dùng nhận trực tiếp kiểu Derived* mà không cần ép kiểu!
    Derived* copyD = d.clone();
    delete copyD;

    return 0;
}
```
"""

# 25.4
lessons["25_4-virtual-destructors-virtual-assignment-and-overriding-virtualization.md"] = """# 25.4 — Hàm Hủy Ảo (Virtual Destructors) & Cạm Bẫy Quên Virtual Destructor

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
    Base() { std::cout << "Base constructor\\n"; }
    // NGUY HIỂM CHÍ MẠNG: Destructor KHÔNG CÓ từ khóa virtual!
    ~Base() { std::cout << "Base destructor\\n"; }
};

class Derived : public Base
{
private:
    int* m_largeBuffer{ nullptr };

public:
    Derived()
    {
        std::cout << "Derived constructor: Cap phat 1MB Heap\\n";
        m_largeBuffer = new int[250000]; // 1 Megabyte
    }

    ~Derived()
    {
        std::cout << "Derived destructor: Giai phong Heap\\n";
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
        std::cout << "Base destructor (Virtual: An toan 100%)\\n";
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
"""

# 25.5
lessons["25_5-early-binding-and-late-binding.md"] = """# 25.5 — Liên Kết Sớm (Early Binding) & Liên Kết Muộn (Late Binding)

---

## 🎯 Mục Tiêu Bài Học
- Phân biệt bản chất của **Liên kết sớm (Early / Static Binding)** và **Liên kết muộn (Late / Dynamic Binding)**.
- Hiểu cách thức CPU thực thi lệnh nhảy trực tiếp (`call <address>`) so với nhảy gián tiếp qua con trỏ.
- Phân tích chi phí hiệu năng (Overhead) thực tế của tính đa hình động.

---

## 1. Liên Kết Sớm (Early Binding / Static Binding)

Liên kết sớm xảy ra khi trình biên dịch (Compiler) và trình liên kết (Linker) có thể xác định chính xác địa chỉ bộ nhớ của hàm cần gọi **ngay tại thời điểm biên dịch**.

Mọi hàm thông thường, hàm quá tải (Overloading) và hàm mẫu (Templates) trong C++ đều sử dụng liên kết sớm.

```cpp
void printNumber(int x) { ... }

int main()
{
    printNumber(5); // Compiler tạo chỉ thị máy: call 0x00401120
}
```

```
Ưu điểm:
- Tốc độ thực thi tối đa (Zero runtime overhead).
- Compiler có thể dễ dàng tối ưu hóa bằng cách nhúng trực tiếp code vào (Function Inlining).
```

---

## 2. Liên Kết Muộn (Late Binding / Dynamic Binding)

Liên kết muộn xảy ra khi địa chỉ của hàm cần gọi **không thể biết trước khi biên dịch**, mà phải chờ đến khi chương trình đang chạy thực tế (Runtime) mới có thể xác định được.

Trong C++, liên kết muộn được kích hoạt thông qua:
1. **Con trỏ hàm (Function Pointers)**.
2. **Hàm ảo (Virtual Functions)**.

```mermaid
flowchart LR
    subgraph EarlyBinding ["Liên Kết Sớm (Compile-time)"]
        Call1["gọi func()"] -->|"Nhảy trực tiếp đến địa chỉ cố định"| Addr1["0x00401000"]
    end
    subgraph LateBinding ["Liên Kết Muộn (Runtime)"]
        Call2["ptr->virtualFunc()"] -->|"1. Đọc __vptr"| VTable["Tra cứu vtable"]
        VTable -->|"2. Lấy địa chỉ con trỏ hàm"| Addr2["Nhảy gián tiếp tới code"]
    end
```

---

## 3. Chi Phí Hiệu Năng Của Liên Kết Động (Runtime Overhead)

Tại sao C++ không mặc định biến tất cả các hàm thành `virtual` như Java hay C#? Triết lý của C++ là: **"Zero-overhead principle: What you don't use, you don't pay for"**.

Chi phí của hàm ảo gồm có:
1. **Bộ nhớ**: Mỗi đối tượng phải mang thêm 1 con trỏ ẩn `__vptr` (8 bytes trên hệ 64-bit).
2. **Thời gian**: Mỗi lời gọi hàm ảo tốn thêm ít nhất 2 lần truy xuất bộ nhớ gián tiếp (Đọc `__vptr` $\\rightarrow$ Đọc ô trong `vtable` $\\rightarrow$ Gọi hàm).
3. **Cản trở tối ưu**: Trình biên dịch không thể thực hiện Inline đối với các lời gọi hàm ảo thông qua con trỏ, đồng thời làm tăng nguy cơ **Branch Misprediction** trong vi xử lý CPU.
"""

# 25.6
lessons["25_6-the-virtual-table.md"] = """# 25.6 — Mổ Xẻ Bảng Hàm Ảo (vtable) & Con Trỏ Ảo (vptr) Trong Bộ Nhớ RAM

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
    virtual void function1() { std::cout << "Base::func1\\n"; }
    virtual void function2() { std::cout << "Base::func2\\n"; }
    void nonVirtual() {}
};

class D1 : public Base
{
public:
    void function1() override { std::cout << "D1::func1\\n"; }
};

class D2 : public Base
{
public:
    void function2() override { std::cout << "D2::func2\\n"; }
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
    std::cout << "sizeof(EmptyWithoutVirtual): " << sizeof(EmptyWithoutVirtual) << " bytes\\n";
    std::cout << "sizeof(EmptyWithVirtual):    " << sizeof(EmptyWithVirtual) << " bytes\\n";
    return 0;
}
```

### Kết quả trên hệ điều hành 64-bit:
```text
sizeof(EmptyWithoutVirtual): 4 bytes
sizeof(EmptyWithVirtual):    16 bytes (4 bytes int + 4 bytes padding + 8 bytes con trỏ __vptr!)
```
"""

# 25.7
lessons["25_7-pure-virtual-functions-abstract-base-classes-and-interface-classes.md"] = """# 25.7 — Hàm Thuần Ảo, Lớp Trừu Tượng & Interface

---

## 🎯 Mục Tiêu Bài Học
- Hiểu định nghĩa của **Hàm thuần ảo (Pure Virtual Function)** với cú pháp `= 0`.
- Nắm vững đặc tính của **Lớp cơ sở trừu tượng (Abstract Base Class)**: Không thể khởi tạo đối tượng trực tiếp.
- Khái niệm và phương pháp thiết kế **Lớp giao diện (Interface Class)** trong C++.

---

## 1. Hàm Thuần Ảo (Pure Virtual Function) Là Gì?

Hàm thuần ảo là một hàm ảo được khai báo trong lớp cơ sở nhưng **không bắt buộc phải có định nghĩa phần thân hàm** tại lớp cơ sở đó. Cú pháp kết thúc bằng `= 0`:

```cpp
virtual void render() = 0; // Hàm thuần ảo
```

Ý nghĩa: Lớp cơ sở tuyên bố: *"Tôi quy định mọi lớp con kế thừa từ tôi BẮT BUỘC phải tự viết mã cho hàm này, nếu không lớp con cũng sẽ trở thành trừu tượng và không thể tạo đối tượng!"*.

---

## 2. Lớp Cơ Sở Trừu Tượng (Abstract Base Class)

Bất kỳ lớp nào có **chứa ít nhất một hàm thuần ảo** thì tự động được trình biên dịch xếp vào loại **Lớp trừu tượng (Abstract Class)**.
- Bạn **KHÔNG THỂ** tạo đối tượng trực tiếp từ lớp trừu tượng (ví dụ: `Shape s;` sẽ báo lỗi biên dịch).
- Nhưng bạn **CÓ THỂ** tạo con trỏ và tham chiếu kiểu lớp trừu tượng để quản lý các lớp con đa hình (`Shape* ptr = new Circle();`).

```cpp
#include <iostream>

// Lớp trừu tượng Shape
class Shape
{
public:
    virtual ~Shape() = default; // Luôn cần virtual destructor

    // Hàm thuần ảo: Định nghĩa giao diện
    virtual double getArea() const = 0;
    virtual void draw() const = 0;
};

class Circle : public Shape
{
private:
    double m_radius;

public:
    Circle(double r) : m_radius{ r } {}

    // Bắt buộc phải ghi đè toàn bộ các hàm thuần ảo
    double getArea() const override { return 3.14159 * m_radius * m_radius; }
    void draw() const override { std::cout << "Ve hinh tron ban kinh " << m_radius << '\\n'; }
};

int main()
{
    // Shape s; // LỖI BIÊN DỊCH: Không thể khởi tạo đối tượng của lớp trừu tượng!
    
    Circle c{ 5.0 };
    Shape* shape = &c;
    shape->draw();
    std::cout << "Dien tich: " << shape->getArea() << '\\n';

    return 0;
}
```

---

## 3. Lớp Giao Diện (Interface Class) Trong C++

Trong C++, không có từ khóa `interface` riêng biệt như Java hay C#. Một lớp được coi là một **Interface** thuần túy nếu nó thỏa mãn:
1. Tất cả các hàm thành viên đều là **hàm thuần ảo** (`= 0`).
2. **Không có bất kỳ biến thành viên dữ liệu nào** (trừ các hằng số static).
3. Có một **Hàm hủy ảo mặc định** (`virtual ~Interface() = default;`).

Quy ước đặt tên phổ biến trong các dự án lớn là bắt đầu bằng tiền tố `I`: ví dụ `ILogger`, `IDatabaseConnection`, `IRenderer`.
"""

# 25.8
lessons["25_8-virtual-base-classes.md"] = """# 25.8 — Lớp Cơ Sở Ảo (Virtual Base Classes) Giải Quyết Vấn Đề Kim Cương

---

## 🎯 Mục Tiêu Bài Học
- Hiểu cách thức từ khóa `virtual` trong cú pháp kế thừa (`class Derived : virtual public Base`) giải quyết triệt để **Bài toán kim cương (The Diamond Problem)**.
- Trực quan hóa cấu trúc bộ nhớ RAM: Đối tượng con chỉ sở hữu duy nhất một Base Subobject dùng chung.
- Nắm bắt quy tắc khởi tạo đặc biệt: Lớp dẫn xuất cuối cùng (**Most-derived class**) chịu trách nhiệm khởi tạo Virtual Base.

---

## 1. Cú Pháp Kế Thừa Ảo (Virtual Inheritance)

Để đảm bảo các nhánh kế thừa không nhân bản đối tượng gốc, chúng ta thêm từ khóa `virtual` vào phát biểu kế thừa:

```cpp
#include <iostream>

class PoweredDevice
{
public:
    int m_power;
    PoweredDevice(int power) : m_power{ power }
    {
        std::cout << "PoweredDevice khoi tao voi cong suat: " << power << "W\\n";
    }
};

// Kế thừa Ảo từ PoweredDevice
class Scanner : virtual public PoweredDevice
{
public:
    Scanner(int power) : PoweredDevice{ power } {}
};

// Kế thừa Ảo từ PoweredDevice
class Printer : virtual public PoweredDevice
{
public:
    Printer(int power) : PoweredDevice{ power } {}
};

// Copier kế thừa từ cả Scanner và Printer
class Copier : public Scanner, public Printer
{
public:
    // LƯU Ý ĐẶC BIỆT: Copier phải chịu trách nhiệm khởi tạo PoweredDevice trực tiếp!
    Copier(int power)
        : PoweredDevice{ power } // Khoi tao truc tiep Virtual Base
        , Scanner{ power }
        , Printer{ power }
    {
    }
};

int main()
{
    Copier copier{ 120 };
    // KHÔNG CÒN NHẬP NHẰNG! Chỉ có DUY NHẤT một m_power trong toàn bộ copier:
    std::cout << "Cong suat may in: " << copier.m_power << "W\\n";

    return 0;
}
```

---

## 2. Trực Quan Hóa Cấu Trúc Bộ Nhớ RAM Của Virtual Inheritance

```
BỐ CỤC BỘ NHỚ RAM CỦA Copier KHI CÓ VIRTUAL INHERITANCE:
+-------------------------------------------------------------+
| [Scanner Subobject]                                         |
|   - Con trỏ virtual base pointer (vbptr)                    |
|   - Dữ liệu riêng của Scanner                               |
+-------------------------------------------------------------+
| [Printer Subobject]                                         |
|   - Con trỏ virtual base pointer (vbptr)                    |
|   - Dữ liệu riêng của Printer                               |
+-------------------------------------------------------------+
| [Copier Members]                                            |
|   - Dữ liệu riêng của Copier                                |
+-------------------------------------------------------------+
| [DUY NHẤT MỘT PoweredDevice Subobject DÙNG CHUNG]          |
|   - int m_power                                             |
+-------------------------------------------------------------+
```
Nhờ cơ chế này, `Scanner` và `Printer` không tự chứa `PoweredDevice` bên trong mình nữa, mà chúng lưu một con trỏ hoặc bảng offset trỏ tới vị trí của `PoweredDevice` dùng chung được đặt ở cuối đối tượng!
"""

# 25.9
lessons["25_9-object-slicing.md"] = """# 25.9 — Cắt Gọt Đối Tượng (Object Slicing) — Cạm Bẫy Kinh Điển

---

## 🎯 Mục Tiêu Bài Học
- **MỔ XẺ BẢN CHẤT CẠM BẪY CẮT GỌT ĐỐI TƯỢNG (OBJECT SLICING) TRONG C++**.
- Trực quan hóa bộ nhớ: Tại sao truyền tham trị (`Pass-by-value`) lại cắt phăng toàn bộ phần dữ liệu chuyên biệt của lớp con và phá hủy con trỏ bảng ảo `__vptr`.
- Nắm vững các phương pháp phòng chống Object Slicing trong thực tế.

---

## 1. Hiện Tượng Object Slicing Là Gì?

Hãy quan sát đoạn code tưởng chừng vô hại sau:

```cpp
#include <iostream>
#include <string_view>

class Base
{
protected:
    int m_value{ 0 };

public:
    Base(int value) : m_value{ value } {}
    virtual ~Base() = default;

    virtual std::string_view getName() const { return "Base"; }
    int getValue() const { return m_value; }
};

class Derived : public Base
{
private:
    double m_extraData{ 99.99 };

public:
    Derived(int value, double extra)
        : Base{ value }, m_extraData{ extra } {}

    std::string_view getName() const override { return "Derived"; }
};

// CẠM BẪY CHÍ MẠNG: Hàm nhận tham trị (Pass-by-value) kiểu Base!
void printName(Base b)
{
    std::cout << "Toi la: " << b.getName() << '\\n';
}

int main()
{
    Derived d{ 5, 3.14 };
    
    // GỌI HÀM VỚI THAM TRỊ:
    printName(d); // IN RA: "Toi la: Base" (!) TÍNH ĐA HÌNH BIẾN MẤT HOÀN TOÀN!

    return 0;
}
```

Tại sao `printName(d)` lại in ra `"Base"` trong khi `d` rõ ràng là `Derived` và `getName()` là hàm ảo `virtual`?

---

## 2. Trực Quan Hóa Quá Trình Cắt Gọt Trong RAM

Khi bạn truyền đối tượng `Derived d` vào tham số `Base b`, hàm khởi tạo sao chép của `Base` (`Base copy constructor`) được kích hoạt để sao chép dữ liệu từ `d` sang biến cục bộ `b`:

```
ĐỐI TƯỢNG BAN ĐẦU: Derived d                            BIẾN CỤC BỘ ĐƯỢC TẠO: Base b
+-----------------------------------+                   +-----------------------------------+
| __vptr (Trỏ tới vtable của D)     | === [BỊ CẮT!] ==> | __vptr (Trỏ tới vtable của Base!) |
+-----------------------------------+                   +-----------------------------------+
| int m_value = 5                   | === SAO CHÉP ===> | int m_value = 5                   |
+-----------------------------------+                   +-----------------------------------+
| double m_extraData = 3.14         | === [BỊ CẮT!] ==> | (Vùng nhớ không tồn tại trong b)  |
+-----------------------------------+                   +-----------------------------------+
(Kích thước: 24 bytes)                                  (Kích thước: 16 bytes)
```

### Diễn giải cơ chế:
1. Đối tượng `b` chỉ có kích thước của `Base`. Do đó, trình biên dịch **cắt bỏ hoàn toàn** trường `m_extraData` của `Derived` vì không có chỗ chứa!
2. Nguy hiểm hơn nữa: Con trỏ bảng ảo `__vptr` của `b` được thiết lập trỏ tới **bảng `vtable của Base`** (chứ không phải `Derived`).
3. Kết quả: Toàn bộ danh tính và tính đa hình của đối tượng con đã bị tước đoạt hoàn toàn!

---

## 3. Cách Phòng Tránh Triệt Để Object Slicing

### Quy tắc 1: Luôn truyền qua Tham Chiếu (`const Base&`) hoặc Con Trỏ (`Base*`)
```cpp
void printName(const Base& b) // An toàn tuyệt đối: Không copy, không slicing!
{
    std::cout << "Toi la: " << b.getName() << '\\n'; // In ra "Derived" đúng chuẩn đa hình
}
```

### Quy tắc 2: Cấm sao chép lớp Base bằng cách khóa Copy Constructor
Nếu một lớp được thiết kế để làm lớp cha đa hình, hãy bảo vệ nó khỏi bị gán hoặc copy nhầm:
```cpp
class Base
{
public:
    Base(const Base&) = delete;            // Cấm copy
    Base& operator=(const Base&) = delete; // Cấm gán
};
```
"""

# 25.10
lessons["25_10-dynamic-casting.md"] = """# 25.10 — Ép Kiểu Động (Dynamic Casting) & RTTI

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
        std::cout << "Goi tinh nang dac biet cua Derived!\\n";
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
        std::cout << "Cast b1 thanh cong!\\n";
        d1->doSomethingSpecial();
    }

    // 2. ÉP KIỂU KHÔNG HỢP LỆ: b2 thực chất là OtherDerived, không phải Derived!
    Derived* d2 = dynamic_cast<Derived*>(b2);
    if (d2 == nullptr)
    {
        std::cout << "Cast b2 THAT BAI! dynamic_cast tra ve nullptr an toan.\\n";
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
        std::cout << "Loi ep kieu tham chieu: " << e.what() << '\\n';
    }
}
```

---

## 3. Lời Khuyên Về Phong Cách Thiết Kế

::: warning Cảnh Báo "Mùi Mã Nguồn" (Code Smell)
Nếu bạn nhận thấy mã nguồn của mình xuất hiện dày đặc các lệnh `if (dynamic_cast<TypeA*>(ptr)) ... else if (dynamic_cast<TypeB*>(ptr))`, bạn đang vi phạm nghiêm trọng nguyên lý thiết kế hướng đối tượng! 
Thay vì liên tục hỏi đối tượng "Bạn là ai?", hãy thêm một hàm ảo `virtual` vào lớp cha và để cơ chế đa hình tự động giải quyết.
:::
"""

# 25.11
lessons["25_11-printing-inherited-classes-using-operator.md"] = """# 25.11 — Xuất Đối Tượng Đa Hình Với Toán Tử `<<`

---

## 🎯 Mục Tiêu Bài Học
- Hiểu vấn đề nan giải: Tại sao `friend std::ostream& operator<<` không thể khai báo là hàm ảo `virtual`.
- Nắm vững mẫu thiết kế (Idiom) kinh điển: Kết hợp `operator<<` thông thường với một hàm ảo hỗ trợ `print()`.

---

## 1. Vấn Đề: Toán Tử `<<` Không Thể Là Hàm Ảo

Toán tử xuất luồng `operator<<` bắt buộc phải nhận tham số đầu tiên là `std::ostream&`. Do đó, nó phải được cài đặt dưới dạng một hàm tự do (Friend function), không thể là một hàm thành viên của lớp.
Vì nó không phải hàm thành viên, **C++ không cho phép khai báo `virtual friend std::ostream& operator<<`**!

Nếu bạn chỉ nạp chồng `operator<<` thông thường cho `Base` và `Derived`, khi in qua con trỏ `Base*`, C++ sẽ chỉ gọi phiên bản của `Base`:

```cpp
Base* b = new Derived();
std::cout << *b; // Sẽ luôn gọi operator<<(ostream&, const Base&) bất kể b là gì!
```

---

## 2. Giải Pháp: Mẫu Thiết Kế Hàm Ảo `print()`

Để in đa hình, chúng ta áp dụng kỹ thuật 2 bước:
1. Khai báo một hàm ảo thành viên: `virtual std::ostream& print(std::ostream& out) const;` trong lớp cơ sở, và ghi đè nó ở các lớp con.
2. Nạp chồng duy nhất **MỘT** toán tử `operator<<` cho lớp `Base`, và bên trong nó chỉ việc ủy quyền cho hàm ảo `print()`!

```cpp
#include <iostream>

class Base
{
public:
    virtual ~Base() = default;

    // 1. Ham ao thanh vien chiu trach nhiem xuat du lieu
    virtual std::ostream& print(std::ostream& out) const
    {
        out << "Base";
        return out;
    }

    // 2. Nap chong operator<< duy nhat tai Base
    friend std::ostream& operator<<(std::ostream& out, const Base& b)
    {
        return b.print(out); // Goi ham ao print() tai runtime!
    }
};

class Derived : public Base
{
public:
    std::ostream& print(std::ostream& out) const override
    {
        out << "Derived da duoc in da hinh ruc ro!";
        return out;
    }
};

int main()
{
    Base b;
    Derived d;

    Base& ref1 = b;
    Base& ref2 = d;

    // In thong qua tham chieu lop co so:
    std::cout << ref1 << '\\n'; // In ra: Base
    std::cout << ref2 << '\\n'; // In ra: Derived da duoc in da hinh ruc ro!

    return 0;
}
```
"""

# 25.x
lessons["25_x-chapter-25-summary-and-quiz.md"] = """# 25.x — Tổng Kết Chương 25 & Bài Kiểm Tra Toàn Diện

---

## 🎯 Mục Tiêu
- Ôn tập toàn diện các trụ cột của Tính Đa Hình trong C++.
- Vượt qua bài kiểm tra trắc nghiệm và thử thách thiết kế hệ thống đồ họa đa hình.

---

## 1. Bảng Tóm Tắt Khái Niệm Chương 25

| Khái Niệm | Mục Đích | Lưu Ý Quan Trọng |
| :--- | :--- | :--- |
| **Virtual Function** | Kích hoạt liên kết động (Dynamic Dispatch) | Chi phí gọi gián tiếp qua vtable |
| **Virtual Destructor** | Đảm bảo dọn dẹp sạch lớp con khi xóa qua `Base*` | Bắt buộc phải có nếu lớp có bất kỳ hàm virtual nào |
| **override** | Bắt compiler đối chiếu chữ ký hàm | Luôn sử dụng trong C++ hiện đại |
| **Pure Virtual (`= 0`)** | Định nghĩa giao diện bắt buộc lớp con phải viết | Biến lớp thành Abstract Class |
| **Object Slicing** | Mất dữ liệu con khi truyền tham trị lớp cha | Luôn truyền `const Base&` hoặc `std::unique_ptr<Base>` |
| **dynamic_cast** | Downcast an toàn tại runtime | Yêu cầu lớp cha có ít nhất 1 hàm virtual (RTTI) |

---

## 2. Bài Tập Thực Chiến Toàn Diện: Hệ Thống Vẽ Hình Học (Vector Graphic Engine)

### Yêu cầu:
1. Định nghĩa lớp cơ sở trừu tượng `Shape` có:
   - Màu sắc (`std::string`).
   - Hàm ảo thuần ảo `virtual double getArea() const = 0;`.
   - Hàm ảo in thông tin `virtual void print() const = 0;`.
   - Hàm hủy ảo `virtual ~Shape() = default;`.
2. Tạo hai lớp con:
   - `Circle`: Có bán kính `double m_radius`.
   - `Rectangle`: Có chiều dài `m_width` và chiều rộng `m_height`.
3. Viết hàm `main()` khởi tạo một danh sách các hình học thông qua `std::vector<std::unique_ptr<Shape>>`, duyệt qua danh sách và tính tổng diện tích toàn bộ các hình.

<details>
<summary><b>Xem lời giải mã nguồn C++20 hoàn chỉnh</b></summary>

```cpp
#include <iostream>
#include <vector>
#include <memory>
#include <string>
#include <string_view>

class Shape
{
protected:
    std::string m_color;

public:
    Shape(std::string_view color) : m_color{ color } {}
    virtual ~Shape() = default; // Virtual Destructor chuan muc

    virtual double getArea() const = 0; // Pure virtual
    virtual void print() const = 0;    // Pure virtual
};

class Circle : public Shape
{
private:
    double m_radius{ 0.0 };

public:
    Circle(std::string_view color, double radius)
        : Shape{ color }, m_radius{ radius } {}

    double getArea() const override
    {
        return 3.1415926535 * m_radius * m_radius;
    }

    void print() const override
    {
        std::cout << "Hinh Tron [Mau: " << m_color << ", Ban kinh: " << m_radius 
                  << "] -> Dien tich: " << getArea() << '\\n';
    }
};

class Rectangle : public Shape
{
private:
    double m_width{ 0.0 };
    double m_height{ 0.0 };

public:
    Rectangle(std::string_view color, double width, double height)
        : Shape{ color }, m_width{ width }, m_height{ height } {}

    double getArea() const override
    {
        return m_width * m_height;
    }

    void print() const override
    {
        std::cout << "Hinh Chu Nhat [Mau: " << m_color << ", Kich thuoc: " 
                  << m_width << "x" << m_height << "] -> Dien tich: " << getArea() << '\\n';
    }
};

int main()
{
    // Quan ly danh sach da hinh an toan bang smart pointer (std::unique_ptr)
    std::vector<std::unique_ptr<Shape>> shapes;
    shapes.push_back(std::make_unique<Circle>("Do", 3.0));
    shapes.push_back(std::make_unique<Rectangle>("Xanh Duong", 4.0, 5.0));
    shapes.push_back(std::make_unique<Circle>("Vang", 2.5));

    double totalArea{ 0.0 };

    std::cout << "=== DANH SACH CAC HINH HOC ===\\n";
    for (const auto& shape : shapes)
    {
        shape->print(); // Dynamic dispatch qua vtable!
        totalArea += shape->getArea();
    }

    std::cout << "--------------------------------\\n";
    std::cout << "TONG DIEN TICH TOAN BO HE THONG: " << totalArea << '\\n';

    return 0;
}
```
</details>
"""

for fname, content in lessons.items():
    fpath = os.path.join(OUT_DIR, fname)
    with open(fpath, "w", encoding="utf-8") as f:
        f.write(content.strip() + "\n")
    print(f" -> Đã tạo ch27: {fname}")

print("HOÀN THÀNH CHƯƠNG 25 (12 bài trong docs/vi/ch27)")
