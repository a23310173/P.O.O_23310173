#Creacion de la clase Jugador
class Jugador:
    #En python no hay posibilidad de crear atributos privados directamente como en C
    # por fines practicos lo dejare asi
    def __init__(self):
        self.registro_en_liga = True
    edad = int(input("Ingrese la edad del jugador: "))
    pie_dominante = str(input("Su jugador es Izquierdo o Derecho: "))
    posicion = [0, 0]

    #Se define el metodo de la clase
    def mover(self, metros, posicion_x, posicion_y):
        print("\nInicia el movimiento del jugador")
        movimiento = float(metros)
        boton = True
        while boton:
            if movimiento <= 0.0:
                print("\nNo pusiste una cantidad en metros")
                new = float(input("Ingresa una nueva cantidad: "))
                if new >= 0.0:
                    movimiento = new
                    boton = False
            else:
                print("\nMovimiento valido.")
                boton = False
            x = posicion_x
            y = posicion_y
            new_x = x + movimiento
            new_y = y + movimiento
            print(f"\nLa nueva posicion del eje x es: {new_x}")
            print(f"La nueva posicion del eje y es: {new_y}")

#Creacion de una subclase Portero, que hereda los atributos y metodos de la clase Jugador
#En este caso solo se estaria heredando el registro en liga y el pie dominante
class Portero(Jugador):
    edad = int(input("\nIngrese la edad del portero: "))
    #Creacion de un metodo especial para el portero
    def despejar(self, fuerza, posicion_x, posicion_y):
        print("\nInicio del despeje del portero.")
        despeje = int(fuerza)
        boton = True
        if despeje <= 0:
            print("\nNo ingresaste una cantidad de fuerza del 1-100")
            new = int(input("Ingrese una nueva cantidad de fuerza: "))
            if new >= 0:
                despeje = new
                boton = False
        else:
            print("\nDespeje realizado con exito")
            x = posicion_x
            y = posicion_y
            new_x = x + fuerza
            new_y = y + fuerza
            print(f"El despeje llego a {new_x}, {new_y}")


jugador = Jugador()
print(Jugador.pie_dominante)
jugador.mover(15, 0, 0)
portero = Portero()
portero.mover(2, 0, 0)
portero.despejar(35, 2, 2)
print(portero.edad)
