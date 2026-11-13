# 8.12 — Dừng Chương Trình Sớm (Halts: std::exit, std::abort)

---

## 🎯 Mục Tiêu Bài Học
- Phân biệt cách thoát chương trình thông thường (`return 0` trong `main`) và các hàm dừng sớm (**Halts**).
- Khám phá các hàm: `std::exit()`, `std::quick_exit()`, `std::abort()`, `std::terminate()`.
- Hiểu cơ chế dọn dẹp biến cục bộ (Stack Unwinding) và hàm hủy (Destructors) khi dừng chương trình.
- Đăng ký hàm dọn dẹp với `std::atexit()`.

---

## 1. Các Hàm Dừng Sớm Phổ Biến

| Hàm | Header | Cơ chế dọn dẹp | Mục đích sử dụng |
| :--- | :---: | :--- | :--- |
| `std::exit(code)` | `<cstdlib>` | Gọi destructor cho biến static/global; **KHÔNG** dọn biến cục bộ trên stack! | Thoát bình thường khi có lỗi nghiêm trọng không thể cứu vãn |
| `std::quick_exit(code)` | `<cstdlib>` | Thoát siêu nhanh, không gọi destructors | Thoát khẩn cấp khi hệ thống chuẩn bị sập |
| `std::abort()` | `<cstdlib>` | Báo lỗi bất thường (SIGABRT), sinh core dump | Phát hiện lỗi logic phần mềm nghiêm trọng |
| `std::terminate()` | `<exception>` | Gọi handler xử lý khi exception không được catch | Trình xử lý ngoại lệ thất bại |
