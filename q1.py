"""
# 🌱 Question 1 — Saying something out loud

Write a Python program that prints a message like:

```md
Hello, DSA!!
Let crack you comfortably...
```

(Only print)


## Understanding

Obviously, just print the stuff...


## Edge Cases

No edge cases for just printing stuff on console..

In worst case OS might kill/crash our program in middle of execution,
if you think that matters, then that an edge case...


## Brute Force Approach

Time:  O(1) ->  ≈2 ms
Space: O(1) ->  ≈0 bits

```python
print("Hello, DSA!!")
print("Let crack you comfortably...")
```


## Optimized Solution

May be one `print()` statement just make one syscall.. But I am not sure..

Time:  O(1) ->  ≈1 ms
Space: O(1) ->  ≈0 bits

```python
print("Hello, DSA!!\nLet crack you comfortably...")
```

"""

print("Hello, DSA!!\nLet crack you comfortably...")
