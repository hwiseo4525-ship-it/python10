# 25
keys = input().split()
values = list(map(int, input().split()))
data = dict(zip(keys, values))
for i in ['alpha', 'delta']:
    del data[i]

print(data)


# 26
park = {'korean': 94, 'english': 91, 'mathmatics': 89, 'science': 83}

print(park['english'])
print(park['science'])


# 27
kim = {'korean': 94, 'english': 91, 'mathmatics': 89, 'science': 83}
for i in kim:
    kim[i] = 100

print(kim)


# 28
lee = {'korean': 94, 'english': 91, 'mathmatics': 89, 'science': 83}
if 'english' in lee:
    del lee['english']

print(lee)


# 29
lim = {'korean': 94, 'english': 91, 'mathmatics': 89, 'science': 83}
for key, value in lim.items():
    print(key, value)


# 30
choi = {'korean': 94, 'english': 91, 'mathmatics': 89, 'science': 83}
result = {i: j for i, j in choi.items() if j >= 90}

print(list(result.keys()))


# 31
yoo = {'korean': 94, 'english': 91, 'mathmatics': 89, 'science': 83}
avg = sum(yoo.values()) / len(yoo)

print(avg)