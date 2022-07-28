import numpy as np
X=np.array([[5,7],[7,3],[3,2],[5,4],[0,0],[-1,-3],[-2,3],[-3,0],])
w=np.array([[0,0]])
d=np.array([1,1,1,1,-1,-1,-1,-1])
c=8
iter=10

def discrete_perceptron(X,d,w,c,iter):
    for i in range(1,iter):
        for j,n in enumerate(X):
            print("Iteration",i)
            print("-------------")
            net=np.dot(X[j],np.transpose(w))
            if net>0:
                out=1
            else:
                out=-1
            print("out",out)
            print("d",d[j])
            r=(d[j]-out)
            print("R",r)
            delta_w=c*r*X[j]
            print("del",delta_w)
            w=w+delta_w
            print(w)
            
discrete_perceptron(X,d,w,c,iter)
