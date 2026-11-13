# 22.5 &#8212; std::string assignment and swapping

**String assignment**

The easiest way to assign a value to a string is to use the overloaded operator= function.  There is also an assign() member function that duplicates some of this functionality.

</p>

**string& string::operator= (const string& str)**

**string& string::assign (const string& str)**

**string& string::operator= (const char* str)**

**string& string::assign (const char* str)**

**string& string::operator= (char c)**

</p>

<li>These functions assign values of various types to the string.
<li>These functions return *this so they can be “chained”.
<li>Note that there is no assign() function that takes a single char.

Sample code:

```cpp
std::string sString;

// Assign a string value
sString = std::string("One");
std::cout << sString << '\n';

const std::string sTwo("Two");
sString.assign(sTwo);
std::cout << sString << '\n';

// Assign a C-style string
sString = "Three";
std::cout << sString << '\n';

sString.assign("Four");
std::cout << sString << '\n';

// Assign a char
sString = '5';
std::cout << sString << '\n';

// Chain assignment
std::string sOther;
sString = sOther = "Six";
std::cout << sString << ' ' << sOther << '\n';
```

Output:

```cpp
One
Two
Three
Four
5
Six Six
```

<p>The assign() member function also comes in a few other flavors:

</p>

**string& string::assign (const string& str, size_type index, size_type len)**</p>

<li>Assigns a substring of str, starting from index, and of length len
<li>Throws an out_of_range exception if the index is out of bounds
<li>Returns *this so it can be “chained”.

Sample code:

```cpp
const std::string sSource("abcdefg");
std::string sDest;

sDest.assign(sSource, 2, 4); // assign a substring of source from index 2 of length 4
std::cout << sDest << '\n';
```

Output:

```cpp
cdef
```

**string& string::assign (const char* chars, size_type len)**</p>

<li>Assigns len characters from the C-style array chars
<li>Throws an length_error exception if the result exceeds the maximum number of characters
<li>Returns *this so it can be “chained”.

Sample code:

```cpp
std::string sDest;

sDest.assign("abcdefg", 4);
std::cout << sDest << '\n';
```

Output:

```cpp
abcd
```

This function is potentially dangerous and its use is not recommended.

**string& string::assign (size_type len, char c)**</p>

<li>Assigns len occurrences of the character c
<li>Throws a length_error exception if the result exceeds the maximum number of characters
<li>Returns *this so it can be “chained”.

Sample code:

```cpp
std::string sDest;

sDest.assign(4, 'g');
std::cout << sDest << '\n';
```

Output:

```cpp
gggg
```

<p>**Swapping**

If you have two strings and want to swap their values, there are two functions both named swap() that you can use.

</p>

**void string::swap (string& str)**

**void swap (string& str1, string& str2)**</p>

<li>Both functions swap the value of the two strings.  The member function swaps *this and str, the global function swaps str1 and str2.
<li>These functions are efficient and should be used instead of assignments to perform a string swap.

Sample code:

```cpp
std::string sStr1("red");
std::string sStr2("blue");

std::cout << sStr1 << ' ' << sStr2 << '\n';
swap(sStr1, sStr2);
std::cout << sStr1 << ' ' << sStr2 << '\n';
sStr1.swap(sStr2);
std::cout << sStr1 << ' ' << sStr2 << '\n';
```

Output:

```cpp
red blue
blue red
red blue
```

<p>
</a>
  	<a class="nav-link" href="/">
  
    <i class="fa fa-home" aria-hidden="true"></i>
    
      Back to table of contents
    
</a>
  	<a class="nav-link" href="https://www.learncpp.com/cpp-tutorial/stdstring-character-access-and-conversion-to-c-style-arrays/">
  
    <i class="fa fa-chevron-circle-left" aria-hidden="true"></i>
    
      Previous lesson
      
        22.4std::string character access and conversion to C-style arrays
      
    
  </a>