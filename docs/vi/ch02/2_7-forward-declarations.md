# 2.7 — Forward declarations and definitions

---

## 🎯 Mục Tiêu Bài Học
- Nắm vững bản chất lý thuyết và cơ chế hoạt động của **Forward declarations and definitions** trong tiêu chuẩn ISO C++.
- Hiểu rõ cách máy tính tổ chức bộ nhớ (RAM, CPU registers) khi thực thi mã nguồn liên quan.
- Nhận biết các cạm bẫy lỗi kinh điển (**Undefined Behavior**, Memory Leak, Bug logic) và cách phòng tránh.
- Áp dụng các quy tắc thực hành tốt nhất (**Best Practices**) chuẩn công nghiệp và cập nhật C++20/C++23 hiện đại.

---

# 2.7 &#8212; Forward declarations and definitions

Take a look at this seemingly innocent sample program:

```cpp
#include <iostream>

int main()
{
    std::cout << "The sum of 3 and 4 is: " << add(3, 4) << '\n';
    return 0;
}

int add(int x, int y)
{
    return x + y;
}
```

You would expect this program to produce the result:

```cpp
The sum of 3 and 4 is: 7
```

But in fact, it doesn’t compile at all!  Visual Studio produces the following compile error:

```cpp
add.cpp(5) : error C3861: 'add': identifier not found
```

The reason this program doesn’t compile is because the trình biên dịch compiles the contents of code files sequentially.  When the trình biên dịch reaches the hàm call *add()* on line 5 of *main*, it doesn’t know what *add* is, because we haven’t defined *add* until line 9!  That produces the error, *identifier not found*.

Older versions of Visual Studio would produce an additional error:

```cpp
add.cpp(9) : error C2365: 'add'; : redefinition; previous definition was 'formerly unknown identifier'
```

This is somewhat misleading, given that *add* wasn’t ever defined in the first place.  Despite this, it’s useful to generally note that it is fairly common for a single error to produce many redundant or related errors or warnings.  It can sometimes be hard to tell whether any error or cảnh báo beyond the first is a consequence of the first issue, or whether it is an independent issue that needs to be resolved separately.

::: tip Thực hành tốt nhất (Best Practice)

When addressing quá trình biên dịch errors or warnings in your programs, resolve the first issue listed and then compile again.

:::

To fix this problem, we need to address the fact that the trình biên dịch doesn’t know what add is.  There are two common ways to address the issue.

Option 1: Reorder the hàm definitions

One way to address the issue is to reorder the hàm definitions so *add* is defined before *main*:

```cpp
#include <iostream>

int add(int x, int y)
{
    return x + y;
}

int main()
{
    std::cout << "The sum of 3 and 4 is: " << add(3, 4) << '\n';
    return 0;
}
```

That way, by the time *main* calls *add*, the trình biên dịch will already know what *add* is.  Because this is such a simple program, this change is relatively easy to do.  However, in a larger program, it can be tedious trying to figure out which các hàm call which other các hàm (and in what order) so they can be declared sequentially.

Furthermore, this option is not always possible.  Let’s say we’re writing a program that has two các hàm *A* and *B*.  If hàm *A* calls hàm *B*, and hàm *B* calls hàm *A*, then there’s no way to order the các hàm in a way that will make the trình biên dịch happy.  If you define *A* first, the trình biên dịch will complain it doesn’t know what *B* is.  If you define *B* first, the trình biên dịch will complain that it doesn’t know what *A* is.  

Option 2: Use a forward declaration

We can also fix this by using a forward declaration.

A **forward declaration** allows us to tell the trình biên dịch about the existence of an identifier *before* actually defining the identifier.

In the case of các hàm, this allows us to tell the trình biên dịch about the existence of a hàm before we define the hàm’s body.  This way, when the trình biên dịch encounters a call to the hàm, it’ll understand that we’re making a hàm call, and can check to ensure we’re calling the hàm correctly, even if it doesn’t yet know how or where the hàm is defined.

To write a forward declaration for a hàm, we use a **hàm declaration** câu lệnh (also called a **hàm prototype**).  The hàm declaration consists of the hàm’s return type, name, and tham số types, terminated with a semicolon.  The names of the tham số can be optionally included.  The hàm body is not included in the declaration.

Here’s a hàm declaration for the *add* hàm:

```cpp
int add(int x, int y); // function declaration includes return type, name, parameters, and semicolon.  No function body!
```

Now, here’s our original program that didn’t compile, using a hàm declaration as a forward declaration for hàm *add*:

```cpp
#include <iostream>

int add(int x, int y); // forward declaration of add() (using a function declaration)

int main()
{
    std::cout << "The sum of 3 and 4 is: " << add(3, 4) << '\n'; // this works because we forward declared add() above
    return 0;
}

int add(int x, int y) // even though the body of add() isn't defined until here
{
    return x + y;
}
```

Now when the trình biên dịch reaches the call to *add* in main, it will know what *add* looks like (a hàm that takes two integer tham số and returns an integer), and it won’t complain.

It is worth noting that hàm declarations do not need to specify the names of the tham số (as they are not considered to be part of the hàm declaration).  In the above code, you can also forward declare your hàm like this:

```cpp
int add(int, int); // valid function declaration
```

However, we prefer to name our tham số (using the same names as the actual hàm).  This allows you to understand what the hàm tham số are just by looking at the declaration.  For example, if you were to see the declaration `void doSomething(int, int, int)`, you may think you remember what each of the tham số represent, but you may also get it wrong.

Also many automated documentation generation tools will generate documentation from the content of header files, which is where declarations are often placed.  We discuss header files and declarations in lesson [2.11 -- Header files](https://www.learncpp.com/cpp-tutorial/header-files/).

::: tip Thực hành tốt nhất (Best Practice)

Keep the tham số names in your hàm declarations.

:::

::: info Tip

You can easily create hàm declarations by copy/pasting your hàm’s header and adding a semicolon.

:::

Why forward declarations?

You may be wondering why we would use a forward declaration if we could just reorder the các hàm to make our programs work.  

Most often, forward declarations are used to tell the trình biên dịch about the existence of some hàm that has been defined in a different code file.  Reordering isn’t possible in this scenario because the caller and the callee are in completely different files!  We’ll discuss this in more detail in the next lesson ([2.8 -- Programs with multiple code files](https://www.learncpp.com/cpp-tutorial/programs-with-multiple-code-files/)).

Forward declarations can also be used to define our các hàm in an order-agnostic manner.  This allows us to define các hàm in whatever order maximizes organization (e.g. by clustering related các hàm together) or reader understanding.

Less often, there are times when we have two các hàm that call each other.  Reordering isn’t possible in this case either, as there is no way to reorder the các hàm such that each is before the other.  Forward declarations give us a way to resolve such circular dependencies.

Forgetting the hàm body

New programmers often wonder what happens if they forward declare a hàm but do not define it.

The answer is: it depends.  If a forward declaration is made, but the hàm is never called, the program will compile and run fine.  However, if a forward declaration is made and the hàm is called, but the program never defines the hàm, the program will compile okay, but the trình liên kết will complain that it can’t resolve the hàm call.

Consider the following program:

```cpp
#include <iostream>

int add(int x, int y); // forward declaration of add()

int main()
{
    std::cout << "The sum of 3 and 4 is: " << add(3, 4) << '\n';
    return 0;
}

// note: No definition for function add
```

In this program, we forward declare *add*, and we call *add*, but we never define *add* anywhere.  When we try and compile this program, Visual Studio produces the following message:

```cpp
Compiling...
add.cpp
Linking...
add.obj : error LNK2001: unresolved external symbol "int __cdecl add(int,int)" (?add@@YAHHH@Z)
add.exe : fatal error LNK1120: 1 unresolved externals
```

As you can see, the program compiled okay, but it failed at the link stage because *int add(int, int)* was never defined.

Other types of forward declarations

Forward declarations are most often used with các hàm.  However, forward declarations can also be used with other identifiers in C++, such as các biến and types.  Variables and types have a different syntax for forward declaration, so we’ll cover these in future lessons.

Declarations vs. definitions

In C++, you’ll frequently hear the words “declaration” and “definition” used, and often interchangeably.  What do they mean?  You now have enough fundamental knowledge to understand the difference between the two.

A **declaration** tells the *trình biên dịch* about the *existence* of an identifier and its associated type information.  Here are some examples of declarations:

```cpp
int add(int x, int y); // tells the compiler about a function named "add" that takes two int parameters and returns an int.  No body!
int x;                 // tells the compiler about an integer variable named x
```

A **definition** is a declaration that actually implements (for các hàm and types) or instantiates (for các biến) the identifier.

Here are some examples of definitions:

```cpp
// because this function has a body, it is an implementation of function add()
int add(int x, int y)
{
    int z{ x + y };   // instantiates variable z

    return z;
}

int x;                // instantiates variable x
```

In C++, all definitions are declarations.  Therefore `int x;` is both a definition and a declaration.

Conversely, not all declarations are definitions.  Declarations that aren’t definitions are called **pure declarations**.  Types of pure declarations include forward declarations for hàm, các biến, and types.

::: info Nomenclature

In common language, the term “declaration” is typically used to mean “a pure declaration”, and “definition” is used to mean “a definition that also serves as a declaration”.  Thus, we’d typically call `int x;` a definition, even though it is both a definition and a declaration.
:::

When the trình biên dịch encounters an identifier, it will check to ensure use of that identifier is valid (e.g. that the identifier is in phạm vi truy cập (scope), that it is used in a syntactically valid manner, etc…).

In most cases, a declaration is sufficient to allow the trình biên dịch to ensure an identifier is being used properly.  For example, when the trình biên dịch encounters hàm call `add(5, 6)`, if it has already seen the declaration for `add(int, int)`, then it can validate that `add` is actually a hàm that takes two `int` tham số.  It does not need to have actually seen the definition for hàm `add` (which may exist in some other file).

However, there are a few cases where the trình biên dịch must be able to see a full definition in order to use an identifier (such as for template definitions and type definitions, both of which we will discuss in future lessons).

Here’s a summary table:

 Term 
 Technical Meaning 
 Examples 

 Declaration 
 Tells trình biên dịch about an identifier and its associated type information. 
 void foo(); // hàm forward declaration (no body)
void goo() {}; // hàm definition (has body)
int x; // biến definition 

 Definition 
 Implements a hàm or instantiates a biến.
Definitions are also declarations. 
 void foo() { } // hàm definition (has body)
int x; // biến definition 

 Pure declaration 
 A declaration that isn’t a definition. 
 void foo(); // hàm forward declaration (no body) 

 Initialization 
 Provides an initial value for a defined object. 
 int x { 2 }; // x is được khởi tạo to value 2 

The term “declaration” is commonly used to mean “pure declaration”, and the term “definition” used for anything that is both a definition and a declaration.  We use this common nomenclature in the example column comments.

The one definition rule (ODR) [](#ODR)

The **one definition rule** (or ODR for short) is a well-known rule in C++.  The ODR has three parts:

<ol start="1">
- Within a *file*, each hàm, biến, type, or template in a given phạm vi truy cập (scope) can only have one definition.  Definitions occurring in different scopes (e.g. local các biến defined inside different các hàm, or các hàm defined inside different namespaces) do not violate this rule.

- Within a *program*, each hàm or biến in a given phạm vi truy cập (scope) can only have one definition.  This rule exists because programs can have more than one file (we’ll cover this in the next lesson).  Functions and các biến not visible to the trình liên kết are excluded from this rule (discussed further in lesson [7.6 -- Internal linkage](https://www.learncpp.com/cpp-tutorial/internal-linkage/)).

- Types, templates, inline các hàm, and inline các biến are allowed to have duplicate definitions in different files, so long as each definition is identical.  We haven’t covered what most of these things are yet, so don’t worry about this for now -- we’ll bring it back up when it’s relevant.

::: info Related content

We discuss ODR part 3 exemptions further in the following lessons:

- Types ([13.1 -- Introduction to program-defined (user-defined) types](https://www.learncpp.com/cpp-tutorial/introduction-to-program-defined-user-defined-types/)).

- Function templates ([11.6 -- Function templates](https://www.learncpp.com/cpp-tutorial/hàm-templates/) and [11.7 -- Function template instantiation](https://www.learncpp.com/cpp-tutorial/hàm-template-instantiation/)).

- Inline các hàm and các biến ([7.9 -- Inline các hàm and các biến](https://www.learncpp.com/cpp-tutorial/inline-các hàm-and-các biến/)).

:::

Violating part 1 of the ODR will cause the trình biên dịch to issue a redefinition error.  Violating ODR part 2 will cause the trình liên kết to issue a redefinition error.  Violating ODR part 3 will cause hành vi không xác định (Hành vi không xác định (Undefined Behavior - UB) - UB).

Here’s an example of a violation of part 1:

```cpp
int add(int x, int y)
{
     return x + y;
}

int add(int x, int y) // violation of ODR, we've already defined function add(int, int)
{
     return x + y;
}

int main()
{
    int x{};
    int x{ 5 }; // violation of ODR, we've already defined x
}
```

In this example, hàm `add(int, int)` is defined twice (in the global phạm vi truy cập (scope)), and local biến `int x` is defined twice (in the phạm vi truy cập (scope) of `main()`).  The Visual Studio trình biên dịch thus issues the following compile errors:

```cpp
project3.cpp(9): error C2084: function 'int add(int,int)' already has a body
project3.cpp(3): note: see previous definition of 'add'
project3.cpp(16): error C2086: 'int x': redefinition
project3.cpp(15): note: see declaration of 'x'
```

However, it is not a violation of ODR part 1 for `main()` to have a local biến defined as `int x` and `add()` to also have a hàm tham số defined as `int x`.  These definitions occur in different scopes (in the phạm vi truy cập (scope) of each respective hàm), so they are considered to be separate definitions for two distinct đối tượng, not a definition and redefinition of the same object.

::: info For advanced readers

Functions that share an identifier but have different sets of tham số are also considered to be distinct các hàm, so such definitions do not violate the ODR.  We discuss this further in lesson [11.1 -- Introduction to hàm overloading](https://www.learncpp.com/cpp-tutorial/introduction-to-hàm-overloading/).

:::

Hệ thống Câu hỏi & Quiz Tự Luyện

Câu hỏi #1

What is a hàm prototype?

::: details Xem lời giải (Solution)

A hàm prototype is a declaration câu lệnh that includes a hàm’s name, return type, tham số types, and optionally the tham số names.  It does not include the hàm body.  It tells the trình biên dịch about the existence of a hàm before it is defined.

:::

Câu hỏi #2

What is a forward declaration?

::: details Xem lời giải (Solution)

A forward declaration tells the trình biên dịch that an identifier exists before it is actually defined.

:::

Câu hỏi #3

How do we declare a forward declaration for các hàm?

::: details Xem lời giải (Solution)

For các hàm, a hàm declaration/prototype serves as a forward declaration.

:::

Câu hỏi #4

Write the hàm declaration for this hàm (use the preferred form with names):

```cpp
int doMath(int first, int second, int third, int fourth)
{
     return first + second * third / fourth;
}
```

::: details Xem lời giải (Solution)
```cpp
// Do not forget the semicolon at the end, since these are statements.
int doMath(int first, int second, int third, int fourth);
```
:::

Câu hỏi #5

For each of the following programs, state whether they fail to compile, fail to link, or compile and link successfully.  If you are not sure, try compiling them!

a)

```cpp
#include <iostream>
int add(int x, int y);

int main()
{
    std::cout << "3 + 4 + 5 = " << add(3, 4, 5) << '\n';
    return 0;
}

int add(int x, int y)
{
    return x + y;
}
```

::: details Xem lời giải (Solution)
Doesn’t compile.  The trình biên dịch will complain that it can’t find a matching `add()` hàm that takes 3 đối số.  The forward declaration of `add()` only has two tham số.
:::

b)

```cpp
#include <iostream>
int add(int x, int y);

int main()
{
    std::cout << "3 + 4 + 5 = " << add(3, 4, 5) << '\n';
    return 0;
}

int add(int x, int y, int z)
{
    return x + y + z;
}
```

::: details Xem lời giải (Solution)
Doesn’t compile.  The trình biên dịch will complain that it can’t find a matching `add()` hàm that takes 3 đối số.  The forward declaration of `add()` only has two tham số, and the definition of hàm `add()` that has 3 tham số hasn’t been seen yet.
:::

c)

```cpp
#include <iostream>
int add(int x, int y);

int main()
{
    std::cout << "3 + 4 = " << add(3, 4) << '\n';
    return 0;
}

int add(int x, int y, int z)
{
    return x + y + z;
}
```

::: details Xem lời giải (Solution)
Doesn’t link.  The trình biên dịch will match the forward declaration of add to the hàm call to add() in main().  However, no add() hàm that takes two tham số was ever implemented (we only implemented one that took 3 tham số), so the trình liên kết will complain.
:::

d)

```cpp
#include <iostream>
int add(int x, int y, int z);

int main()
{
    std::cout << "3 + 4 + 5 = " << add(3, 4, 5) << '\n';
    return 0;
}

int add(int z, int y, int x) // names don't match the declaration
{
    return x + y + z;
}
```

::: details Xem lời giải (Solution)
Compiles and links.  The types in the hàm call to add() matches the forward declaration, and the definition of add() also matches.  The fact that the names don’t match the declaration doesn’t matter, as the names in a declaration are optional (and if provided, ignored by the trình biên dịch).
:::

e)

```cpp
#include <iostream>
int add(int, int, int); // no parameter names

int main()
{
    std::cout << "3 + 4 + 5 = " << add(3, 4, 5) << '\n';
    return 0;
}

int add(int x, int y, int z)
{
    return x + y + z;
}
```

::: details Xem lời giải (Solution)
Compiles and links.  This is the same as the prior case.  Function declarations do not need to specify the names of the tham số (even though we generally prefer to include them).
:::

f)

```cpp
#include <iostream>

int add(int x, int y);

int add(int x, int y, int z)
{
    return x + y + z;
}

int main()
{
    std::cout << "3 + 4 + 5 = " << add(3, 4, 5) << '\n';
    return 0;
}
```

::: details Xem lời giải (Solution)
Compiles and links.  The forward declaration of add() with two tham số is not used.
:::

  	
  	

---

::: tip 💡 Tóm Tắt Quy Tắc Vàng (Core Guidelines)
1. Luôn hiểu rõ vòng đời và quyền sở hữu (Ownership) của dữ liệu trước khi viết code.
2. Ưu tiên khởi tạo đồng nhất với dấu ngoặc nhọn `{}` để ngăn chặn lỗi thu hẹp kiểu dữ liệu (Narrowing conversions).
3. Bật toàn bộ cờ cảnh báo `-Wall -Wextra -Wpedantic` để compiler giúp bạn phát hiện bug từ sớm!
:::
