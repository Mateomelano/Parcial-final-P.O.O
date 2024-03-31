from Modelo.Pacientes import Pacientes
from Vista.Vista import Vista

class Controlador():
    def __init__(self,modelo=Pacientes(),vista = Vista()):
        self.modelo = modelo
        self.vista = vista
        self.datos = []

    def leer_archivo(self):
        try:
            with open("C:/Users/mateo/OneDrive/Escritorio/parcial.txt","r") as f:
                for line in f:
                    line = line.split(";")
                    paciente = Pacientes(line[0],int(line[1]),int(line[2]),line[3],int(line[4]),int(line[5]))
                    self.datos.append(paciente)
        except FileNotFoundError:
            self.vista.archivo_error()
            

    def menu(self):
        while True:
            a = self.vista.menu()
            if a == 1:
                self.mostrar_mayor_edad()
            if a == 2:
                self.registrar_peso_actual()
            if a == 3:
                self.calcular_peso_ideal()
            if a == 4:
                self.diferencia_peso()
            if a == 5:
                return False


    def mostrar_mayor_edad(self):
        for paciente in self.datos:
            if paciente.get_edad() >= 18:
                self.vista.mostrar_dato(paciente.get_nombre())
    
    def registrar_peso_actual(self):
        a = self.vista.pedir_paciente()
        for paciente in self.datos:
            if paciente.get_nombre() == a:
                paciente.set_peso_act(self.vista.pedir_peso_act())
                self.vista.peso_exito()
                return
        self.vista.error_nombre()
    
    def calcular_peso_ideal(self):
        a = self.vista.pedir_paciente()
        for paciente in self.datos:
            if paciente.get_nombre() == a:
                if paciente.get_peso_act() == 0:
                    self.vista.error_peso_actual()
                    return
                if paciente.get_peso_act() != 0:
                    peso = 0
                    b = paciente.get_altura()/100
                    peso = (paciente.get_peso_act() / (b*2))
                    if peso < 20:
                        print("Esta en su peso ideal")
                    if peso >= 20 and peso <= 25:
                        print("La persona esta por debajo de su peso ideal")
                    if peso > 25:
                        print("La persona tiene sobrepeso")
                    return
        self.vista.error_nombre()

    def diferencia_peso(self):
        a = self.vista.pedir_paciente()
        for paciente in self.datos:
            if paciente.get_nombre() == a:
                if paciente.get_peso_act == 0:
                    self.vista.error_peso_actual()
                    return
                if paciente.get_peso_act() != 0:
                    if paciente.get_peso_act() > paciente.get_peso():
                        self.vista.aumento()
                    if paciente.get_peso_act() < paciente.get_peso():
                        self.vista.disminuyo()
                    if paciente.get_peso_act() == paciente.get_peso():
                        self.vista.igual()
                    return
        self.vista.error_nombre()
 
        


 