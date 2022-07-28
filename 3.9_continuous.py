import numpy as np
#-------------------Trainning set--------------------------------------------------------------
X=np.array([[0.8,0.5,0],[0.9,0.7,0.3],[1,0.8,0.5],[0,0.2,0.3],[0.2,0.1,1.3],[0.2,0.7,0.8],])
w=np.array([[0,0,0]])
d=np.array([1,1,1,-1,-1,-1])
c=7
itera=13
l=9

def Continuous_perceptron(X,d,w,c,iteration):
    for i in range(1,iteration):
        print("Iteration",i)
        print("-----------------")
        for j,n in enumerate(X):
            net=np.dot(X[j],np.transpose(w))
            out=(2/(1+np.exp(-l*net)))-1
            r=(d[j]-out)*(1-(out*out))
            delta_w=c*r*n
            w=w+delta_w
            print(w)
    return w
            
w1=Continuous_perceptron(X,d,w,c,iteration)
