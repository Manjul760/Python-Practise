# Ai consists of alpha beta prubing but can use min max as well which is commented out


from cmath import inf
from tkinter import *
import numpy as np
import random

Symbols = ("O","X")

#goal condition
def state(array:list) -> str:
    
    draw_flag = True
    for each in array:
        if type(each) != str:
            draw_flag = False
            break

    array = np.array(array).reshape(3,3).tolist()
    
    for each in array:
        if (each[0] == each[1] == each[2] == "O") or (each[0] == each[1] == each[2] == "X"): return each[0]
    
    col = list(np.array(array).T.tolist())
    for each in col:
        if (each[0] == each[1] == each[2] == "O") or (each[0] == each[1] == each[2] == "X"): return each[0]
    
    if (array[0][0] == array[1][1] == array[2][2] == "O") or (array[0][0] == array[1][1] == array[2][2] == "X"): return array[0][0]
    
    if (array[0][2] == array[1][1] == array[2][0] == "O") or (array[0][2] == array[1][1] == array[2][0] == "X"): return array[1][1]

    if (draw_flag == True): return "d" 

    return "continue"


#The AI or bot
class AI:  
    def __init__(self)->None: self.first = True; self.me = "O"

    def return_position(self,array:list) -> int: # return position of win index
        count_me = 0
        count_other = 0

        for each in array: # to count number of plots made by player in array
            if each == self.me: count_me += 1
            elif each == Symbols[(Symbols.index(self.me)+1)%2]: count_other += 1
        
        if(state(array) == "d"):return None # if draw return none 
        
        if (self.first) and (count_me != count_other): return None #to check if ai needs to plot or not based on the count of plots by players
        elif (not self.first) and (count_me == count_other): return None  #to check if ai needs to plot or not based on the count of plots by players 

        if (self.first) and (count_me == count_other == 0): return random.choice(list(range(9))) #reduce pointless computation time
        # # return self.recursion_min_max(array,self.me,individual_data=True)  #for min amx algo

        return self.recursion_alpha_beta(array,self.me,individual_data=True) # for alppha beta prubing

    def recursion_min_max(self,array:list,symbol:str,individual_data:bool = False,max:bool = True) -> int: #min max tree searh algo

        Winner = self.me #indicates the symbol used by ai
        loser = Symbols[(Symbols.index(Winner) + 1)%2]

        #final terminal values
        if state(array) == loser:return -1
        elif state(array) == "d":return 0
        elif state(array) == Winner:return 1

        nxt_symbol = Symbols[(Symbols.index(symbol) + 1)%2]

        if individual_data: #for each remaining index min value return
            sum = []
            for idx,each in enumerate(array):
                pseudo_array = array.copy()
                if type(each) == int:
                    pseudo_array[idx] = symbol
                    s = self.recursion_min_max(pseudo_array,nxt_symbol)
                    sum.append([idx,s])     

            print(np.array(sum).T)

            max = np.max(np.array(sum).T[1])
            return_value = np.array(np.array(sum).T[0]).tolist()
            prob = np.array(np.array(sum).T[1]).tolist()

            
            if prob.count(max) == 1: #if only one max value return it else return any random value from max values
                index = prob.index(max)
                return np.array(sum).T[0][index]
            else:
                list_of_return_value = []
                for idx,each in enumerate(prob):
                    if each == max:
                        list_of_return_value.append(idx)

                index = random.choice(list_of_return_value)
                return np.array(sum).T[0][index]

        else:
            
            #maximizer minimizer code combined
            return_value = []
            for idx,each in enumerate(array):
                pseudo_array = array.copy()
                if type(each) == int:
                    pseudo_array[idx] = symbol

                    if max: s = int(self.recursion_min_max(pseudo_array,nxt_symbol,max = False))
                    else: s = int(self.recursion_min_max(pseudo_array,nxt_symbol,max=True))
                    
                    return_value.append(s)

            if max: return np.min(return_value)
            else: return np.max(return_value)
            
        
    def recursion_alpha_beta(self,array:list,symbol:str,individual_data = False,min = True,a:int = -inf,b:int = inf): #alpha bets tree search algo

        Winner = self.me
        loser = Symbols[(Symbols.index(Winner) + 1)%2]

        #return values #terminal values
        if state(array) == loser:
            if not min: return [-1,b]
            else: return [a,-1]

        elif state(array) == "d":
            if not min: return [0,b]
            else: return [a,0]

        elif state(array) == Winner:
            if not min: return [1,b]
            else: return [a,1]

        nxt_symbol = Symbols[(Symbols.index(symbol) + 1)%2]

        if individual_data:#for each index beta values
            sum = []
            for idx,each in enumerate(array):
                pseudo_array = array.copy()
                if type(each) == int:
                    pseudo_array[idx] = symbol
                    s = self.recursion_alpha_beta(pseudo_array,nxt_symbol)
                    sum.append([idx,s[1]])     

            print(np.array(sum).T)

            max = np.max(np.array(sum).T[1])
            return_value = np.array(np.array(sum).T[0]).tolist()
            prob = np.array(np.array(sum).T[1]).tolist()

            
            if prob.count(max) == 1:#if only one index max return dirctly or chose from all indexes
                index = prob.index(max)
                return np.array(sum).T[0][index]
            else:
                list_of_return_value = []
                for idx,each in enumerate(prob):
                    if each == max:
                        list_of_return_value.append(idx)

                index = random.choice(list_of_return_value)
                return np.array(sum).T[0][index]


        else:

            if min:#minimizer code
                alpha = a
                beta = b
                return_value = []
                for idx,each in enumerate(array):
                    pseudo_array = array.copy()
                    if type(each) == int:
                        pseudo_array[idx] = symbol
                        s = self.recursion_alpha_beta(pseudo_array,nxt_symbol,a=alpha,b= beta,min=False)
                        return_value.append(s[0])
                        beta = np.min(return_value)
                        if alpha >= np.min(return_value):break
        
                return [alpha,np.min(return_value)]
            
            else:#maximizer code
                alpha = a
                beta = b
                return_value = []
                for idx,each in enumerate(array):
                    pseudo_array = array.copy()
                    if type(each) == int:
                        pseudo_array[idx] = symbol
                        s = self.recursion_alpha_beta(pseudo_array,nxt_symbol,a = alpha,b = beta)
                        return_value.append(s[1])
                        alpha = np.max(return_value)
                        if np.max(return_value) >= beta:break
                        

                return [np.max(return_value),beta]

    



#basic declaration before starting program        
a = list(range(9))  #array for main program evaluation #game
i = random.choice([0,1]) #index of initial symbol of ai or player
AI_active = False #state of AI
Bot = AI() #AI declaration
once_count = 1  # for frame update when AI initialized


#basic needed functions before declaration acceptable

#button functions to update array
def input0(): #function for button
    global i; i = (i+ 1)%2; a[0] = Symbols[i] ;button_0.configure(text=Symbols[i],state=DISABLED)
    if(state(a)=="O")or(state(a)=="X"):disable_all() #disable button once winner found
    AI_plays(a);update_frame() #update frame based on state of AI

def input1(): #function for button
    global i; i = (i+ 1)%2; a[1] = Symbols[i] ;button_1.configure(text=Symbols[i],state=DISABLED)
    if(state(a)=="O")or(state(a)=="X"):disable_all() #disable button once winner found
    AI_plays(a);update_frame() #update frame based on state of AI

def input2(): #function for button
    global i;i = (i+ 1)%2;a[2] = Symbols[i] ;button_2.configure(text=Symbols[i],state=DISABLED)
    if(state(a)=="O")or(state(a)=="X"):disable_all() #disable button once winner found
    AI_plays(a);update_frame() #update frame based on state of AI

def input3(): #function for button
    global i;i = (i+ 1)%2;a[3] = Symbols[i] ;button_3.configure(text=Symbols[i],state=DISABLED)
    if(state(a)=="O")or(state(a)=="X"):disable_all() #disable button once winner found
    AI_plays(a);update_frame() #update frame based on state of AI

def input4(): #function for button
    global i;i = (i+ 1)%2;a[4] = Symbols[i] ;button_4.configure(text=Symbols[i],state=DISABLED)
    if(state(a)=="O")or(state(a)=="X"):disable_all() #disable button once winner found
    AI_plays(a);update_frame() #update frame based on state of AI

def input5(): #function for button
    global i;i = (i+ 1)%2;a[5] = Symbols[i] ;button_5.configure(text=Symbols[i],state=DISABLED)
    if(state(a)=="O")or(state(a)=="X"):disable_all() #disable button once winner found
    AI_plays(a);update_frame() #update frame based on state of AI

def input6(): #function for button
    global i;i = (i+ 1)%2;a[6] = Symbols[i] ;button_6.configure(text=Symbols[i],state=DISABLED)
    if(state(a)=="O")or(state(a)=="X"):disable_all() #disable button once winner found
    AI_plays(a);update_frame() #update frame based on state of AI

def input7(): #function for button
    global i;i = (i+ 1)%2;a[7] = Symbols[i] ;button_7.configure(text=Symbols[i],state=DISABLED)
    if(state(a)=="O")or(state(a)=="X"):disable_all() #disable button once winner found
    AI_plays(a);update_frame() #update frame based on state of AI

def input8(): #function for button
    global i;i = (i+ 1)%2;a[8] = Symbols[i] ;button_8.configure(text=Symbols[i],state=DISABLED)
    if(state(a)=="O")or(state(a)=="X"):disable_all() #disable button once winner found
    AI_plays(a); update_frame() #update frame based on state of AI

    
def reset(): # to reset everything  
    global i,a,once_count ;i = random.choice([0,1]);a =list(range(9));enable_all();once_count = 1;initial_AI = True
    if AI_active:AI_plays(a);Bot.me = Symbols[i]
    else: i = random.choice([0,1]) 

def Activate_Ai(): #to make ai active
    global AI_active,Bot
    if AI_active == False:
        AI_active = True; AI_or_not_button.configure(text="Vs Human")
        Ai_first.pack(side=RIGHT)
        You_are.pack(side=LEFT,padx=2)
    else:
        AI_active = False; AI_or_not_button.configure(text="Vs AI")
        Ai_first.pack_forget()
        You_are.pack_forget()
    reset()
    update_frame()

def Ai_first_or_not(): #to make ai first or second
    if Bot.first: Bot.first = False; Ai_first.configure(text="AI Second")
    else: Bot.first = True; Ai_first.configure(text="AI First")
    reset()




#main program start

#frame declaration
root = Tk()
root.title("MLproductions")
root.resizable(False,False)

# design of label and button
design_label = Label(root,text="Tic Tac Toe",font="Times 20 bold")
You_are = Label(root,background="black",fg="white") #when ai active shows what the non ai player is
frame = LabelFrame(root,text=Symbols[(i+1)%2]+"'s turn") 
reset_button = Button(root,text="Reset",command=reset) 
Ai_first = Button(root,text="AI First",command=Ai_first_or_not)
AI_or_not_button = Button(root,text="Vs AI",command=Activate_Ai)
button_0 = Button(frame,height=2,width=4,command=input0,font="Times 20 bold",disabledforeground="black")
button_1 = Button(frame,height=2,width=4,command=input1,font="Times 20 bold",disabledforeground="black")
button_2 = Button(frame,height=2,width=4,command=input2,font="Times 20 bold",disabledforeground="black")
button_3 = Button(frame,height=2,width=4,command=input3,font="Times 20 bold",disabledforeground="black")
button_4 = Button(frame,height=2,width=4,command=input4,font="Times 20 bold",disabledforeground="black")
button_5 = Button(frame,height=2,width=4,command=input5,font="Times 20 bold",disabledforeground="black")
button_6 = Button(frame,height=2,width=4,command=input6,font="Times 20 bold",disabledforeground="black")
button_7 = Button(frame,height=2,width=4,command=input7,font="Times 20 bold",disabledforeground="black")
button_8 = Button(frame,height=2,width=4,command=input8,font="Times 20 bold",disabledforeground="black")


#inserting button and label in app
design_label.pack()
frame.pack(padx=0,pady=0)
reset_button.pack(side=RIGHT,padx=1)
AI_or_not_button.pack(side=LEFT,padx=1)
button_0.grid(column=0,row=0)
button_1.grid(column=1,row=0)
button_2.grid(column=2,row=0)
button_3.grid(column=0,row=1)
button_4.grid(column=1,row=1)
button_5.grid(column=2,row=1)
button_6.grid(column=0,row=2)
button_7.grid(column=1,row=2)
button_8.grid(column=2,row=2)



#basic needed functions after declaration acceptable
def disable_all(): #disable all button used during reset and win condition
    update_frame()
    button_0.configure(state=DISABLED)
    button_1.configure(state=DISABLED)
    button_2.configure(state=DISABLED)
    button_3.configure(state=DISABLED)
    button_4.configure(state=DISABLED)
    button_5.configure(state=DISABLED)
    button_6.configure(state=DISABLED)
    button_7.configure(state=DISABLED)
    button_8.configure(state=DISABLED)
    
def enable_all(): #enable all button only used when reset
    update_frame()
    button_0.configure(text="",height=2,width=4,state=ACTIVE)
    button_1.configure(text="",height=2,width=4,state=ACTIVE)
    button_2.configure(text="",height=2,width=4,state=ACTIVE)
    button_3.configure(text="",height=2,width=4,state=ACTIVE)
    button_4.configure(text="",height=2,width=4,state=ACTIVE)
    button_5.configure(text="",height=2,width=4,state=ACTIVE)
    button_6.configure(text="",height=2,width=4,state=ACTIVE)
    button_7.configure(text="",height=2,width=4,state=ACTIVE)
    button_8.configure(text="",height=2,width=4,state=ACTIVE)
    
def update_frame():#update frame for indication for winner and loser or draw
    global once_count

    if state(a) == "continue": frame.configure(text=Symbols[(i+1)%2].upper()+"'s turn")
    elif state(a) == "O" or state(a) == "X": frame.configure(text=state(a).upper()+" is the winner")
    else: frame.configure(text=" It's a draw")

    if AI_active and once_count == 1: You_are.configure(text="You are "+Symbols[(i+1)%2]);once_count = 0
        
def AI_plays(array):# AI returns index to plot in array
    if AI_active == True and state(array) == "continue":
        position = Bot.return_position(array)
        if position == 0: input0() 
        elif position == 1: input1() 
        elif position == 2: input2() 
        elif position == 3: input3() 
        elif position == 4: input4() 
        elif position == 5: input5() 
        elif position == 6: input6() 
        elif position == 7: input7() 
        elif position == 8: input8() 
       
root.mainloop()

