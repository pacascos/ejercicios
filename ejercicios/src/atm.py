# Withdraw without any incident 
# 120 - 10 - 0.5 - 1% = floor(109.4) = 109
# 109 - 20 - 0.5 - 1% = floor(88.3) = 88
# 88 - 30 - 0.5 - 1% = floor(57.2) = 57

def tengoSaldo(saldo, retirar):
    return (saldo > (retirar + 0.5 + (retirar * 0.01)))

def esDivisible(valor, divisor):
    return (valor // divisor == valor / divisor)


def checkio(data):
    balance, withdrawal = data
    balance = data[0]
    withdrawal = data[1]
    for i in range(0, len(withdrawal)):
        if tengoSaldo(balance, withdrawal[i]) and esDivisible(withdrawal[i], 5) and withdrawal[i] > 0:
            print ("descuento ", withdrawal[i] * 0.01)
            print(balance - withdrawal[i] - 0.5 - (withdrawal[i] * 0.01))
            balance = round(balance - withdrawal[i] - 0.5 - (withdrawal[i] * 0.01))

    return (balance)

if __name__ == '__main__':
    assert checkio([120, [10 , 20, 30]]) == 57, 'First'
   

    # With one Insufficient Funds, and then withdraw 10 $
    assert checkio([120, [200 , 10]]) == 109, 'Second'

    # with one incorrect amount
    assert checkio([120, [3, 10]]) == 109, 'Third'

    assert checkio([120, [200, 119]]) == 120 , 'Fourth'

    assert checkio([120, [120, 10, 122, 2, 10, 10, 30, 1]]) == 56, "It's mixed all base tests"
    
    print(checkio([100, [90, 3]]))
    print('All Ok')
