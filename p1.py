nl = []
nl2 = []

m = 0

for i in range(9):
    nl.append(int(input()))
    nl2.append(nl[i])

the_num_max = 0

for j in range(9):
    for k in range(j, 9):
        if nl[j] < nl[k]:
            m = nl[j]
            nl[j] = nl[k]
            nl[k] = m

for i in range(9):
    if max(nl2) == nl2[i]:  # 최대값을 찾는 부분을 수정
        the_num_max = i+1
        break

print(nl[0])
print(the_num_max)