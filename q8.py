"""
# 🌱 Question 8 — The Echo Machine

A machine does not understand meaning. It only repeats.

Write a program that:
- asks the user to type any sentence
- stores it in a variable
- prints the sentence exactly twice, on two new lines

Input:
```md
I like slow learning
```

Output:
```md
I like slow learning
I like slow learning
```



## Understanding

Make a program that take input as a sentence.
and the print it twice.



## Edge Cases

No edge case, for such a simple thing...



## Brute Force Approach

Time:  O(1) ->  ≈3 ms
Space: O(1) ->  ≈N bits (N = total No. of character user inputs)

```python
sentence = input()

print(sentence)
print(sentence)
```



## Optimized Solution

May be one `print()` statement just make one syscall.. But I am not sure..

Time:  O(1) ->  ≈2 ms
Space: O(1) ->  ≈N bits (N = total No. of character user inputs)

```python
sentence = input()
print(sentence + "\n" + sentence)
```

"""

sentence = input()
print(sentence + "\n" + sentence)
