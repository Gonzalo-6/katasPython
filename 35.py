#Crea la clase UsuarioBanco
# Representa a un usuario de un banco con su nombre, saldo y si tiene o no cuenta corriente.
# Métodos: retirar_dinero, transferir_dinero, agregar_dinero.
# Código a seguir:
# Inicializar un usuario con nombre, saldo y un indicador (True o False) de cuenta corriente.
# Implementar retirar_dinero para sustraer dinero del saldo, lanzando un error si no es posible.
# Implementar transferir_dinero para transferir dinero desde otro usuario, lanzando un error en caso de fallo.
# Implementar agregar_dinero para aumentar el saldo del usuario.
# Caso de uso:
#  a. Crear dos usuarios: "Alicia" con saldo inicial de 100 y "Bob" con saldo inicial de 50, ambos con cuenta corriente.
#  b. Agregar 20 unidades al saldo de Bob.
#  c. Transferir 80 unidades de Bob a Alicia.
#  d. Retirar 50 unidades del saldo de Alicia.

class UsuarioBanco:
    def __init__(self, nombre, saldo_inicial, cuenta_corriente):
        self.nombre = nombre
        self.saldo = saldo_inicial
        self.cuenta_corriente = cuenta_corriente

    def retirar_dinero(self, cantidad):
        if cantidad > self.saldo:
            raise ValueError("Fondos insuficientes para retirar.")
        self.saldo -= cantidad

    def transferir_dinero(self, otro_usuario, cantidad):
        if cantidad > self.saldo:
            raise ValueError("Fondos insuficientes para transferir.")
        self.retirar_dinero(cantidad)
        otro_usuario.agregar_dinero(cantidad)

    def agregar_dinero(self, cantidad):
        self.saldo += cantidad

if __name__ == "__main__":
    # Caso de uso
    alicia = UsuarioBanco("Alicia", 100, True)
    bob = UsuarioBanco("Bob", 50, True)

    bob.agregar_dinero(20)  # b. Agregar 20 unidades al saldo de Bob
    try:
        bob.transferir_dinero(alicia, 80)  # c. Transferir 80 unidades de Bob a Alicia
    except ValueError as e:
        print(e)

    try:
        alicia.retirar_dinero(50)  # d. Retirar 50 unidades del saldo de Alicia
    except ValueError as e:
        print(e)

    print(f"Saldo de Alicia: {alicia.saldo}")
    print(f"Saldo de Bob: {bob.saldo}")        