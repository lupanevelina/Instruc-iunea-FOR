s1=0
s2=0
s3=0
s4=0
s5=0
s6=0
n=eval(input("Introduceti un numar : "))
for i in range(1,n+1,1):
    s1+=i
n=eval(input("Introduceti un numar : "))
for i in range(2,n+1):
    s2+=(i-1)*i
n=eval(input("Introduceti un numar : "))
for i in range(1,n+1):
    a=1
    for n in range(1,i+1):
        a*=n
    s3+=a
n=eval(input("Introduceti un numar : "))
for i in range(1,n+1):
    s4+=i*10+2
n=eval(input("Introduceti un numar : "))
for i in range(1,n+1):
    s5+=i/(i+1)
n=eval(input("Introduceti un numar : "))
for i in range(2,n+1):
    if i<10:
        s6+=20+i
    else:
        s6+=20*(10**(i//10))+i
print("s1=",s1)
print("s2=",s2)
print("s3=",s3)
print("s4=",s4)
print("s5=",round(s5,2))
print("s6=",s6)


  
