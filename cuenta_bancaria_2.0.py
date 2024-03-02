class Persona:
    def __init__(self, nombre, apellido):
        self.nombre = nombre
        self.apellido = apellido

class Cliente(Persona):
    def __init__(self, nombre, apellido, numero_cuenta, balance=0):
        super().__init__(nombre, apellido)
        self.numero_cuenta = numero_cuenta
        self.balance = balance
    
    def __str__(self):
        return f"Cliente: {self.nombre} {self.apellido}\nBalance de cuenta {self.numero_cuenta}: ${self.balance}"

    def depositar(self, cantidad):
        self.balance += cantidad
        return "Depósito aceptado."

    def retirar(self, cantidad):
        if self.balance >= cantidad:
            self.balance -= cantidad
            return "¡Retiro realizado con éxito!"
        else:
            return "Fondos insuficientes."

def crear_cliente(nombre, apellido, numero_cuenta, balance=0):
    cliente = Cliente(nombre, apellido, numero_cuenta, balance)
    return cliente

def solicitar_datos_cliente():
    nombre = input("Ingrese su nombre: ")
    apellido = input("Ingrese su apellido: ")
    numero_cuenta = input("Ingrese su numero de cuenta: ")
    balance = input("Ingrese su saldo inicial (deje en blanco para 0): ")
    balance = int(balance) if balance else 0
    return nombre, apellido, numero_cuenta, balance

def inicio():
    nombre, apellido, numero_cuenta, balance = solicitar_datos_cliente()
    mi_cliente = crear_cliente(nombre, apellido, numero_cuenta, balance)
    print(mi_cliente)

    while True:
        print("Elija: Depositar (D), Retirar (R), Salir (S)")
        opcion = input().upper()

        if opcion == 'D':
            try:
                cantidad_deposito = int(input("Cantidad a depositar: "))
                mensaje = mi_cliente.depositar(cantidad_deposito)
                print(mensaje)
            except ValueError:
                print("Por favor, introduzca un número válido.")

        elif opcion == 'R':
            try:
                cantidad_retiro = int(input("Cantidad a retirar: "))
                mensaje = mi_cliente.retirar(cantidad_retiro)
                print(mensaje)
            except ValueError:
                print("Por favor, introduzca un número válido.")
        
        elif opcion == 'S':
            print("Gracias por operar con Banco Python")
            break
        else:
            print("Opción no válida. Intente nuevamente.")

        print(mi_cliente) # Muestra el estado actual del cliente

inicio()
