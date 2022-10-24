
class hash_tabla:
    #En primer lugar creo un constructor donde se crea la tabla hash.
    def __init__(self):
        self.tabla = [None] * 125

    #Funcion hash
    def funcion_hash(self, value):
        key = 0
        for i in range(0, len(value)):
            key +=ord(value[i])
        return key % 125
    
    #Método para ingresar elementos
    def Insertar_elementos(self, value):
        hash = self.funcion_hash(value)
        if self.tabla[hash] is None:
            self.table[hash] = value
