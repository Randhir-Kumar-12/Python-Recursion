def binary(n):
    remainder=n%2
    if n>0:
        n//=2
        binary(n)
        print(remainder, end='')

binary(13)