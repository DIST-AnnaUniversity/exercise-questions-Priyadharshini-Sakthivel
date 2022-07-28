import numpy as np
#input
X=np.array([[0.8,0.5,0],[0.9,0.7,0.3],[1,0.8,0.5],[0,0.2,0.3],[0.2,0.1,1.3],[0.2,0.7,0.8],])
#print(X)
#weight
w=np.array([[0,0,0]])
#print(w)
d=np.array([1,1,1,-1,-1,-1])
c=9
itera=15

def discrete_perceptron(X,d,w,c,itera):
    for i in range(1,iteration):
        print("Iteration",i)
        print("-----------------")
        for j,n in enumerate(X):
            net=np.dot(X[j],np.transpose(w))
            if net>0:
                out=1
            else:
                out=-1
            r=(d[j]-out)
            delta_w=c*r*n
            w=w+delta_w
            print(w)
            
discrete_perceptron(X,d,w,c,iteration)
