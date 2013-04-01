from itertools import combinations
 
def checkio(stones):
    '''
    minimal possible weight difference between stone piles
    '''
    weight = sum(stones)
    min_diff = weight
    for i in range(1, (len(stones) // 2 + 2)):
        for var in combinations(stones, i):
            min_diff = min(min_diff, abs(weight - 2 * sum(var)))
    return min_diff
 
if __name__ == '__main__':
    assert checkio([10, 10]) == 0, 'First, with equal weights'
    assert checkio([10]) == 10, 'Second, with a single stone'
    assert checkio([5, 8, 13, 27, 14]) == 3, 'Third'
    assert checkio([5, 5, 6, 5]) == 1, 'Fourth'
    print ('All is ok')
