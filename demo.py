from itertools import permutations
f=0
count=0
for i in permutations("0123456789",r=6):
    x="".join(i)
    for g in range(len(x)-1):
        if (int(x[g])%2==0 and int(x[g+1])%2!=0) or (int(x[g])%2!=0 and int(x[g+1])%2==0):
            f+=1
    if f==5:
        count+=1

print(count)
