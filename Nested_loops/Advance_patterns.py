"""
        5
      4 5
    3 4 5
  2 3 4 5 
1 2 3 4 5
"""

for i in range(5, 0, -1):
    for j in range(i - 1):
        print(" ", end=" ")
    for k in range(i, 6):
        print(k, end=" ")
    print()


print()
"""
*
* *
* * *
* * * *
* * * * *
* * * * 
* * * 
* *
*
"""


for i in range(1, 6):
    for j in range(1, i + 1):
        print("*", end=" ")
    print()
for k in range(1, 6):
    for l in range(1, 6 - k):
        print("*", end=" ")
    print()


print()
"""
        1
      2 1 
    3 2 1 
  4 3 2 1 
5 4 3 2 1 
"""

for i in range(1, 6):
    for j in range(0, 5 - i):
        print(" ", end=" ")
    for k in range(i, 0, -1):
        print(k, end=" ")
    print()


print()


"""
n is given by user
        1
      2 2 2
    3 3 3 3 3
  4 4 4 4 4 4 4
5 5 5 5 5 5 5 5 5
"""

n = 5

for i in range(1, n + 1):
    for j in range(1, n - i + 1):
        print(" ", end=" ")
    for k in range(1, 2 * i):
        print(i, end=" ")
    print()


print()


"""
o is given by user

        1
      2 2 2
    3 3 3 3 3
  4 4 4 4 4 4 4
5 5 5 5 5 5 5 5 5
  4 4 4 4 4 4 4
    3 3 3 3 3
      2 2 2
        1

"""
o = 9

for i in range(1, o // 2 + 2):
    for j in range(1, o // 2 - i + 2):
        print(" ", end=" ")
    for k in range(1, 2 * i):
        print(i, end=" ")
    print()
for i in range(o // 2, 0, -1):
    for j in range(1, o // 2 - i + 2):
        print(" ", end=" ")
    for k in range(1, 2 * i):
        print(i, end=" ")
    print()
