A = {1,2,3,4,5,6}
B = {5,6,7,8,9}
C = "tılfındır şenikliği yapmayın"
print(type(A))
print(set(C))
A.add(48)
print(A)
A.discard(2) #elemanı çıkar
print(A)
print(A.difference(B))
print(B.difference(A))
print(A.intersection(B))
print(A.isdisjoint(B)) #ayrık küme mi değilse false
print(A.issubset(B)) #alt kümesi mi evet ise true
print(A.union(B)) #kümelerin birleşimini alır
print(dir(A))










