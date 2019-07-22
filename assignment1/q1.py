#prg to check if gvn num is prime or not

def is_prime(N):
 if N<2:
  return False
 for i in range(2,N//2+2):
  if N%i==0:
    return False
  return True

Num=int(input("Enter a number:"))
if is_prime(Num):
 print(f"{Num} is prime")
else:
 print(f"{Num} is not prime")  