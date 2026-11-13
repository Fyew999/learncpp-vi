# 21.1 — Introduction to operator overloading

---

## 🎯 Mục Tiêu Bài Học
- Nắm vững bản chất lý thuyết và cơ chế hoạt động của **Introduction to operator overloading** trong tiêu chuẩn ISO C++.
- Hiểu rõ cách máy tính tổ chức bộ nhớ (RAM, CPU registers) khi thực thi mã nguồn liên quan.
- Nhận biết các cạm bẫy lỗi kinh điển (**Undefined Behavior**, Memory Leak, Bug logic) và cách phòng tránh.
- Áp dụng các quy tắc thực hành tốt nhất (**Best Practices**) chuẩn công nghiệp và cập nhật C++20/C++23 hiện đại.

---

# 21.1 &#8212; Introduction to toán tử overloading

Trong bài học [11.1 -- Introduction to hàm overloading](https://www.learncpp.com/cpp-tutorial/introduction-to-hàm-overloading/), you learned about hàm overloading, which provides a mechanism to create and resolve hàm calls to multiple các hàm with the same name, so long as each hàm has a unique hàm prototype.  This allows you to create variations of a hàm to work with different các kiểu dữ liệu, without having to think up a unique name for each variant.

In C++, các toán tử are implemented as các hàm.  By using hàm overloading on the toán tử các hàm, you can define your own versions of the các toán tử that work with different các kiểu dữ liệu (including classes that you’ve written).  Using hàm overloading to overload các toán tử is called **toán tử overloading**.

In this chapter, we’ll examine topics related to toán tử overloading.

**Operators as các hàm**

Consider the following example:

```cpp
int x { 2 };
int y { 3 };
std::cout << x + y << '\n';
```

The trình biên dịch comes with a built-in version of the plus toán tử (+) for integer operands -- this hàm adds integers x and y together and returns an integer result.  When you see the biểu thức `x + y`, you can translate this in your head to the hàm call `toán tử+(x, y)` (where toán tử+ is the name of the hàm). 

Now consider this similar snippet:

```cpp
double z { 2.0 };
double w { 3.0 };
std::cout << w + z << '\n';
```

The trình biên dịch also comes with a built-in version of the plus toán tử (+) for double operands.  Expression w + z becomes hàm call `toán tử+(w, z)`, and hàm overloading is used to determine that the trình biên dịch should be calling the double version of this hàm instead of the integer version.

Now consider what happens if we try to add two đối tượng of a program-defined class:

```cpp
Mystring string1 { "Hello, " };
Mystring string2 { "World!" };
std::cout << string1 + string2 << '\n';
```

What would you expect to happen in this case?  The intuitive expected result is that the string “Hello, World!” would be printed on the screen.  However, because Mystring is a program-defined type, the trình biên dịch does not have a built-in version of the plus toán tử that it can use for Mystring operands.  So in this case, it will give us an error.  In order to make it work like we want, we’d need to write an overloaded hàm to tell the trình biên dịch how the + toán tử should work with two operands of type Mystring.  We’ll look at how to do this in the next lesson.

**Resolving overloaded các toán tử**

When evaluating an biểu thức containing an toán tử, the trình biên dịch uses the following rules:

`<li>`If *all* of the operands are fundamental các kiểu dữ liệu, the trình biên dịch will call a built-in routine if one exists.  If one does not exist, the trình biên dịch will produce a trình biên dịch error.
`<li>`If *any* of the operands are program-defined types (e.g. one of your classes, or an enum type), the trình biên dịch will use the hàm overload resolution algorithm (described in lesson [11.3 -- Function overload resolution and ambiguous matches](https://www.learncpp.com/cpp-tutorial/hàm-overload-resolution-and-ambiguous-matches/)) to see if it can find an overloaded toán tử that is an unambiguous best match.  This may involve implicitly converting one or more operands to match the tham số types of an overloaded toán tử.  It may also involve implicitly converting program-defined types into các kiểu dữ liệu cơ bản (via an overloaded typecast, which we’ll cover later in this chapter) so that it can match a built-in toán tử.  If no match can be found (or an ambiguous match is found), the trình biên dịch will error.

**What are the limitations on toán tử overloading?**

First, almost any existing toán tử in C++ can be overloaded.  The exceptions are: conditional (?:), sizeof, phạm vi truy cập (scope) (::), member selector (.), con trỏ member selector (.*), typeid, and the casting các toán tử.

Second, you can only overload the các toán tử that exist.  You can not create new các toán tử or rename existing các toán tử.  For example, you could not create an `toán tử**` to do exponents.

Third, at least one of the operands in an overloaded toán tử must be a user-defined type.  This means you could overload `toán tử+(int, Mystring)`, but not `toán tử+(int, double)`.

Because standard library classes are considered to be user-defined, this means you could define `toán tử+(double, std::string)`.  However, this is not a good idea because a future language standard could define this overload, which could break any programs that used your overload.  Thus a thực hành tốt nhất (Best Practice) is that your overloaded các toán tử should operate on at least one program-defined type.  This guarantees that a future language standard won’t potentially break your programs.

::: tip Thực hành tốt nhất (Best Practice)

An overloaded toán tử should operate on at least one program-defined type (either as a tham số of the hàm, or the implicit object).

:::

Fourth, it is not possible to change the number of operands an toán tử supports.

Finally, all các toán tử keep their default precedence and associativity (regardless of what they’re used for) and this can not be changed.

Some new programmers attempt to overload the bitwise XOR toán tử (^) to do exponentiation.  However, in C++, toán tử^ has a lower precedence level than the basic arithmetic các toán tử, which causes biểu thức to evaluate incorrectly.

In basic mathematics, exponentiation is resolved before basic arithmetic, so 4 + 3 ^ 2 resolves as 4 + (3 ^ 2) =&gt; 4 + 9 =&gt; 13.

However, in C++, the arithmetic các toán tử have higher precedence than toán tử^, so 4 + 3 ^ 2 resolves as (4 + 3) ^ 2 =&gt; 7 ^ 2 =&gt; 49.

You’d need to explicitly parenthesize the exponent portion (e.g. 4 + (3 ^ 2)) every time you used it for this to work properly, which isn’t intuitive, and is potentially error-prone.

Because of this precedence issue, it’s generally a good idea to use các toán tử only in an analogous way to their original intent.

::: tip Thực hành tốt nhất (Best Practice)

When overloading các toán tử, it’s best to keep the hàm of the các toán tử as close to the original intent of the các toán tử as possible.

:::

Furthermore, because các toán tử don’t have descriptive names, it’s not always clear what they are intended to do.  For example, toán tử+ might be a reasonable choice for a string class to do concatenation of strings.  But what about toán tử-?  What would you expect that to do?  It’s unclear.

::: tip Thực hành tốt nhất (Best Practice)

If the meaning of an overloaded toán tử is not clear and intuitive, use a named hàm instead.

:::

Finally, overloaded các toán tử should các giá trị trả về in the way that is consistent with the original các toán tử.  Operators that do not modify their operands (e.g. arithmetic các toán tử) should generally return results by value.  Operators that modify their leftmost operand (e.g. pre-increment, any of the phép gán các toán tử) should generally return the leftmost operand by tham chiếu.

::: tip Thực hành tốt nhất (Best Practice)

Operators that do not modify their operands (e.g. arithmetic các toán tử) should generally return results by value.

Operators that modify their leftmost operand (e.g. pre-increment, any of the phép gán các toán tử) should generally return the leftmost operand by tham chiếu.

:::

Within those confines, you will still find plenty of useful functionality to overload for your custom classes!  You can overload the + toán tử to concatenate your program-defined string class, or add two Fraction class đối tượng together.  You can overload the &lt;&lt; toán tử to make it easy to print your class to the screen (or a file).   You can overload the equality toán tử (==) to compare two class đối tượng.  This makes toán tử overloading one of the most useful features in C++ -- simply because it allows you to work with your classes in a more intuitive way.

In the upcoming lessons, we’ll take a deeper look at overloading different kinds of các toán tử.

  	
  	

---

::: tip 💡 Tóm Tắt Quy Tắc Vàng (Core Guidelines)
1. Luôn hiểu rõ vòng đời và quyền sở hữu (Ownership) của dữ liệu trước khi viết code.
2. Ưu tiên khởi tạo đồng nhất với dấu ngoặc nhọn `{}` để ngăn chặn lỗi thu hẹp kiểu dữ liệu (Narrowing conversions).
3. Bật toàn bộ cờ cảnh báo `-Wall -Wextra -Wpedantic` để compiler giúp bạn phát hiện bug từ sớm!
:::
