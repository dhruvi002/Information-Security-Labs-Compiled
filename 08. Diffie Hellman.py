# Take input of p g a b
p = int(input("Enter value of p:"))
g = int(input("Enter value of g:"))
a = int(input("Enter value of a:"))
b = int(input("Enter value of b:"))

# Calculate Xa and Xb
Xa = g**a % p
Xb = g**b % p
print("Xa =", Xa)
print("Xb =", Xb)

# Calculate Ak and Bk
Ak = Xb**a % p
Bk = Xa**b % p
print("Ak =", Ak)
print("Bk =", Bk)

if Ak == Bk:
  print("Success!")
else: 
  print("A and B cannot communicate.")