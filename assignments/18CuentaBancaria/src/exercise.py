def main():
    #escribe tu código abajo de esta línea
    print('Dame el saldo del mes anterior:')
    sma = float(input())
    print('Dame los ingresos:')
    i= float(input())
    print('Dame los egresos: ')
    e = float(input())
    print('Dame el número de cheques: ')
    nc = int(input())

    sf= (sma+i-e-(nc*13))*0.925
    print('El saldo final de la cuenta es: ' + str(round(sf, 8)))
    pass

if __name__ == '__main__':
    main()
