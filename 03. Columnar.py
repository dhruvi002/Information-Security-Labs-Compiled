def columnar(pt,key):
  mat=[[]]
  count=0
  col=len(key)
  row=len(pt)//col+1
  
  for i in range(row):
    for j in range(col):
      if(count<len(pt)):
        mat[i].append(pt[count])
        count+=1
      else:
        mat[i].append("x")
    mat.append([])
  mat.pop()
  print(mat)
  lkey=[]
  for i in range(len(key)):
    lkey.append((key[i],ord(key[i]),i))
  print(lkey)
  lkey.sort(key=lambda x:x[1])
  print(lkey)
  ct=''
  for i in range(len(lkey)):
    for j in range(row):
      ct+=mat[j][lkey[i][2]]
  print(ct)
  return ct

ct = columnar("columnar transposition",'heaven')
print(ct)

def deccolumnar(ct,key):
  mat=[[]]
  col = len(key)
  row = len(ct)//col
  for i in range(row):
    for j in range(col):
      mat[i].append('x')
    mat.append([])
  mat.pop()
  count=0
  for i in range(col):
    for j in range(row):
      mat[j][i]=ct[count]
      count+=1
  print(mat)
  lkey=[]
  for i in range(len(key)):
    lkey.append((key[i],ord(key[i]),i))
  lkey.sort(key= lambda x:x[1])
  print(lkey)
  pt=''
  order=''
  for i in range(len(lkey)):
    order+=str(lkey[i][2])
  print(order)
  for i in range(row):
    for j in range(len(lkey)):
      # print(order.index(j))
      pt+= mat[i][order.index(str(j))]
      # print(pt)
  pt=pt.replace("x","")
  return pt

deccolumnar('LTONORPOMAIxCASINNTxURSx','heaven')

def double_enc(pt,key1,key2):              # double encryption is performed
  ct1 = columnar(pt,key1)
  ct2 = columnar(ct1,key2)
  return ct2

double_enc('informationsecurity','theory','practs')