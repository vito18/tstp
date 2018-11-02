s1 = set([10, 20, 30, 40, 50])
s2 = set([10, 30, 50, 70, 90])

s_add = s1 | s2
print(s_add)

s_multiply = s1 & s2
print(s_multiply)

s_diff = s1 - s2
print(s_diff)
