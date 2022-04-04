def sum_of_digits(n):
    sum=0
    last_digit=n%10
    if n==1 or n==2 or n==3 or n==4 or n==5 or n==6 or n==7 or n==8 or n==9:
        return last_digit

    n//=10  # to get whole number we use--> n//=10 
    sum= last_digit + sum_of_digits(n)
    return sum

sum=sum_of_digits(123)
print(f"sum of digits: {sum}")
