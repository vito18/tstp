import statistics

lists = []

for i in range(0, 100):
    lists.append(i)

print(lists)

print(statistics.mean(lists))

print(statistics.median(lists))

print(statistics.pstdev(lists))

print(statistics.median_low(lists))

print(statistics.median_high(lists))
