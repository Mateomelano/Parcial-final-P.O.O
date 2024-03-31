class Vista():
    def __init__(self):
        pass

    def menu(self):
        a = 1
        while a == 1:
            try:
                print("Digite 1 para consultar los pacientes mayores de edad")
                print("Digite 2 para registrar el peso actual de un paciente")
                print("Digite 3 para calcular el peso ideal de un paciente")
                print("Digite 4 para calcular diferencia de peso de un paciente")
                print("Digite 5 para salir")
                return int(input("Digite la opcion\n"))
            except ValueError:
                print("Dato no valido")
                a = 1
    
    def pedir_peso_act(self):
        a = 1
        while a == 1:
            try:
                return int(input("Digite el peso actual del paciente"))
            except ValueError:
                print("Dato no valido")
                a = 1

    def mostrar_dato(self,x):
        print(x)
    def pedir_paciente(self):
        return str(input("Digite el nombre del paciente"))
    def error_peso_actual(self):
        print ("Esta paciente no tiene registrado su peso acutal")
    def peso_exito(self):
        print("Se registro el peso con exito")
    def aumento(self):
        print("Aumento de peso")
    def disminuyo(self):
        print("Disminuyo de peso")
    def igual(self):
        print("Su peso es el mismo")
    def error_nombre(self):
        print("No se encontro el nombre del paciente")
    def archivo_error(self):
        print("No se encontro el archivo")