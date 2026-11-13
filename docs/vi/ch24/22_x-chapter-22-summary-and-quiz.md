# 22.x — Chapter 22 summary and quiz

---

## 🎯 Mục Tiêu Bài Học
- Nắm vững bản chất lý thuyết và cơ chế hoạt động của **Chapter 22 summary and quiz** trong tiêu chuẩn ISO C++.
- Hiểu rõ cách máy tính tổ chức bộ nhớ (RAM, CPU registers) khi thực thi mã nguồn liên quan.
- Nhận biết các cạm bẫy lỗi kinh điển (**Undefined Behavior**, Memory Leak, Bug logic) và cách phòng tránh.
- Áp dụng các quy tắc thực hành tốt nhất (**Best Practices**) chuẩn công nghiệp và cập nhật C++20/C++23 hiện đại.

---

# 22.x &#8212; Chapter 22 summary and quiz

A smart con trỏ class is a composition class that is designed to manage dynamically allocated memory, and ensure that memory gets deleted when the smart con trỏ object goes out of phạm vi truy cập (scope).

Copy semantics allow our classes to be copied.  This is done primarily via the copy hàm tạo (constructor) and copy phép gán toán tử.

Move semantics mean a class will transfer ownership of the object rather than making a copy.  This is done primarily via the move hàm tạo (constructor) and move phép gán toán tử.

std::auto_ptr is deprecated and should be avoided.

An r-value tham chiếu is a tham chiếu that is designed to be được khởi tạo with an r-value.  An r-value tham chiếu is created using a double ampersand.  It’s fine to write các hàm that take r-value tham chiếu tham số, but you should almost never return an r-value tham chiếu.

If we construct an object or do an phép gán where the đối số is an l-value, the only thing we can reasonably do is copy the l-value. We can’t assume it’s safe to alter the l-value, because it may be used again later in the program. If we have an biểu thức “a = b”, we wouldn’t reasonably expect b to be changed in any way.

However, if we construct an object or do an phép gán where the đối số is an r-value, then we know that r-value is just a temporary object of some kind. Instead of copying it (which can be expensive), we can simply transfer its resources (which is cheap) to the object we’re constructing or assigning. This is safe to do because the temporary will be destroyed at the end of the biểu thức anyway, so we know it will never be used again!

You can use the delete keyword to disable copy semantics for classes you create by deleting the copy hàm tạo (constructor) and copy phép gán toán tử.

std::move allows you to treat an l-value as r-value.  This is useful when we want to invoke move semantics instead of copy semantics on an l-value.

std::unique_ptr is the smart con trỏ class that you should probably be using.  It manages a single non-shareable resource.  std::make_unique() (in C++14) should be preferred to create new std::unique_ptr.  std::unique_ptr disables copy semantics.

std::shared_ptr is the smart con trỏ class used when you need multiple đối tượng accessing the same resource.  The resource will not be destroyed until the last std::shared_ptr managing it is destroyed.  std::make_shared() should be preferred to create new std::shared_ptr.  With std::shared_ptr, copy semantics should be used to create additional std::shared_ptr pointing to the same object.

std::weak_ptr is the smart con trỏ class used when you need one or more đối tượng with the ability to view and access a resource managed by a std::shared_ptr, but unlike std::shared_ptr, std::weak_ptr is not considered when determining whether the resource should be destroyed.

**Hệ thống Câu hỏi & Quiz Tự Luyện**


- Explain when you should use the following types of các con trỏ.

1a) std::unique_ptr

::: details Xem lời giải (Solution)

std::unique_ptr should be used when you want a smart con trỏ to manage a dynamic object that is not going to be shared.

:::

1b) std::shared_ptr

::: details Xem lời giải (Solution)

std::shared_ptr should be used when you want a smart con trỏ to manage a dynamic object that may be shared.  The object won’t be deallocated until all std::shared_ptr holding the object are destroyed.

:::

1c) std::weak_ptr

::: details Xem lời giải (Solution)

std::weak_ptr should be used when you want access to an object that is being managed by a std::shared_ptr, but don’t want the lifetime of the std::shared_ptr to be tied to the lifetime of the std::weak_ptr.

:::

1d) std::auto_ptr

::: details Xem lời giải (Solution)

std::auto_ptr has been deprecated and was removed in C++17.  It should not be used.

:::


- Explain why move semantics is focused around r-values.

::: details Xem lời giải (Solution)

Because r-values are temporary, we know they are going to get destroyed after they are used.  When passing or returning an r-value by value, it’s wasteful to make a copy and then destroy the original.  Instead, we can simply move (steal) the r-value’s resources, which is generally more efficient.

:::


- What’s wrong with the following code?  Update the program to be best practices compliant.

3a)

```cpp
#include <iostream>
#include <memory> // for std::shared_ptr
 
class Resource
{
public:
	Resource() { std::cout << "Resource acquired\n"; }
	~Resource() { std::cout << "Resource destroyed\n"; }
};
 
int main()
{
	auto* res{ new Resource{} };
	std::shared_ptr<Resource> ptr1{ res };
	std::shared_ptr<Resource> ptr2{ res };

	return 0;
}
```

::: details Xem lời giải (Solution)

`ptr2` was created from `res` instead of from `ptr1`.  This means that you now have two `std::shared_ptr` each independently trying to manage the `Resource` (they are not aware of each other).  When one goes out of phạm vi truy cập (scope), the other will be left with a dangling con trỏ.

`ptr2` should instead be được khởi tạo with `ptr1` instead of from `res`.  This will allow both `ptr1` and `ptr2` to share ownership of `res`.  `std::make_shared()` should be used instead of manual cấp phát động.

```cpp
#include <iostream>
#include <memory> // for std::shared_ptr
 
class Resource
{
public:
	Resource() { std::cout << "Resource acquired\n"; }
	~Resource() { std::cout << "Resource destroyed\n"; }
};
 
int main()
{
	auto ptr1{ std::make_shared<Resource>() };
	auto ptr2{ ptr1 };

	return 0;
}
```
:::

  	
  	

---

::: tip 💡 Tóm Tắt Quy Tắc Vàng (Core Guidelines)
1. Luôn hiểu rõ vòng đời và quyền sở hữu (Ownership) của dữ liệu trước khi viết code.
2. Ưu tiên khởi tạo đồng nhất với dấu ngoặc nhọn `{}` để ngăn chặn lỗi thu hẹp kiểu dữ liệu (Narrowing conversions).
3. Bật toàn bộ cờ cảnh báo `-Wall -Wextra -Wpedantic` để compiler giúp bạn phát hiện bug từ sớm!
:::
