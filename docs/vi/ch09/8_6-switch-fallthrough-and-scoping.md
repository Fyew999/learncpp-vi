# 8.6 — Cơ Chế Fallthrough và Phạm Vi Biến Trong Switch (Switch Fallthrough & Scoping)

---

## 🎯 Mục Tiêu Bài Học
- Hiểu hiện tượng **Trôi qua (Fallthrough)** khi thiếu lệnh `break`.
- Ứng dụng chủ động của fallthrough (Gom nhóm nhiều `case` chung một khối xử lý).
- Thuộc tính chuẩn C++17: **`[[fallthrough]]`**.
- Quy tắc khai báo và khởi tạo biến bên trong thân câu lệnh `switch`.

---

## 1. Hiện Tượng Fallthrough Là Gì?

Khi một nhãn `case` khớp với giá trị điều kiện, CPU sẽ nhảy thẳng tới nhãn đó và thực thi mã. Nếu tại cuối nhãn không có lệnh `break` hoặc `return`, CPU sẽ **tiếp tục thực thi tuần tự xuống các nhãn `case` bên dưới** bất kể giá trị của các case đó có khớp hay không!

```cpp
#include <iostream>

int main()
{
    int x { 1 };
    switch (x)
    {
    case 1:
        std::cout << "Mot\n"; // Chạy dòng này
        // Quên break! Trôi tiếp xuống case 2!
    case 2:
        std::cout << "Hai\n"; // Vẫn chạy dòng này!
        break;
    }
    return 0;
}
```

---

## 2. 🚀 Thuộc Tính `[[fallthrough]]` Chuẩn C++17

Trong thực tế, đôi khi lập trình viên cố tình muốn fallthrough. Để tránh bị trình biên dịch cảnh báo lỗi (`-Wimplicit-fallthrough`), C++17 cung cấp thuộc tính chuẩn **`[[fallthrough]]`**:

```cpp
switch (cmd)
{
case 'a':
case 'A': // Gom nhóm case 'a' và 'A'
    doActionA();
    break;

case 'w':
    logWarning();
    [[fallthrough]]; // Thông báo cho compiler: Tôi cố tình fallthrough xuống dưới!
case 'e':
    logError();
    break;
}
```

---

## 3. Khai Báo Biến Bên Trong `switch`

::: warning ⚠️ Cạm Bẫy: Khởi Tạo Biến Bên Dưới Nhãn Case
Bạn không thể nhảy qua một câu lệnh khởi tạo biến:
```cpp
switch (x)
{
case 1:
    int y { 5 }; // 💥 LỖI BIÊN DỊCH nếu case 2 được gọi, vì nó nhảy qua khởi tạo của y!
    break;
case 2:
    std::cout << y;
    break;
}
```
**Cách khắc phục chuẩn**: Hãy bọc phần thân của `case` trong một khối mã `{}` riêng biệt:
```cpp
case 1:
{ // Tạo scope riêng cho case 1
    int y { 5 };
    std::cout << y;
    break;
}
```
:::
