
from ast import Num


class hash_tabla:
    #En primer lugar creo un constructor donde se crea la tabla hash de un determinado tamaño: tamaño_tab 
    def __init__(self, tamaño_tab):
        self.tamaño_tab = tamaño_tab
        self.tabla = [None] * tamaño_tab

    #Calcula la función hash de una cadena.
    #Asigno un valor de la tabla hash a cada caracter
    #Nos basamos en la función de Bernstein, el número 33 es conocido como el número mágico.
    def funcion_hash(self, caracter):
        return ord(caracter) * 33 % self.tamaño_tab
    
    #Método para ingresar elementos
    #Añade en la posición de la tabla hash corresppondiente el elemento.
    def Insertar_elementos(self, valor):
        #Calcula la posición de la tabla
        hash = self.funcion_hash(valor)
        #Si esta posición esta vacía lo añade.
        if self.tabla[hash] is None:
            self.table[hash] = valor

alfabeto = [chr(i) for i in range(32, 125)]
#Creo la tabla hash del tamaño de la longitud del alfabeto
A = hash_tabla(len(alfabeto))
num = A.funcion_hash("A")
print(num)