def Look_and_Say(k):
    lst = []
    a = 0
    while a < len(k):
        j= 1
        if a+1 < len(k) and k[a]==k[a+1]:
            a+= 1 
            j+= 1          
        lst.append(str(j)+k[a])
        a+= 1 
    return ''.join(lst)
    
n = int(input())
num = 1
for i in range (n):
    print(num)
    num = Look_and_Say(str(num))