class Pacientes():
    def __init__(self,nombre = "",edad = 0,dni=0,genero="",peso=0,altura=0,peso_act=0):
        self._nombre = nombre
        self._edad = edad
        self._genero = genero
        self._dni = dni
        self._peso = peso
        self._altura = altura
        self._peso_act = peso_act
    #Getters
    def get_nombre(self):
        return self._nombre
    def get_edad(self):
        return self._edad
    def get_dni(self):
        return self._dni
    def get_genero(self):
        return self._genero
    def get_peso(self):
        return self._peso
    def get_altura(self):
        return self._altura
    def get_peso_act(self):
        return self._peso_act
    #Setters
    def set_nombre(self,x):
        self._nombre = x
    def set_edad(self,x):
        self._edad = x
    def set_dni(self,x):
        self._dni = x
    def set_genero(self,x):
        self._genero = x
    def set_peso(self,x):
        self._peso = x
    def set_altura(self,x):
        self._altura = x
    def set_peso_act(self,x):
        self._peso_act = x

    def paciente():
        return "Paciente" + self._get_nombre() + self.get_dni()


