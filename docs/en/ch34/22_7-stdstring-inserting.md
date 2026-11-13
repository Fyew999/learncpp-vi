# 22.7 &#8212; std::string inserting

**Inserting**

Inserting characters into an existing string can be done via the insert() function.

</p>

**string& string::insert (size_type index, const string& str)**

**string& string::insert (size_type index, const char* str)**</p>

<li>Both functions insert the characters of str into the string at index
<li>Both function return *this so they can be “chained”.
<li>Both functions throw out_of_range if index is invalid
<li>Both functions throw a length_error exception if the result exceeds the maximum number of characters.
<li>In the C-style string version, str must not be NULL.

Sample code:

```cpp
string sString("aaaa");
cout << sString << endl;

sString.insert(2, string("bbbb"));
cout << sString << endl;

sString.insert(4, "cccc");
cout << sString << endl;
```

Output:

```cpp
aaaa
aabbbbaa
aabbccccbbaa
```

<p>Here’s a crazy version of insert() that allows you to insert a substring into a string at an arbitrary index:

</p>

**string& string::insert (size_type index, const string& str, size_type startindex, size_type num)**</p>

<li>This function inserts num characters str, starting from startindex, into the string at index.
<li>Returns *this so it can be “chained”.
<li>Throws an out_of_range if index or startindex is out of bounds
<li>Throws a length_error exception if the result exceeds the maximum number of characters.

Sample code:

```cpp
string sString("aaaa");

const string sInsert("01234567");
sString.insert(2, sInsert, 3, 4); // insert substring of sInsert from index [3,7) into sString at index 2
cout << sString << endl;
```

Output:

```cpp
aa3456aa
```

<p>There is a flavor of insert() that inserts the first portion of a C-style string:

</p>

**string& string::insert(size_type index, const char* str, size_type len)**</p>

<li>Inserts len characters of str into the string at index
<li>Returns *this so it can be “chained”.
<li>Throws an out_of_range exception if the index is invalid
<li>Throws a length_error exception if the result exceeds the maximum number of characters.
<li>Ignores special characters (such as ”)

Sample code:

```cpp
string sString("aaaa");

sString.insert(2, "bcdef", 3);
cout << sString << endl;
```

Output:

```cpp
aabcdaa
```

<p>There’s also a flavor of insert() that inserts the same character multiple times:

</p>

**string& string::insert(size_type index, size_type num, char c)**</p>

<li>Inserts num instances of char c into the string at index
<li>Returns *this so it can be “chained”.
<li>Throws an out_of_range exception if the index is invalid
<li>Throws a length_error exception if the result exceeds the maximum number of characters.

Sample code:

```cpp
string sString("aaaa");

sString.insert(2, 4, 'c');
cout << sString << endl;
```

Output:

```cpp
aaccccaa
```

<p>And finally, the insert() function also has three different versions that use iterators:

</p>

**void insert(iterator it, size_type num, char c)**

**iterator string::insert(iterator it, char c)**

**void string::insert(iterator it, InputIterator begin, InputIterator end)**</p>

<li>The first function inserts num instances of the character c before the iterator it.
<li>The second inserts a single character c before the iterator it, and returns an iterator to the position of the character inserted.
<li>The third inserts all characters between [begin,end) before the iterator it.
<li>All functions throw a length_error exception if the result exceeds the maximum number of characters.

<p>
</a>
  	<a class="nav-link" href="/">
  
    <i class="fa fa-home" aria-hidden="true"></i>
    
      Back to table of contents
    
</a>
  	<a class="nav-link" href="https://www.learncpp.com/cpp-tutorial/stdstring-appending/">
  
    <i class="fa fa-chevron-circle-left" aria-hidden="true"></i>
    
      Previous lesson
      
        22.6std::string appending
      
    
  </a>