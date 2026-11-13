# 🏆 CP.04: Số Học & Toán Học Cốt Lõi Cho Chuyên Tin

&gt; **Toán học - Linh hồn của Chuyên Tin**: Hầu hết các đề thi vào lớp 10 Chuyên Tin và kỳ thi Học sinh Giỏi đều dành ít nhất 1 đến 2 bài cho mảng **Số Học (Number Theory)**: số nguyên tố, ước số, phép toán đồng dư và tổ hợp. Nắm chắc phần này giúp bạn giành trọn 40% điểm của đề thi!

---

## 1. Số Học Đồng Dư (Modular Arithmetic) Chuẩn Mực

Khi kết quả bài toán quá lớn, đề bài thường yêu cầu: *"Hãy in ra kết quả sau khi chia lấy dư cho $10^9 + 7$"*.

### 4 Quy Tắc Bất Di Bất Dịch:

1. **Phép cộng**: $(A + B) \pmod M = ((A \pmod M) + (B \pmod M)) \pmod M$
2. **Phép nhân**: $(A \times B) \pmod M = ((A \pmod M) \times (B \pmod M)) \pmod M$
3. **Phép trừ (Cực kỳ dễ ăn bẫy số âm!)**:
   ```cpp
   // ❌ SAI LẦM: (A - B) % MOD có thể ra số âm trong C++!
   // ✅ CHUẨN XÁC: Luôn cộng thêm MOD trước khi chia dư:
   int ans = ((A % MOD) - (B % MOD) + MOD) % MOD;
   ```
4. **Phép chia**: **KHÔNG ĐƯỢC PHÉP** chia trực tiếp $((A \pmod M) / (B \pmod M)) \pmod M$! Phải dùng **Nghịch đảo Modulo (Modular Inverse)**!

---

## 2. Lũy Thừa Nhị Phân (Binary Exponentiation) $O(\log B)$

Tính $A^B \pmod M$ với $B$ lên tới $10^{18}$ chỉ trong khoảng 60 phép tính:

```cpp
#include <iostream>

using namespace std;
using ll = long long;

// Hàm tính (base^exp) % mod trong O(log exp)
ll power_mod(ll base, ll exp, ll mod) {
    ll res = 1;
    base %= mod;
    while (exp > 0) {
        if (exp % 2 == 1) { // Nếu bit cuối là 1
            res = (__int128_t)res * base % mod; // Dùng __int128_t chống tràn nếu mod lớn
        }
        base = (__int128_t)base * base % mod;
        exp /= 2;
    }
    return res;
}

int main() {
    cout << "2^100 % (1e9+7) = " << power_mod(2, 100, 1e9 + 7) << '\n';
    return 0;
}
```

---

## 3. Sàng Số Nguyên Tố Eratosthenes Siêu Nhanh

Kiểm tra số nguyên tố cho toàn bộ các số từ $1$ đến $N$ ($N \le 10^7$) trong thời gian $O(N \log \log N)$:

```cpp
#include <vector>
#include <iostream>

using namespace std;

const int MAXN = 1e7 + 5;
// Dùng vector<bool> được C++ tối ưu hóa từng bit (1 bit/phần tử) tiết kiệm 8 lần RAM!
vector<bool> is_prime(MAXN, true);

void sieve(int n) {
    is_prime[0] = is_prime[1] = false;
    for (int p = 2; p * p <= n; ++p) {
        if (is_prime[p]) {
            // Đánh dấu các bội số của p bắt đầu từ p*p
            for (int i = p * p; i <= n; i += p) {
                is_prime[i] = false;
            }
        }
    }
}

int main() {
    int n = 1000000;
    sieve(n);
    cout << "So 999983 co nguyen to khong? " << (is_prime[999983] ? "Co" : "Khong") << '\n';
    return 0;
}
```

---

## 4. Nghịch Đảo Modulo & Định Lý Fermat Nhỏ

&gt; **Định lý Fermat Nhỏ**: Nếu $M$ là một số nguyên tố và $B$ không chia hết cho $M$, thì:
&gt; $$B^{M-1} \equiv 1 \pmod M \implies B \cdot B^{M-2} \equiv 1 \pmod M$$
&gt; Do đó, nghịch đảo modulo của $B$ theo modulo $M$ chính là:
&gt; $$B^{-1} \equiv B^{M-2} \pmod M$$

### Ứng dụng tính phép chia dư:
$$\frac{A}{B} \pmod M = (A \times B^{M-2}) \pmod M$$

```cpp
ll mod_inverse(ll b, ll mod) {
    return power_mod(b, mod - 2, mod);
}

ll divide_mod(ll a, ll b, ll mod) {
    return (a % mod * mod_inverse(b, mod)) % mod;
}
```

---

## 5. Tính Tổ Hợp Chập $K$ Của $N$ ($nCk \pmod M$) Trong $O(1)$

Bài toán đếm số cách chọn trong đề thi thường có $N, K \le 10^6$ và có nhiều truy vấn:

```cpp
#include <vector>
#include <iostream>

using namespace std;
using ll = long long;

const int MAXN = 1e6 + 5;
const ll MOD = 1e9 + 7;

ll fact[MAXN];    // fact[i] = i! % MOD
ll inv_fact[MAXN];// inv_fact[i] = (i!)^(-1) % MOD

ll power_mod(ll base, ll exp) {
    ll res = 1;
    base %= MOD;
    while (exp > 0) {
        if (exp & 1) res = (res * base) % MOD;
        base = (base * base) % MOD;
        exp >>= 1;
    }
    return res;
}

// Tiền xử lý mảng giai thừa trong O(N)
void precompute(int n) {
    fact[0] = 1;
    inv_fact[0] = 1;
    for (int i = 1; i <= n; ++i) {
        fact[i] = (fact[i - 1] * i) % MOD;
    }
    // Nghịch đảo của n!
    inv_fact[n] = power_mod(fact[n], MOD - 2);
    for (int i = n - 1; i >= 1; --i) {
        inv_fact[i] = (inv_fact[i + 1] * (i + 1)) % MOD;
    }
}

// Trả về nCk % MOD chỉ trong O(1)!
ll nCr(int n, int r) {
    if (r < 0 || r > n) return 0;
    return fact[n] * inv_fact[r] % MOD * inv_fact[n - r] % MOD;
}

int main() {
    precompute(1000000);
    cout << "So cach chon 3 hoc sinh tu 10 hoc sinh: " << nCr(10, 3) << '\n'; // 120
    return 0;
}
```
