def expanding(lst):
    lst2 = []
    for i in range(1, len(lst)):
        x = lst[i] - lst[i-1]
        lst2.append(abs(x))
    a = True
    for j in range(1, len(lst2)):
        if lst2[j]>=lst2[j-1]:
            a = False
            break
    return a
lst = list(map(int,input().split()))
print(expanding(lst))