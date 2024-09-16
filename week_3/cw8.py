n = 4
i = 0

m = -1
while i < n:
    x = int(input())
    if x  > m:
        m = x
    i = i + 1
print("max is", m)