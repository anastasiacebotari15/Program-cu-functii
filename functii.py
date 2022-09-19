n=int(input('n='))
m=int(input('m='))
# a)Suma numerelor
def suma(n,m):
    s=0
    s=n+m
    return s
print('Suma numerelor: ',suma(n,m))

# b)Produsul numerelor
def produs(n,m):
    p=1
    p=n*m
    return p
print('Produsul numerelor: ',produs(n,m))

# c)Media aritmetica
def medar(n,m):
    med=1
    med=(n+m)/2
    return med
print('Media aritmetica a numerelor: ', medar(n,m))

# d) Cel mai mare divizor comun
div=[]
def divmax(n, m):
    x=0
    for i in range(1, min(n, m)+1):
        if n%i==m%i==0:
            x+=1
            div.append(i)
divmax(n, m)

print("Cel mai mare divizor comun= ",div[-1])

# e) Cel mai mic divizor comun
d=[]
def multiplu_mic(n, m):
    return (n*m)//div[-1]

print("Cel mai mic multiplu comun= ",multiplu_mic(n, m))

# f) Numarul minim 
print("Numarul minim= ",min(n,m))

# g) Numarul maxim
print("Numarul maxim= ",max(n,m))

# h) Suma numerelor in formatul a+b=c, daca a si b reprezinta numerele citite
def suma(n,m):
    s=0
    s=n+m
    return s
    
print('a+b=c :', n,'+',m,'=', suma(n,m))

# i) Produsul numerelor in formatul a*b=c, daca a si b reprezinta numerele citite
def produs(n,m):
    pd=0
    pd=n*m
    return pd
    
print('a*b=c :', n,'*',m,'=', produs(n,m))

# j) Toti divizorii comuni 
print("Toti divizorii comuni:",*div,sep=',')

# k) 5 multipli comuni 
multiplic=[]
def mult_c(n,m):
    x=n*m
    for i in range(5):
        multiplic.append(x)
        x=x*2
mult_c(n,m)

print("Cinci multipli comuni:",*multiplic,sep=',')

# l) Cifrele care se contin in ambele numere
digits_n,digits_m=[],[]
def comun(n,m):
    digits_n.append([int(x) for x in str(n)])
    digits_m.append([int(x) for x in str(m)])
    c=[*set([x for x in str(n) if x in str(m)])]
    p=[*set([x for x in str(n) if x not in str(m)])]
    c.sort();p.sort()
    return c,p

print("Cifrele care se contin in ambele numere sunt:",*(comun(n,m)[0]),sep=' ')
# m) Cifrele care sunt in primul si nu sunt in al doilea
print ('Cifrele care se regasesc doar in primul numar sunt :', *comun(n,m)[1], sep=' ')
# n) Va afisa mesajul PRIETENE, daca numerele sunt prietene.Doua numere sunt prietene daca au acelasi numar de divizori.
def nr_divizori(x):
    div=[]
    for i in range(1,x+1):
        if x%i==0:
            div.append(i)
    return(len(div))

if nr_divizori(n)==nr_divizori(m):
    print("PRIETENE")
else:
    print('Numerele nu sunt PRIETENE')