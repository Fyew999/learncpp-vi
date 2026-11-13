# 2.9 — Naming collisions and an introduction to namespaces

---

## 🎯 Mục Tiêu Bài Học
- Nắm vững bản chất lý thuyết và cơ chế hoạt động của **Naming collisions and an introduction to namespaces** trong tiêu chuẩn ISO C++.
- Hiểu rõ cách máy tính tổ chức bộ nhớ (RAM, CPU registers) khi thực thi mã nguồn liên quan.
- Nhận biết các cạm bẫy lỗi kinh điển (**Undefined Behavior**, Memory Leak, Bug logic) và cách phòng tránh.
- Áp dụng các quy tắc thực hành tốt nhất (**Best Practices**) chuẩn công nghiệp và cập nhật C++20/C++23 hiện đại.

---

# 2.9 &#8212; Naming collisions and an introduction to namespaces

Let’s say you are driving to a friend’s house for the first time, and the address given to you is 245 Front Street in Mill City.  Upon reaching Mill City, you take out your map, only to discover that Mill City actually has two different Front Streets across town from each other!  Which one would you go to?  Unless there were some additional clue to help you decide (e.g. you remember your friend’s house is near the river) you’d have to call your friend and ask for more information.  Because this would be confusing and inefficient (particularly for your mail carrier), in most countries, all street names and house addresses within a city are required to be unique.

Similarly, C++ requires that all identifiers be non-ambiguous.  If two identical identifiers are introduced into the same program in a way that the trình biên dịch or trình liên kết can’t tell them apart, the trình biên dịch or trình liên kết will produce an error. This error is generally referred to as a **naming collision** (or **naming conflict**).

If the colliding identifiers are introduced into the same file, the result will be a trình biên dịch error.  If the colliding identifiers are introduced into separate files belonging to the same program, the result will be a trình liên kết error.

An example of a naming collision

a.cpp:

```cpp
#include <iostream>

void myFcn(int x)
{
    std::cout << x;
}
```

main.cpp:

```cpp
#include <iostream>

void myFcn(int x)
{
    std::cout << 2 * x;
}

int main()
{
    return 0;
}
```

When the trình biên dịch compiles this program, it will compile *a.cpp* and *main.cpp* independently, and each file will compile with no problems.

However, when the trình liên kết executes, it will link all the definitions in *a.cpp* and *main.cpp* together, and discover conflicting definitions for hàm `myFcn()`.  The trình liên kết will then abort with an error.  Note that this error occurs even though `myFcn()` is never called!

Most naming collisions occur in two cases:

<ol start="1">
- Two (or more) identically named các hàm (or global các biến) are introduced into separate files belonging to the same program.  This will result in a trình liên kết error, as shown above.

- Two (or more) identically named các hàm (or global các biến) are introduced into the same file.  This will result in a trình biên dịch error.

As programs get larger and use more identifiers, the odds of a naming collision being introduced increases significantly.  The good news is that C++ provides plenty of mechanisms for avoiding naming collisions.  Local phạm vi truy cập (scope), which keeps local các biến defined inside các hàm from conflicting with each other, is one such mechanism.  But local phạm vi truy cập (scope) doesn’t work for hàm names.  So how do we keep hàm names from conflicting with each other?

Scope regions

Back to our address analogy for a moment, having two Front Streets was only problematic because those streets existed within the same city.  On the other hand, if you had to deliver mail to two addresses, one at 245 Front Street in Mill City, and another address at 245 Front Street in Jonesville, there would be no confusion about where to go.  Put another way, cities provide groupings that allow us to disambiguate addresses that might otherwise conflict with each other.

A **phạm vi truy cập (scope) region** is an area of source code where all declared identifiers are considered distinct from names declared in other scopes (much like the cities in our analogy).  Two identifiers with the same name can be declared in separate phạm vi truy cập (scope) regions without causing a naming conflict.  However, within a given phạm vi truy cập (scope) region, all identifiers must be unique, otherwise a naming collision will result.

The body of a hàm is one example of a phạm vi truy cập (scope) region.  Two identically-named identifiers can be defined in separate các hàm without issue -- because each hàm provides a separate phạm vi truy cập (scope) region, there is no collision.  However, if you try to define two identically-named identifiers within the same hàm, a naming collision will result, and the trình biên dịch will complain.

Namespaces

A **namespace** provides another type of phạm vi truy cập (scope) region (called **namespace phạm vi truy cập (scope)**) that allows you to declare or define names inside of it for the purpose of disambiguation.  The names declared in a namespace are isolated from names declared in other scopes, allowing such names to exist without conflict.

::: info Hiểu biết cốt lõi

A name declared within a phạm vi truy cập (scope) region (such as a namespace) is distinct from any identical name declared in another phạm vi truy cập (scope).

:::

For example, two các hàm with identical declarations can be defined inside different namespaces, and no naming collision or ambiguity will occur.

Namespaces may only contain declarations and definitions (e.g. các biến and các hàm).  Executable câu lệnh are not allowed unless they are part of a definition (e.g. within a hàm).  

::: info Hiểu biết cốt lõi

A namespace may only contain declarations and definitions.  Executable câu lệnh are only allowed as part of a definition (e.g. of a hàm).

:::

Namespaces are often used to group related identifiers in a large project to help ensure they don’t inadvertently collide with other identifiers.  For example, if you put all your math các hàm in a namespace named `math`, then your math các hàm won’t collide with identically named các hàm outside the `math` namespace.

We’ll talk about how to create your own namespaces in a future lesson.

The global namespace

In C++, any name that is not defined inside a class, hàm, or a namespace is considered to be part of an implicitly-defined namespace called the **global namespace** (sometimes also called **the global phạm vi truy cập (scope)**).

In the example at the top of the lesson, các hàm `main()` and both versions of `myFcn()` are defined inside the global namespace.  The naming collision encountered in the example happens because both versions of `myFcn()` end up inside the global namespace, which violates the rule that all names in the phạm vi truy cập (scope) region must be unique.

We discuss the global namespace in more detail in lesson [7.4 -- Introduction to global các biến](https://www.learncpp.com/cpp-tutorial/introduction-to-global-các biến/).

For now, there are two things you should know:

- Identifiers declared inside the global phạm vi truy cập (scope) are in phạm vi truy cập (scope) from the point of declaration to the end of the file.

- Although các biến can be defined in the global namespace, this should generally be avoided (we discuss why in lesson [7.8 -- Why (non-const) global các biến are evil](https://www.learncpp.com/cpp-tutorial/why-non-const-global-các biến-are-evil/)).

For example:

```cpp
#include <iostream> // imports the declaration of std::cout into the global scope

// All of the following statements are part of the global namespace

void foo();    // okay: function forward declaration
int x;         // compiles but strongly discouraged: non-const global variable definition (without initializer)
int y { 5 };   // compiles but strongly discouraged: non-const global variable definition (with initializer)
x = 5;         // compile error: executable statements are not allowed in namespaces

int main()     // okay: function definition
{
    return 0;
}

void goo();    // okay: A function forward declaration
```

The std namespace

When C++ was originally designed, all of the identifiers in the C++ standard library (including std::cin and std::cout) were available to be used without the `std::` prefix (they were part of the global namespace).  However, this meant that any identifier in the standard library could potentially conflict with any name you picked for your own identifiers (also defined in the global namespace).  Code that was once working might suddenly have a naming conflict when you include a different part of the standard library.   Or worse, code that compiled under one version of C++ might not compile under the next version of C++, as new identifiers introduced into the standard library could have a naming conflict with already written code.  So C++ moved all of the functionality in the standard library into a namespace named `std` (short for “standard”).

It turns out that `std::cout`‘s name isn’t really `std::cout`.  It’s actually just `cout`, and `std` is the name of the namespace that identifier `cout` is part of.  Because `cout` is defined in the `std` namespace, the name `cout` won’t conflict with any đối tượng or các hàm named `cout` that we create outside of the `std` namespace (such as in the global namespace).

::: info Hiểu biết cốt lõi

When you use an identifier that is defined inside a non-global namespace (e.g. the `std` namespace), you need to tell the trình biên dịch that the identifier lives inside the namespace.”
:::

There are a few different ways to do this.

Explicit namespace qualifier std::

The most straightforward way to tell the trình biên dịch that we want to use `cout` from the `std` namespace is by explicitly using the `std::` prefix.  For example:

```cpp
#include <iostream>

int main()
{
    std::cout << "Hello world!"; // when we say cout, we mean the cout defined in the std namespace
    return 0;
}
```

The :: symbol is an toán tử called the **phạm vi truy cập (scope) resolution toán tử**.  The identifier to the left of the `::` symbol identifies the namespace that the name to the right of the `::` symbol is contained within.  If no identifier to the left of the `::` symbol is provided, the global namespace is assumed.

So when we say `std::cout` we’re saying “the `cout` that is declared in namespace `std`“.

This is the safest way to use `cout`, because there’s no ambiguity about which `cout` we’re referencing (the one in the `std` namespace).

::: tip Thực hành tốt nhất (Best Practice)

Use explicit namespace prefixes to access identifiers defined in a namespace.

:::

When an identifier includes a namespace prefix, the identifier is called a **qualified name**.

Using namespace std (and why to avoid it)

Another way to access identifiers inside a namespace is to use a using-directive câu lệnh.  Here’s our original “Hello world” program with a using-directive:

```cpp
#include <iostream>

using namespace std; // this is a using-directive that allows us to access names in the std namespace with no namespace prefix

int main()
{
    cout << "Hello world!";
    return 0;
}
```

A **using directive** allows us to access the names in a namespace without using a namespace prefix.  So in the above example, when the trình biên dịch goes to determine what identifier `cout` is, it will match with `std::cout`, which, because of the using-directive, is accessible as just `cout`.

Many texts, tutorials, and even some IDEs recommend or use a using-directive at the top of the program.  However, used in this way, this is a bad practice, and highly discouraged.

Consider the following program:

```cpp
#include <iostream> // imports the declaration of std::cout into the global scope

using namespace std; // makes std::cout accessible as "cout"
 
int cout() // defines our own "cout" function in the global namespace
{
    return 5;
}
 
int main()
{
    cout << "Hello, world!"; // Compile error!  Which cout do we want here?  The one in the std namespace or the one we defined above?
 
    return 0;
}
```

The above program doesn’t compile, because the trình biên dịch now can’t tell whether we want the `cout` hàm that we defined, or `std::cout`.

When using a using-directive in this manner, *any* identifier we define may conflict with *any* identically named identifier in the `std` namespace.  Even worse, while an identifier name may not conflict today, it may conflict with new identifiers added to the std namespace in future language revisions.  This was the whole point of moving all of the identifiers in the standard library into the `std` namespace in the first place!

::: danger Cảnh báo nguy hiểm

Avoid using-directives (such as `using namespace std;`) at the top of your program or in header files.  They violate the reason why namespaces were added in the first place.
:::

::: info Related content

We talk more about using-declarations and using-directives (and how to use them responsibly) in lesson [7.13 -- Using declarations and using directives](https://www.learncpp.com/cpp-tutorial/using-declarations-and-using-directives/).

:::

Curly braces and indented code

In C++, curly braces are often used to delineate a phạm vi truy cập (scope) region that is nested within another phạm vi truy cập (scope) region (braces are also used for some non-phạm vi truy cập (scope)-related purposes, such as list sự khởi tạo).  For example, a hàm defined inside the global phạm vi truy cập (scope) region uses curly braces to separate the phạm vi truy cập (scope) region of the hàm from the global phạm vi truy cập (scope).

In certain cases, identifiers defined outside the curly braces may still be part of the phạm vi truy cập (scope) defined by the curly braces rather than the surrounding phạm vi truy cập (scope) -- hàm tham số are a good example of this.

For example:

```cpp
#include <iostream> // imports the declaration of std::cout into the global scope

void foo(int x) // foo is defined in the global scope, x is defined within scope of foo()
{ // braces used to delineate nested scope region for function foo()
    std::cout << x << '\n';
} // x goes out of scope here

int main()
{ // braces used to delineate nested scope region for function main()
    foo(5);

    int x { 6 }; // x is defined within the scope of main()
    std::cout << x << '\n';
 
    return 0;
} // x goes out of scope here
// foo and main (and std::cout) go out of scope here (the end of the file)
```

The code that exists inside a nested phạm vi truy cập (scope) region is conventionally indented one level, both for readability and to help indicate that it exists inside a separate phạm vi truy cập (scope) region.

The `#include` and hàm definitions for `foo()` and `main()` exist in the global phạm vi truy cập (scope) region, so they are not indented.  The câu lệnh inside each hàm exist inside the nested phạm vi truy cập (scope) region of the hàm, so they are indented one level.

  	
  	

---

::: tip 💡 Tóm Tắt Quy Tắc Vàng (Core Guidelines)
1. Luôn hiểu rõ vòng đời và quyền sở hữu (Ownership) của dữ liệu trước khi viết code.
2. Ưu tiên khởi tạo đồng nhất với dấu ngoặc nhọn `{}` để ngăn chặn lỗi thu hẹp kiểu dữ liệu (Narrowing conversions).
3. Bật toàn bộ cờ cảnh báo `-Wall -Wextra -Wpedantic` để compiler giúp bạn phát hiện bug từ sớm!
:::
