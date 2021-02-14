
def nwd(a,b):
    if b>0:
        return nwd(b,a%b)
    else:
        return a

cialo_niez=int(input("Podaj z ciala/pierscienia: "))
element_niez=int(input("Podaj element do odwrócenia w tym ciele: "))
cialo=cialo_niez
element=element_niez
print(pow(26,419,473))
if element>cialo:
    element=element%cialo
if nwd(cialo,element)!=1:
    print("Ten element nie należy do pierścienia")
    exit()
else:
    while cialo>1:
        print(cialo,"=",cialo//element,"*",element,"+",cialo%element)
        temp=cialo
        cialo=element
        element=temp%element
    for i in range(cialo_niez):
        if (element_niez*i%cialo_niez)==1:
            element_odw=i
    for j in range(cialo_niez):
        if (element_niez*element_odw -(j*cialo_niez))==1:
            x=j
    print("1=",element_niez,"*",element_odw,"-",x,"*",cialo_niez)
    print("Elementem odwrotnym do: ",element_niez," jest: ",element_odw)
    input("Press Enter to continue...")

