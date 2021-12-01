f=open('caractere.txt','w')
c=str(input('dati nr de caractere'))
f.write(c)
 #citire din fisier
f=open('caractere.txt','r')
d=f.read()
print(d)
x=[]
for i in range (0,len(d)):
    if d[i]=='a' or d[i]=='A' or d[i]=='e' or d[i]=='E' or d[i]=='i' or d[i]=='I' or d[i]=='o' or d[i]=='O' or d[i]=='u' or d[i]=='U':
        x.extend(d[i])
y=str(len(x))
f=open('vocale.txt','w')
f.write(x)
f.write(str(x))
f.write('\n')
f.write('numarul de vocale din sir: ')
f.write(y)
f.close()

f=open("vocale.txt","r")
z=f.read()
print("Vocalele din sir sunt:", z)
f.close()