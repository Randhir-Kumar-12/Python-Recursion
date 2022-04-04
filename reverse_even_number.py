def even_number(n):
    if n>0:                  # n>0 is optimize logic
        print(2*n, end=' ')  # camapare to n>=1          
        even_number(n-1)
        

even_number(5)        