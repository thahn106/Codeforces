import math

def check(big,small):
    div = round(big/small)
    if abs(div - (big/small)) < 0.0001:
        return True
    return False


#x0,y0, run, rise
def mid_norm(X,Y):
    return ((X[0]+Y[0])/2, (X[1]+Y[1])/2, X[1]-Y[1], -X[0]+Y[0])

def angle(X,Y,Z):
    v1 = [X[0]-Y[0],X[1]-Y[1]]
    v2 = [Z[0]-Y[0],Z[1]-Y[1]]
    dot = v2[0]*v1[0]+v2[1]*v1[1]
    dot /= math.hypot(*v1)
    dot /= math.hypot(*v2)
    return math.acos(dot)

def main():
    A = [float(x) for x in input().split()]
    B = [float(x) for x in input().split()]
    C = [float(x) for x in input().split()]
    l1 = mid_norm(A,B)
    l2 = mid_norm(B,C)
    x0 = -l1[3]*l1[0]+l1[2]*l1[1]
    y0 = -l2[3]*l2[0]+l2[2]*l2[1]
    #[a,b;  c,d]
    a = -l1[3]
    b = l1[2]
    c = -l2[3]
    d = l2[2]
    det = a*d-b*c
    cx = (x0*d-y0*b)/det
    cy = (-x0*c+y0*a)/det
    #print("{} {}".format(cx,cy))
    O = [cx, cy]
    R2 = (cx-A[0])**2+(cy-A[1])**2
    AOB= angle(A,O,B)
    BOC= angle(B,O,C)
    COA= angle(B,O,C)
    for n in range(3,101):
        adj_angle = 2*math.pi / n
        if check(AOB, adj_angle) and check(BOC, adj_angle) and check(COA, adj_angle):
            print(0.5*n*R2*math.sin(adj_angle))
            return
    while(True):
        i=1

if __name__ == "__main__":
    main()
