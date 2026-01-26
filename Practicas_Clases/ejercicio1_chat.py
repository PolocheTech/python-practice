class Cliente():

    def __init__(self, nombre, valor_compra):
        self.nombre = nombre
        self.valor_compra = valor_compra
    
    def calcular_descuento(self):
        descuento_total = 0
        if self.valor_compra >= 200000:
            return self.valor_compra * 0.20
        elif self.valor_compra < 200000:
            return self.valor_compra * 0.05
        else:
            print("Valor ingresado incorrecto")

    def calcular_total_pagar(self):
        descuento = self.calcular_descuento()
        return self.valor_compra - descuento
    
def validar_valor_compra():
    while True:
        try:
            valor = float(input("Ingresa el valor de las compras\n>>> "))
            if valor < 0:
                print("Error: el valor no puede ser negativo.")
            else:
                return valor
        except ValueError:
            print("Error: debes ingresar un número válido.")

def crear_cliente():
    nombre_cliente = str(input("Ingresar tu nombre\n>>> "))
    valor_de_las_compras = validar_valor_compra()
    cliente = Cliente(nombre_cliente, valor_de_las_compras)
    return cliente

def main():
    lista_clientes = []
    
    opcion = input("\nBienvenido desear crear algun cliente? [s/n]\n>>> ").lower()

    if opcion == "s":
        cantidad = int(input("Cuantos clientes desea crear? [1-10]\n>>> "))

        if cantidad < 1 or cantidad > 10:
            print("Cantidad no valida")
            return
        
        for i in range(cantidad):
            print(f"\nCliente #{i + 1}")
            cliente = crear_cliente()
            lista_clientes.append(cliente)

    else:
        print("No se crearon clientes")
        return
    
    print("\n--- RESUMEN DE CLIENTES ---")

    for cliente in lista_clientes:
        descuento = cliente.calcular_descuento()
        total = cliente.calcular_total_pagar()

        print(f"\nCliente: {cliente.nombre}¡")
        print(f"Valor compra: {cliente.valor_compra}")
        print(f"Descuento aplicado: {descuento}")
        print(f"Total a pagar: {total}")

main()