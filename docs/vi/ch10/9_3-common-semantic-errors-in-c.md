# 9.3 — Các Lỗi Ngữ Nghĩa Phổ Biến Trong C++ (Common Semantic Errors)

---

## 🎯 Mục Tiêu Bài Học
- Phân biệt giữa **Lỗi cú pháp (Syntax Error)** (Compiler phát hiện) và **Lỗi ngữ nghĩa (Semantic Error / Logic Bug)** (Chương trình chạy được nhưng cho kết quả sai).
- Danh mục 6 cạm bẫy ngữ nghĩa kinh điển trong C++:
  1. Lỗi lệch một đơn vị (Off-by-one errors)
  2. Tràn số nguyên (Integer overflow)
  3. Đọc biến chưa khởi tạo (Uninitialized variables)
  4. Phép chia số nguyên làm mất số thập phân
  5. Thứ tự ưu tiên toán tử sai
  6. Biến con trỏ vô định (Dangling pointers)

---

## 1. Bảng Tổng Hợp 6 Cạm Bẫy Ngữ Nghĩa Kinh Điển

| Loại Lỗi | Mã Nguồn Gây Lỗi | Giải Thích & Cách Khắc Phục |
| :--- | :--- | :--- |
| **Off-by-One** | `for (int i=0; i<=size; ++i)` | Duyệt quá biên mảng 1 phần tử. Đổi `<= size` thành `< size`. |
| **Integer Overflow** | `int val = maxInt + 1;` | Tràn số có dấu là UB. Dùng `int64_t` hoặc kiểm tra trước khi cộng. |
| **Uninitialized Read** | `int x; std::cout << x;` | Đọc giá trị rác bộ nhớ. Luôn khởi tạo: `int x {};`. |
| **Integer Division** | `double r = 5 / 2;` | `5/2` ra `2`. Sửa thành `5.0 / 2` để nhận `2.5`. |
| **Precedence Bug** | `if (x & 1 == 0)` | `==` chạy trước `&`. Sửa thành: `if ((x & 1) == 0)`. |
| **Dangling Pointer** | `return &localVar;` | Vùng nhớ bị thu hồi khi thoát hàm. Không bao giờ trả về địa chỉ biến cục bộ. |
