def calcular_descuento(precio):
    if precio > 500:
        descuento = precio * 0.10
        return descuento
    else:
        return 0

def main():
    precio_producto = float(input("Ingrese el precio del producto en cordobas: "))
    descuento = calcular_descuento(precio_producto)

    if descuento > 0:
        print(f"Usted tiene derecho para un descuento del 10%.")
        print(f"El descuento aplicado es de ${descuento:.2f} cordobas.")
        precio_con_descuento = precio_producto - descuento
        print(f"El precio final con descuento es de C${precio_con_descuento:.2f} cordobas.")
    else:
        print("Este producto no califica para ningún descuento.")

if __name__ == "__main__":
    main()
