line_to_find = ('20', '20552', '3')
#line_to_find = [(int(i) for i in input().split()]
print(line_to_find)
stats_dict = {}
n = len(line_to_find)
with open('stats.csv') as f:
    for line in f:
        line = line.strip().split(',')
        if n < len(line):
            stats_dict[tuple(line[:n])] = line[n]
        else:
            print('недостаточно числа столбцов для вычислений')
            break
if n < len(line):
    for i in stats_dict:
        cost = stats_dict[line_to_find]
    print(cost)