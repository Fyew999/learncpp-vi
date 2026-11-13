# 17.11 — Hằng Chuỗi Ký Tự Biểu Tượng Kiểu C (C-Style String Symbolic Constants)

---

## 🎯 Mục Tiêu Bài Học
- Hiểu vị trí lưu trữ của chuỗi ký tự hằng (String Literals) trong bộ nhớ chỉ đọc (Read-Only Data Segment).
- Nhận diện cạm bẫy sửa đổi chuỗi ký tự qua con trỏ không hằng (`char*`).
- Nắm vững quy tắc khai báo: `const char*` thay vì `char*`.

---

## 1. Chuỗi Ký Tự Hằng Nằm Ở Đâu Trong Bộ Nhớ?

Khi bạn viết một chuỗi hằng như `"Xin chao"`, chuỗi này được trình biên dịch đặt vào phân vùng **Dữ liệu chỉ đọc (Read-Only Data Segment / Text Segment)** của tệp thực thi. Vùng nhớ này có vòng đời tĩnh (Static Duration) - tồn tại suốt từ lúc chương trình bắt đầu đến khi kết thúc.

```cpp
#include <iostream>

int main()
{
    // BẮT BUỘC PHẢI CÓ 'const':
    const char* message{ "Xin chao" }; // message là con trỏ trên Stack trỏ tới chuỗi trong Read-only Memory
    std::cout << message << '
';

    // CẠM BẪY CHÍ MẠNG TRONG C CŨ:
    // char* bad = "Hello"; // C++11 trở lên cấm tiệt!
    // bad[0] = 'h'; // CRASH NGAY LẬP TỨC: Access Violation Writing to Read-Only Memory!

    return 0;
}
```

---

## 2. So Sánh `const char*` vs `char[]`

| Tiêu chí | `const char* str = "Hello";` | `char str[] = "Hello";` |
| :--- | :--- | :--- |
| **Vùng nhớ chuỗi** | Nằm trong **Read-only Data** (Chỉ đọc) | Sao chép một bản sang **Stack** |
| **Có thể sửa ký tự không?** | **KHÔNG** (Gây crash nếu cố sửa) | **CÓ** (Có thể sửa `str[0] = 'h';`) |
| **Bộ nhớ tiêu tốn** | Chỉ tốn 8 bytes cho con trỏ trên Stack | Tốn $N+1$ bytes trên Stack |

---

## 3. 📝 Hệ Thống Quiz & Bài Tập Tự Luyện

::: details Câu hỏi 1: Tại sao C++11 lại biến việc khai báo `char* str = "Hello";` thành lỗi biên dịch thay vì chỉ cảnh báo như các chuẩn trước?
**Lời giải chi tiết**:
Bởi vì `"Hello"` là một mảng hằng ký tự `const char[6]` nằm trong vùng nhớ chỉ đọc của hệ điều hành. Nếu cho phép gán ngầm định sang `char*` (con trỏ không hằng), lập trình viên có thể vô tình thực hiện thao tác ghi đè như `str[0] = 'M';`. Khi đó hệ điều hành sẽ kích hoạt lỗi phân đoạn bộ nhớ (Segmentation Fault) và làm sập chương trình ngay tại runtime. Bắt lỗi ngay tại compile-time là nguyên tắc an toàn cốt lõi của C++.
:::
