def main():
    #escribe tu código abajo de esta línea
    print('Dame el número de palabras:')
    p= int(input())
    p1= (475 / p)

    if p1 < 1:
        t1 =(p // 475)
        t2= ((t1 + 1) * 60)* 0.90
        print('El costo de la publicación es:' + str(round(t2,4 )))
    else:
        t3 = 60*0.90
        print('El costo de la publicación es: ' + str(round(t3,4 )))
    pass


if __name__ == '__main__':
    main()
