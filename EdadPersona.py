def es_mayor_de_edad(edad, genero):
    if genero.lower() == "mujer":
        if edad >= 18:
            return True
    else:
        if edad >= 21:
            return True
    return False

def main():
    genero = input("Ingrese el género (hombre/mujer): ")
    edad = int(input("Ingrese la edad: "))

    if es_mayor_de_edad(edad, genero):
        print("Es mayor de edad.")
    else:
        print("Es menor de edad.")

if __name__ == "__main__":
    main()
