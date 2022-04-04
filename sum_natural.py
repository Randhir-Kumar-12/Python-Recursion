def sum_natural(n):
    s=0
    if n==1:
        return 1
    s=n + sum_natural(n-1)
    return s

sum=sum_natural(4)
print(f"sum of natural number= {sum}")