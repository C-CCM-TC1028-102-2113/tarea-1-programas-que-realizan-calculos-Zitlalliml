def main():
    #escribe tu código abajo de esta línea
    
    #Leer los datos
    print('Dame el número de mensajes: ')
    m = int(input())
    print('Dame el número de megas:')
    mg = float(input())
    print('Dame el número de minutos: ')
    min = int(input())

    tm =float( round(m * 0.80,4))
    tmg =float( round(mg * 0.80,4))
    tmin =float( round(min * 0.80,4))
    t= float(tm + tmg + tmin)
    print ('El costo mensual es: ' + str(t))

    pass


if __name__ == '__main__':
    main()
