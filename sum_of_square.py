def sum_of_square(n):
    s=0
    if n==1:
        return 1
    s=n*n + sum_of_square(n-1)
    return s 

s_sum=sum_of_square(3)
print(s_sum)  