
class hash_tabla:
    #En primer lugar creo un constructor donde se crea la tabla hash de un determinado tamaño: tamaño_tab 
    def __init__(self, tamaño_tab):
        self.tamaño_tab = tamaño_tab
        self.tabla = [None] * tamaño_tab

    #Calcula la función hash de una cadena.
    #Recorro la cadena sumando los valores ascii de los elementos de la cadena.
    def funcion_hash(self, cadena):
        llave = 0
        for i in range(0, len(cadena)):
            llave +=ord(cadena[i])
        return cadena % self.tamaño_tab
    
    #Método para ingresar elementos
    def Insertar_elementos(self, value):
        hash = self.funcion_hash(value)
        if self.tabla[hash] is None:
            self.table[hash] = value

alfabeto = [chr(i) for i in range(32, 125)]
#Creo la tabla hash del tamaño de la longitud del alfabeto
A = hash_tabla(len(alfabeto))