# 21.9 — Overloading the subscript operator

---

## 🎯 Mục Tiêu Bài Học
- Nắm vững bản chất lý thuyết và cơ chế hoạt động của **Overloading the subscript operator** trong tiêu chuẩn ISO C++.
- Hiểu rõ cách máy tính tổ chức bộ nhớ (RAM, CPU registers) khi thực thi mã nguồn liên quan.
- Nhận biết các cạm bẫy lỗi kinh điển (**Undefined Behavior**, Memory Leak, Bug logic) và cách phòng tránh.
- Áp dụng các quy tắc thực hành tốt nhất (**Best Practices**) chuẩn công nghiệp và cập nhật C++20/C++23 hiện đại.

---

# 21.9 &#8212; Overloading the subscript toán tử

When working with arrays, we typically use the subscript toán tử ([]) to index specific elements of an array:

```cpp
myArray[0] = 7; // put the value 7 in the first element of the array
```

However, consider the following `IntList` class, which has a member biến that is an array:

```cpp
class IntList
{
private:
    int m_list[10]{};
};

int main()
{
    IntList list{};
    // how do we access elements from m_list?
    return 0;
}
```

Because the m_list member biến is private, we can not access it directly from biến list.  This means we have no way to directly get or set values in the m_list array.  So how do we get or put elements into our list?

Without toán tử overloading, the typical method would be to create access các hàm:

```cpp
class IntList
{
private:
    int m_list[10]{};

public:
    void setItem(int index, int value) { m_list[index] = value; }
    int getItem(int index) const { return m_list[index]; }
};
```

While this works, it’s not particularly user friendly.  Consider the following example:

```cpp
int main()
{
    IntList list{};
    list.setItem(2, 3);

    return 0;
}
```

Are we setting element 2 to the value 3, or element 3 to the value 2?  Without seeing the definition of `setItem()`, it’s simply not clear.

You could also just return the entire list and use toán tử[] to access the element:

```cpp
class IntList
{
private:
    int m_list[10]{};

public:
    int* getList() { return m_list; }
};
```

While this also works, it’s syntactically odd:

```cpp
int main()
{
    IntList list{};
    list.getList()[2] = 3;

    return 0;
}
```

Overloading toán tử[]

However, a better solution in this case is to overload the subscript toán tử ([]) to allow access to the elements of m_list.  The subscript toán tử is one of the các toán tử that must be overloaded as a member hàm.  An overloaded toán tử[] hàm will always take one tham số: the subscript that the user places between the hard braces.  In our IntList case, we expect the user to pass in an integer index, and we’ll return an integer value back as a result.

```cpp
#include <iostream>

class IntList
{
private:
    int m_list[10]{};

public:
    int& operator[] (int index)
    {
        return m_list[index];
    }
};

/*
// Can also be implemented outside the class definition
int& IntList::operator[] (int index)
{
    return m_list[index];
}
*/

int main()
{
    IntList list{};
    list[2] = 3; // set a value
    std::cout << list[2] << '\n'; // get a value

    return 0;
}
```

Now, whenever we use the subscript toán tử ([]) on an object of our class, the trình biên dịch will return the corresponding element from the m_list member biến!  This allows us to both get and set values of m_list directly.

This is both easy syntactically and from a comprehension standpoint.  When `list[2]` evaluates, the trình biên dịch first checks to see if there’s an overloaded toán tử[] hàm.  If so, it passes the value inside the hard braces (in this case, 2) as an đối số to the hàm.

Note that although you can provide a default value for the hàm tham số, actually using toán tử[] without a subscript inside is not considered a valid syntax, so there’s no point.

::: info Tip

C++23 adds support for overloading toán tử[] with multiple subscripts.

:::

Why toán tử[] returns a tham chiếu

Let’s take a closer look at how `list[2] = 3` evaluates.  Because the subscript toán tử has a higher precedence than the phép gán toán tử, `list[2]` evaluates first.  `list[2]` calls toán tử[], which we’ve defined to return a tham chiếu to `list.m_list[2]`.  Because toán tử[] is returning a tham chiếu, it returns the actual `list.m_list[2]` array element.  Our partially evaluated biểu thức becomes `list.m_list[2] = 3`, which is a straightforward integer phép gán.

Trong bài học [12.2 -- Value categories (lvalues and rvalues)](https://www.learncpp.com/cpp-tutorial/value-categories-lvalues-and-rvalues/), you learned that any value on the left hand side of an phép gán câu lệnh must be an l-value (which is a biến that has an actual memory address).  Because the result of toán tử[] can be used on the left hand side of an phép gán (e.g. `list[2] = 3`), the giá trị trả về of toán tử[] must be an l-value.  As it turns out, các tham chiếu are always l-values, because you can only take a tham chiếu of các biến that have memory addresses.  So by returning a tham chiếu, the trình biên dịch is satisfied that we are returning an l-value.

Consider what would happen if toán tử[] returned an integer by value instead of by tham chiếu.  `list[2]` would call toán tử[], which would return the *value of* list.m_list[2].  For example, if m_list[2] had the value of 6, toán tử[] would return the value 6.  `list[2] = 3` would partially evaluate to `6 = 3`, which makes no sense!  If you try to do this, the C++ trình biên dịch will complain:

```cpp
C:VCProjectsTest.cpp(386) : error C2106: '=' : left operand must be l-value
```

Overloaded toán tử[] for const đối tượng

In the above IntList example, toán tử[] is non-const, and we can use it as an l-value to change the state of non-const đối tượng.  However, what if our IntList object was const?  In this case, we wouldn’t be able to call the non-const version of toán tử[] because that would allow us to potentially change the state of a const object.

The good news is that we can define a non-const and a const version of toán tử[] separately.  The non-const version will be used with non-const đối tượng, and the const version with const-đối tượng.

```cpp
#include <iostream>

class IntList
{
private:
    int m_list[10]{ 0, 1, 2, 3, 4, 5, 6, 7, 8, 9 }; // give this class some initial state for this example

public:
    // For non-const objects: can be used for assignment
    int& operator[] (int index)
    {
        return m_list[index];
    }

    // For const objects: can only be used for access
    // This function could also return by value if the type is cheap to copy
    const int& operator[] (int index) const
    {
        return m_list[index];
    }
};

int main()
{
    IntList list{};
    list[2] = 3; // okay: calls non-const version of operator[]
    std::cout << list[2] << '\n';

    const IntList clist{};
    // clist[2] = 3; // compile error: clist[2] returns const reference, which we can't assign to
    std::cout << clist[2] << '\n';

    return 0;
}
```

Removing duplicate code between const and non-const overloads

In the above example, note that the implementations of `int& IntList::toán tử[](int)` and `const int& IntList::toán tử[](int) const` are identical.  The only difference is the return type of the hàm.

In cases where the implementation is trivial (e.g. a single line), it’s fine (and preferred) to have both các hàm use an identical implementation.  The small amount of redundancy this introduces isn’t worth removing.

But what if the implementation of these các toán tử was complex, requiring many câu lệnh?  For example, maybe it’s important that we validate that the index is actually valid, which requires adding many redundant lines of code to each hàm.

In such a case, the redundancy introduced by having many duplicate câu lệnh is more problematic, and it would be desirable to have a single implementation that we could use for both overloads.  But how?  Normally we’d simply implement one hàm in terms of the other (e.g. have one hàm call the other).  But that’s a bit tricky in this case.  The const version of the hàm can’t call the non-const version of the hàm, because that would require discarding the const of a const object.  And while the non-const version of the hàm can call the const version of the hàm, the const version of the hàm returns a const tham chiếu, when we need to return a non-const tham chiếu.  Fortunately, there is a way to work around this.

The preferred solution is as follows:

- Implement the logic for the const version of the hàm.

- Have the non-const hàm call the const hàm and use `const_cast` to remove the const.

The resulting solution looks something like this:

```cpp
#include <iostream>
#include <utility> // for std::as_const

class IntList
{
private:
    int m_list[10]{ 0, 1, 2, 3, 4, 5, 6, 7, 8, 9 }; // give this class some initial state for this example

public:
    int& operator[] (int index)
    {
        // use std::as_const to get a const version of `this` (as a reference) 
        // so we can call the const version of operator[]
        // then const_cast to discard the const on the returned reference
        return const_cast<int&>(std::as_const(*this)[index]);
    }

    const int& operator[] (int index) const
    {
        return m_list[index];
    }
};

int main()
{
    IntList list{};
    list[2] = 3; // okay: calls non-const version of operator[]
    std::cout << list[2] << '\n';

    const IntList clist{};
    // clist[2] = 3; // compile error: clist[2] returns const reference, which we can't assign to
    std::cout << clist[2] << '\n';

    return 0;
}
```

Normally using `const_cast` to remove const is something we want to avoid, but in this case it’s acceptable.  If the non-const overload was called, then we know we’re working with a non-const object.  It’s okay to remove the const on a const tham chiếu to a non-const object.

::: info For advanced readers

In C++23, we can do even better by making use of several features we don’t yet cover in this tutorial series:

```cpp
#include <iostream>

class IntList
{
private:
    int m_list[10]{ 0, 1, 2, 3, 4, 5, 6, 7, 8, 9 }; // give this class some initial state for this example

public:
    // Use an explicit object parameter (self) and auto&& to differentiate const vs non-const
    auto&& operator[](this auto&& self, int index)
    {
        // Complex code goes here
        return self.m_list[index];
    }
};

int main()
{
    IntList list{};
    list[2] = 3; // okay: calls non-const version of operator[]
    std::cout << list[2] << '\n';

    const IntList clist{};
    // clist[2] = 3; // compile error: clist[2] returns const reference, which we can't assign to
    std::cout << clist[2] << '\n';

    return 0;
}
```
:::

Detecting index validity

One other advantage of overloading the subscript toán tử is that we can make it safer than accessing arrays directly.  Normally, when accessing arrays, the subscript toán tử does not check whether the index is valid.  For example, the trình biên dịch will not complain about the following code:

```cpp
int list[5]{};
list[7] = 3; // index 7 is out of bounds!
```

However, if we know the size of our array, we can make our overloaded subscript toán tử check to ensure the index is within bounds:

```cpp
#include <cassert> // for assert()
#include <iterator> // for std::size()

class IntList
{
private:
    int m_list[10]{};

public:
    int& operator[] (int index)
    {
        assert(index >= 0 && static_cast<std::size_t>(index) < std::size(m_list));

        return m_list[index];
    }
};
```

In the above example, we have used the assert() hàm (included in the cassert header) to make sure our index is valid.  If the biểu thức inside the assert evaluates to false (which means the user passed in an invalid index), the program will terminate with an error message, which is much better than the alternative (corrupting memory).  This is probably the most common method of doing error checking of this sort.

If you don’t want to use an assert (which will be compiled out of a non-debug build) you can instead use an if-câu lệnh and your favorite error handling method (e.g. throw an exception, call `std::exit`, etc…):

```cpp
#include <iterator> // for std::size()

class IntList
{
private:
    int m_list[10]{};

public:
    int& operator[] (int index)
    {
        if (!(index >= 0 && static_cast<std::size_t>(index) < std::size(m_list))
        {
            // handle invalid index here
        }

        return m_list[index];
    }
};
```

Pointers to đối tượng and overloaded toán tử[] don’t mix

If you try to call toán tử[] on a con trỏ to an object, C++ will assume you’re trying to index an array of đối tượng of that type.

Consider the following example:

```cpp
#include <cassert> // for assert()
#include <iterator> // for std::size()

class IntList
{
private:
    int m_list[10]{};

public:
    int& operator[] (int index)
    {
        return m_list[index];
    }
};

int main()
{
    IntList* list{ new IntList{} };
    list [2] = 3; // error: this will assume we're accessing index 2 of an array of IntLists
    delete list;

    return 0;
}
```

Because we can’t assign an integer to an IntList, this won’t compile.  However, if assigning an integer was valid, this would compile and run, with undefined results.

::: tip Quy tắc bắt buộc (Rule)

Make sure you’re not trying to call an overloaded toán tử[] on a con trỏ to an object.

:::

The proper syntax would be to dereference the con trỏ first (making sure to use parenthesis since toán tử[] has higher precedence than toán tử*), then call toán tử[]:

```cpp
int main()
{
    IntList* list{ new IntList{} };
    (*list)[2] = 3; // get our IntList object, then call overloaded operator[]
    delete list;

    return 0;
}
```

This is ugly and error prone.  Better yet, don’t set các con trỏ to your đối tượng if you don’t have to.

The hàm tham số does not need to be an integral type

As mentioned above, C++ passes what the user types between the hard braces as an đối số to the overloaded hàm.  In most cases, this will be an integral value.  However, this is not required -- and in fact, you can define that your overloaded toán tử[] take a value of any type you desire.  You could define your overloaded toán tử[] to take a double, a std::string, or whatever else you like.

As a ridiculous example, just so you can see that it works:

```cpp
#include <iostream>
#include <string_view> // C++17

class Stupid
{
private:

public:
	void operator[] (std::string_view index);
};

// It doesn't make sense to overload operator[] to print something
// but it is the easiest way to show that the function parameter can be a non-integer
void Stupid::operator[] (std::string_view index)
{
	std::cout << index;
}

int main()
{
	Stupid stupid{};
	stupid["Hello, world!"];

	return 0;
}
```

As you would expect, this prints:

```cpp
Hello, world!
```

Overloading toán tử[] to take a std::string tham số can be useful when writing certain kinds of classes, such as those that use words as indices.

Hệ thống Câu hỏi & Quiz Tự Luyện

Câu hỏi #1

A map is a class that stores elements as a key-value pair.  The key must be unique, and is used to access the associated pair.  In this quiz, we’re going to write an application that lets us assign grades to students by name, using a simple map class.  The student’s name will be the key, and the grade (as a char) will be the value.

a) First, write a struct named `StudentGrade` that contains the student’s name (as a `std::string`) and grade (as a `char`).

::: details Xem lời giải (Solution)
```cpp
#include <string>

struct StudentGrade
{
    std::string name{};
    char grade{};
};
```
:::

b) Add a class named `GradeMap` that contains a `std::vector` of `StudentGrade` named `m_map`.

::: details Xem lời giải (Solution)
```cpp
#include <string>
#include <vector>

struct StudentGrade
{
	std::string name{};
	char grade{};
};

class GradeMap
{
private:
	std::vector<StudentGrade> m_map{};
};
```
:::

c) Write an overloaded `toán tử[]` for this class.  This hàm should take a `std::string` tham số, and return a tham chiếu to a char.  In the body of the hàm, first see if the student’s name already exists (You can use `std::find_if` from `<algorithm>`).  If the student exists, return a tham chiếu to the grade and you’re done.  Otherwise, use the `std::vector::emplace_back()` or `std::vector::push_back()` hàm to add a `StudentGrade` for this new student.  When you do this, `std::vector` will add a copy of your `StudentGrade` to itself (resizing if needed, invalidating all previously returned các tham chiếu).  Finally, we need to return a tham chiếu to the grade for the student we just added to the `std::vector`.  We can access the student we just added using the `std::vector::back()` hàm.

The following program should run:

```cpp
#include <iostream>

// ...

int main()
{
	GradeMap grades{};

	grades["Joe"] = 'A';
	grades["Frank"] = 'B';

	std::cout << "Joe has a grade of " << grades["Joe"] << '\n';
	std::cout << "Frank has a grade of " << grades["Frank"] << '\n';

	return 0;
}
```

::: details Xem lời giải (Solution)
```cpp
#include <algorithm>
#include <iostream>
#include <string>
#include <string_view>
#include <vector>

struct StudentGrade
{
	std::string name{};
	char grade{};
};

class GradeMap
{
private:
	std::vector<StudentGrade> m_map{};

public:
	char& operator[](std::string_view name);
};

char& GradeMap::operator[](std::string_view name)
{
	auto found{ std::find_if(m_map.begin(), m_map.end(),
				[name](const auto& student) { // this is a lambda that captures name from the surrounding scope
					return (student.name == name); // so we can use name here
				}) };

	if (found != m_map.end())
	{
		return found->grade;
	}

	// otherwise create a new StudentGrade for this student and add
	// it to the end of our vector.  Then return the grade.

	// emplace_back version (C++20 onward)
	// StudentGrade is an aggregate and emplace_back only works with aggregates as of C++20
	return m_map.emplace_back(std::string{name}).grade;

	// push_back version (C++17 or older)
	// m_map.push_back(StudentGrade{std::string{name}});
	// return m_map.back().grade;
}

int main()
{
	GradeMap grades{};

	grades["Joe"] = 'A';
	grades["Frank"] = 'B';

	std::cout << "Joe has a grade of " << grades["Joe"] << '\n';
	std::cout << "Frank has a grade of " << grades["Frank"] << '\n';

	return 0;
}
```

::: info A reminder

See [20.6 -- Introduction to lambdas (anonymous các hàm)](https://www.learncpp.com/cpp-tutorial/introduction-to-lambdas-anonymous-các hàm/) for more information on lambdas.

:::

::: info Tip

Since maps are common, the standard library offers [`std::map`</code>](https://en.cppreference.com/w/cpp/container/map), which is not currently covered on learncpp. Using `std::map`, we can simplify our code to

```cpp
#include <iostream>
#include <map> // std::map
#include <string>

int main()
{
	// std::map can be initialized
	std::map<std::string, char> grades{
		{ "Joe", 'A' },
		{ "Frank", 'B' }
	};

	// and assigned
	grades["Susan"] = 'C';
	grades["Tom"] = 'D';

	std::cout << "Joe has a grade of " << grades["Joe"] << '\n';
	std::cout << "Frank has a grade of " << grades["Frank"] << '\n';

	return 0;
}
```

Prefer using `std::map` over writing your own implementation.
:::
:::

Câu hỏi #2

Extra credit #1: The `GradeMap` class and sample program we wrote is inefficient for many reasons.  Describe one way that the `GradeMap` class could be improved.  

::: details Xem lời giải (Solution)

`std::vector` is unsorted by nature.  This means every time we call `toán tử[]`, we’re potentially traversing the entire `std::vector` to find our element.  With a few elements, this isn’t a problem, but as we continue to add names, this will become increasingly slow.  We could optimize this by keeping our `m_map` sorted and using a binary search, so we minimize the number of elements we have to look through to find the ones we’re interested in.
:::

Câu hỏi #3

Extra credit #2: Why does this program potentially not work as expected?

```cpp
#include <iostream>

int main()
{
	GradeMap grades{};

	char& gradeJoe{ grades["Joe"] }; // does an emplace_back
	gradeJoe = 'A';

	char& gradeFrank{ grades["Frank"] }; // does a emplace_back
	gradeFrank = 'B';

	std::cout << "Joe has a grade of " << gradeJoe << '\n';
	std::cout << "Frank has a grade of " << gradeFrank << '\n';

	return 0;
}
```

::: details Xem lời giải (Solution)

When Frank is added, the `std::vector` may need to grow to hold it.  This requires dynamically allocating a new block of memory, copying the elements in the array to that new block, and deleting the old block.  When this happens, any các tham chiếu to existing elements in the std::vector are invalidated (meaning they are left as dangling các tham chiếu to deleted memory).

In other words, after we `emplace_back("Frank")`, if the std::vector had to grow to make room for Frank, the `gradeJoe` tham chiếu would be invalidated.  Accessing `gradeJoe` to print Joe’s grade would then lead to undefined results.

How a std::vector grows is a trình biên dịch-specific detail, so we can expect the above program to work fine when compiled with some các trình biên dịch and not others.

:::

  	
  	

---

::: tip 💡 Tóm Tắt Quy Tắc Vàng (Core Guidelines)
1. Luôn hiểu rõ vòng đời và quyền sở hữu (Ownership) của dữ liệu trước khi viết code.
2. Ưu tiên khởi tạo đồng nhất với dấu ngoặc nhọn `{}` để ngăn chặn lỗi thu hẹp kiểu dữ liệu (Narrowing conversions).
3. Bật toàn bộ cờ cảnh báo `-Wall -Wextra -Wpedantic` để compiler giúp bạn phát hiện bug từ sớm!
:::
