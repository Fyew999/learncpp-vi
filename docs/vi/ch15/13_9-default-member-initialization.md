# 13.9 — Default member initialization

---

## 🎯 Mục Tiêu Bài Học
- Nắm vững bản chất lý thuyết và cơ chế hoạt động của **Default member initialization** trong tiêu chuẩn ISO C++.
- Hiểu rõ cách máy tính tổ chức bộ nhớ (RAM, CPU registers) khi thực thi mã nguồn liên quan.
- Nhận biết các cạm bẫy lỗi kinh điển (**Undefined Behavior**, Memory Leak, Bug logic) và cách phòng tránh.
- Áp dụng các quy tắc thực hành tốt nhất (**Best Practices**) chuẩn công nghiệp và cập nhật C++20/C++23 hiện đại.

---

# 13.9 &#8212; Default member sự khởi tạo

When we define a struct (or class) type, we can provide a default sự khởi tạo value for each member as part of the type definition.  For members not marked as `static`, this process is sometimes called **non-static member sự khởi tạo**.  The sự khởi tạo value is called a **default member initializer**.

::: info Related content

We cover static members and static member sự khởi tạo in lesson [15.6 -- Static member các biến](https://www.learncpp.com/cpp-tutorial/static-member-các biến/).

:::

Here’s an example:

```cpp
struct Something
{
    int x;       // no initialization value (bad)
    int y {};    // value-initialized by default
    int z { 2 }; // explicit default value
};

int main()
{
    Something s1; // s1.x is uninitialized, s1.y is 0, and s1.z is 2

    return 0;
}
```

In the above definition of `Something`, `x` has no default value, `y` is value-được khởi tạo by default, and `z` has the default value `2`.  These default member sự khởi tạo values will be used if the user doesn’t provide an explicit sự khởi tạo value when instantiating an object of type `Something`.

Our `s1` object doesn’t have an initializer, so the members of `s1` are được khởi tạo to their default values.  `s1.x` has no default initializer, so it remains chưa được khởi tạo.  `s1.y` is value được khởi tạo by default, so it gets value `0`.  And `s1.z` is được khởi tạo with the value `2`.

Note that even though we haven’t provided an explicit initializer for `s1.z`, it is được khởi tạo to a non-zero value because of the default member initializer provided.

::: info Hiểu biết cốt lõi

Using default member initializers (or other mechanisms that we’ll cover later), structs and classes can self-khởi tạo even when no explicit initializers are provided!

:::

::: info For advanced readers

CTAD (which we cover in lesson [13.14 -- Class template đối số deduction (CTAD) and deduction guides](https://www.learncpp.com/cpp-tutorial/class-template-đối số-deduction-ctad-and-deduction-guides/)) cannot be used in non-static member sự khởi tạo.

:::

Explicit sự khởi tạo values take precedence over default values

Explicit values in a list initializer always take precedence over default member sự khởi tạo values.

```cpp
struct Something
{
    int x;       // no default initialization value (bad)
    int y {};    // value-initialized by default
    int z { 2 }; // explicit default value
};

int main()
{
    Something s2 { 5, 6, 7 }; // use explicit initializers for s2.x, s2.y, and s2.z (no default values are used)
   
    return 0;
}
```

In the above case, `s2` has explicit sự khởi tạo values for every member, so the default member sự khởi tạo values are not used at all.  This means `s2.x`, `s2.y` and `s2.z` are được khởi tạo to the values `5`, `6`, and `7` respectively.

Missing initializers in an initializer list when default values exist

In the previous lesson ([13.8 -- Struct aggregate sự khởi tạo](https://www.learncpp.com/cpp-tutorial/struct-aggregate-sự khởi tạo/)) we noted that if an aggregate is được khởi tạo but the number of sự khởi tạo values is fewer than the number of members, then all remaining members will be value-được khởi tạo.  However, if a default member initializer is provided for a given member, that default member initializer will be used instead.

```cpp
struct Something
{
    int x;       // no default initialization value (bad)
    int y {};    // value-initialized by default
    int z { 2 }; // explicit default value
};

int main()
{
    Something s3 {}; // value initialize s3.x, use default values for s3.y and s3.z
   
    return 0;
}
```

In the above case, `s3` is list được khởi tạo with an empty list, so all initializers are missing.  This means that a default member initializer will be used if it exists, and value sự khởi tạo will occur otherwise.  Thus, `s3.x` (which has no default member initializer) is value được khởi tạo to `0`, `s3.y` is value được khởi tạo by default to `0`, and `s3.z` is defaulted to value `2`.

Recapping the sự khởi tạo possibilities

If an aggregate is defined with an sự khởi tạo list:

- If an explicit sự khởi tạo value exists, that explicit value is used.

- If an initializer is missing and a default member initializer exists, the default is used.

- If an initializer is missing and no default member initializer exists, value sự khởi tạo occurs.

If an aggregate is defined with no sự khởi tạo list:

- If a default member initializer exists, the default is used.

- If no default member initializer exists, the member remains chưa được khởi tạo.

Members are always được khởi tạo in the order of declaration.

The following example recaps all possibilities:

```cpp
struct Something
{
    int x;       // no default initialization value (bad)
    int y {};    // value-initialized by default
    int z { 2 }; // explicit default value
};

int main()
{
    Something s1;             // No initializer list: s1.x is uninitialized, s1.y and s1.z use defaults
    Something s2 { 5, 6, 7 }; // Explicit initializers: s2.x, s2.y, and s2.z use explicit values (no default values are used)
    Something s3 {};          // Missing initializers: s3.x is value initialized, s3.y and s3.z use defaults
   
    return 0;
}
```

The case we want to watch out for is `s1.x`.  Because `s1` has no initializer list and `x` has no default member initializer, `s1.x` remains chưa được khởi tạo (which is bad, since we should always khởi tạo our các biến).

Always provide default values for your members

To avoid the possibility of chưa được khởi tạo members, simply ensure that each member has a default value (either an explicit default value, or an empty pair of braces).  That way, our members will be được khởi tạo with some value regardless of whether we provide an initializer list or not.

Consider the following struct, which has all members defaulted:

```cpp
struct Fraction
{
	int numerator { }; // we should use { 0 } here, but for the sake of example we'll use value initialization instead
	int denominator { 1 };
};

int main()
{
	Fraction f1;          // f1.numerator value initialized to 0, f1.denominator defaulted to 1
	Fraction f2 {};       // f2.numerator value initialized to 0, f2.denominator defaulted to 1
	Fraction f3 { 6 };    // f3.numerator initialized to 6, f3.denominator defaulted to 1
	Fraction f4 { 5, 8 }; // f4.numerator initialized to 5, f4.denominator initialized to 8

	return 0;
}
```

In all cases, our members are được khởi tạo with values.

::: tip Thực hành tốt nhất (Best Practice)

Provide a default value for all members.  This ensures that your members will be được khởi tạo even if the biến definition doesn’t include an initializer list.

:::

Default sự khởi tạo vs value sự khởi tạo for aggregates

Revisiting two lines from the above example:

```cpp
Fraction f1;          // f1.numerator value initialized to 0, f1.denominator defaulted to 1
	Fraction f2 {};       // f2.numerator value initialized to 0, f2.denominator defaulted to 1
```

You’ll note that `f1` is default được khởi tạo and `f2` is value được khởi tạo, yet the results are the same (`numerator` is được khởi tạo to `0` and `denominator` is được khởi tạo to `1`).  So which should we prefer?

The value sự khởi tạo case (`f2`) is safer, because it will ensure any members with no default values are value được khởi tạo (and although we should always provide default values for members, this protects against the case where one is missed).

Preferring value sự khởi tạo has one more benefit -- it’s consistent with how we khởi tạo đối tượng of other types.  Consistency helps prevent errors.

::: tip Thực hành tốt nhất (Best Practice)

For aggregates, prefer value sự khởi tạo (with an empty braces initializer) to default sự khởi tạo (with no braces).

:::

That said, it’s not uncommon for programmers to use default sự khởi tạo instead of value sự khởi tạo for class types.  This is partly for historic reasons (as value sự khởi tạo wasn’t introduced until C++11), and partly because there is a particular case (for non-aggregates) where default sự khởi tạo can be more efficient than value sự khởi tạo (we cover this case in lesson [14.11 -- Default các hàm tạo (constructors) and default đối số](https://www.learncpp.com/cpp-tutorial/default-các hàm tạo (constructors)-and-default-đối số/)).

Therefore, we won’t be militant about enforcing use of value sự khởi tạo for structs and classes in these tutorials, but we do strongly recommend it.

  	
  	

---

::: tip 💡 Tóm Tắt Quy Tắc Vàng (Core Guidelines)
1. Luôn hiểu rõ vòng đời và quyền sở hữu (Ownership) của dữ liệu trước khi viết code.
2. Ưu tiên khởi tạo đồng nhất với dấu ngoặc nhọn `{}` để ngăn chặn lỗi thu hẹp kiểu dữ liệu (Narrowing conversions).
3. Bật toàn bộ cờ cảnh báo `-Wall -Wextra -Wpedantic` để compiler giúp bạn phát hiện bug từ sớm!
:::
