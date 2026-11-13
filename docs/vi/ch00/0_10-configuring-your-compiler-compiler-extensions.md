# 0.10 — Phần Mở Rộng Của Trình Biên Dịch (Compiler Extensions)

---

## 🎯 Mục Tiêu Bài Học
- Hiểu khái niệm phần mở rộng trình biên dịch (Compiler Extensions).
- Nhận biết lý do vì sao Compiler Extensions phá vỡ tính khả di động (Portability) của mã nguồn.
- Cấu hình vô hiệu hóa phần mở rộng để đảm bảo code tuân thủ 100% chuẩn ISO C++.

---

## 1. Compiler Extensions Là Gì?

Tiêu chuẩn C++ được Ủy ban Quốc tế ISO ban hành định kỳ (C++11, C++17, C++20, C++23). Tuy nhiên, các nhà sản xuất trình biên dịch lớn như GCC, Clang hay Microsoft Visual C++ (MSVC) thường tự ý bổ sung thêm các tính năng hoặc cú pháp riêng của họ vào trình biên dịch. Những tính năng không nằm trong chuẩn ISO chính thức này được gọi là **Compiler Extensions**.

---

## 2. Vì Sao Bạn Nên TẮT Phần Mở Rộng Trình Biên Dịch?

::: warning Nguy cơ phá hủy tính di động của mã nguồn (Portability Bug)
Nếu bạn vô tình sử dụng một tính năng mở rộng của GCC (ví dụ: mảng có kích thước động trên ngăn xếp VLA - Variable Length Arrays), code của bạn sẽ biên dịch chạy ngon lành trên máy bạn (dùng GCC).

Nhưng khi bạn nộp bài lên hệ thống chấm điểm tự động (dùng Clang) hoặc khi đồng nghiệp mở dự án bằng Visual Studio trên Windows, **chương trình sẽ lập tức báo lỗi biên dịch và không thể chạy được!**
:::

---

## 3. Cách Tắt Compiler Extensions Trong Thực Tế

Khi biên dịch với GCC hoặc Clang, bạn nên thêm cờ `-pedantic-errors` để ép trình biên dịch từ chối mọi mã nguồn vi phạm chuẩn ISO:

```bash
g++ -std=c++20 -pedantic-errors main.cpp -o main
```

Trong IDE Visual Studio, bạn vào:
`Project Properties -> C/C++ -> Language -> Conformance mode -> Chọn Yes (/permissive-)`.
