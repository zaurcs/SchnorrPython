import random
import sys
  
PRIMENO = 89
generator = 3
  
  
secretVal = random.randint(1, 97)
  
X = pow(generator, secretVal) % PRIMENO
y = random.randint(1, 97)
Y = pow(generator, y) % PRIMENO
  
print("Sanchita (the Prover) generates these values:")
print("secretVal(secret)= ", secretVal)
print("PRIMENO= ", PRIMENO)
print("X= ", X)
  
print("\nSanchita generates a random value (y):")
print("y=", y)
  
print("\nSanchita computes Y = generator^y \
(mod PRIMENO) and passes to Sachin:")
  
print("Y=", Y)
  
print("\nSachin generates a random value (c) and\
passes to Sanchita:")
  
c = random.randint(1, 97)
print("c=", c)
print("\nSanchita calculates z = y.secretVal^c \
(mod PRIMENO) and send to Sachin (the Verifier):")
  
z = (y + c * secretVal)
  
print("z=", z)
  
print("\nSachin now computes val=generator^z (mod PRIMENO)\
and (Y X^c (mod PRIMENO)) and determines if they are the same\primeNo")
  
val1 = pow(generator, z) % PRIMENO
val2 = (Y * (X**c)) % PRIMENO
  
print("val1= ", val1, end=' ')
print(" val2= ", val2)
  
if (val1 == val2):
    print("Sanchita has proven that she knows x")
else:
    print("Failure to prove")
