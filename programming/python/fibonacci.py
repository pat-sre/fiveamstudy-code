# n = (n-1)+(n-2)

def fib_sequential(n: int) -> int:
    if n == 0:
        return 0
    if n == 1:
        return 1
    n1 = 0
    n2 = 1
    for i in range(n-1):
        n = n1+n2
        n1 = n2
        n2 = n
    return n

def fib_reqursive(n: int) -> int:
    if n == 0 or n == 1:
        return n
    return fib_reqursive(n-2) + fib_reqursive(n-1)

print(fib_sequential(3))

answers = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144]
outputs1 = []
outputs2 = []
for i in range(len(answers)):
    outputs1.append(fib_sequential(i))
    outputs2.append(fib_reqursive(i))

print(f"{outputs1=}")
print(f"{outputs2=}")
print(f"{answers=}")