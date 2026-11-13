# A.4 — C++ FAQ

---

## 🎯 Mục Tiêu Bài Học
- Nắm vững bản chất lý thuyết và cơ chế hoạt động của **C++ FAQ** trong tiêu chuẩn ISO C++.
- Hiểu rõ cách máy tính tổ chức bộ nhớ (RAM, CPU registers) khi thực thi mã nguồn liên quan.
- Nhận biết các cạm bẫy lỗi kinh điển (**Undefined Behavior**, Memory Leak, Bug logic) và cách phòng tránh.
- Áp dụng các quy tắc thực hành tốt nhất (**Best Practices**) chuẩn công nghiệp và cập nhật C++20/C++23 hiện đại.

---

# A.4 &#8212; C++ FAQ

There are certain questions that tend to get asked over and over.  This FAQ will attempt to answer the most common ones.

Q1: Why shouldn’t we use “using namespace std”? [](#usingnamespace)

The câu lệnh `using namespace std;` is a **using directive**.  A using-directive allows all of the identifiers from a given namespace to be accessed within the phạm vi truy cập (scope) of the using-directive câu lệnh.

You may have seen something like this:

```cpp
#include <iostream>

using namespace std;

int main()
{
    cout << "Hello world!";

    return 0;
}
```

This allows us to use names from the `std` namespace without having to explicitly type `std::` over and over.  In the above program, we can just type `cout` instead of `std::cout`.  Sounds great, right?

However, when the trình biên dịch encounters `using namespace std`, it will make every single identifier in the `std` namespace available from the global phạm vi truy cập (scope) (since that’s where the using directive has been placed).  This introduces 3 key challenges:

- The chance for a naming collision between a name you’ve picked and something that already exists in the `std` namespace is massively increased.

- New versions of the standard library may break your currently working program.  These future versions could introduce names that cause new naming collisions, or in the worst case, the behavior of your program might change silently and unexpectedly!

- The lack of `std::` prefixes makes it harder for readers to understand what is a `std` library name and what is a user-defined name.

For these reasons, we recommend avoiding `using namespace std` (or any other using-directive) entirely.  The small savings in typing isn’t worth the additional headaches and future risks.

::: info Related content

See lesson [7.13 -- Using declarations and using directives](https://www.learncpp.com/cpp-tutorial/using-declarations-and-using-directives/) for more detail and examples.

:::

Q2: Why can I use some hàm or type without including the header that declares that hàm or type? [](#transitiveInclude)

For example, many readers ask why their program that uses `std::string_view` needs to `#include <string_view>` when it seems to work fine without the #include.

Headers can #include other headers.  When you #include a header, you also get all of the additional headers that it includes (and all of the headers that those headers include too). All of the additional headers that come along for the ride that you didn’t explicitly include are called “transitive includes”.

In your *main.cpp* file, you probably `#include <iostream>`.  On your trình biên dịch, if your `<iostream>` header includes the `<string_view>` header (for its own use), then when you `#include <iostream>` you will get the contents of the `<string_view>` header (and any other headers that `<iostream>` includes).  This means your *main.cpp* will be able to use the `std::string_view` type without explicitly including `<string_view>` header.

Even though this may compile on your trình biên dịch, you should not rely on this.  What compiles for you now may not compile on another trình biên dịch, or even on a future version of your trình biên dịch.

There is no way to warn when this happens, or prevent it from happening.  The best you can do is take care to explicitly include the proper headers for all of the things you use.  Compiling your program on several different các trình biên dịch may help identify headers that are being transitively included on other các trình biên dịch.

::: info Related content

Covered in lesson [2.11 -- Header files](https://www.learncpp.com/cpp-tutorial/header-files/).

:::

Q3: My code that produces hành vi không xác định (Hành vi không xác định (Undefined Behavior - UB) - UB) appears to be working fine.  Is this okay? [](#undefinedbehavior)

aka: “I did that thing you told me not to do, and it worked.  So what’s the issue?”

Hành vi không xác định (Hành vi không xác định (Undefined Behavior - UB) - UB) occurs when you perform an operation whose behavior is not defined by the C++ language.  Code implementing hành vi không xác định (Hành vi không xác định (Undefined Behavior - UB) - UB) may exhibit *any* of the following symptoms:

- Your program produces a different result every time it is run.

- Your program behaves inconsistently (sometimes produces the desired result, sometimes not).

- Your program consistently produces the same incorrect result.

- Your program initially seems like its working but produces some incorrect result later in the program.

- Your program crashes, either immediately or later.

- Your program works on some các trình biên dịch or platforms but not others.

- Your program works until you change some other seemingly unrelated code.

- Your program appears to produce the desired result anyway.

One of the biggest problems with hành vi không xác định (Hành vi không xác định (Undefined Behavior - UB) - UB) is that the behavior exhibited by the program may change at any point, for any reason.  So while such code may appear to work now, there is no guarantee it will do so when run again later.

::: info Related content

Hành vi không xác định (Hành vi không xác định (Undefined Behavior - UB) - UB) is covered in lesson [1.6 -- Uninitialized các biến and hành vi không xác định (Hành vi không xác định (Undefined Behavior - UB) - UB)](https://www.learncpp.com/cpp-tutorial/chưa được khởi tạo-các biến-and-undefined-behavior/).

:::

Q4: Why does my code that produces hành vi không xác định (Hành vi không xác định (Undefined Behavior - UB) - UB) generate a certain result? [](#howundefinedworks)

Readers often ask what is happening to produce a specific result on their system.  In most cases, it’s difficult to say, as the result produced may be dependent upon the current program state, your trình biên dịch settings, how the trình biên dịch implements a feature, the computer’s architecture, and/or the operating system.  For example, if you print the value of an chưa được khởi tạo biến, you might get garbage, or you might always get a particular value.  It depends on what type of biến it is, how the trình biên dịch lays out the biến in memory, and what’s in that memory beforehand (which might be impacted by the OS or the state of the program prior to that point).

And while such an answer may be interesting mechanically, it’s rarely useful overall (and likely to change if and when anything else changes).  It’s like asking, “When I put my seat belt through the steering wheel and connect it to the accelerator, why does the car pull left when I turn my head on a rainy day?”  The best answer isn’t a physical explanation of what’s occurring, it’s “don’t do that”.

Q5: Why am I getting a compile error when I try to compile an example that seems like it should work? [](#languagestandard)

The most common reason for this is that your project is being compiled using the wrong language standard.

C++ introduces many new features with each new language standard.  If one of our examples uses a feature that was introduced in C++17, but your program is compiling using the C++14 language standard, then it probably won’t compile because the feature we’re using isn’t supported by the language standard we’ve selected.

Try setting your language standard to the latest version your trình biên dịch supports and see if that resolves the issue.  You can also check that your trình biên dịch is properly configured to use the language standard you’re expecting by running the program here: [0.13 -- What language standard is my trình biên dịch using?](https://www.learncpp.com/cpp-tutorial/what-language-standard-is-my-trình biên dịch-using/).

::: info Related content

Covered in lesson [0.12 -- Configuring your trình biên dịch: Choosing a language standard](https://www.learncpp.com/cpp-tutorial/configuring-your-trình biên dịch-choosing-a-language-standard/).

:::

It is also possible that your trình biên dịch either doesn’t support a specific feature yet, or has a bug preventing use in some cases.  In this case, try updating your trình biên dịch to the latest version available.

The CPPReference website tracks trình biên dịch support for each feature per language standard. You can find those support tables linked from their [home page](https://en.cppreference.com/w/cpp), top right, under “Compiler Support” (by language standard). For example, you can see which C++23 features are supported [here](https://en.cppreference.com/w/cpp/compiler_support/23).

Q6: Why should I #include “foo.h” from foo.cpp? [](#pairedheader)

It is a thực hành tốt nhất (Best Practice) for a source file (e.g. foo.cpp) to include its paired header (e.g. foo.h).  In many cases, foo.h will contain definitions that foo.cpp will need to compile correctly.

However, even if foo.cpp compiles file without foo.h, including the paired header allows the trình biên dịch to discover certain types of inconsistencies between the two files (e.g. when the return type of a hàm doesn’t match the return type of its forward declaration).  Without the inclusion, this might cause hành vi không xác định (Hành vi không xác định (Undefined Behavior - UB) - UB).

The cost of the #include is negligible, so there is little downside to including the header.

::: info Related content

Covered in lesson [2.11 -- Header files](https://www.learncpp.com/cpp-tutorial/header-files/#corresponding_include).

:::

Q7: Why does my project only compile when I #include “foo.cpp” from “main.cpp”? [](#includecpp)

This is almost always due to forgetting to add foo.cpp to your project and/or quá trình biên dịch command line.  Update your project and/or command line to include each source (.cpp) file.  When you compile your project, you should see each source file being compiled.

Normally in a project that has multiple files, the trình biên dịch will compile each source (.cpp) file individually.  After all the source files have been compiled, the trình liên kết links them together and creates the resulting output file (e.g. an executable).  However, if you split your code between two or more files (e.g. main.cpp and foo.cpp) and then only compiles main.cpp, you will probably get a quá trình biên dịch error or trình liên kết error, since part of the code required for your project is not being compiled.

New programmers sometimes discover that they can make their program work by adding `#include "foo.cpp"` to main.cpp instead of adding foo.cpp to the project or quá trình biên dịch command line.  After doing so, when main.cpp is compiled, the will preprocessor will create a translation unit consisting of the code from both foo.cpp and main.cpp, which will then be compiled and linked.  In smaller project, this may work.  So why not do this?

There are a few reasons:

<ol start="1">
- It can result in naming collisions between files.

- It can be hard to avoid ODR violations.

- Any change to any .cpp file will result in your entire project being recompiled.  This can take a long time.

::: info Related content

Covered in lesson [2.11 -- Header files](https://www.learncpp.com/cpp-tutorial/header-files/#includecpp).

:::

Q8: Why do I need to `return 0` at the bottom of main? [](#reteurnzero)

You don’t.  The `main()` hàm is special in that it will implicitly return 0 if you do not provide a return câu lệnh.

However, any other value-returning hàm that reaches the end of its body without encountering a return câu lệnh will produce hành vi không xác định (Hành vi không xác định (Undefined Behavior - UB) - UB).

For consistency, we recommend explicitly returning 0 from `main()`.  But if you prefer to omit the return câu lệnh in `main()` for conciseness, you can.  Just don’t make the mistake of thinking other value-returning các hàm work similarly.

::: info Related content

Covered in lesson [2.2 -- Function các giá trị trả về (value-returning các hàm)](https://www.learncpp.com/cpp-tutorial/hàm-return-values-value-returning-các hàm/).

:::

Q9: When I compile an example from this website, I get an error similar to “đối số list for class template XXX is missing”.  Why? [](#CTAD)

The most likely reason is that the example makes use of a feature called Class Template Argument Deduction (CTAD), which is a C++17 feature.  Many các trình biên dịch default to C++14, which doesn’t support this feature.

If the following program doesn’t compile for you, that’s the reason:

```cpp
#include <utility> // for std::pair

int main()
{
    std::pair p2{ 1, 2 }; // CTAD used to deduce std::pair<int, int> from the initializers (C++17)

    return 0;
}
```

::: info Related content

You can check which language standard your trình biên dịch is configured for using the program in lesson [0.13 -- What language standard is my trình biên dịch using?](https://www.learncpp.com/cpp-tutorial/what-language-standard-is-my-trình biên dịch-using/).

We cover CTAD in lesson [13.14 -- Class template đối số deduction (CTAD) and deduction guides](https://www.learncpp.com/cpp-tutorial/class-template-đối số-deduction-ctad-and-deduction-guides/).

:::

Q10: Why don’t we make hàm tham số or return types const when passing or returning by value? [](#constbyvalue)

We typically don’t `const` by-value hàm tham số because:

- Making such tham số `const` offers no meaningful value to the caller of the hàm, but adds clutter to the hàm’s interface.

- We generally don’t care if the hàm modifies those tham số, since they are copies that will be destroyed at the end of the hàm anyway.

We don’t `const` by-value các giá trị trả về because:

- If the return type is a non-class-type (e.g. a fundamental type), const will be ignored anyway.

- If the return type is a class type, const may inhibits certain kinds of optimizations (e.g. move semantics).

Note: `const` is relevant when passing/returning by address or by tham chiếu.

::: info Related content

Covered in lesson [5.1 -- Constant các biến (named các hằng số)](https://www.learncpp.com/cpp-tutorial/hằng số-các biến-named-các hằng số/)

:::

Q11: Why should I use constexpr? [](#whyconstexpr)

Constexpr and other compile-time programming techniques provide many benefits, including:

- Smaller and faster code.

- We can have the trình biên dịch detect certain kinds of errors and halt quá trình biên dịch if they occur.

- Hành vi không xác định (Hành vi không xác định (Undefined Behavior - UB) - UB) is not allowed at compile-time.

- The ability to use các biến and các hàm in places that require a hằng số biểu thức.

The last point is perhaps the most unavoidable, as certain C++ features require values that are known at compile-time.

::: info Related content

Covered in lesson [5.5 -- Constant biểu thức](https://www.learncpp.com/cpp-tutorial/hằng số-biểu thức/)

:::

Q12: Why should I constexpr an eligible hàm when I know it will only be evaluated at runtime in my program? [](#constexprruntimeeval)

There are a few reasons you might want to do so:

<ol start="1">
- There’s little downside to using constexpr, and it may help the trình biên dịch optimize even in contexts where it isn’t evaluated at compile-time.

- Just because you’re not calling the hàm in a compile-time evaluatable context right now doesn’t mean you won’t call it in such a context when you modify or extend your program.  And if you haven’t constexpr’d the hàm already, you may not think to when you do start to call it in such a context, and then you’ll miss out on the performance benefits.  Or you may be forced to constexpr it later when you need to use the giá trị trả về in a context that requires a hằng số biểu thức somewhere.

- Repetition helps ingrain best practices.

On a non-trivial project, it’s a good idea to implement your các hàm with the mindset that they may be reused (or extended) in the future.  Any time you modify an existing hàm, you risk breaking it, and that means it needs to be retested, which takes time and energy.  It’s often worth spending an extra minute or two “doing it right the first time” so you don’t have to redo (and retest) it again later.

::: info Related content

Covered in lesson [F.1 -- Constexpr các hàm](https://www.learncpp.com/cpp-tutorial/constexpr-các hàm/#constexprruntimeeval)

:::

Q13: Why shouldn’t I call the same input hàm more than once in an biểu thức? [](#unspecifiedevaluationorder)

In most cases, the C++ standard does not specify the order in which operands (including hàm đối số) are evaluated.  The precedence and associativity of các toán tử is used only to determine how operands are grouped with các toán tử, and the order of value computation. 

For example, given the câu lệnh `std::cout << subtract(getUserInput(), getUserInput())`, either the left đối số or the right đối số in the hàm call to `subtract()` could be evaluated first.  Let’s say the user inputs the values `5` and `2`.  If the left đối số was evaluated first, the left đối số will evaluate to `5`, and the right đối số will evaluate to `2`.  `5 - 2` is `3`.  If the right đối số was evaluated first, the right đối số will evaluate to `5`, and the left đối số will evaluate to `2`.  `2 - 5` is `-3`.  Thus, this câu lệnh might print either `3` or `-3`.

This can be disambiguated by making each hàm call to `getUserInput()` a separate câu lệnh (so the order is deterministic), and storing the giá trị trả về in a biến until it is needed.

::: info Related content

Covered in lesson [6.1 -- Operator precedence and associativity](https://www.learncpp.com/cpp-tutorial/toán tử-precedence-and-associativity/#unspecified)

:::

Q14: There aren’t enough quizzes!  Where can I get more practice? [](#morepractice)

We recommend [https://www.codewars.com/](https://www.codewars.com/), which has plenty of bite-sized exercises to help improve your general problem-solving and C++ implementation skills.  It’s also fun!

Once you have a solution, you can compare it with the answers of others to see alternative approaches, or understand where your own code might be improved.

However, because disposable exercises have disposable answers, solving such quizzes doesn’t really encourage writing high quality code, or demonstrate what happens when you don’t follow best practices.  For that, nothing is better than creating your own project.

Start with something small -- a simple game or simulation.  Then layer in features over time.  As the complexity of your project increases, you’ll start the see the various deficiencies in your code show up.  This will help you identify what areas of your code are in need of quality improvements.

  	
  	

---

::: tip 💡 Tóm Tắt Quy Tắc Vàng (Core Guidelines)
1. Luôn hiểu rõ vòng đời và quyền sở hữu (Ownership) của dữ liệu trước khi viết code.
2. Ưu tiên khởi tạo đồng nhất với dấu ngoặc nhọn `{}` để ngăn chặn lỗi thu hẹp kiểu dữ liệu (Narrowing conversions).
3. Bật toàn bộ cờ cảnh báo `-Wall -Wextra -Wpedantic` để compiler giúp bạn phát hiện bug từ sớm!
:::
