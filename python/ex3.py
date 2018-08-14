def idade():
    a=int(input("Fala sua idade: "))
    while a < 1:
        a=int(input("idade invalida, ta querendo me fuder?"))
    if a <= 20:
        res = "Jovem"
    elif a >20 and a <=60:
        res = "Adulto"
    else:
        res = "Velho"
    return res

print (idade())