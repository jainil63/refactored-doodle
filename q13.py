"""
# 🌱 Question 13 — The Password Guess (Gentle Version)

Ask the user to enter a password.

- If the password is exactly: `python`
- Print: `Access granted.`
- Else: `Access denied.`

(Yes — this is intentionally naive.)



## Understanding

Ask a password from user, check it & protect mocked system.



## Edge Cases

No edge cases for such a simple thing.



## Brute Force Approach

Time:  O(1) ->  ≈3 ms
Space: O(1) ->  ≈N bits (N = total No. of character user inputs)

```python
password = input("enter password: ")

if password == "python":
    print("Access granted.")
else:
    print("Access denied.")
```



## Optimized Solution

No optimizion possible

Time:  O(1) ->  ≈3 ms
Space: O(1) ->  ≈N bits (N = total No. of character user inputs)

```python
password = input("enter password: ")

if password == "python":
    print("Access granted.")
else:
    print("Access denied.")
```

"""

password = input("enter password: ")

if password == "python":
    print("Access granted.")
else:
    print("Access denied.")
