def substitute(plaintext, key):
    ciphertext = ""
    for letter in plaintext:
        if letter in key:
            ciphertext += key[letter]
        else:
            ciphertext += letter
    return ciphertext

def decrypt(ct,key):
    plt = " "
    for i in ct:
        if i in key:
            plt += key[i]
        else:
            plt += i

    return plt
key = {'A': 'Z', 'B': 'Y', 'C': 'X', 'D': 'W', 'E': 'V', 'F': 'U', 'G': 'T', 'H': 'S', 'I': 'R', 'J': 'Q', 'K': 'P', 'L': 'O', 'M': 'N', 'N': 'M', 'O': 'L', 'P': 'K', 'Q': 'J', 'R': 'I', 'S': 'H', 'T': 'G', 'U': 'F', 'V': 'E', 'W': 'D', 'X': 'C', 'Y': 'B', 'Z': 'A'}

plaintext = "hello world".upper()
print(plaintext)
ciphertext = substitute(plaintext, key)
pt = decrypt(ciphertext,key)
print(ciphertext)  # Output: "svool dliow"
print(pt)