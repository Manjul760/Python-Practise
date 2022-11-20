import neuron
import Read_HL_2 as Read
import generate_data as gd
import numpy as np


x = gd.x_test_data
y = gd.y_test_data

H1 = neuron.neuron_layer(8,64)
H2 = neuron.neuron_layer(64,64)
O = neuron.neuron_layer(64,1)

H1.bias = Read.H1_bias_data
H1.weight =Read.H1_weight_data
H2.bias =Read.H2_bias_data
H2.weight =Read.H2_weight_data
O.bias =Read.O_bias_data
O.weight =Read.O_weight_data

hit = 0

for w,p in zip (O.sigmoid( H2.sigmoid(  H1.sigmoid(  x  )  )  )  ,y  ):
    
    if (w[0] > 0.5 and p == 1) or (w[0] < 0.5 and p == 0):print(np.round(w,0),p,"HIT");hit+=1
    else:print(np.round(w,0),p)
    
print(hit/len(y),hit,len(y),len(y) - hit)  

