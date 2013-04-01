'''
Created on 01/04/2013

@author: cascos
'''
class punto:
    def __init__(self,x,y):
        self.x = x
        self.y = y
    def __str__(self):
        return "("+str(self.x)+","+str(self.y)+")"
    
class linea:
    def __init__(self, p0, p1):
        self.p0 = p0
        self.p1 = p1
        self.A = p1.x - p0.x
        self.B = p1.y - p0.y
        self.C = p1.x*p0.y - p0.x*p1.y
    def intersecta(self, otro):
        det = self.A*otro.B - otro.A*self.B
        x = otro.A*self.C-self.A*otro.C
        y = otro.B*self.C-self.B*otro.C
        return punto(x/det,y/det)
    def __str__(self):
        return str(self.p0) + "," + str(self.p1)
    
def checkio(data):
    xw1, yw1 = data[0]
    xw2, yw2 = data[1]
    xa, ya = data[2]
    xb, yb = data[3]
    
    meta = linea(punto(xw1,yw1),punto(xw2,yw2))
    bala = linea(punto(xa,ya),punto(xb,yb))
    resultado = meta.intersecta(bala)
    print ('------',resultado)
    print ('x: ',xw1,'<=',resultado.x,'<=',xw2,'-->',(xw1 <= resultado.x and resultado.x <= xw2))
    print ('y: ',yw1,'<=',resultado.y,'<=',yw2,'-->',(yw1 <= resultado.y  and resultado.y <= yw2))
    return ((xw1 <= resultado.x and resultado.x <= xw2) and (yw1 <= resultado.y  and resultado.y <= yw2))

    
    
    return True
    
if __name__=="__main__":
    l1 =linea(punto(0,0),punto(2,2))
    l2 =linea(punto(6,0),punto(3,1))  
    #print (l1,l2)
    #print (l1.intersecta(l2))
    assert checkio([[0,0], [0,2], [5,1], [3,1]]) == True, "First"
    assert checkio([[0, 0], [0, 2], [3, 1], [5, 1]]) == False, "Reverse First"
    assert checkio([[0, 0], [2, 2], [6, 0], [3, 1]]) == True, "Second"
    assert checkio([[6, 0], [5, 5], [4, 0], [5, 6]]) == False, "Third"
    assert checkio([[0, 0], [1, 1], [3, 3], [2, 2]]) == True, "Fourth, shot in butt of wall :)"
    assert checkio([[0, 0], [1, 1], [3, 2], [2, 1]]) == False, "Fifth, parallel"
