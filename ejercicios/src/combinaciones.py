'''
Created on 29/03/2013

@author: cascos
'''
import itertools


def sumarLista(lista):
    suma = 0
    for i in range(0, len(lista)):
        suma = suma + lista[i]
    return suma


def checkio(a):
    minimo = 9999
    resultado = [0, 0]
    if len(a) == 1:
        return (a[0])
    if len(a) == 2:
        return (abs(a[0] - a[1]))
    
    if sumarLista(a) % 2 == 0:
        objetivo = sumarLista(a) / 2
    else:
        objetivo = sumarLista(a) // 2
        
    for i in range(1, len(a) + 1):
        for j in itertools.combinations(a, i):
            # print('objetivo: ',objetivo)
            # print('sumarLista: ',sumarLista(j))
            # print('diferencia: ',objetivo - sumarLista(j))
            if (abs(objetivo - sumarLista(j))) < minimo:
                minimo = abs(objetivo - sumarLista(j))
                resultado[0] = j
                resultado[1] = minimo
    return (abs(sumarLista(a) - sumarLista(resultado[0]) - sumarLista(resultado[0])))

                 
             

if __name__ == '__main__':
    print (checkio([10, 1, 6, 18, 47, 36, 38]))
    '''
    assert checkio([10,1,6,18,47,36,38]) == 4, 'First, with equal weights'
    assert checkio([10]) == 10, 'Second, with a single stone'
    assert checkio([5, 8, 13, 27, 14]) == 3, 'Third'
    assert checkio([5,5,6,5]) == 1, 'Fourth'
    assert checkio([12, 30, 30, 32, 42, 49]) == 9, 'Fifth'
    assert checkio([1, 1, 1, 3]) == 0, "Six, don't forget - you can hold different quantity of parts"
    assert checkio([771, 121, 281, 854, 885, 734, 486, 1003, 83, 62]) == 0
    print ('All is ok')
    '''
        
        



'''
1,0,0
1,0,3
1,2,0
1,2,3
0,0,0
0,0,3
0,2,0
0,2,3
'''
    
    
