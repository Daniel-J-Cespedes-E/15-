"""
Autor: Daniel J. Cespedes E.
Apodo: Yon White
Septiembre 2018
"""

def sum():
    n1 = float(input("N1:"))
    n2 = float(input("N2:"))
    op_s = round(n1 + n2)
    print("resultado", op_s)
    print("--------------------------------------------------")


def res():
    n1 = float(input("N1:"))
    n2 = float(input("N2:"))

    op_r = round(n1 - n2)
    print("resultado", op_r)
    print("--------------------------------------------------")


def div():
    n1 = float(input("N1:"))

    n2 = float(input("N2:"))

    op_d = round(n1 / n2)
    print("resultado", op_d)
    print("--------------------------------------------------")


def mul():
    n1 = float(input("N1:"))
    n2 = float(input("N2:"))
    op_m = round(n1 * n2)
    print("resultado", op_m)
    print("--------------------------------------------------")

def ele():
    n1 = float(input("N1:"))
    n2 = float(input("N2:"))
    op_e = round(n1 ** n2)
    print("resultado", op_e)

    print("--------------------------------------------------")


def main ():

    while(True):
        print("Solo se puede con dos numeros")
        print("A) Sumar")
        print("B) Restar")
        print("C) Dividir")
        print("D) Multiplicar")
        print("E) Elevar")
        print("F) Salir")
        p = input("Opcion:")
        p = p.lower().strip()

        if (p == "a"):
            sum()
        elif (p == "b"):
            res()
        elif (p == "c"):
            div()
        elif (p == "d"):
            mul()
        elif (p == "e"):
            ele()
        elif(p == "f"):
            break
main()