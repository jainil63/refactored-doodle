"""
# 🌱 Question 11 — The Yes or No Gate

- Ask the user:
    Do you like programming? (yes/no)
- If the input is yes, print:
    That’s great!
- Else, print:
    That’s okay, everyone learns differently.



## Understanding

Ask user's about wether they like programming..
if yes then print good. else, comfort them by something good..


## Edge Cases

We are assume user is smart enough to enter either yes or no...



## Brute Force Approach

Time:  O(1) ->  ≈2 ms
Space: O(1) ->  ≈N bits (N = total No. of character user inputs)

```python
x = input("Do you like programming? (yes/no): ")

if x == "yes":
    print("That’s great!")
else:
    print("That’s okay, everyone learns differently.")
```



## Optimized Solution

Time:  O(1) ->  ≈2 ms
Space: O(1) ->  ≈N bits (N = total No. of character user inputs)

```python
# No optimization possible
x = input("Do you like programming? (yes/no): ")

if x == "yes":
    print("That’s great!")
else:
    print("That’s okay, everyone learns differently.")
```

"""

x = input("Do you like programming? (yes/no): ")

if x == "yes":
    print("That’s great!")
else:
    print("That’s okay, everyone learns differently.")
