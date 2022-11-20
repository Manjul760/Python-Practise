import sys
import pandas as pd


"PassengerId,Survived,Pclass,Name,Sex,Age,SibSp,Parch,Ticket,Fare,Cabin,Embarked"

# My_data = pd.read_csv("E:/Python_lab/AI_lab_Manjul/Regression/Mywork/titanic_data/test.csv")
My_data = pd.read_csv("E:/Python_lab/AI_lab_Manjul/Regression/Mywork/titanic_data/train.csv")

y = My_data["Survived"].tolist()

passenger_id = My_data["PassengerId"].tolist()

pclass = My_data["Pclass"].tolist()
name_data = My_data["Name"].tolist()
sex_data = My_data["Sex"].tolist()
age = My_data["Age"].fillna(0).tolist()
sibsp = My_data["SibSp"].tolist()
parch = My_data["Parch"].tolist()
fare = My_data["Fare"].tolist()
cabin_data = My_data["Cabin"].fillna(0).tolist()


sex=[]
for each in sex_data:
    if each[0] == "m":sex.append(-1)
    elif each[0] == "f" :sex.append(1)

name = []
for each in name_data:name.append(ord(each[0]))

cabin = []
for each in cabin_data:
    if each == 0: cabin.append(each)
    else: cabin.append(1)

x=[]
for a,b,c,d,e,f,g,h in zip(pclass,name,sex,age,sibsp,parch,fare,cabin):
    x.append([a,b,c,d,e,f,g,h])

x_test_data = []
y_test_data = []

start = 0
end = len(y)

for i in range(start,end):
    y_test_data.append(y[i])
    x_test_data.append(x[i])


def specific(id = []):
    global passenger_id,x,y
    if type(id) == int:
        for k,w,z in zip(passenger_id,x,y):
            print("survival data for id",k,"is",z)
            if k == id:print(z);return w
        print("data out of bounds");sys.exit(0)
    elif type(id) == list:
        list_x = []
        for k,w,z in zip(passenger_id,x,y):
            if k in id:print("survival data for id",k,"is",z);list_x.append(w)
        if list_x.__len__() == 0:print("data out of bounds");sys.exit(0)
        return list_x
    else:
        print("invalid input")
        sys.exit(0)



if __name__ == "__main__":
    for k,w,z in zip(passenger_id,x,y):
        print(k,w,z)
