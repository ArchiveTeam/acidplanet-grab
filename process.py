import os

users = set()
num = 0

for name in os.listdir('TEXT'):
    num += 1
    print(num, len(users))
    with open(os.path.join('TEXT', name), 'r') as f:
        for line in f:
            line = line.strip()
            if len(line) > 0:
                users.add(line)

with open('results', 'w') as f:
    f.write('\n'.join(list(users)))
