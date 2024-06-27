import random
import time
import math
random.seed(time.time())

def gcd(m,n):
    while n!=0: m,n=n,m%n
    return m


if __name__=="__main__":
    n=(2**1024-8049) * (2**64+13) #4,294,049,777 
    print(f"n={n}")
    while True :

        if n%math.isqrt(n)==0:print(f"{math.isqrt(n)} perfect sqrt") ;break
        r = random.randint(2,n-2)

        if gcd(n,r)!=1:print(f" printed random f={gcd(n,r)} {n//gcd(n,r)}") ;break
        print("random number:",r)

        firstidx=0
        p,m=0,r
        for i in range(2,2*n):#A quantum computer is used to determine the unknown period p of the function fr, N (x) = rx mod N.
            
            if gcd(m+1,n%(m+1))!=1:
                print(f"{m+1} solvable ++++++++++++ {gcd(n,m+1)}",end=" ")
                if firstidx==0:firstidx=i

            elif m>1 and gcd(m-1,n%(m-1))!=1:
                print(f"{m-1} solvable ------------- {gcd(n,m-1)}",end=" ")
                if firstidx==0:firstidx=i
            
            elif gcd(m,n%(m))!=1:
                print(f"{m} solvable 00000000000000 {gcd(n,m+1)}",end=" ")
                if firstidx==0:firstidx=i

            print(end="\r")

            m=(r*m)%n
            print(f"{i} iter", end=" ")
            if m==r:p=i;break
            if firstidx!=0:break
        
        print()
        if firstidx!=0:break
        
        p-=1
        print(f"period={p}  :{p} % 2={p%2} if even continue ie 0")

        # if p%2!=0 :continue #If p is an odd integer, then go back to Step 1. Else move to the next step. 
        #not necessary its to satisfy condition but works with odd and int division

        
        #Since p is an even integer so, (rp/2 – 1)(rp/2 + 1) = rp – 1 = 0 mod N.
        print(f"r({r}) ^ p/2({p//2}) % n({n}) + 1={pow(r,p//2,n)+1} (mod {n})")
        if pow(r,p//2,n)+1==0:continue #if the value of rp/2 + 1 = 0 mod N, go back to Step 1.


        print(f"computing gcd {pow(r,p//2,n)-1}  {gcd(pow(r,p//2,n)+1,n) }")
        d = gcd(n,pow(r,p//2,n)-1) #Compute d = gcd(rp/2-1, N).
        if n%d !=0:print(f"reinitiating {r}");continue
        

        print(f"factors are {d} {n//d}  fidx={firstidx}")
        break

















