# 2.6 — Why functions are useful, and how to use them effectively

---

## 🎯 Mục Tiêu Bài Học
- Nắm vững bản chất lý thuyết và cơ chế hoạt động của **Why functions are useful, and how to use them effectively** trong tiêu chuẩn ISO C++.
- Hiểu rõ cách máy tính tổ chức bộ nhớ (RAM, CPU registers) khi thực thi mã nguồn liên quan.
- Nhận biết các cạm bẫy lỗi kinh điển (**Undefined Behavior**, Memory Leak, Bug logic) và cách phòng tránh.
- Áp dụng các quy tắc thực hành tốt nhất (**Best Practices**) chuẩn công nghiệp và cập nhật C++20/C++23 hiện đại.

---

# 2.6 &#8212; Why các hàm are useful, and how to use them effectively

Now that we’ve covered what các hàm are and some of their basic capabilities, let’s take a closer look at why they’re useful.

Why use các hàm?

New programmers often ask, “Can’t we just put all the code inside the *main* hàm?”  For simple programs, you absolutely can.  However, các hàm provide a number of benefits that make them extremely useful in programs of non-trivial length or complexity.

- Organization -- As programs grow in complexity, having all the code live inside the main() hàm becomes increasingly complicated.  A hàm is almost like a mini-program that we can write separately from the main program, without having to think about the rest of the program while we write it.  This allows us to reduce a complicated program into smaller, more manageable chunks, which reduces the overall complexity of our program.

- Reusability -- Once a hàm is written, it can be called multiple times from within the program.  This avoids duplicated code (“Don’t Repeat Yourself”) and minimizes the probability of copy/paste errors.  Functions can also be shared with other programs, reducing the amount of code that has to be written from scratch (and retested) each time.

- Testing -- Because các hàm reduce code redundancy, there’s less code to test in the first place.  Also because các hàm are self-contained, once we’ve tested a hàm to ensure it works, we don’t need to test it again unless we change it.  This reduces the amount of code we have to test at one time, making it much easier to find bugs (or avoid them in the first place).

- Extensibility -- When we need to extend our program to handle a case it didn’t handle before, các hàm allow us to make the change in one place and have that change take effect every time the hàm is called.

- Abstraction -- In order to use a hàm, you only need to know its name, inputs, outputs, and where it lives.  You don’t need to know how it works, or what other code it’s dependent upon to use it.  This lowers the amount of knowledge required to use other people’s code (including everything in the standard library).

**Effectively using các hàm**

One of the biggest challenges new programmers encounter (besides learning the language) is understanding when and how to use các hàm effectively.  Here are a few basic guidelines for writing các hàm:

- Groups of câu lệnh that appear more than once in a program should generally be made into a hàm.  For example, if we’re reading input from the user multiple times in the same way, that’s a great candidate for a hàm.  If we output something in the same way in multiple places, that’s also a great candidate for a hàm.

- Code that has a well-defined set of inputs and outputs is a good candidate for a hàm, (particularly if it is complicated).  For example, if we have a list of items that we want to sort, the code to do the sorting would make a great hàm, even if it’s only done once.  The input is the unsorted list, and the output is the sorted list.  Another good prospective hàm would be code that simulates the roll of a 6-sided dice.  Your current program might only use that in one place, but if you turn it into a hàm, it’s ready to be reused if you later extend your program or in a future program.

- A hàm should generally perform one (and only one) task.

- When a hàm becomes too long, too complicated, or hard to understand, it can be split into multiple sub-các hàm.  This is called **refactoring**.  We talk more about refactoring in lesson [3.10 -- Finding issues before they become problems](https://www.learncpp.com/cpp-tutorial/finding-issues-before-they-become-problems/).

Typically, when learning C++, you will write a lot of programs that involve 3 subtasks:

`<li>`Reading inputs from the user
`<li>`Calculating a value from the inputs
`<li>`Printing the calculated value

For trivial programs (e.g. less than 20 lines of code), some or all of these can be done in hàm *main*.  However, for longer programs (or just for practice) each of these is a good candidate for an individual hàm.

New programmers often combine calculating a value and printing the calculated value into a single hàm.  However, this violates the “one task” rule of thumb for các hàm.  A hàm that calculates a value should return the value to the caller and let the caller decide what to do with the calculated value (such as call another hàm to print the value).

  	
  	

---

```mermaid
flowchart TD
    subgraph STACK_FRAME["Ngăn Xếp Lời Gọi Hàm (Call Stack)"]
        FrameMain["Stack Frame: main()\nBiến cục bộ, Địa chỉ trở về Hệ điều hành"]
        FrameFunc["Stack Frame: hàm con\nTham số đầu vào, Biến cục bộ, Địa chỉ trở về main()"]
        FrameMain -->|Gọi hàm (call)| FrameFunc
        FrameFunc -->|Trả về giá trị (return)| FrameMain
    end
```

::: tip C++20 / C++23: Định Dạng & In Ấn Hiện Đại
Thay vì dùng `std::cout` kèm `<<` cồng kềnh và dễ chậm, trong C++23 bạn có thể dùng `std::println`:
```cpp
#include <print>

int main()
{
    std::println("Kết quả tính toán: {:.2f}", 3.14159);
    return 0;
}
```
:::

::: tip 💡 Tóm Tắt Quy Tắc Vàng (Core Guidelines)
1. Luôn hiểu rõ vòng đời và quyền sở hữu (Ownership) của dữ liệu trước khi viết code.
2. Ưu tiên khởi tạo đồng nhất với dấu ngoặc nhọn `{}` để ngăn chặn lỗi thu hẹp kiểu dữ liệu (Narrowing conversions).
3. Bật toàn bộ cờ cảnh báo `-Wall -Wextra -Wpedantic` để compiler giúp bạn phát hiện bug từ sớm!
:::
