# 🏆 CP.03: Kho Vũ Khí STL C++17 Thi Đấu

&gt; **Sức mạnh vô địch của C++**: C++ được mệnh danh là "ông vua lập trình thi đấu" nhờ sở hữu thư viện mẫu chuẩn **Standard Template Library (STL)**. Nắm vững STL giúp bạn rút ngắn bài toán phức tạp từ 100 dòng code xuống chỉ còn 5 dòng ngắn gọn!

---

## 1. `std::vector` & Kỹ Thuật Tối Ưu Mảng Động

Khác với mảng tĩnh, `std::vector` có thể thay đổi kích thước linh hoạt và sở hữu hàng loạt phương thức hữu ích.

```cpp
#include <vector>
#include <iostream>

using namespace std;

int main() {
    // Khởi tạo vector n phần tử với giá trị mặc định là 0
    int n = 5;
    vector<int> a(n, 0);

    // Kỹ thuật reserve() tránh cấp phát lại (reallocation) O(N) khi biết trước số phần tử
    vector<int> b;
    b.reserve(100000); // Tiết kiệm đáng kể thời gian push_back!

    // Khởi tạo ma trận động 2 chiều (N dòng, M cột) giá trị 0
    int rows = 3, cols = 4;
    vector<vector<int>> matrix(rows, vector<int>(cols, 0));

    return 0;
}
```

---

## 2. Structured Binding C++17 Với `std::pair` & `std::tuple`

C++17 mang đến tính năng **Structured Binding** (phân rã cấu trúc) giúp việc duyệt và truy xuất các phần tử trong `pair` hay `tuple` trở nên vô cùng thanh lịch:

```cpp
#include <iostream>
#include <vector>
#include <tuple>

using namespace std;

int main() {
    // Danh sách cạnh đồ thị có trọng số: {u, v, weight}
    vector<tuple<int, int, int>> edges = {
        {1, 2, 10},
        {2, 3, 15},
        {1, 3, 20}
    };

    // Trước C++17: Phải dùng get<0>(e), get<1>(e), get<2>(e) rất dài dòng
    // Chuẩn C++17: Phân rã tức thì!
    for (const auto& [u, v, w] : edges) {
        cout << "Canh tu " << u << " den " << v << " co trong so: " << w << '\n';
    }

    return 0;
}
```

---

## 3. Sắp Xếp Nâng Cao Với `std::sort` & Lambda C++17

```cpp
#include <algorithm>
#include <vector>
#include <iostream>

using namespace std;

struct ThiSinh {
    string ten;
    int diem_toan;
    int diem_tin;
};

int main() {
    vector<ThiSinh> ds = {
        {"An", 9, 10},
        {"Binh", 10, 8},
        {"Cuong", 10, 10}
    };

    // Sắp xếp theo thứ tự: Điểm Tin giảm dần, nếu bằng nhau thì Điểm Toán giảm dần
    sort(ds.begin(), ds.end(), [](const ThiSinh& a, const ThiSinh& b) {
        if (a.diem_tin != b.diem_tin) {
            return a.diem_tin > b.diem_tin; // Tin lớn hơn đứng trước
        }
        return a.diem_toan > b.diem_toan;   // Toán lớn hơn đứng trước
    });

    for (const auto& [ten, toan, tin] : ds) {
        cout << ten << ": Toan=" << toan << ", Tin=" << tin << '\n';
    }

    return 0;
}
```

---

## 4. Chặt Nhị Phân Thần Tốc: `lower_bound` & `upper_bound`

&gt; [!IMPORTANT] Điều Kiện Tiên Quyết
&gt; Mảng hoặc vector **BẮT BUỘC PHẢI ĐƯỢC SẮP XẾP TĂNG DẦN** trước khi gọi `lower_bound` hoặc `upper_bound`.

- `lower_bound(begin, end, val)`: Trả về iterator trỏ tới phần tử đầu tiên **$\ge val$**.
- `upper_bound(begin, end, val)`: Trả về iterator trỏ tới phần tử đầu tiên **$&gt; val$**.

```cpp
#include <algorithm>
#include <vector>
#include <iostream>

using namespace std;

int main() {
    vector<int> a = {1, 3, 3, 5, 7, 9};

    // Tìm vị trí phần tử đầu tiên >= 3
    auto it1 = lower_bound(a.begin(), a.end(), 3);
    int idx1 = it1 - a.begin(); // Vị trí (chỉ số 0): 1

    // Tìm vị trí phần tử đầu tiên > 3
    auto it2 = upper_bound(a.begin(), a.end(), 3);
    int idx2 = it2 - a.begin(); // Vị trí (chỉ số 0): 3 (giá trị 5)

    // Đếm số lần xuất hiện của giá trị 3 trong O(log N):
    int count_3 = upper_bound(a.begin(), a.end(), 3) - lower_bound(a.begin(), a.end(), 3);
    cout << "So luong phan tu 3 la: " << count_3 << '\n'; // In ra: 2

    return 0;
}
```

---

## 5. Hàng Đợi Ưu Tiên: `std::priority_queue` (Max-Heap & Min-Heap)

`priority_queue` tự động duy trì phần tử lớn nhất hoặc nhỏ nhất ở đỉnh trong thời gian $O(\log N)$.

```cpp
#include <queue>
#include <vector>
#include <iostream>

using namespace std;

int main() {
    // 1. Mặc định là Max-Heap (Phần tử lớn nhất luôn ở top)
    priority_queue<int> max_heap;
    max_heap.push(10);
    max_heap.push(30);
    max_heap.push(20);
    cout << "Dinh Max-Heap: " << max_heap.top() << '\n'; // In ra 30

    // 2. Khởi tạo Min-Heap (Phần tử nhỏ nhất ở top - Cực kỳ hữu dụng cho Dijkstra)
    priority_queue<int, vector<int>, greater<int>> min_heap;
    min_heap.push(10);
    min_heap.push(30);
    min_heap.push(20);
    cout << "Dinh Min-Heap: " << min_heap.top() << '\n'; // In ra 10

    return 0;
}
```

---

## 6. `std::set`, `std::multiset` vs `std::unordered_map`

### Bảng So Sánh Chiến Lược Chọn Cấu Trúc Dữ Liệu:

| Cấu trúc | Cơ chế cốt lõi | Tìm kiếm / Thêm / Xóa | Điểm mạnh | Bẫy cần tránh |
| :--- | :--- | :--- | :--- | :--- |
| `std::set` | Cây Đỏ Đen (Red-Black Tree) | $O(\log N)$ | Tự động sắp xếp, không trùng lặp | Chậm hơn Hash Table nếu không cần thứ tự |
| `std::multiset` | Cây Đỏ Đen | $O(\log N)$ | Cho phép các giá trị trùng nhau | `ms.erase(val)` sẽ xóa TẤT CẢ bản sao! |
| `std::unordered_map` | Bảng Băm (Hash Table) | $O(1)$ trung bình | Cực nhanh khi đếm tần suất | Bị hack $O(N)$ bởi anti-hash test trên Codeforces! |

&gt; [!WARNING] Cạm Bẫy Hàm Xóa Của `std::multiset`
&gt; - `ms.erase(x)`: Sẽ xóa **TOÀN BỘ** các phần tử có giá trị bằng $x$ trong multiset!
&gt; - Nếu chỉ muốn xóa **MỘT bản sao duy nhất**: Phải xóa qua iterator:  
&gt;   `auto it = ms.find(x); if (it != ms.end()) ms.erase(it);`

---

## 7. Các Hàm Thuật Toán Thần Thánh C++17

1. **`std::gcd` và `std::lcm` (Chuẩn C++17 trong `<numeric>`)**:
   ```cpp
   #include <numeric>
   int ucln = std::gcd(24, 36); // 12
   int bcnn = std::lcm(12, 18); // 36
   ```
2. **Sinh hoán vị kế tiếp với `std::next_permutation`**:
   ```cpp
   vector<int> p = {1, 2, 3};
   do {
       // Xử lý từng hoán vị: 1 2 3, 1 3 2, 2 1 3...
   } while (next_permutation(p.begin(), p.end()));
   ```
3. **Thao tác mảng nhanh**:
   - `std::fill(a.begin(), a.end(), -1);`
   - `std::reverse(a.begin(), a.end());`
   - `std::accumulate(a.begin(), a.end(), 0LL);` (Tính tổng mảng)
