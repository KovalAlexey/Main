n = int(input())
sum1 = 0
n_org = n
for x in range(n-1):
    n = int(input())
    sum1+=n
for i in range(n_org):
    n_org+=i
    i+=1
n_org-=sum1
print(n_org)