def reverse_natural_number(n):
    if n>0:
        print(n, end=' ')
        reverse_natural_number(n-1)
        

reverse_natural_number(5)
