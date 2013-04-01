def checkio(data):
    'Return True if password strong and False if not'
    unNumero = False
    unaLetra = False
    if len(data) < 10:
        return (False)
    if data == data.upper():
        return (False)
    if data == data.lower():
        return (False)
    for c in data:
        if c.isdigit():
            unNumero = True
        else:
            unaLetra = True
    return (unNumero and unaLetra)
    

    
        
    

if __name__ == '__main__':
    assert checkio('A1213pokl') == False, 'First'
    assert checkio('bAse730onE4') == True, 'Second'
    assert checkio('asasasasasasasaas') == False, 'Third'
    assert checkio('QWERTYqwerty') == False, 'Fourth'
    assert checkio('123456123456') == False, 'Fifth'
    assert checkio('QwErTy911poqqqq') == True, 'Sixth'
    print('All ok')
