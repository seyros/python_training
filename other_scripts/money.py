def money():
    res = []
    if step > 0:
        x = start
        while x < stop:
            res += [x]
            x += step
    elif step < 0:
        x = start
        while x > stop:
            res += [x]
            x += step
    return res

a = int(input())
b = int(input())
c = int(input())
print(my_range(a, b, c))