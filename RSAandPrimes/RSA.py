
def String_to_int(string):
    binpt=""
    for i in string:
        v = bin(ord(i))[2:]
        if len(v)<8:v = ("0"*(8-len(v)))+v
        binpt+=v
    return int(binpt,2)

def Int_to_string(int_input):
    binot = bin(int_input)[2:]
    remaining = len(binot)%8
    if remaining!=0:binot = "0"*(8-remaining)+binot
    return_v = ""
    for i in range(0,len(binot),8): return_v+= chr(int(binot[i:i+8],2))
    return return_v


if __name__ == "__main__":
    import os
    import json


    currrentdir = os.path.dirname(os.path.realpath(__file__))
    with open(os.path.join(os.path.join(currrentdir,"RSAKeyPair"),"ID_42991a37-ca57-4cc9-98fa-1956ec2284e7.json"),"r") as f:data = json.load(f)

    ct = pow(String_to_int("Mancool"),int(data["keys"]["public"]),int(data["n"]))
    print(Int_to_string(ct).__len__())
    print()

    pt= pow(ct,int(data["keys"]["private"]),int(data["n"]))
    print(Int_to_string(pt))




        