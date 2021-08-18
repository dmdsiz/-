a = int(input())
b = int(input())
c = int(input())
d = int(input())

e = (a*10**9)+(b*10**6)+(c*10**3)+d
f = e%2**30//2**20
g = e%2**30%2**20//2**10
h = e%2**30%2**20%2**10
print(e,'b',sep='')
print(e//2**30,'Gib, ',f,'Mib, ',g,'Kib, ',h,'b',sep='')