x = []
y = []
distance = []
total = 0
with open("day1_input.txt", "r") as f:
    for line in f:
        x.append(int(line.split()[0]))
        y.append(int(line.split()[1]))
x = sorted(x)
y = sorted(y)
for i in range(len(x)):
    if x[i] > y[i]:
        distance.append(x[i] - y[i])
    else:
        distance.append(y[i] - x[i])
for i in distance:
    total += i
print(total)