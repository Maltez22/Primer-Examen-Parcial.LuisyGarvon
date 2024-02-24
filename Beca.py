def otorgar_beca(nota):
    if nota > 95:
        return True
    else:
        return False

def main():
    nota_estudiante = float(input("Ingrese la nota del estudiante: "))

    if otorgar_beca(nota_estudiante):
        print("Se le puede otorgar una beca.")
    else:
        print("su nota no cumple con los requisitos para recibir una beca.")

if __name__ == "__main__":
    main()
