'''
Created on 29/03/2013

@author: cascos
'''

def pinta(data):
    print('----')
    for i in data:
        print(i)
    print('----')
    
def rotate(l):
    b = zip(*l[::-1])   
    lista = [] 
    for i, en in enumerate(b):
        lista.append(list((en)))
    return lista

def cadenaLista(t):
    r = [[], [], [], []]
    for i in range(0, len(t)):
        for j in t[i]:
            r[i].append(j)
    return(r)    


def checkio(input_data):
    'Return password of given cipher map'
    respuesta = ''
    clave, mensaje = input_data
    clave = (cadenaLista(clave))
    mensaje = (cadenaLista(mensaje))
    for x in range(0, 4):
        for i in range (0, len(clave)):
            for j in range (0, len(clave[i])):
                if clave[i][j] == 'X':
                    respuesta += mensaje[i][j]
        clave = rotate(clave)
    return (respuesta)
                
        



if __name__ == '__main__':
    
    # a = [1,0,0,0],[1,0,0,0],[0,0,0,0],[0,0,0,0]

    # print(cadenaLista(['X...','..X.','X..X','....']));
    # pinta(a)
    # pinta(rotate(a))
    
    print(checkio([[
    'X...',
    '..X.',
    'X..X',
    '....'], [
    'itdf',
    'gdce',
    'aton',
    'qrdi']])) 



    
    '''
    assert checkio([[
    'X...',
    '..X.',
    'X..X',
    '....'],[
    'itdf',
    'gdce',
    'aton',
    'qrdi']]) == 'icantforgetiddqd', 'First'

    assert checkio( [[
    '....',
    'X..X',
    '.X..',
    '...X'],[
    'xhwc',
    'rsqx',
    'xqzz',
    'fyzr']]) == 'rxqrwsfzxqxzhczy', 'Second'
    print('All ok')
    '''
