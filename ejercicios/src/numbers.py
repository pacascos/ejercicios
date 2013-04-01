'''
Created on 28/03/2013

@author: cascos


1 one
2 two
3 

para numeros de 0 a 20 tirar de diccionario
para numeros de 2 cifras mayores de 20:
identificar la decena de diccionario y concatenar las unidades (si distinto de cero)
par los de tres cifras
identificar la centena y concatenar "hundred"
para la decenas+unidades tirar de lo mismo de antes y concatenar


'''

FIRST_TEN = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"] 
SECOND_TEN = ["ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"]
OTHER_TENS = ["twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"]
HUNDRED = "hundred"

def checkio(number):
    textoSalida = ''
#    print('-------')
#    print ('numero:',number)
    numberStr = str(number)
#    print (numberStr.rjust(3,'0'))
    centenas, decenas, unidades = numberStr.rjust(3, '0')
   
#    print ('unidades: ', unidades)
#    print ('decenas: ', decenas)
#    print ('centenas: ' ,centenas)
    
    veintePrimeros = FIRST_TEN + SECOND_TEN
    if number < 20:
#        print (veintePrimeros[number])
        textoSalida = veintePrimeros[number]
    elif len(numberStr) == 2:
#        print ('mas de 20 y dos cifras:',int(numberStr[0]))
        textoSalida = (OTHER_TENS[int(numberStr[0]) - 2]) 
        if unidades != '0':
#            print  (veintePrimeros[int(unidades)])
            textoSalida = textoSalida + ' ' + (veintePrimeros[int(unidades)])
    else:
#        print(FIRST_TEN[int(centenas)] + " " + HUNDRED + checkio(int(decenas+unidades)))
#        print((decenas+unidades))
        if int(decenas + unidades) == 0:
            textoSalida = (FIRST_TEN[int(centenas)] + " " + HUNDRED)
        else:
            textoSalida = (FIRST_TEN[int(centenas)] + " " + HUNDRED + ' ' + checkio(int(decenas + unidades)))
    return textoSalida
        

#    return 'string representation of n'

if __name__ == '__main__':
    
    print (checkio(900))


'''
    assert checkio(4) == 'four', "First"
    assert checkio(133) == 'one hundred thirty three', "Second"
    assert checkio(12)=='twelve', "Third"
    assert checkio(101)=='one hundred one', "Fifth"
    assert checkio(212)=="two hundred twelve", "Sixth"
    assert checkio(40)=='forty', "Seventh, forty - it is correct"

'''
