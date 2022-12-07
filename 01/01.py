with open('01/input.txt') as f:
    lines = [line.rstrip() for line in f];


# 1a
res = 0;
current = 0;
for line in lines:
    if line == "":
        res = max(current, res)
        current = 0;
    else:
        current += int(line);

print("1a:", res);

# 1b
current = 0;
totals = [];
for line in lines:
    if line == "":
        totals.append(current);
        current = 0;
    else:
        current += int(line);
totals.append(current);
totals.sort()
totals.reverse();
print(totals);
print("1b:", sum(totals[:3]));