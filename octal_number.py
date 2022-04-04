def octal(n):
    remainder=n%8
    if n>0:
        n//=8
        octal(n)
        print(remainder, end='')

octal(525)