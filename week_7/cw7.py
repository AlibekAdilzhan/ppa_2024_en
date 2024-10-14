l = [1, 5, 5, 2, 8, 2, 1, 0, 0, 2, 1]
# d = {1: 3, 5: 2, 2: 3, 8: 1, 0: 2}
d = dict()
# if x not in d:
#     d[x] = 1
# else:
#     d[x] = d[x] + 1
for x in l:
    d[x] = d.get(x, 0) + 1
print(d)