def bernstein(cadena):
    #Función hash de Bernstein para cadenas
    h = 0
    for caracter in cadena:
        h = h * 33 + ord(caracter)
    return h

#Se pone el % para calcular el modulo
hash = bernstein("hola")%10
print(hash)