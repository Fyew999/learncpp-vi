# 11.5 — Tham Số Mặc Định (Default Arguments)

---

## 🎯 Mục Tiêu Bài Học
- Hiểu và sử dụng Tham số mặc định (Default Arguments).
- Nắm vững quy tắc đặt tham số mặc định: Phải đặt ở các tham số tận cùng bên phải (Rightmost parameters).
- Nắm quy tắc tổ chức tệp: Khai báo tham số mặc định trong Header (`.h`) chứ không lặp lại trong Source (`.cpp`).
- Tránh xung đột mơ hồ giữa tham số mặc định và nạp chồng hàm.

---

## 1. Tham Số Mặc Định Là Gì?

**Tham số mặc định (Default Argument)** là giá trị được cung cấp tự động cho tham số hàm nếu người gọi hàm không truyền đối số tương ứng.

```cpp
#include <iostream>

void printValues(int x, int y = 10, int z = 20)
{
    std::cout << "x: " << x << ", y: " << y << ", z: " << z << '
';
}

int main()
{
    printValues(1, 2, 3); // Cung cấp đủ 3 đối số -> x: 1, y: 2, z: 3
    printValues(1, 2);    // Thiếu z -> z nhận mặc định 20
    printValues(1);       // Thiếu y, z -> y nhận 10, z nhận 20

    return 0;
}
```

---

## 2. Quy Tắc Bắt Buộc: Phải Nằm Ở Cùng Phía Bên Phải

Nếu một tham số có giá trị mặc định, thì **tất cả các tham số đứng sau nó cũng bắt buộc phải có giá trị mặc định**:

```cpp
// LỖI BIÊN DỊCH!
// void print(int x = 10, int y); // error: default argument missing for parameter 2 of 'void print(int, int)'
```
Lý do: Khi gọi `print(5)`, compiler sẽ gán `5` cho tham số đầu tiên `x`, và tham số `y` sẽ bị bỏ đói không có giá trị!

---

## 3. Quy Tắc Đặt Trong Dự Án Nhiều Tệp (Header vs Source)

::: tip Quy Tắc Vàng
Tham số mặc định **chỉ được khai báo 1 lần duy nhất trong tệp tiêu đề (Header file `.h`)**. Tuyệt đối không lặp lại giá trị mặc định trong tệp định nghĩa (`.cpp`).
:::

::: code-group
```cpp [Foo.h]
#ifndef FOO_H
#define FOO_H

// Khai báo tham số mặc định tại Header
void display(int count = 5);

#endif
```

```cpp [Foo.cpp]
#include "Foo.h"
#include <iostream>

// KHÔNG lặp lại '= 5' ở đây!
void display(int count)
{
    for (int i{ 0 }; i < count; ++i)
        std::cout << "*";
    std::cout << '
';
}
```
:::

---

## ⚠️ Cạm Bẫy: Xung Đột Với Nạp Chồng Hàm

```cpp
void print(int x);
void print(int x, int y = 20);

int main()
{
    // print(10); // LỖI BIÊN DỊCH: Ambiguous call!
    return 0;
}
```
Lời gọi `print(10)` có thể hiểu là gọi `print(int)` hoặc gọi `print(int, int=20)`. Compiler sẽ báo lỗi Khớp mơ hồ!

---

## 📝 Bài Tập Tự Luyện & Quiz Củng Cố

### Câu hỏi 1:
Khai báo hàm nào sau đây là KHÔNG HỢP LỆ trong C++?
A) `void foo(int a, int b = 1, int c = 2);`  
B) `void foo(int a = 1, int b = 2, int c = 3);`  
C) `void foo(int a = 1, int b, int c = 2);`  
D) `void foo(int a, int b, int c = 3);`

::: details [Xem lời giải]
**Đáp án đúng: C**  
Giải thích: Tham số `a` có giá trị mặc định nhưng `b` đứng sau nó lại không có. Điều này vi phạm quy tắc: Mọi tham số đứng sau một tham số mặc định đều phải có giá trị mặc định.
:::
