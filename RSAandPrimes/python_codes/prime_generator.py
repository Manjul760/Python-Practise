import random 
import time
from prime_test import Prime_test
from os.path import dirname,realpath,join
current_dir = dirname(realpath(__file__))
random.seed(time.time())


if __name__=="__main__":
    power = 7
    p,iter,iter2 = 2**power,1,1

    try:f=open(join(current_dir ,f"primes{power}latest.txt"),"r");[iter,iter2]= f.read().split(",");del f;iter,iter2=eval(iter),eval(iter2)
    except:pass

    while not (pow(16,p-iter-1,p-iter)==1 and Prime_test(p-iter,100)):iter+=2
    print("one done")
    while not (pow(16,p+iter2-1,p+iter2)==1 and Prime_test(p+iter2,100)):iter2+=2
    print("two generated")

    with open(join(current_dir,f"primes{power}latest.txt"),"w") as f:f.write(f"{iter+2},{iter2+2}")
    with open(join(current_dir,f"primes{power}.txt"),"a") as f:f.write(f"2**{power}-{iter}\n2**{power}+{iter2}\n")
