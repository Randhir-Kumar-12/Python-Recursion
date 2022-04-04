
def even_sum(n):
  s=0
  if n==1:
      return 2

  if n%2==0:
    s=s+ even_sum(n-1)
  
  return s
      
    
sum=even_sum(3)
print(sum)
