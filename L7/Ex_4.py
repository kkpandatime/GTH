import os

dir = 'my_project'
interval = [100, 1000, 10000, 100000]
result = dict.fromkeys(interval, 0)

for addr, dirs, files in os.walk(dir):
    for file in files:
        path = os.path.join(addr, file)
        size = os.path.getsize(path)

        group = min(filter(lambda x: size < x, interval))
        result[group] += 1

print(result)