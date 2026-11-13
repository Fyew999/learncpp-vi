# 27.6 — Ném Lại Ngoại Lệ (Rethrowing Exceptions)

---

## 🎯 Mục Tiêu Bài Học
- Hiểu mục đích của việc ném lại ngoại lệ (**Rethrow**): Khi một hàm chỉ muốn ghi log sự cố rồi chuyển tiếp lỗi lên cấp cao hơn xử lý.
- Phân biệt sự khác nhau sống còn giữa cú pháp **`throw;`** và **`throw e;`**.
- Tránh cạm bẫy cắt gọt đối tượng (Object Slicing) khi ném lại ngoại lệ.

---

## 1. Khi Nào Cần Rethrow Ngoại Lệ?

Đôi khi một hàm ở tầng giữa bắt được ngoại lệ, nó cần làm một số thao tác cục bộ (ví dụ: ghi log lỗi vào file, giải phóng tài nguyên tạm thời), nhưng nó **không thể khắc phục hoàn toàn sự cố**. Lúc này nó cần chuyển tiếp chính ngoại lệ đó lên tầng trên bằng cách **ném lại (Rethrow)**.

---

## 2. Cạm Bẫy Chết Người: `throw;` vs `throw e;`

```cpp
#include <iostream>
#include <stdexcept>

class CustomDerivedException : public std::runtime_error
{
public:
    CustomDerivedException() : std::runtime_error{ "Loi tuy bien dac biet cua Derived!" } {}
};

void handleProcess()
{
    try
    {
        throw CustomDerivedException{};
    }
    catch (const std::exception& e)
    {
        std::cout << "Ghi log su co tai handleProcess...\n";

        // CÁCH 1 (SAI LẦM): throw e;
        // throw e; // NGUY HIỂM: Tạo ra bản sao mới kiểu std::exception -> GÂY OBJECT SLICING!

        // CÁCH 2 (ĐÚNG CHUẨN): throw;
        throw; // Ném lại CHÍNH XÁC đối tượng ngoại lệ ban đầu, giữ nguyên kiểu Derived!
    }
}

int main()
{
    try
    {
        handleProcess();
    }
    catch (const CustomDerivedException& e)
    {
        std::cout << "main() bat dung kieu CustomDerivedException: " << e.what() << '\n';
    }
    catch (const std::exception& e)
    {
        std::cout << "main() bat std::exception (neu bi slicing se roi vao day!)\n";
    }

    return 0;
}
```

::: tip Quy Tắc Vàng
Để ném lại ngoại lệ đang bắt, **LUÔN LUÔN DÙNG TỪ KHÓA `throw;` ĐỨNG ĐỘC LẬP KHÔNG CÓ THAM SỐ!**
:::
