# 27.9 — Từ Khóa `noexcept` Trong C++11

---

## 🎯 Mục Tiêu Bài Học
- Hiểu ý nghĩa của chỉ định đặc tả **`noexcept`** trong C++11.
- Nắm vững toán tử kiểm tra tại compile-time: `noexcept(biểu_thức)`.
- Hiểu tại sao `noexcept` là điều kiện tiên quyết để các container như `std::vector` kích hoạt Move Semantics siêu tốc.

---

## 1. Từ Khóa `noexcept` Là Gì?

Trong C++11, từ khóa `noexcept` được dùng để thông báo cho trình biên dịch và lập trình viên biết rằng: **Hàm này đảm bảo 100% sẽ không bao giờ ném ra bất kỳ ngoại lệ nào**.

```cpp
void doSomethingFast() noexcept // Cam ket khong nem ngoai le
{
    // ...
}
```

Nếu một hàm được đánh dấu `noexcept` mà bên trong nó vẫn ném ra ngoại lệ mà không tự bắt, `std::terminate()` sẽ được gọi ngay lập tức để ngắt chương trình.

---

## 2. Lợi Ích Khổng Lồ Của `noexcept` Với Hiệu Năng

Khi trình biên dịch biết một hàm là `noexcept`, nó có thể áp dụng các tối ưu hóa cực kỳ mạnh tay:
1. Compiler không cần sinh các mã bảo vệ cuộn ngược ngăn xếp cho hàm đó, giúp kích thước code nhỏ gọn hơn.
2. **Kích hoạt Move Semantics trong Thư viện chuẩn**:
   Khi một `std::vector` cần mở rộng dung lượng, nó phải chuyển các phần tử từ vùng nhớ cũ sang vùng nhớ mới. 
   - Nếu Move Constructor của đối tượng là `noexcept`, vector sẽ dùng **Move** (nhanh gấp hàng trăm lần).
   - Nếu Move Constructor có thể ném ngoại lệ, vector sẽ buộc phải chuyển về dùng **Copy** chậm chạp để đảm bảo an toàn dữ liệu!
