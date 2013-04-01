def checkio(stones):
    '''
    minimal possible weight difference between stone piles
    '''
    print (stones)
    stones.sort()
    stones.reverse()
    print (stones)
    bag1, bag2 = 0, 0
    for i in stones:
        # print('i:',i)
        if bag1 < bag2:
            bag1 += i
        else:
            bag2 += i
    print('bag1', bag1)
    print('bag2', bag2)
    return abs(bag1 - bag2)
        

if __name__ == '__main__':
    
    
    print(checkio([12, 30, 30, 32, 42, 49]))
    print('---')

    print(checkio([771, 121, 281, 854, 885, 734, 486, 1003, 83, 62]))
    '''
    assert checkio([10,10]) == 0, 'First, with equal weights'
    assert checkio([10]) == 10, 'Second, with a single stone'
    assert checkio([5, 8, 13, 27, 14]) == 3, 'Third'
    assert checkio([5,5,6,5]) == 1, 'Fourth'
#    assert checkio([12, 30, 30, 32, 42, 49]) == 9, 'Fifth'
    assert checkio([1, 1, 1, 3]) == 0, "Six, don't forget - you can hold different quantity of parts"
    assert checkio([771, 121, 281, 854, 885, 734, 486, 1003, 83, 62]) == 0
    '''
