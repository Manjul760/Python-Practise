import numpy as np
import neuron
import keyboard 

def write_in_file():
    f = open("neuron_1_HL.docx","w")
    f.write("x ="+str(np.array(x).tolist())+"\ny ="+str(np.array(y).tolist())+ "\nH1.bias ="+str(np.array(H1.bias).tolist())+"\nH1.weight ="+str(np.array(H1.weight).tolist())+ "\nO.bias ="+str(np.array(O.bias).tolist())+"\nO.weight ="+str(np.array(O.weight).tolist()))
    f.close()

x =[1,3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]
y =[0, 1, 2, 3,   4,  5,  6,  7,  8,  9,  10,11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23,24]

H1 = neuron.neuron_layer(1,2)
O = neuron.neuron_layer(2,1)

alpha = 0.1

H1.alpha =alpha
O.alpha = alpha

#front prop
H1.input_data(x,y)
O.input_data(H1.sigmoid(),y)


for i in range(50000000000000000000000000):
    #back prop
    error = O.sigmoid() - O.get_y()
    RMSE = np.sqrt(np.average(np.square(error),axis=0)/2)

    hit = 0
    for w,p in zip(O.sigmoid(),y):
        if w > 0.5 and p == 1:hit+=1
        if w < 0.5 and p == 0:hit+=1

    print(i,RMSE,round(hit*100/len(y),2),"%-----",end = "\r")

    H1.bias -= H1.alpha * np.array(np.average(np.multiply(np.multiply(O.derivative_sigmoid(),H1.derivative_sigmoid()),error),axis=0)).reshape(len(H1.bias),1)
    H1.weight -= H1.alpha * np.matmul(np.array(np.multiply(np.multiply(H1.derivative_sigmoid(),O.derivative_sigmoid()),error)).T,H1.get_x())/len(H1.get_x())

    O.bias -=  O.alpha * np.average(np.multiply(O.derivative_sigmoid(),error),axis=0)
    O.weight -= O.alpha * np.matmul(np.array(np.multiply(O.derivative_sigmoid(),error)).T,O.get_x())/len(O.get_x())

    #front prop
    O.update_x(H1.sigmoid())

    if keyboard.is_pressed("p + 1")  or RMSE < 0.0001:break
    if keyboard.is_pressed("w+1"):write_in_file()

write_in_file()

