from turtle import color
import numpy as np
import sys
import keyboard
import pandas as pd

def generate_classification_array(y,output_class):  value = np.zeros((len(y),output_class));value[list(range(len(value))),y]=1;return value


class neuron_layer:

    def __init__(self,input_layer_number:int,number_of_neurons:int) -> None:
        self.weight = np.random.randn(number_of_neurons,input_layer_number)
        self.bias = np.zeros((number_of_neurons,1))
        self.alpha = 0.1;self.__x = [];self.__y = []


    def input_data(self,xdata:list,ydata:list) -> None:
        if len(xdata) != len(ydata):print("Data input error length doesnt match");sys.exit(0)
        if type(xdata[0]) == list:
            for idx,each in enumerate(xdata):
                if len(each) != len(self.weight[0]):print(f"Data input error in x weight doesnt match near index {idx}");sys.exit(0)
        else:
            if np.array(xdata).shape == (len(xdata),):xdata = np.array(xdata).reshape(len(xdata),1)
            for idx,each in enumerate(xdata):
                if len(each) != len(self.weight[0]):print(f"Data input error in x weight doesnt match near index {idx}");sys.exit(0)

        self.__x = np.array(xdata)
        if type(ydata[0]) != list:
            self.__y = np.array(ydata).reshape(len(ydata),1)
        else:
            length = len(ydata[0])
    
            for each in ydata:
                if len(each) != length:print("data length error in y");sys.exit(0)
            self.__y = np.array(ydata)

    def update_x(self,xdata:list = []):
        if len(xdata) != len(self.__y):print("Data input error length doesnt match");sys.exit(0)
        if type(xdata[0]) == list:
            for idx,each in enumerate(xdata):
                if len(each) != len(self.weight[0]):print(f"Data input error in x weight doesnt match near index {idx}");sys.exit(0)
        else:
            if np.array(xdata).shape == (len(xdata),):xdata = np.array(xdata).reshape(len(xdata),1)
            for idx,each in enumerate(xdata):
                if len(each) != len(self.weight[0]):print(f"Data input error in x weight doesnt match near index {idx}");sys.exit(0)

        self.__x = np.array(xdata)

    def get_x(self) -> list:return self.__x
    def get_y(self) -> list:return self.__y

    def __evaluation_error(self,x):
        empty = []
        if type(x[0]) != list:
            if np.array(x).shape == (len(x),):x = np.array(x).reshape(len(x),1).tolist()
        try:
            for idx,each in enumerate(x): 
                if len(each) != len(self.weight[0]):print(f"Wrong evaluation near index {idx}");sys.exit(0)
        except:print("error data type");sys.exit(0)

        return x


    def evaluate(self,x = []) -> list:
        if len(x)==0:return np.array(np.matmul(self.weight,np.array(self.__x).T)+self.bias).T
        else:return np.array(np.matmul(self.weight,np.array( self.__evaluation_error(x) ).T)+self.bias).T        
    
    def sigmoid(self,x:list = []) -> list:
        if len(x)==0:return np.array(1/(1+np.exp(-self.evaluate())))
        else:return np.array(1/(1+np.exp(-self.evaluate(np.array( x ))))).tolist()

    def Relu(self,x:list =[]) -> list:
        if len(x)==0:return np.array(np.maximum(0,self.evaluate()))
        else:return np.array(np.maximum(0,self.evaluate(x)))
    
    def softmax(self,x:list =[]) -> list:
        if len(x)==0:return np.exp(np.clip(self.evaluate(),-1000,700))
        else:return np.exp(np.clip(self.evaluate(x), -1000,700))

    def softmax_probability_distribution(self,x:list = []): return self.softmax(x)/np.sum(self.softmax(x),axis = 1,keepdims= True)

    def derivative_cross_entropy(self) -> list: return -np.divide(self.__y,np.clip(self.softmax_probability_distribution(),0.000001,1))+np.divide(1 - np.array(self.__y),1 - np.clip(self.softmax_probability_distribution(),0,0.999999))
    def derivative_sigmoid(self) -> list:return np.multiply(self.sigmoid(), 1 - self.sigmoid())
    def derivative_relu(self) -> list:return (self.Relu() >= 0) * 1

    def mul_deriv_sig_error(self)->list:
        error = self.sigmoid() - self.get_y()
        return np.multiply(self.derivative_sigmoid(),error)

    def process_sigmoid(self,iterations:int=50000,xdata:list = [] ,ydata:list = []) -> list|list:
        if len(xdata) == len(ydata) != 0 :self.input_data(xdata,ydata)
        elif len(self.__x) == len(self.__y) == 0:print("error in data input");sys.exit(0)
        print("Process started press q to exit in between")

        for i in range(iterations):
            error = self.sigmoid() - self.get_y()
            RMSE = np.sqrt(np.average(np.square(error))/2)
            print("iterations =",i+1,"loss =",RMSE,end = "\r")
            
            self.bias -= self.alpha * np.average(np.multiply(error,self.derivative_sigmoid()))
            self.weight -= self.alpha * np.matmul(np.multiply(error,self.derivative_sigmoid()).T,self.get_x())/len(self.get_x())
            if RMSE < 0.0000001 or keyboard.is_pressed("q"):break
        print()
        return self.weight,self.bias
    
    def process_evaluate(self,iterations:int=50000,xdata:list = [] ,ydata:list = []) -> list|list:
        if len(xdata) == len(ydata) != 0 :self.input_data(xdata,ydata)
        elif len(self.__x) == len(self.__y) == 0:print("error in data input");sys.exit(0)
        print("Process started press q to exit in between")

        for i in range(iterations):
            error = self.evaluate() - self.get_y()
            RMSE = np.sqrt(np.average(np.square(error))/2)
            print("iterations =",i+1,"loss =",RMSE,end = "\r")
            
            self.bias -= self.alpha * np.average(error)
            self.weight -= self.alpha * np.matmul(np.array(error).T,self.get_x())/len(self.get_x())
            if RMSE < 0.0000001 or keyboard.is_pressed("q"):break
        print()
        return self.weight,self.bias



if __name__ == "__main__":
    data = pd.read_csv("data.csv")
    x =np.array(data["x"].tolist())
    y =data["y"].tolist()
    H = neuron_layer(1,1)
    H.alpha = 0.0001

    print(H.process_evaluate(xdata=x,ydata=y,iterations=5000))
    for each,each1 in zip(H.evaluate(x),y):
        print(each,each1)

    from matplotlib import pyplot as plot
    plot.scatter(x,y)
    plot.plot(x,H.evaluate(x),color="red")
    plot.show()
    

    

    
    




















































