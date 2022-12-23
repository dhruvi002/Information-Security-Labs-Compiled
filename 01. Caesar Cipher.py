#Caesar Cipher
# key = int(input("Enter the key:"))
key = 2
# pt = input("Enter the plain text:")
pt = 'PLAIN TEXT AS INPUT'
print("The plain text is:",pt)
print("The ket is:",key,"\n")
letter=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']

def encryption(plain_text,key):
  ct = []
  for i in plain_text:
    if i in letter:
      ind = letter.index(i)
      c = (ind + key) % 26  
      ct.append(letter[c])
      
  return ("".join(ct))

cipher_text = encryption(pt,key)
print("After Encryption\nThe encrypted text is:",cipher_text,"\n")

cipher_text=list(cipher_text)
def decryption(cipher_text,key):
  pt = []
  for i in cipher_text:
    if i in letter:
      ind = letter.index(i)
      c = (ind - key) % 26
      pt.append(letter[c])
  
  return ("".join(pt))

plain_text = decryption(cipher_text,key)
print("After Decryption\nThe decrypted text is:",plain_text)