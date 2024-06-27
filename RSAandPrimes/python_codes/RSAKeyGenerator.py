def coprime(a,b):
    c=a%b 
    while c>= 2:  a,b,c = b,c,a%b
    return True if c==1 else False

def modinv(n,i):
    x1,y1,pn = 0,1,n
    while i: q,n,i = n//i,i,n%i;  x1,y1 = y1,x1-q*y1
    while x1<0:x1+=pn
    return x1


if __name__ == "__main__":
    import uuid
    import random
    import time
    import json
    from os import path
    random.seed(time.time())
    id = uuid.uuid4()
    current_dir = path.dirname(path.realpath(__file__))

    prime_power = 1024

    with open(path.join(current_dir ,f"primes{prime_power}.txt"),"r") as f:primes = f.read().rstrip("\n").split("\n");del f
    r1,r2 = random.randint(0,len(primes)-1),random.randint(0,len(primes)-1)
    while r1 == r2:random.randint(0,len(primes)-1)

    p1,p2 = eval(primes[r1]),eval(primes[r2])

    n,t = p1*p2  ,  (p1-1)*(p2-1)
    del r1,r2,primes,p1,p2

    pk,notpk,dict_of_key_pair=0,0,{ "n_power":f"{prime_power*2}","n":f"{n}",  "keys":None }

    r = random.randint(2,t-1)
    for i in range(65537,t):
        if coprime(t,i):
            power_dec = 0;dict_of_key_pair["keys"]={"public":f"{i}","private":f"{modinv(t,i)}"}; break


    with open(path.join(path.join(path.dirname(current_dir),"RSAKeyPair"),f"ID_{id}.json"),"w") as f:
        json.dump(dict_of_key_pair,f)

    print(id)
