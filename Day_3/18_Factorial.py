def calc_fact(n):
    fact=1
    for i in range(1,n+1):
        fact=fact*i
    return fact
ans=calc_fact(5)
print("factorial Of is :",ans)
