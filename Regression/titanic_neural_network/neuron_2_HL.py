import numpy as np
import keyboard
import neuron
import generate_data as gd
import Read_HL_2 as Read

def is_prime(input):
    if(input == 1):return False
    elif (input == 3 or input == 2):return True
    if(input%2==0):return False
    n = 4
    for i in range(3,input,2):
        n = (input//i)+1
        if(input%i==0):return False 
        if i>n:break
    return True
list_of_prime = []
index_of_prime = []
# print(is_prime(2**82589933-1))
idx=0
for i in range(0,5000):
    if is_prime(i):
        list_of_prime.append(i)
        index_of_prime.append(idx)
        idx+=1









def write_in_file():
    f = open("neuron_2_HL.docx","w")
    f.write("x ="+str(np.array(x).tolist())+
        "\ny ="+str(np.array(y).tolist())+ 
        "\nH1.bias ="+str(np.array(H1.bias).tolist())+
        "\nH1.weight ="+str(np.array(H1.weight).tolist())+
        "\nH2.bias ="+str(np.array(H2.bias).tolist())+
        "\nH2.weight ="+str(np.array(H2.weight).tolist())+
        "\nO.bias ="+str(np.array(O.bias).tolist())+
        "\nO.weight ="+str(np.array(O.weight).tolist())   )
    f.close()

x = gd.x_test_data
y = gd.y_test_data

input_layer = 8
H1_layer = H2_layer = 64
output_layer = 1

H1 = neuron.neuron_layer(input_layer,H1_layer)
H2 = neuron.neuron_layer(H1_layer,H2_layer)
O = neuron.neuron_layer(H2_layer,output_layer)
 
H1.input_data(x,y)
H2.input_data(H1.sigmoid(),y)
O.input_data(H2.sigmoid(),y)

alpha = 0.23

H1.alpha =alpha
H2.alpha = alpha
O.alpha = alpha

H1.bias = Read.H1_bias_data
H1.weight = Read.H1_weight_data
H2.bias = Read.H2_bias_data
H2.weight = Read.H2_weight_data
O.bias = Read.O_bias_data
O.weight = Read.O_weight_data

for i in range(7000000000000000000000000000):

    error = O.sigmoid() - O.get_y()
    RMSE = np.sqrt(np.average(np.square(error),axis=0)/2)
    
    hit = 0
    for w,p in zip(O.sigmoid(),y):
        if w > 0.5 and p == 1:hit+=1
        if w < 0.5 and p == 0:hit+=1

    print(i,RMSE,round(hit*100/len(y),2),"%-----",end = "\r")

    H1.bias -= H1.alpha * np.array(np.average(np.multiply(np.multiply(np.multiply(O.derivative_sigmoid(),H2.derivative_sigmoid()),H1.derivative_sigmoid()),error),axis=0)).reshape(len(H1.bias),1)
    H1.weight -= H1.alpha * np.matmul(np.array(np.multiply(np.multiply(H1.derivative_sigmoid(),np.multiply(O.derivative_sigmoid(),H2.derivative_sigmoid())),error)).T,H1.get_x())/len(H1.get_x())

    H2.bias -= H2.alpha * np.array(np.average(np.multiply(np.multiply(O.derivative_sigmoid(),H2.derivative_sigmoid()),error),axis=0)).reshape(len(H2.bias),1)
    H2.weight -= H2.alpha * np.matmul(np.array(np.multiply(np.multiply(H2.derivative_sigmoid(),O.derivative_sigmoid()),error)).T,H2.get_x())/len(H2.get_x())

    O.bias -=  O.alpha * np.average(np.multiply(O.derivative_sigmoid(),error),axis=0)
    O.weight -= O.alpha * np.matmul(np.array(np.multiply(O.derivative_sigmoid(),error)).T,O.get_x())/len(O.get_x())

    H2.update_x(H1.sigmoid())
    O.update_x(H2.sigmoid())

    if keyboard.is_pressed("p + 2")  or RMSE < 0.0001:break
    if keyboard.is_pressed("w + 2"):write_in_file()

write_in_file()


