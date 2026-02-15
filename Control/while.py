i = 0  #Le asignamos el valor inicial a variable o constante i 

while i < 10:  #En el bucle while le damos la instrucción que inicie con la variable i que vale 0 y que se repita hasta que sea menor a 10
    i += 1  #Sumamos 1 antes de imprimir. Por eso el primer numero que vas a ver va ser el 1 y el ultimo el 10
    if i == 5:
        continue #Saltamos el print cuando i vale 5 y volvemos arriba 
    print(i) # imprime la incrementación del contador en cada vuelta
else:  # imprimase una vez el resultado sea verdadero
    print("i dejo de ser menor a 10")