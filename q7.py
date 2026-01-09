"""
# 🌱 Question 8 — The Echo Machine

You are generating a very simple “identity card” in text form.

Ask the user for:
- name
- profession
- favorite programming language

Then print three separate lines, each using the stored variables.

```md
Name: Jeel
Profession: Developer
Favorite Language: Python
```

(Spacing and wording matter — pretend a machine will read it.)



## Understanding

Make a the program that respects formatting...
And prints the statements in order given by question...



## Edge Cases

No edge case, for such a simple thing...



## Brute Force Approach

Time:  O(1) ->  ≈6 ms
Space: O(1) ->  ≈N bits (N = total No. of character user inputs)

```python
name = input()
prof = input()
lang = input()

print(f"Name: {name}")
print(f"Profession: {prof}")
print(f"Favorite Language: {lang}")
```



## Optimized Solution

May be one `print()` statement just make one syscall.. But I am not sure..

Time:  O(1) ->  ≈4 ms
Space: O(1) ->  ≈N bits (N = total No. of character user inputs)

```python
name = input()
prof = input()
lang = input()
print(f"Name: {name}\nProfession: {prof}\nFavorite Language: {lang}")
```

"""

name = input()
prof = input()
lang = input()
print(f"Name: {name}\nProfession: {prof}\nFavorite Language: {lang}")
