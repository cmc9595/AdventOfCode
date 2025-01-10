with open('1.txt', 'r') as f:
    lines = f.read()
    lines = lines.split('\n')

pairs = []
for line in lines:
    pairs.append(list(map(int, line.split())))

first_column = [pairs[i][0] for i in range(len(pairs))]
second_column = [pairs[i][1] for i in range(len(pairs))]

answer1 = 0
for i, j in zip(sorted(first_column), sorted(second_column)):
    answer1 += abs(i-j)
print(answer1)


from collections import defaultdict
appear = defaultdict(int)
for i in second_column:
    appear[i] += 1
answer2 = sum(i*appear[i] for i in first_column)
print(answer2)
