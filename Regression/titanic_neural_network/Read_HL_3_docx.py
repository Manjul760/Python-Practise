import numpy as np

f = open("neuron_3_HL.docx","r")
data = f.read().split("\n")

x_data = data[0].split("=")[1].split("],")
for i in range(len(x_data)): x_data[i] = np.float64(x_data[i].replace(" ","").replace("[","").replace("]","").split(",")).tolist()

y_data = np.int0(data[1].split("=")[1].replace(" ","").replace("[","").replace("]","").split(",")).tolist()

H1_bias_data = data[2].split("=")[1].split("],")
for i in range(len(H1_bias_data)): H1_bias_data[i] = np.float64(H1_bias_data[i].replace(" ","").replace("[","").replace("]","").split(",")).tolist()

H1_weight_data = data[3].split("=")[1].split("],")
for i in range(len(H1_weight_data)): H1_weight_data[i] = np.float64(H1_weight_data[i].replace(" ","").replace("[","").replace("]","").split(",")).tolist()


H2_bias_data = data[4].split("=")[1].split("],")
for i in range(len(H2_bias_data)): H2_bias_data[i] = np.float64(H2_bias_data[i].replace(" ","").replace("[","").replace("]","").split(",")).tolist()

H2_weight_data = data[5].split("=")[1].split("],")
for i in range(len(H2_weight_data)): H2_weight_data[i] = np.float64(H2_weight_data[i].replace(" ","").replace("[","").replace("]","").split(",")).tolist()


H3_bias_data = data[6].split("=")[1].split("],")
for i in range(len(H3_bias_data)): H3_bias_data[i] = np.float64(H3_bias_data[i].replace(" ","").replace("[","").replace("]","").split(",")).tolist()

H3_weight_data = data[7].split("=")[1].split("],")
for i in range(len(H3_weight_data)): H3_weight_data[i] = np.float64(H3_weight_data[i].replace(" ","").replace("[","").replace("]","").split(",")).tolist()


O_bias_data = data[8].split("=")[1].split("],")
for i in range(len(O_bias_data)): O_bias_data[i] = np.float64(O_bias_data[i].replace(" ","").replace("[","").replace("]","").split(",")).tolist()

O_weight_data = data[9].split("=")[1].split("],")
for i in range(len(O_weight_data)): O_weight_data[i] = np.float64(O_weight_data[i].replace(" ","").replace("[","").replace("]","").split(",")).tolist()

f.close()