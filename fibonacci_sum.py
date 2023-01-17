def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)

def sum_fibonacci(n):
    sum = 0
    for i in range(n+1):
        sum += fibonacci(i)
    return sum

print(sum_fibonacci(n))