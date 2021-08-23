def main():
    #escribe tu código abajo de esta línea
    print('Dame la cantidad de juegos nuevos:')
    n= int(input())
    print('Dame la cantidad de juegos usados:')
    u= int(input())

    t=(n*1000)+(u*350)
    print('El total de la compra es:'+ str(t))

   pass



if __name__ == '__main__':
    main()
