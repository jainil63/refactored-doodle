"""
# 🌱 Question 15 — The Simple Choice

- Ask the user:
    Choose a number: 1 or 2
- If the input is 1, print:
    You chose option one.
- Else:
    You chose option two.



## Understanding

...



## Edge Cases

User might end up type anything, even a alpha numeric in real world.
but we are assume only numeric string might be enter in worst case, never the alpha-numeric.

Besides user might even enter other number then 1 & 2.



## Brute Force Approach

Time:  O(1) ->  ≈6 ms
Space: O(1) ->  ≈N bits (N = total No. of character user inputs)

```python
number = input("Choose a number: 1 or 2> ")

if int(number) == 1:
    print("You chose option one.")

if int(number) == 2:
    print("You chose option two.")
```



## Optimized Solution

Optmizied code assume user input is either 1 or 2.

Time:  O(1) ->  ≈3 ms
Space: O(1) ->  ≈N bits (N = total No. of character user inputs)

```python
number = input("Choose a number: 1 or 2> ")

if number == "1":
    print("You chose option one.")
else:
    print("You chose option two.")
```

"""

number = input("Choose a number: 1 or 2> ")

if number == "1":
    print("You chose option one.")
else:
    print("You chose option two.")
