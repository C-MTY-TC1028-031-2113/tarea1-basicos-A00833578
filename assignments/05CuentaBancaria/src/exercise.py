def main():
    #escribe tu código abajo de esta línea
    pass
    saldo_anterior = float(input("Dame el saldo del mes anterior: "))
    ingresos = float(input("Dame los ingresos: "))
    egresos = float(input("Dame los egresos: "))
    cheques = int(input("Dame el número de cheques: "))
    saldo_actual = saldo_anterior + ingresos - egresos - (cheques * 13)
    saldo_intereses = saldo_actual - (0.075 * saldo_actual)
    print("El saldo final de la cuenta es: " + str(saldo_intereses))

if __name__ == '__main__':
    main()
