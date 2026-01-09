"""
# 🌱 Question 9 — The Time Capsule

You are writing a message to your future self.

Ask the user for:
- current year
- a short message

Then print:
```md
In 2026, you said:
Let's Crack DSA!!!!
```

(Formatting matters more than logic.)



## Understanding

Take current year & message, then print it.



## Edge Cases

No edge case, for such a simple thing...



## Brute Force Approach

Time:  O(1) ->  ≈4 ms
Space: O(1) ->  ≈N bits (N = total No. of character user inputs)

```python
year = input()
msg = input()

print(f"In {year}, you said:")
print(msg)
```



## Optimized Solution

May be one `print()` statement just make one syscall.. But I am not sure..

Time:  O(1) ->  ≈3 ms
Space: O(1) ->  ≈N bits (N = total No. of character user inputs)

```python
year = input()
msg = input()
print(f"In {year}, you said:", msg, sep="\n")
```

"""

year = input()
msg = input()
print(f"In {year}, you said:", msg, sep="\n")
