import neuron
import generate_data as gd
import Read_HL_1 as Read
import numpy as np

x =[[1, 1], [1, 0], [0, 1], [0,0]]
y =[1, 0,0, 1]

H1 = neuron.neuron_layer(2,2)
O = neuron.neuron_layer(2,1)


H1.bias = Read.H1_bias_data
H1.weight = Read.H1_weight_data
O.bias = Read.O_bias_data
O.weight = Read.O_weight_data


if __name__ =="__main__":
    for w,p in zip( O.sigmoid( H1.sigmoid(  x  )  )    ,y):
        print(np.round(w,0),p)


















































































