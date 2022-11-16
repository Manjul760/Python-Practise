""" i = 1, v = 10 ,x = 10 ,l = 50, c = 100 ,d = 500, m = 1000 """

def precidency(a):
    if a == "i":return 1
    elif a == "v":return 1.5
    elif a == "x":return 2
    elif a == "l":return 2.5
    elif a == "c":return 3
    elif a == "d":return 3.5
    elif a == "m":return 4
    else :return -1
    
def value(a):
    if a == "i":return 1
    elif a == "v":return 5
    elif a == "x":return 10
    elif a == "l":return 50
    elif a == "c":return 100
    elif a == "d":return 500
    elif a == "m":return 1000
    else :return -1
    
def find_value_of_roman_number(input_num):
    lenght = len(input_num)
    pos = -1
    repeat = 0
    error_flag = False
    input_num = input_num.lower()
    a = value(input_num[-1])
    count = 1
    for i in range(lenght-1):
        last = input_num[pos]
        second_last = input_num[pos-1]
        
        if value(input_num[pos]) != -1:
            if last == second_last: repeat += 1
            else: repeat = 0
            
            if repeat>2:
                error_flag = True
                print("number repeatation more then 3 not allowed")
                break
            
            if count < 1:
                if repeat==1 and precidency(input_num[pos+1]) > precidency(second_last):
                    error_flag = True
                    print("small number repeatation over big number not allowed")
                    break
                if  precidency(input_num[pos+1]) == precidency(last) and precidency(input_num[pos+1]) > precidency(second_last):
                    error_flag = True
                    print("big number repeatation over small number not allowed")
                    break
                if  precidency(input_num[pos+1]) > precidency(last) > precidency(second_last):
                    error_flag = True
                    print("multiple small number over big number not allowed")
                    break
                if  precidency(input_num[pos+1]) < precidency(last) and precidency(input_num[pos+1]) == precidency(second_last):
                    error_flag = True
                    print("Invalid organization error")
                    break
                if  (type(precidency(second_last)) == float) and (precidency(second_last) == precidency(input_num[pos+1])):
                    error_flag = True
                    print("positional error please try again")
                    break
            
            if ((precidency(second_last) - precidency(last)) < -1):
                error_flag = True
                print("value range problem found")
                break
            
            if  (type(precidency(second_last)) == float) and ((precidency(second_last) - precidency(last)) < 0):
                error_flag = True
                print("positional error")
                break
            
            if  (type(precidency(second_last)) == float) and repeat > 0:
                error_flag = True
                print("invalid number repeatation error")
                break
            
            
            if precidency(last)<=precidency(second_last):  a += value(second_last)
            else: a-= value(second_last)
            pos -= 1
            count-= 1
        else:
            error_flag = True
            print("Please enter roman number values only")
            break

    if error_flag == False: print(a)




while(1):
    print("""\n Roman Numbers are i = 1, v = 5 ,x = 10 ,l = 50, c = 100 ,d = 500, m = 1000 """)
    input_num = input("Enter roman number: ")
    find_value_of_roman_number(input_num)




























