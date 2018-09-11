"""
Autor: Daniel J. Cespedes E.
Apodo: Yon White
Septiembre 2018
opciones: Apagar, Reiniciar, Ver información del sistema operativo, ver información del kernel, Ver autor (Su nombre y
una pequeña biografía), Ejecutar proyecto 1, salir. Todo lo anteriormente descrito en el proyecto_2, se debe desarrollar
con funciones en bash, con la ayuda de sentencias de decisión if. Siéntase libre de enviar los commit que quiera.
"""
import subprocess
import sys

########################################################################################################################

def apa():

    plataforma = sys.platform

    if plataforma == 'linux':
        subprocess.call("shutdown -h")
    else:
        subprocess.call("shutdown -s")


########################################################################################################################


def reini():
    plataforma = sys.platform

    if plataforma == 'linux':
        subprocess.call("reboot")
    else:
        subprocess.call("shutdown -r")


########################################################################################################################


def sistem():
    pass


########################################################################################################################


def kernel():


    plataforma = sys.platform

    if plataforma == 'linux':
        print('Sin lugar a dudas, donde esté el pingüino que se quite todo lo demás')
    elif plataforma == 'darwin':  # La firma del Mac
        print('Siempre he sentido simpatía por la manzana, se nota dónde hay calidad')
    elif plataforma == 'win32':
        print('Abrid las ventanas, que entre la luz...')
    else:  # Para otros sistemas y variantes de Unix
        print('No me gusta ninguno de los tres; ¿coincides conmigo?')


########################################################################################################################


def autor():
    print("Autor: Daniel J. Cespedes E.")
    print("Apodo: Yon White")
    print("Programador novato(Primer año de estudio en Ingenieria en Informatica)")


########################################################################################################################


def ejecuP_1():

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

    class cl:
        while (True):
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
            elif (p == "f"):
                break

    pass

#########################################################################################################################


def mainn():
    while (True):
        print("Solo se puede con dos numeros")
        print("A) Apagar")
        print("B) Reiniciar")
        print("C) Ver información del sistema operativo")
        print("D) Ver información del kernel")
        print("E) Ver Autor")
        print("F) Calculadora")
        print("G) Salir")
        ps = input("Opcion:")
        ps = ps.lower().strip()

        if (ps == "a"):
            apa()
        elif (ps == "b"):
            reini()
        elif (ps == "c"):
            sistem()
        elif (ps == "d"):
            kernel()
        elif (ps == "e"):
            autor()
        elif (ps == "f"):
            ejecuP_1()
        elif(ps == "g"):
            break
mainn()


########################################################################################################################
