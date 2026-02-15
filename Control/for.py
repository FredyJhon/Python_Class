palabra = "Python"

for letra in palabra:
    print(letra)


adjetivos =["Rica", "Saludable"]
frutas =["Manzana", "Naranja", "Kiwi"]

# for adjetivo in adjetivos:
#     for fruta in frutas:
#         print(fruta, adjetivo)   


for fruta in frutas:
    for adjetivo in adjetivos:
        print(fruta, adjetivo)     

# Manzana Rica
# Naranja Rica
# Kiwi Rica
# Manzana Saludable
# Naranja Saludable
# Kiwi Saludable        

# for fruta in frutas:
#     if fruta == "Naranja":
#        continue
#     print(fruta)
# else:
#     print("Ya hemos terminado el bucle for")



print("------------------------")

#Range

# Comienza desde el numero 0 y termina en el numero que asignemos sin incluirlo
# for i in range(10):
#     print(i)

# for i in range(3,5):
#     print(i)

# for i in range(0,10,2):
#     print(i)


for i in range(10):
    pass


