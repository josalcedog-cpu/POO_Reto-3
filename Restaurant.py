class MenuItem:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def total(self):
        return self.price


class Bebida(MenuItem):
    def __init__(self, size, name, price):
        self.size = size
        super().__init__(name, price)


class Entrada(MenuItem):
    def __init__(self, name, price):
        super().__init__(name, price)

    def es_adicion(self):
        adicion = input("¿Desea una adición de (s/n)?: ")
        return adicion


class PlatoPrincipal(MenuItem):
    def __init__(self, name, price):
        super().__init__(name, price)


class Cliente:
    def __init__(self, nombre, n_mesa):
        self.nombre = nombre
        self.n_mesa = n_mesa


class Pedido:
    def __init__(self):
        self.items = []

    def mostrar_cuenta(self):
        for item in self.items:
            print(f"- {item.name}: ${item.price}")

    def agregar(self, item):
        self.items.append(item)
        print(f"[{item.name}] añadido al pedido.")

    def sumar_cuenta(self):
        total = 0
        for item in self.items:
            total += item.total()
        return total

    def hay_descuento(self, total):
        total_desc = total * 0.2
        return total - total_desc


def main():
    print("Buenas tardes\nBienvenido a la Fonda Chill, me recuerda su nombre sr/a...\n")
    nombre = input("> ")
    print(f"Listo, sr/a {nombre} su mesa es la n°1 ")
    
    cliente1 = Cliente(nombre, 1)
    pedido = Pedido()
    
    print("Sr/a en el dia de hoy le ofrecemos las siguientes entradas:")
    print(" 1.Ensalada Roja\n 2.Porcion de auyama\n")
    print(f"Que opcion le gustaria sr/a {nombre}, ¿la opcion 1 o 2?")

    while True:
        try:
            op_ent = int(input())
            if op_ent == 1:
                print(f"Listo sr/a {nombre}, Ensalada roja pues.")
                pedido.agregar(Entrada("Ensalada roja", 7000))
                break
            elif op_ent == 2:
                print(f"Listo sr/a {nombre}, Auyama entonces.")
                pedido.agregar(Entrada("Auyama", 100000))
                break
            else:
                print("Esa opcion no esta en el menu, sea serio/a.")
        except ValueError:
            print("Solo introduzca los números 1 o 2.")

    while True:
        try:
            print("De principal le ofrecemos:\n 1.Cocido Boyacense\n 2.Changua\n Cual desea?")
            op_princ = int(input())
            if op_princ == 1:
                print("mmm, listo el cocido entonces.")
                pedido.agregar(PlatoPrincipal("Cocido Boyacense", 1000000))
                break
            elif op_princ == 2:
                print(f"Changuita pues...\n Excelente gusto Dr/a {nombre}")
                pedido.agregar(PlatoPrincipal("Changua", 20000))
                break
            else:
                print("Ya en serio.\n¿Cual opcion sr/a?")
        except ValueError:
            print("Solo introduzca los números 1 o 2.")

    while True:
        try:
            print("Finalmente le ofrecemos de bebida:")
            print(" 1. Jugo de tomate de arbol calientico en leche\n 2.Jugo de Borojo ")
            op_beb = int(input())
            if op_beb == 1 or op_beb == 2:
                beb_size = input("¿Pequeño o grande la bebida veci? ").strip().lower()
                if beb_size == "pequeño":
                    if op_beb == 1:
                        print("Increible.\nJugo de Tomate entonces...")
                        pedido.agregar(Bebida("pequeño", "Jugo de Tomate", 7000))
                    elif op_beb == 2:
                        print("Borojo entonces veci.")
                        pedido.agregar(Bebida("pequeño", "Jugo de Borojo", 10000))
                    break
                elif beb_size == "grande":
                    if op_beb == 1:
                        print("Increible.\nJugo de Tomate entonces...")
                        pedido.agregar(Bebida("grande", "Jugo de Tomate", 10000))
                    elif op_beb == 2:
                        print("Borojo entonces veci.")
                        pedido.agregar(Bebida("grande", "Jugo de Borojo", 130))
                    elif op_beb == 2:
                        print("Borojo entonces veci.")
                        pedido.agregar(Bebida("grande", "Jugo de Borojo", 13000))
                    break
                else:
                    print("Elija los valores que se le han indicado.")
            else:
                print("Esa opcion no esta en el menu, sea serio/a.")
        except ValueError:
            print("Elija los valores numéricos que se le han indicado.")

    print("\n\t---------------------")
    print("\tFACTURA\n\tLA FONDA CHILL")
    print("\t---------------------")
    print(f"Cliente: {cliente1.nombre} | Mesa: {cliente1.n_mesa}")
    print("\nDetalle de su orden:")

    pedido.mostrar_cuenta()

    total_total = pedido.sumar_cuenta()
    print(f"\nSubtotal: ${total_total}")

    desc = input("\n¿Usted es estudiante o profesor de la Universidad Nacional? (si/no)\n> ")
    if desc.strip().lower() == "si":
        total_final = pedido.hay_descuento(total_total)
        print(f"EL TOTAL DE SU FACTURA (con 20% de decuento) ES: ${total_final}")
    else:
        print(f"EL TOTAL DE SU FACTURA ES: ${total_total}")


if __name__ == "__main__":
    main()
