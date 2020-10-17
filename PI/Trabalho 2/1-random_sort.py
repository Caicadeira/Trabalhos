import random
lista_exemplo = [7, 3, 1, 4, 5]

listatmp = []
listarandused = []
not_sorted = True
while not_sorted:
    for i in range(0, len(lista_exemplo)):
        rand_value = random.randint(0, len(lista_exemplo) - 1)
        while rand_value in listarandused and len(listarandused) <= len(lista_exemplo):
            rand_value = random.randint(0, len(lista_exemplo) - 1)
        if len(listarandused) <= len(lista_exemplo):
            listarandused.append(rand_value)
    for i in listarandused:
        listatmp.append(lista_exemplo[i])
    total_tested = 0
    for i in listatmp:
        if i + 1 < len(listatmp) and listatmp[i] > listatmp[i]:
            total_tested += 1
    if total_tested == len(listatmp):
        not_sorted = False
    else:
        print("not sorted", listatmp)
        listatmp = []
        listarandused = []
print(listatmp)
