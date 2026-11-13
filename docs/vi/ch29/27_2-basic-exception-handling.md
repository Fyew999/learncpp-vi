# 27.2 — Cơ Chế Xử Lý Ngoại Lệ Cơ Bản (try, throw, catch)

---

## 🎯 Mục Tiêu Bài Học
- Nắm vững 3 từ khóa nền tảng: **`throw`**, **`try`**, và **`catch`**.
- Hiểu luồng chuyển giao quyền điều khiển khi một ngoại lệ được kích hoạt.
- Thực hành bắt các ngoại lệ với nhiều kiểu dữ liệu khác nhau.

---

## 1. Cấu Trúc Khối `try - catch` Và Lệnh `throw`

Xử lý ngoại lệ trong C++ dựa trên bộ ba từ khóa:
1. **`throw`**: Dùng để ném ra một đối tượng ngoại lệ khi phát hiện sự cố.
2. **`try`**: Bao bọc một khối lệnh có thể phát sinh ngoại lệ.
3. **`catch`**: Bắt và xử lý ngoại lệ có kiểu dữ liệu tương ứng.

```cpp
#include <iostream>
#include <string_view>

double divide(double a, double b)
{
    if (b == 0.0)
    {
        // 1. Ném ngoại lệ kiểu const char*
        throw "Loi chia cho so 0!";
    }
    return a / b;
}

int main()
{
    std::cout << "Nhap hai so: ";
    double x{ 10.0 };
    double y{ 0.0 };

    // 2. Bao bọc mã nguồn rủi ro trong khối try
    try
    {
        double result = divide(x, y);
        // Dòng lệnh dưới đây SẼ BỊ BỎ QUA nếu có ngoại lệ ném ra!
        std::cout << "Ket qua: " << result << '\n';
    }
    // 3. Bắt ngoại lệ kiểu const char*
    catch (const char* errorMessage)
    {
        std::cerr << "Phat hien su co: " << errorMessage << '\n';
    }

    std::cout << "Chuong trinh tiep tuc thuc thi an toan!\n";
    return 0;
}
```

### Kết quả xuất ra màn hình:
```text
Phat hien su co: Loi chia cho so 0!
Chuong trinh tiep tuc thuc thi an toan!
```

---

## 2. Luồng Điều Khiển Khi Ném Ngoại Lệ

1. Khi lệnh `throw` được thực thi, C++ **lập tức tạm dừng hàm hiện tại**.
2. Nó kiểm tra xem lệnh `throw` có nằm bên trong một khối `try` hay không.
3. Nếu có, nó so khớp kiểu của đối tượng được ném với danh sách các khối `catch` bên dưới theo thứ tự từ trên xuống dưới.
4. Khi tìm thấy khối `catch` phù hợp, luồng điều khiển nhảy thẳng vào khối đó. Sau khi khối `catch` chạy xong, chương trình tiếp tục chạy các lệnh bình thường phía sau khối `catch` đó!
