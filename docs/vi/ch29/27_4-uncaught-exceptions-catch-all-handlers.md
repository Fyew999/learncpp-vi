# 27.4 — Ngoại Lệ Chưa Được Bắt & Trình Bắt Tất Cả `catch (...)`

---

## 🎯 Mục Tiêu Bài Học
- Hiểu số phận của chương trình khi một ngoại lệ không có khối `catch` nào khớp: **`std::terminate()`**.
- Sử dụng khối **Trình bắt tất cả (Catch-all handler: `catch (...)`)** để làm chốt chặn an toàn cuối cùng.
- Tùy chỉnh hàm xử lý khi sập chương trình với `std::set_terminate()`.

---

## 1. Ngoại Lệ Chưa Được Bắt (Uncaught Exception)

Nếu một ngoại lệ được ném ra mà cuộn ngược lên tận hàm `main()` vẫn không tìm thấy bất kỳ khối `catch` nào tương ứng, chương trình sẽ rơi vào trạng thái **Uncaught Exception**:
- Hệ thống runtime lập tức kích hoạt hàm **`std::terminate()`**.
- Hàm này mặc định sẽ gọi tiếp `std::abort()` để **hủy diệt tiến trình ngay lập tức (Crash)**.
- Khi bị crash bởi `std::terminate()`, trình biên dịch có thể **không bảo đảm thực hiện việc cuộn ngược ngăn xếp**, khiến các tài nguyên, file đang mở hoặc kết nối database bị đóng đột ngột mà không kịp lưu!

---

## 2. Khối Trình Bắt Tất Cả: `catch (...)`

Để ngăn chặn chương trình bị crash bất ngờ, C++ cung cấp cú pháp dấu ba chấm `...` trong mệnh đề `catch`, cho phép **bắt bất kỳ kiểu ngoại lệ nào**, bất kể đó là số nguyên, chuỗi, hay đối tượng ngoại lệ phức tạp:

```cpp
#include <iostream>

void riskyFunction()
{
    throw 404; // Ném một kiểu bất kỳ
}

int main()
{
    try
    {
        riskyFunction();
    }
    catch (double d)
    {
        std::cout << "Bat kieu double\n";
    }
    // CHỐT CHẶN CUỐI CÙNG: Bắt tất cả mọi ngoại lệ còn lại!
    catch (...)
    {
        std::cerr << "Da bat mot ngoai le khong xac dinh! Ngan chan crash thanh cong.\n";
    }

    return 0;
}
```

::: warning Vị Trí Của Khối `catch (...)`
Khối `catch (...)` **BẮT BUỘC PHẢI ĐẶT Ở VỊ TRÍ CUỐI CÙNG** trong danh sách các khối catch. Nếu bạn đặt nó lên đầu, nó sẽ nuốt chửng mọi ngoại lệ và khiến tất cả các khối `catch` cụ thể bên dưới trở thành mã chết (Dead code)!
:::
