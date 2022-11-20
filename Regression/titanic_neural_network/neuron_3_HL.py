import numpy as np
import keyboard
import generate_data as gd
import Read_HL_3_docx as Read
import neuron


def write_in_file():
    f = open("neuron_3_HL.docx","w")
    f.write("x ="+str(np.array(x).tolist())+
            "\ny ="+str(np.array(y).tolist())+ 
            "\nH1.bias ="+str(np.array(H1.bias).tolist())+
            "\nH1.weight ="+str(np.array(H1.weight).tolist())+
            "\nH2.bias ="+str(np.array(H2.bias).tolist())+
            "\nH2.weight ="+str(np.array(H2.weight).tolist())+
            "\nH3.bias ="+str(np.array(H3.bias).tolist())+
            "\nH3.weight ="+str(np.array(H3.weight).tolist())+
            "\nO.bias ="+str(np.array(O.bias).tolist())+
            "\nO.weight ="+str(np.array(O.weight).tolist()))
    f.close()


x = gd.x_test_data
y = gd.y_test_data

# x= [[1,1],[1,0],[0,1],[0,0]]
# y = [1,0,0,1]

input_layer = 8
Hidden_layer_1 = Hidden_layer_2 = Hidden_layer_3 = 32
Output_layer = 1

H1 = neuron.neuron_layer(input_layer,Hidden_layer_1)
H2 = neuron.neuron_layer(Hidden_layer_1,Hidden_layer_2)
H3 = neuron.neuron_layer(Hidden_layer_2,Hidden_layer_3)
O = neuron.neuron_layer(Hidden_layer_3,Output_layer)

H1.input_data(x,y)
H2.input_data(H1.sigmoid(),y)
H3.input_data(H2.sigmoid(),y)
O.input_data(H3.sigmoid(),y)

alpha = 2.5

H1.alpha =alpha 
H2.alpha = alpha
H3.alpha = alpha
O.alpha = alpha

H1.bias = Read.H1_bias_data
H1.weight = Read.H1_weight_data
H2.bias = Read.H2_bias_data
H2.weight = Read.H2_weight_data
H3.bias = Read.H3_bias_data
H3.weight = Read.H3_weight_data
O.bias = Read.O_bias_data
O.weight = Read.O_weight_data


for i in range(5000000000000): 

    error = O.sigmoid() - O.get_y()
    RMSE = np.sqrt(np.average(np.square(error),axis=0)/2)

    hit = 0
    for w,p in zip(O.sigmoid(),y):
        if w > 0.5 and p == 1:hit+=1
        if w < 0.5 and p == 0:hit+=1

    print(i,RMSE,round(hit*100/len(y),2),"%-----",end = "\r")

    H1.bias -= H1.alpha * np.array(np.average(np.multiply(np.multiply(np.multiply(np.multiply(O.derivative_sigmoid(),H3.derivative_sigmoid()),H2.derivative_sigmoid()),H1.derivative_sigmoid()),error),axis=0)).reshape(len(H1.bias),1)
    H1.weight -= H1.alpha * np.matmul(np.array(np.multiply(np.multiply(H1.derivative_sigmoid(),np.multiply(np.multiply(O.derivative_sigmoid(),H3.derivative_sigmoid()),H2.derivative_sigmoid())),error)).T,H1.get_x())/len(H1.get_x())

    H2.bias -= H2.alpha * np.array(np.average(np.multiply(np.multiply(np.multiply(O.derivative_sigmoid(),H3.derivative_sigmoid()),H2.derivative_sigmoid()),error),axis=0)).reshape(len(H2.bias),1)
    H2.weight -= H2.alpha * np.matmul(np.array(np.multiply(np.multiply(H2.derivative_sigmoid(),np.multiply(O.derivative_sigmoid(),H3.derivative_sigmoid())),error)).T,H2.get_x())/len(H2.get_x())

    H3.bias -= H3.alpha * np.array(np.average(np.multiply(np.multiply(O.derivative_sigmoid(),H3.derivative_sigmoid()),error),axis=0)).reshape(len(H3.bias),1)
    H3.weight -= H3.alpha * np.matmul(np.array(np.multiply(np.multiply(H3.derivative_sigmoid(),O.derivative_sigmoid()),error)).T,H3.get_x())/len(H3.get_x())

    O.bias -=  O.alpha * np.average(np.multiply(O.derivative_sigmoid(),error),axis=0)
    O.weight -= O.alpha * np.matmul(np.array(np.multiply(O.derivative_sigmoid(),error)).T,O.get_x())/len(O.get_x())

    H2.update_x(H1.sigmoid())
    H3.update_x(H2.sigmoid())
    O.update_x(H3.sigmoid())

    if keyboard.is_pressed("p + 3")  or RMSE < 0.0001:break
    if keyboard.is_pressed("w +3"):write_in_file()
    
write_in_file()
print()
# hit = 0
# i=0
# for w,p in zip(O.sigmoid(),y):
#     print(p,np.round(w,3),end=",");i+=1
#     if i % 9 == 0:print()
    


