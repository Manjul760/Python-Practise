def convert(n,a=""):

    if n < 1:  return a
    elif n < 4: n = n - 1; a = a + "i"
    elif n < 5: n = n - 4; a = a + "iv"
    elif n < 9: n = n - 5; a = a + "v"
    elif n < 10: n = n - 9; a = a + "ix"
    elif n < 40: n = n - 10; a = a + "x"
    elif n < 50: n = n - 40; a = a + "xl"
    elif n < 90: n = n - 50; a = a + "l"
    elif n < 100: n = n - 90; a = a + "xc"
    elif n < 400: n = n - 100; a = a + "c"
    elif n < 500: n = n - 400; a = a + "cd"
    elif n < 900: n = n - 500; a = a + "d"
    elif n < 1000: n = n - 900; a = a + "cm"
    elif n < 4000: n = n - 1000; a = a + "m"
    
    return convert(n,a)
    
print("""\n Roman Numbers are i = 1, v = 5 ,x = 10 ,l = 50, c = 100 ,d = 500, m = 1000 """)
n = int(input("Enter any number: "))
print("The roman number is:",convert(n))

