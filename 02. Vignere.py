letter = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']

# This function generates the key in a cyclic manner until it's length isn't equal to the length of original text
def generateKey(string, key):
    if len(string) == len(key):
        return(key)
    else:
        for i in range(len(string) - len(key)):
            key += key[i % len(key)]
    return key
     
# This function returns the encrypted text generated with the help of the key
def Encryption(pt, key):
  ct = []
  for i in range(len(pt)):
    p = letter.index(pt[i])
    k = letter.index(key[i])
    x = (p + k) % 26
    ct.append(letter[x])
  return("" . join(ct))
     
# This function decrypts the encrypted text and returns the original text
def Decryption(cipher_text, key):
  pt = []
  for i in range(len(cipher_text)):
    c = letter.index(cipher_text[i])
    k = letter.index(key[i])
    x = (c - k + 26) % 26
    pt.append(letter[x])
  return("" . join(pt))
     

pt = "WEAREDISCOVEREDSAVEYOURSELF"
print("The plain text is:",pt,"\n")

keyword = "DECEPTIVE"
print("The keyword is:",keyword,"\n")

key = generateKey(pt, keyword)
print("Key after its length equal to plain text:",key,"\n")

cipher_text = Encryption(pt,key)
print("After Encryption\nThe ciphertext is:", cipher_text,"\n")
print("After Decryption\nThe plaintext is:",Decryption(cipher_text, key))