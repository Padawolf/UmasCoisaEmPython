def media():
    a = float(input("Digita algo ai: "))
    b = float(input("Digita algo ai: "))
    c = float(input("Digita algo ai: "))
    lista = []
    lista.append(a)
    lista.append(b)
    lista.append(c)
    tot =0
    for x in lista:
        tot = tot + x
    return tot/3

print (media())