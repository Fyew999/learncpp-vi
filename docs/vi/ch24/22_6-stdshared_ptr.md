# 22.6 — std::shared_ptr

---

## 🎯 Mục Tiêu Bài Học
- Nắm vững bản chất lý thuyết và cơ chế hoạt động của **std::shared_ptr** trong tiêu chuẩn ISO C++.
- Hiểu rõ cách máy tính tổ chức bộ nhớ (RAM, CPU registers) khi thực thi mã nguồn liên quan.
- Nhận biết các cạm bẫy lỗi kinh điển (**Undefined Behavior**, Memory Leak, Bug logic) và cách phòng tránh.
- Áp dụng các quy tắc thực hành tốt nhất (**Best Practices**) chuẩn công nghiệp và cập nhật C++20/C++23 hiện đại.

---

# 22.6 &#8212; std::shared_ptr

Unlike std::unique_ptr, which is designed to singly own and manage a resource, std::shared_ptr is meant to solve the case where you need multiple smart các con trỏ co-owning a resource.

This means that it is fine to have multiple std::shared_ptr pointing to the same resource.  Internally, std::shared_ptr keeps track of how many std::shared_ptr are sharing the resource.  As long as at least one std::shared_ptr is pointing to the resource, the resource will not be deallocated, even if individual std::shared_ptr are destroyed.  As soon as the last std::shared_ptr managing the resource goes out of phạm vi truy cập (scope) (or is reassigned to point at something else), the resource will be deallocated.

Like std::unique_ptr, std::shared_ptr lives in the `<memory>` header.

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
	// allocate a Resource object and have it owned by std::shared_ptr
	Resource* res { new Resource };
	std::shared_ptr<Resource> ptr1{ res };
	{
		std::shared_ptr<Resource> ptr2 { ptr1 }; // make another std::shared_ptr pointing to the same thing

		std::cout << "Killing one shared pointer\n";
	} // ptr2 goes out of scope here, but nothing happens

	std::cout << "Killing another shared pointer\n";

	return 0;
} // ptr1 goes out of scope here, and the allocated Resource is destroyed
```

This prints:

```cpp
Resource acquired
Killing one shared pointer
Killing another shared pointer
Resource destroyed
```

In the above code, we create a dynamic Resource object, and set a std::shared_ptr named ptr1 to manage it.  Inside the nested block, we use the copy hàm tạo (constructor) to create a second std::shared_ptr (ptr2) that points to the same Resource.  When ptr2 goes out of phạm vi truy cập (scope), the Resource is not deallocated, because ptr1 is still pointing at the Resource.  When ptr1 goes out of phạm vi truy cập (scope), ptr1 notices there are no more std::shared_ptr managing the Resource, so it deallocates the Resource.

Note that we created a second shared con trỏ from the first shared con trỏ.  This is important.  Consider the following similar program:

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
	Resource* res { new Resource };
	std::shared_ptr<Resource> ptr1 { res };
	{
		std::shared_ptr<Resource> ptr2 { res }; // create ptr2 directly from res (instead of ptr1)

		std::cout << "Killing one shared pointer\n";
	} // ptr2 goes out of scope here, and the allocated Resource is destroyed

	std::cout << "Killing another shared pointer\n";

	return 0;
} // ptr1 goes out of scope here, and the allocated Resource is destroyed again
```

This program prints:

```cpp
Resource acquired
Killing one shared pointer
Resource destroyed
Killing another shared pointer
Resource destroyed
```

and then crashes (at least on the author’s machine).

The difference here is that we created two std::shared_ptr independently from each other.  As a consequence, even though they’re both pointing to the same Resource, they aren’t aware of each other.  When ptr2 goes out of phạm vi truy cập (scope), it thinks it’s the only owner of the Resource, and deallocates it.  When ptr1 later goes out of the phạm vi truy cập (scope), it thinks the same thing, and tries to delete the Resource again.  Then bad things happen.

Fortunately, this is easily avoided: if you need more than one std::shared_ptr to a given resource, copy an existing std::shared_ptr.

::: tip Thực hành tốt nhất (Best Practice)

Always make a copy of an existing std::shared_ptr if you need more than one std::shared_ptr pointing to the same resource.

:::

Just like with std::unique_ptr, std::shared_ptr can be a null con trỏ, so check to make sure it is valid before using it.

std::make_shared

Much like std::make_unique() can be used to create a std::unique_ptr in C++14, std::make_shared() can (and should) be used to make a std::shared_ptr.  std::make_shared() is available in C++11.

Here’s our original example, using std::make_shared():

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
	// allocate a Resource object and have it owned by std::shared_ptr
	auto ptr1 { std::make_shared<Resource>() };
	{
		auto ptr2 { ptr1 }; // create ptr2 using copy of ptr1

		std::cout << "Killing one shared pointer\n";
	} // ptr2 goes out of scope here, but nothing happens

	std::cout << "Killing another shared pointer\n";

	return 0;
} // ptr1 goes out of scope here, and the allocated Resource is destroyed
```

The reasons for using std::make_shared() are the same as std::make_unique() -- std::make_shared() is simpler and safer (there’s no way to create two independent std::shared_ptr pointing to the same resource but unaware of each other using this method).  However, std::make_shared() is also more performant than not using it.  The reasons for this lie in the way that std::shared_ptr keeps track of how many các con trỏ are pointing at a given resource.

Digging into std::shared_ptr

Unlike std::unique_ptr, which uses a single con trỏ internally, std::shared_ptr uses two các con trỏ internally.  One con trỏ points at the resource being managed.  The other points at a “control block”, which is a dynamically allocated object that tracks of a bunch of stuff, including how many std::shared_ptr are pointing at the resource.  When a std::shared_ptr is created via a std::shared_ptr hàm tạo (constructor), the memory for the managed object (which is usually passed in) and control block (which the hàm tạo (constructor) creates) are allocated separately.  However, when using std::make_shared(), this can be optimized into a single memory allocation, which leads to better performance.

This also explains why independently creating two std::shared_ptr pointed to the same resource gets us into trouble.  Each std::shared_ptr will have one con trỏ pointing at the resource.  However, each std::shared_ptr will independently allocate its own control block, which will indicate that it is the only con trỏ owning that resource.  Thus, when that std::shared_ptr goes out of phạm vi truy cập (scope), it will deallocate the resource, not realizing there are other std::shared_ptr also trying to manage that resource.

However, when a std::shared_ptr is cloned using copy phép gán, the data in the control block can be appropriately updated to indicate that there are now additional std::shared_ptr co-managing the resource.

Shared các con trỏ can be created from unique các con trỏ

A std::unique_ptr can be converted into a std::shared_ptr via a special std::shared_ptr hàm tạo (constructor) that accepts a std::unique_ptr r-value.  The contents of the std::unique_ptr will be moved to the std::shared_ptr.

However, std::shared_ptr can not be safely converted to a std::unique_ptr.  This means that if you’re creating a hàm that is going to return a smart con trỏ, you’re better off returning a std::unique_ptr and assigning it to a std::shared_ptr if and when that’s appropriate.

The perils of std::shared_ptr

std::shared_ptr has some of the same challenges as std::unique_ptr -- if the std::shared_ptr is not properly disposed of (either because it was dynamically allocated and never deleted, or it was part of an object that was dynamically allocated and never deleted) then the resource it is managing won’t be deallocated either.  With std::unique_ptr, you only have to worry about one smart con trỏ being properly disposed of.  With std::shared_ptr, you have to worry about them all.  If any of the std::shared_ptr managing a resource are not properly destroyed, the resource will not be deallocated properly.

std::shared_ptr and arrays

In C++17 and earlier, std::shared_ptr does not have proper support for managing arrays, and should not be used to manage a C-style array.  As of C++20, std::shared_ptr does have support for arrays.

Conclusion

std::shared_ptr is designed for the case where you need multiple smart các con trỏ co-managing the same resource.  The resource will be deallocated when the last std::shared_ptr managing the resource is destroyed.   

  	
  	

---

::: tip 💡 Tóm Tắt Quy Tắc Vàng (Core Guidelines)
1. Luôn hiểu rõ vòng đời và quyền sở hữu (Ownership) của dữ liệu trước khi viết code.
2. Ưu tiên khởi tạo đồng nhất với dấu ngoặc nhọn `{}` để ngăn chặn lỗi thu hẹp kiểu dữ liệu (Narrowing conversions).
3. Bật toàn bộ cờ cảnh báo `-Wall -Wextra -Wpedantic` để compiler giúp bạn phát hiện bug từ sớm!
:::
