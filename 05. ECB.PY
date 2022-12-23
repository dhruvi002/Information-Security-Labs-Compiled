import math

def csl(text, t):
    shift = text[:t]
    text = text[t:]

    text += shift
    return text

def csr(text, t):
    shift = text[-(t):]
    text = text[:len(text)-t]

    shift += text
    return shift

def encryption(pt, key, myt):
    
    if(len(pt)%16!=0):
        extra = 16 - len(pt)%16
        for i in range(extra):
            pt += 'X'
    
    pt_list = list(pt)

    blocks = []
    while pt_list != []:
        blocks.append(pt_list[:16])
        pt_list = pt_list[16:]
    
    ascii = []
    for block in blocks:
        temp = []
        for i in block:
            temp.append(ord(i))

        ascii.append(temp)

    binary_list = []
    for block in ascii:
        temp = []
        for i in block:
            temp.append(bin(i)[2:])

        binary_list.append(temp)
    
    for block in binary_list:
        for i in range(len(block)):
            if len(block[i]) == 7:
                block[i] = '0' + block[i]
            elif len(block[i]) == 6:
                block[i] = '00' + block[i]

    binary_bits = []
    for block in binary_list:
        temp = ''
        for i in block:
            temp += i
        binary_bits.append(temp)
    
    
    ct = []
    for block in binary_bits:
        t = ''
        
        for p,k in zip(block, key):
            temp = int(p) ^ int(k)
            t += str(temp)

        ct.append(t)

    shifted_ct = []
    for i in ct:
        shifted_ct.append(csl(i, myt))
    ct_text = ''
    for i in shifted_ct:
        ct_text += i
    
    ascii = []
    while(ct_text != ''):
        ascii.append(('0b' + ct_text[:8]))
        ct_text = ct_text[8:]
    
    encrypted = ''
    for i in ascii:
        temp = int(i,2)
        encrypted += chr(temp)
    
    return encrypted

def decryption(ct, key, t):
    ct_16_block = []
    while ct!='':
        ct_16_block.append(ct[:16])
        ct = ct[16:]
    
    ascii_blocks = []
    for block in ct_16_block:
        temp = []
        for char in block:
            temp.append(ord(char))
        
        ascii_blocks.append(temp)

    binary_blocks = []
    for block in ascii_blocks:
        temp = []
        for i in block:
            temp.append(bin(i)[2:])
        binary_blocks.append(temp)

    for block in binary_blocks:
        for i in range(len(block)):
            if len(block[i]) == 7:
                block[i] = '0' + block[i]
            elif len(block[i]) == 6:
                block[i] = '00' + block[i]
            elif len(block[i]) == 5:
                block[i] = '000' + block[i]
            elif len(block[i]) == 4:
                block[i] = '000' + block[i]
    
    bits128 = []
    for block in binary_blocks:
        temp = ''
        for i in block:
            temp += i
        bits128.append(temp)
    
    r_shifted = []
    for i in bits128:
        r_shifted.append(csr(i, t))
    
    ct_exored = []
    for block in r_shifted:
        t = ''
        for p,k in zip(block, key):
            
            temp = int(p) ^ int(k)
            t += str(temp)
        ct_exored.append(t)
    
    ct_text = ''
    for i in ct_exored:
        ct_text += i

    ascii = []
    while(ct_text != ''):
        ascii.append(('0b' + ct_text[:8]))
        ct_text = ct_text[8:]
    
    encrypted = ''
    for i in ascii:
        temp = int(i,2)
        encrypted += chr(temp)
    
    return encrypted

pt = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
key = '00111111101110000000011111000011110011011110011101001010010100111100010000111100011001100011111101011001111111110110101000100010'

ct = encryption(pt, key, 4)
print(ct)

new_pt = decryption(ct, key, 4)
print(new_pt)

d = {}
d['ORIGINAL TEXT'] = pt
d['ENCRYPTED TEXT'] = ct
d['DECRYPTED TEXT'] = new_pt

for i in d.keys():
    print(str(i) + ' : ' + str(d[i]))