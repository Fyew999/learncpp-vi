# 8.3 — Các Vấn Đề Thường Gặp Với Câu Lệnh If (Common If Problems)

---

## 🎯 Mục Tiêu Bài Học
- Nhận diện 3 cạm bẫy kinh điển nhất với câu lệnh `if`:
  1. Nhầm lẫn giữa toán tử gán `=` và toán tử so sánh `==`.
  2. Dấu chấm phẩy `;` vô tình đặt sau điều kiện `if () ;`.
  3. Lỗi **Dangling Else** (Else lơ lửng) khi lồng ghép câu lệnh `if` không dùng ngoặc nhọn.

---

## 1. Cạm Bẫy 1: Nhầm Lẫn `=` và `==`

```cpp
int x { 0 };

if (x = 5) // 💥 NGUY HIỂM: Đây là phép GÁN, không phải so sánh!
{
    std::cout << "x bang 5\n";
}
```
Cơ chế: Phép gán `x = 5` gán giá trị 5 vào `x`, và toàn bộ biểu thức trả về giá trị 5. Vì 5 khác 0, điều kiện này **LUÔN LUÔN ĐÚNG (`true`)**!
Mẹo phòng vệ cổ điển (Yoda Conditions): Viết hằng số ở bên trái `if (5 == x)`. Nếu bạn gõ nhầm `if (5 = x)`, trình biên dịch sẽ báo lỗi cú pháp ngay lập tức!

---

## 2. Cạm Bẫy 2: Dấu Chấm Phẩy Vô Tình `;`

```cpp
int x { 10 };

if (x == 0); // 💥 Dấu chấm phẩy tạo thành một câu lệnh rỗng (Null statement)!
{
    std::cout << "x bang 0\n"; // Khối mã này LUÔN ĐƯỢC CHẠY bất kể x là gì!
}
```

---

## 3. Cạm Bẫy 3: Dangling Else (Else Lơ Lửng)

Khi lồng ghép các câu lệnh `if` mà không dùng ngoặc nhọn `{}`:
```cpp
if (x > 0)
    if (y > 0)
        std::cout << "Ca hai deu duong\n";
else
    std::cout << "x am hoac bang 0\n"; // 💥 SAI HOÀN TOÀN!
```

Theo chuẩn C++, mệnh đề `else` luôn được kết nối với **câu lệnh `if` gần nó nhất chưa có else**! Do đó `else` này thực chất thuộc về `if (y > 0)`, khiến thông báo in ra hoàn toàn sai logic.

::: tip 💡 Giải Pháp Tuyệt Đối
**Luôn luôn sử dụng cặp dấu ngoặc nhọn `{}` cho mọi nhánh `if` và `else`!**
:::
