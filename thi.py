
import numpy as np
import matplotlib.pyplot as plt
# %matplotlib inline 
while(True):
    p = float(input('p ='))
    mat = np.matrix([[1-p,p],[p,1-p]],dtype=float)
    def kbl(mtrx):
        a = mtrx[0,0]
        b = mtrx[1,0]
        ret = a*np.log(a/b) + (1-a)*np.log((1-a)/(1-b))
        return ret
    div = kbl(mat)
    temp = 0
    x_arr = []
    arr = []
    while(div>0):
        mat = mat*mat
        div = kbl(mat)
        x_arr.append(temp)
        temp += 1
        arr.append(div)
        # print(temp)
    print(mat)
    plt.plot(x_arr, arr)
    plt.show()


print("p = 0.8\n0.500000 0.499999\n0.499999 0.500000")
print("\n")
print("\n")
print("p = 0.9\n0.499999 0.500000\n0.500000 0.499999")