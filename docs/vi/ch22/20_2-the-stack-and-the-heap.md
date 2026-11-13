# 20.2 — The stack and the heap

---

## 🎯 Mục Tiêu Bài Học
- Nắm vững bản chất lý thuyết và cơ chế hoạt động của **The stack and the heap** trong tiêu chuẩn ISO C++.
- Hiểu rõ cách máy tính tổ chức bộ nhớ (RAM, CPU registers) khi thực thi mã nguồn liên quan.
- Nhận biết các cạm bẫy lỗi kinh điển (**Undefined Behavior**, Memory Leak, Bug logic) và cách phòng tránh.
- Áp dụng các quy tắc thực hành tốt nhất (**Best Practices**) chuẩn công nghiệp và cập nhật C++20/C++23 hiện đại.

---

# 20.2 &#8212; The ngăn xếp Stack and the vùng nhớ Heap (Free Store)

The memory that a program uses is typically divided into a few different areas, called segments:

- The code segment (also called a text segment), where the compiled program sits in memory.  The code segment is typically read-only.
`<li>`The bss segment (also called the chưa được khởi tạo data segment), where zero-được khởi tạo global and static các biến are stored.
`<li>`The data segment (also called the được khởi tạo data segment), where được khởi tạo global and static các biến are stored.
`<li>`The vùng nhớ Heap (Free Store), where dynamically allocated các biến are allocated from.
`<li>`The call ngăn xếp Stack, where hàm tham số, local các biến, and other hàm-related information are stored.

For this lesson, we’ll focus primarily on the vùng nhớ Heap (Free Store) and the ngăn xếp Stack, as that is where most of the interesting stuff takes place.

**The vùng nhớ Heap (Free Store) segment**

The vùng nhớ Heap (Free Store) segment (also known as the “free store”) keeps track of memory used for dynamic memory allocation.  We talked about the vùng nhớ Heap (Free Store) a bit already in lesson [19.1 -- Dynamic memory allocation with new and delete](https://www.learncpp.com/cpp-tutorial/dynamic-memory-allocation-with-new-and-delete/), so this will be a recap.

In C++, when you use the new toán tử to allocate memory, this memory is allocated in the application’s vùng nhớ Heap (Free Store) segment.

Assuming an int is 4 bytes:

```cpp
int* ptr { new int }; // new int allocates 4 bytes in the heap
int* array { new int[10] }; // new int[10] allocates 40 bytes in the heap
```

The address of this memory is passed back by toán tử new, and can then be stored in a con trỏ.  You do not have to worry about the mechanics behind the process of how free memory is located and allocated to the user.  However, it is worth knowing that sequential memory requests may not result in sequential memory addresses being allocated!

```cpp
int* ptr1 { new int };
int* ptr2 { new int };
// ptr1 and ptr2 may not have sequential addresses
```

When a dynamically allocated biến is deleted, the memory is “returned” to the vùng nhớ Heap (Free Store) and can then be reassigned as future allocation requests are received.  Remember that deleting a con trỏ does not delete the biến, it just returns the memory at the associated address back to the operating system.

The vùng nhớ Heap (Free Store) has advantages and disadvantages:

`<li>`Allocating memory on the vùng nhớ Heap (Free Store) is comparatively slow.

- Allocated memory stays allocated until it is specifically deallocated (beware memory leaks) or the application ends (at which point the OS should clean it up).

- Dynamically allocated memory must be accessed through a con trỏ.  Dereferencing a con trỏ is slower than accessing a biến directly.

- Because the vùng nhớ Heap (Free Store) is a big pool of memory, large arrays, structures, or classes can be allocated here.

**The call ngăn xếp Stack**

The **call ngăn xếp Stack** (usually referred to as “the ngăn xếp Stack”) has a much more interesting role to play.  The call ngăn xếp Stack keeps track of all the active các hàm (those that have been called but have not yet terminated) from the start of the program to the current point of execution, and handles allocation of all hàm tham số and local các biến.

The call ngăn xếp Stack is implemented as a ngăn xếp Stack data structure.  So before we can talk about how the call ngăn xếp Stack works, we need to understand what a ngăn xếp Stack data structure is.

**The ngăn xếp Stack data structure**

A **data structure** is a programming mechanism for organizing data so that it can be used efficiently.  You’ve already seen several types of data structures, such as arrays and structs.  Both of these data structures provide mechanisms for storing data and accessing that data in an efficient way.  There are many additional data structures that are commonly used in programming, quite a few of which are implemented in the standard library, and a ngăn xếp Stack is one of those.

Consider a ngăn xếp Stack of plates in a cafeteria.  Because each plate is heavy and they are stacked, you can really only do one of three things:

<ol start="1">
- Look at the surface of the top plate

- Take the top plate off the ngăn xếp Stack (exposing the one underneath, if it exists)

- Put a new plate on top of the ngăn xếp Stack (hiding the one underneath, if it exists)

In computer programming, a ngăn xếp Stack is a container data structure that holds multiple các biến (much like an array).  However, whereas an array lets you access and modify elements in any order you wish (called **random access**), a ngăn xếp Stack is more limited.  The operations that can be performed on a ngăn xếp Stack correspond to the three things mentioned above:

<ol start="1">
- Look at the top item on the ngăn xếp Stack (usually done via a hàm called top(), but sometimes called peek())

- Take the top item off of the ngăn xếp Stack (done via a hàm called pop())

- Put a new item on top of the ngăn xếp Stack (done via a hàm called push())

A ngăn xếp Stack is a last-in, first-out (LIFO) structure.  The last item pushed onto the ngăn xếp Stack will be the first item popped off.  If you put a new plate on top of the ngăn xếp Stack, the first plate removed from the ngăn xếp Stack will be the plate you just pushed on last.  Last on, first off.  As items are pushed onto a ngăn xếp Stack, the ngăn xếp Stack grows larger -- as items are popped off, the ngăn xếp Stack grows smaller.

For example, here’s a short sequence showing how pushing and popping on a ngăn xếp Stack works:

```cpp
Stack: empty
Push 1
Stack: 1
Push 2
Stack: 1 2
Push 3
Stack: 1 2 3
Pop
Stack: 1 2
Pop
Stack: 1
```

The plate analogy is a pretty good analogy as to how the call ngăn xếp Stack works, but we can make a better analogy.  Consider a bunch of mailboxes, all stacked on top of each other.  Each mailbox can only hold one item, and all mailboxes start out empty.  Furthermore, each mailbox is nailed to the mailbox below it, so the number of mailboxes can not be changed.  If we can’t change the number of mailboxes, how do we get a ngăn xếp Stack-like behavior?

First, we use a marker (like a post-it note) to keep track of where the bottom-most empty mailbox is.  In the beginning, this will be the lowest mailbox (on the bottom of the ngăn xếp Stack).  When we push an item onto our mailbox ngăn xếp Stack, we put it in the mailbox that is marked (which is the first empty mailbox), and move the marker up one mailbox.  When we pop an item off the ngăn xếp Stack, we move the marker down one mailbox (so it’s pointed at the top non-empty mailbox) and remove the item from that mailbox.  Anything below the marker is considered “on the ngăn xếp Stack”.  Anything at the marker or above the marker is not on the ngăn xếp Stack.

**The call ngăn xếp Stack segment**

The call ngăn xếp Stack segment holds the memory used for the call ngăn xếp Stack.  When the application starts, the main() hàm is pushed on the call ngăn xếp Stack by the operating system.  Then the program begins executing.

When a hàm call is encountered, the hàm is pushed onto the call ngăn xếp Stack.  When the current hàm ends, that hàm is popped off the call ngăn xếp Stack (this process is sometimes called **unwinding the ngăn xếp Stack**).  Thus, by looking at the các hàm that are currently on the call ngăn xếp Stack, we can see all of the các hàm that were called to get to the current point of execution.

Our mailbox analogy above is fairly analogous to how the call ngăn xếp Stack works.  The ngăn xếp Stack itself is a fixed-size chunk of memory addresses.  The mailboxes are memory addresses, and the “items” we’re pushing and popping on the ngăn xếp Stack are called **ngăn xếp Stack frames**.  A ngăn xếp Stack frame keeps track of all of the data associated with one hàm call.  We’ll talk more about ngăn xếp Stack frames in a bit.  The “marker” is a register (a small piece of memory in the CPU) known as the ngăn xếp Stack con trỏ (sometimes abbreviated “SP”).  The ngăn xếp Stack con trỏ keeps track of where the top of the call ngăn xếp Stack currently is.

We can make one further optimization: When we pop an item off the call ngăn xếp Stack, we only have to move the ngăn xếp Stack con trỏ down -- we don’t have to clean up or zero the memory used by the popped ngăn xếp Stack frame (the equivalent of emptying the mailbox).  This memory is no longer considered to be “on the ngăn xếp Stack” (the ngăn xếp Stack con trỏ will be at or below this address), so it won’t be accessed.   If we later push a new ngăn xếp Stack frame to this same memory, it will overwrite the old value we never cleaned up.

**The call ngăn xếp Stack in action**

Let’s examine in more detail how the call ngăn xếp Stack works.  Here is the sequence of steps that takes place when a hàm is called:

<ol start="1">
- The program encounters a hàm call.

</li>
- A ngăn xếp Stack frame is constructed and pushed on the ngăn xếp Stack. The ngăn xếp Stack frame consists of:

</li>

- The address of the instruction beyond the hàm call (called the **return address**).  This is how the CPU remembers where to return to after the called hàm exits.

- All hàm đối số.

- Memory for any local các biến

- Saved copies of any registers modified by the hàm that need to be restored when the hàm returns

<ol start="3">
- The CPU jumps to the hàm’s start point.

- The instructions inside of the hàm begin executing.

When the hàm terminates, the following steps happen:

- Registers are restored from the call ngăn xếp Stack

- The ngăn xếp Stack frame is popped off the ngăn xếp Stack.  This frees the memory for all local các biến and đối số.

- The giá trị trả về is handled.

- The CPU resumes execution at the return address.

Return values can be handled in a number of different ways, depending on the computer’s architecture.  Some architectures include the giá trị trả về as part of the ngăn xếp Stack frame.  Others use CPU registers.

Typically, it is not important to know all the details about how the call ngăn xếp Stack works.  However, understanding that các hàm are effectively pushed on the ngăn xếp Stack when they are called and popped off (unwound) when they return gives you the fundamentals needed to understand recursion, as well as some other concepts that are useful when debugging.

A technical note: on some architectures, the call ngăn xếp Stack grows away from memory address 0.  On others, it grows towards memory address 0.  As a consequence, newly pushed ngăn xếp Stack frames may have a higher or a lower memory address than the previous ones.

**A quick and dirty call ngăn xếp Stack example**

Consider the following simple application:

```cpp
int foo(int x)
{
    // b
    return x;
} // foo is popped off the call stack here

int main()
{
    // a
    foo(5); // foo is pushed on the call stack here
    // c

    return 0;
}
```

The call ngăn xếp Stack looks like the following at the labeled points:

a:

```cpp
main()
```

b:

```cpp
foo() (including parameter x)
main()
```

c:

```cpp
main()
```

**Stack overflow**

The ngăn xếp Stack has a limited size, and consequently can only hold a limited amount of information.  On Visual Studio for Windows, the default ngăn xếp Stack size is 1MB.  With g++/Clang for Unix variants, it can be as large as 8MB.  If the program tries to put too much information on the ngăn xếp Stack, ngăn xếp Stack overflow will result.  **Stack overflow** happens when all the memory in the ngăn xếp Stack has been allocated -- in that case, further allocations begin overflowing into other sections of memory.

Stack overflow is generally the result of allocating too many các biến on the ngăn xếp Stack, and/or making too many nested hàm calls (where hàm A calls hàm B calls hàm C calls hàm D etc…)  On modern operating systems, overflowing the ngăn xếp Stack will generally cause your OS to issue an access violation and terminate the program.

Here is an example program that will likely cause a ngăn xếp Stack overflow.  You can run it on your system and watch it crash:

```cpp
#include <iostream>

int main()
{
    int stack[10000000];
    std::cout << "hi" << stack[0]; // we'll use stack[0] here so the compiler won't optimize the array away

    return 0;
}
```

This program tries to allocate a huge (likely 40MB) array on the ngăn xếp Stack.  Because the ngăn xếp Stack is not large enough to handle this array, the array allocation overflows into portions of memory the program is not allowed to use.

On Windows (Visual Studio), this program produces the result:

```cpp
HelloWorld.exe (process 15916) exited with code -1073741571.
```

-1073741571 is c0000005 in hex, which is the Windows OS code for an access violation.  Note that “hi” is never printed because the program is terminated prior to that point.

Here’s another program that will cause a ngăn xếp Stack overflow for a different reason:

```cpp
// h/t to reader yellowEmu for the idea of adding a counter
#include <iostream>

int g_counter{ 0 };

void eatStack()
{
    std::cout << ++g_counter << ' ';

    // We use a conditional here to avoid compiler warnings about infinite recursion
    if (g_counter > 0)
        eatStack(); // note that eatStack() calls itself

    // Needed to prevent compiler from doing tail-call optimization
    std::cout << "hi";
}

int main()
{
    eatStack();

    return 0;
}
```

In the above program, a ngăn xếp Stack frame is pushed on the ngăn xếp Stack every time hàm eatStack() is called.  Since eatStack() calls itself (and never returns to the caller), eventually the ngăn xếp Stack will run out of memory and cause an overflow.

::: info Author’s note

When run on the author’s Windows 10 machine (from within the Visual Studio Community IDE), eatStack() crashed after 4848 calls in debug mode, and 128,679 calls in release mode.

:::

::: info Related content

We talk more about các hàm that call themselves in upcoming lesson [20.3 -- Recursion](https://www.learncpp.com/cpp-tutorial/recursion/).

:::

The ngăn xếp Stack has advantages and disadvantages:

- Allocating memory on the ngăn xếp Stack is comparatively fast.

`<li>`Memory allocated on the ngăn xếp Stack stays in phạm vi truy cập (scope) as long as it is on the ngăn xếp Stack.  It is destroyed when it is popped off the ngăn xếp Stack.
`<li>`All memory allocated on the ngăn xếp Stack is known at compile time.  Consequently, this memory can be accessed directly through a biến.
`<li>`Because the ngăn xếp Stack is relatively small, it is generally not a good idea to do anything that eats up lots of ngăn xếp Stack space.  This includes allocating or copying large arrays or other memory-intensive structures.

::: info Author’s note

[This comment](https://www.learncpp.com/cpp-tutorial/introduction-to-đối tượng-and-các biến/#comment-560618) has some additional (simplified) information about how các biến on the ngăn xếp Stack are laid out and receive actual memory addresses at runtime.
:::

  	
  	

---

::: tip 💡 Tóm Tắt Quy Tắc Vàng (Core Guidelines)
1. Luôn hiểu rõ vòng đời và quyền sở hữu (Ownership) của dữ liệu trước khi viết code.
2. Ưu tiên khởi tạo đồng nhất với dấu ngoặc nhọn `{}` để ngăn chặn lỗi thu hẹp kiểu dữ liệu (Narrowing conversions).
3. Bật toàn bộ cờ cảnh báo `-Wall -Wextra -Wpedantic` để compiler giúp bạn phát hiện bug từ sớm!
:::
