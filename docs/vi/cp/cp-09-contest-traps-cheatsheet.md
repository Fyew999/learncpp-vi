# 🏆 CP.09: Bí Kíp Bắt Lỗi, Bẫy Phòng Thi & Cheatsheet C++17 Tóm Tắt

&gt; **Lời dặn trước giờ thi**: Trong phòng thi áp lực cao, một dấu chấm phẩy, một lỗi tràn số hay một lần quên reset mảng có thể cướp đi công sức ôn luyện cả năm trời của bạn. Hãy ghi nhớ bảng kiểm tra (checklist) này trước khi nhấn nút nộp bài!

---

## 1. 10 Lỗi Mất Điểm Oan Uổng Kinh Điển

1. **Khác tên file `freopen`**:
   - Đề bài ghi `BAI1.INP` nhưng bạn gõ `bai1.inp` hoặc `bai1.in` $\to$ **0 điểm**.
   - Hãy sao chép chính xác từng ký tự tên file trong đề bài!

2. **Tràn số nguyên `int`**:
   - Kết quả hoặc tổng trung gian vượt quá $2 \cdot 10^9$ nhưng vẫn dùng `int`.
   - Phép nhân `a * b` mà không ép kiểu `1LL * a * b`.

3. **Truy cập ngoài biên mảng (Out of Bounds)**:
   - Mảng khai báo `a[100]` nhưng truy cập `a[100]` khi chỉ số từ $0 \dots 99$.
   - Mảng toàn cục luôn khai báo dư ra ít nhất 5 phần tử: `const int MAXN = 1e5 + 5; int a[MAXN];`.

4. **Khai báo mảng lớn cục bộ trong hàm**:
   - Gây tràn ngăn xếp (Stack Overflow) dẫn đến lỗi **SIGSEGV / Crash**. Luôn đưa mảng lớn ra biến toàn cục!

5. **Quên làm sạch dữ liệu khi có nhiều bộ test (`while (T--)`)**:
   - Mảng hoặc vector của test trước vẫn còn dữ liệu sang test sau.
   - Nhớ `clear()`, `fill()`, hoặc `memset()` ở đầu mỗi vòng lặp `while (T--)`!
   - &gt; [!WARNING] Cảnh Báo
     &gt; Đừng dùng `memset(a, 0, sizeof(a))` nếu kích thước mảng là $10^6$ nhưng mỗi test case chỉ dùng $N \le 100$! Việc `memset` toàn bộ mảng $10^6$ lặp lại $1000$ lần sẽ gây TLE! Chỉ reset đúng $N$ phần tử đã dùng.

6. **Duyệt `v.size() - 1` khi vector rỗng**:
   - Phương thức `.size()` trả về kiểu số nguyên không dấu `size_t` (unsigned).
   - Nếu vector rỗng, `0 - 1` sẽ bị biến thành $18446744073709551615$ và vòng lặp chạy vô tận!
   - Khắc phục: Ép kiểu `int(v.size())` hoặc dùng macro `#define sz(x) (int)((x).size())`.

7. **Dùng `pow()` của `<cmath>` cho số nguyên**:
   - Hàm `pow(a, b)` tính trên số thực `double`, có thể bị sai số dấu phẩy động (e.g. $5^2$ ra $24.9999999 \to$ ép kiểu `int` thành $24$!).
   - Luôn tự viết hàm lũy thừa nhị phân cho số nguyên!

8. **So sánh hai số thực bằng `==`**:
   - `if (a == b)` với số thực rất dễ sai. Phải dùng: `if (abs(a - b) < 1e-9)`.

9. **Đọc xâu ký tự có dấu cách**:
   - `cin >> s;` chỉ đọc đến dấu cách đầu tiên.
   - Dùng `getline(cin, s);`. Lưu ý: Nếu trước đó có lệnh `cin >> n;`, phải thêm `cin.ignore();` để nuốt ký tự xuống dòng còn sót lại!

10. **Bỏ quên các trường hợp góc (Corner Cases / Edge Cases)**:
    - $N = 1$, $N = 0$.
    - Đồ thị không liên thông, đồ thị là một đường thẳng, cây chỉ có 1 đỉnh.
    - Dãy số toàn số âm.
    - Giá trị $K = 0$.

---

## 2. Bí Kíp Bắt Lỗi Với Cờ Biên Dịch `-fsanitize=address`

Khi luyện tập trên máy cá nhân (Linux / macOS / WSL), hãy biên dịch mã nguồn với cờ kiểm tra lỗi bộ nhớ của GCC:

```bash
g++ -std=c++17 -O2 -fsanitize=address,undefined -Wall solution.cpp -o solution
```

Khi chạy chương trình, nếu bạn truy cập mảng ngoài phạm vi hoặc chia cho 0, trình biên dịch sẽ lập tức chỉ ra **chính xác dòng code** gây lỗi thay vì chỉ báo một câu vô nghĩa "Segmentation Fault"!

---

## 3. Cheatsheet C++17 Thi Đấu Tóm Tắt

```cpp
// 1. Fast I/O
ios_base::sync_with_stdio(false); cin.tie(nullptr);

// 2. Chặt nhị phân
auto it = lower_bound(all(a), x); // >= x
auto it = upper_bound(all(a), x); // > x

// 3. Sắp xếp giảm dần
sort(all(a), greater<int>());

// 4. Tìm Min / Max trong mảng
int min_val = *min_element(all(a));
int max_val = *max_element(all(a));

// 5. Tổng mảng với long long
long long sum = accumulate(all(a), 0LL);

// 6. Xóa phần tử trùng lặp trong vector
sort(all(a));
a.erase(unique(all(a)), a.end());

// 7. Ước chung lớn nhất & Bội chung nhỏ nhất C++17
int g = std::gcd(a, b);
int l = std::lcm(a, b);

// 8. Đảo chuỗi / mảng
reverse(all(a));

// 9. Sinh tập con bằng Bitmask (N <= 20)
for (int mask = 0; mask < (1 << n); ++mask) {
    for (int i = 0; i < n; ++i) {
        if (mask & (1 << i)) {
            // Phần tử thứ i được chọn
        }
    }
}
```

Chúc bạn ôn luyện vững vàng, tư duy sắc bén và đạt kết quả rực rỡ trong kỳ thi vào Chuyên Tin và các đấu trường lập trình! 🚀
