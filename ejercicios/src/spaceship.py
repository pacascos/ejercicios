
def checkio(offers):
    '''
       the amount of money that Petr will pay for the ride
       
       comprobar que la oferta es menor que el precio
       comprobar que se puede bajar la cantidad que propone cada uno
       mientras oferta > demanda reintentar
      
    '''
    x = offers[0]
    print(offers[0] < offers[2])
    while  offers[0] <= offers[2]:
        if offers[0] + offers[1] > offers[2]:
            print ("salir2 con: ", offers[2])
            x = offers[2]
            break
        else:
            offers[0] = offers[0] + offers[1]
            offers[2] = offers[2] - offers[3]
            x = offers[0]
 
    return x





if __name__ == '__main__':

#    countdown(10)
#    print ( checkio([200,200,500,250]))
    assert checkio([150, 50, 1000, 100]) == 450, 'First'
    assert checkio([150, 50, 900, 100]) == 400, 'Second'
    print ('All is ok')
    
