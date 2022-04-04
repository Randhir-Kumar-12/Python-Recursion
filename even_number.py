def even_number(n):
    if n>0:              # n>0 is optimize logic
        even_number(n-1) # camapare to n>=1
        print(2*n, end=' ')

even_number(5)        