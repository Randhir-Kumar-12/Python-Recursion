def reverse_odd_number(n):
    if n>0:
        print(2*n-1, end=' ')
        reverse_odd_number(n-1)

reverse_odd_number(5)