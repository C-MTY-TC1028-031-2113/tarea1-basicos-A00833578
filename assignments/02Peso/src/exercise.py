def main():
    #escribe tu código abajo de esta línea
    pass
    pesoi = float(input("Dame el peso inicial en kg: "))
    pesof = float(input("Dame el peso final en kg: "))
    meses = int(input("Dame la cantidad de meses: "))
    pesom = (pesoi - pesof) / meses
    print("Lo que debes bajar por mes es: " + str(pesom) + str(" kg"))

if __name__ == '__main__':
    main()
