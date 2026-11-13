# 8.7 — Câu Lệnh Goto (Goto Statements)

---

## 🎯 Mục Tiêu Bài Học
- Hiểu cú pháp của câu lệnh `goto` và các nhãn câu lệnh (Statement Labels).
- Hiểu lý do tại sao `goto` biến mã nguồn thành "Spaghetti Code" và bị cấm trong hầu hết quy chuẩn lập trình hiện đại.
- Trường hợp ngoại lệ duy nhất được chấp nhận: Thoát nhanh khỏi nhiều vòng lặp lồng nhau sâu.

---

## 1. Cú Pháp Câu Lệnh `goto`

Câu lệnh `goto` thực hiện một cú nhảy vô điều kiện đến một **Nhãn (Label)** trong cùng một hàm:

```cpp
#include <iostream>

int main()
{
    double x {};
tryAgain: // Nhãn câu lệnh kết thúc bằng dấu hai chấm :
    std::cout << "Nhap so khong am: ";
    std::cin >> x;

    if (x < 0.0)
        goto tryAgain; // Nhảy ngược lại nhãn tryAgain!

    std::cout << "So da nhap: " << x << '\n';
    return 0;
}
```

---

## 2. Vì Sao Phải Hạn Chế Tối Đa `goto`?

Năm 1968, nhà khoa học máy tính huyền thoại Edsger Dijkstra đã viết bài báo nổi tiếng: *"Go To Statement Considered Harmful"*. 
- `goto` cho phép nhảy tự do tới bất kỳ đâu trong hàm, phá vỡ cấu trúc khối, làm mất khả năng suy luận logic và khiến việc theo dõi luồng chạy trở thành ác mộng (Spaghetti Code).
- Không bao giờ được dùng `goto` để nhảy qua một câu lệnh khởi tạo biến.

::: tip 💡 Trường Hợp Ngoại Lệ Hiếm Hoi
Thoát ra khỏi 3-4 vòng lặp lồng nhau sâu khi phát hiện lỗi hoặc tìm thấy kết quả:
```cpp
for (int i = 0; i < N; ++i)
    for (int j = 0; j < M; ++j)
        for (int k = 0; k < K; ++k)
            if (foundTarget(i, j, k))
                goto end_search; // Thoát ngay lập tức khỏi cả 3 vòng lặp!

end_search:
    std::cout << "Tim kiem hoan tat.\n";
```
:::
