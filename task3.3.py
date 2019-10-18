line_to_find = ('20', '20552', '3')
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
cost = stats_dict[line_to_find]
print(cost)
