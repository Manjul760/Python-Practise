import numpy as np
import neuron
import generate_data as gd
import Read_HL_3_docx as Read

input_layer = 8
Hidden_layer_1 = 32
Hidden_layer_2 = 32
Hidden_layer_3 = 32
Output_layer = 1

H1 = neuron.neuron_layer(input_layer,Hidden_layer_1)
H2 = neuron.neuron_layer(Hidden_layer_1,Hidden_layer_2)
H3 = neuron.neuron_layer(Hidden_layer_2,Hidden_layer_3)
O = neuron.neuron_layer(Hidden_layer_3,Output_layer)

H1.bias = Read.H1_bias_data
H1.weight = Read.H1_weight_data
H2.bias = Read.H2_bias_data
H2.weight = Read.H2_weight_data
H3.bias = Read.H3_bias_data
H3.weight = Read.H3_weight_data
O.bias = Read.O_bias_data
O.weight = Read.O_weight_data

if __name__ == "__main__":
    passenger_id_number = list(range(1,10))
    evaluate_data = gd.specific(passenger_id_number)
    print(  np.round( O.sigmoid( H3.sigmoid( H2.sigmoid(  H1.sigmoid( evaluate_data  )  )  )  ) ,3 )   )
    
