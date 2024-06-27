import random 
import time
random.seed(time.time())

def Prime_test(n,k=100):
    if n in [2,3,5,7]:return True
    if n%2==0 or n<=1:return False

    r,p = n-1,0
    while(r%2==0 and r !=0):  p+=1;r=r//2

    rno = random.randint(2,n-2)
    a_list = [rno]
    
    for _ in range(k):
        if rabin_miller(n,p,r,a_list[len(a_list)-1]):
            while rno in a_list: rno = random.randint(2,n-2)
            a_list.append(rno)
        else: return False
        
    return True

def rabin_miller(n,p,r,rno):
    x=pow(rno,r,n)
    if x ==1 or x== n-1:return True
    for _ in range(p-1):
        x=(x*x)%n
        if x ==1 or x== n-1:return True
    return False


