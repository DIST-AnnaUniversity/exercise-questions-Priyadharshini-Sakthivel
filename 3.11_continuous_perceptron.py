X=np.array([[0.8,0.5,0],[0.9,0.7,0.3],[1,0.8,0.5],[0,0.2,0.3],[0.2,0.1,1.3],[0.2,0.7,0.8],])
c=8
l=35
def Test_perceptron(X,w,l):
    for j,n in enumerate(X):
            net=np.dot(X[j],np.transpose(w))
            out=(2/(1+np.exp(-l*net)))-1
            if out>0:
                print("Class I for given inputs")
            else:
                print("Class II for given inputs")
Test_perceptron(X,w1,l)
