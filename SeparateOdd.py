A = [int(x) for x in input().split()]
odd = []
even = []
for i in A:
    if i % 2 == 0:
        even.append(i)
    else:
        odd.append(i)
