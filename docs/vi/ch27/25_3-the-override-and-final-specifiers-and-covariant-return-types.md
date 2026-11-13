# 25.3 — Từ Khóa `override`, `final` & Kiểu Trả Về Đồng Biến

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
