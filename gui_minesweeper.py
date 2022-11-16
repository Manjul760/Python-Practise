from tkinter import *
import random
import numpy as np
import math

class BFS:
    def __init__(self,input,search_sides) -> None:
        self.queue = []
        self.search_sides = search_sides
        if input == []:print("empty list")
        else: self.input = input;self.queue.append(self.input[0])
        self.visited = []
        self.final_answer = []
        self.continue_flag = True

    def __main_process(self):
        global Grid_size
        if self.input == []:...
        else:
            if self.search_sides == "8 sides":
                for each in self.queue:
                    self.visited.append(each)
                    for every in generate_8_side_index(each[0],each[1],Grid_size):
                        if every in self.input and every not in self.queue and every not in self.visited:self.queue.append(every)
            elif self.search_sides =="4 sides":
                for each in self.queue:
                    self.visited.append(each)
                    for every in generate_4_side_index(each[0],each[1],Grid_size):
                        if every in self.input and every not in self.queue and every not in self.visited:self.queue.append(every)


            for each in self.queue:self.input.remove(each)
            self.final_answer.append(self.queue.copy())

            if self.input != []:
                self.queue = []
                self.visited = []
                self.queue.append(self.input[0])
                self.__main_process()
    def __call__(self):
        self.__main_process()
        return self.final_answer

"""basic informtion and declarations"""
information = {"b" : [10,(9,9)],  "i" : [40,(16,16)],  "a" : [99,(16,30)] } 
color_info = {"1":"#0000ff","2":"#008000","3":"#ff0000","4":"#00008b","5":"#a52a2a","6":"#00ffff","7":"#000000","8":"#8b0000","Bdefault":"SystemButtonFace"}
Total_mines = information["b"][0];Grid_size = information["b"][1];Level_index = 0;MarKed_count = 0
Winner = False;Help_needed = True
mines_left = Total_mines-MarKed_count

"""Generate grid for game"""
def Grid_generator(Level:str) -> list:
    #basic info
    global information,color_info
    Grid_size = information[Level][1]
    Number_of_mine = information[Level][0] 
    Total_positions = Grid_size[0]*Grid_size[1]
    
    #generating mines location
    a = list(range(Total_positions));Mine_list = [];Zero_list = []
    for i in range(Number_of_mine): b = random.choice(a); a.pop(a.index(b)); Mine_list.append(b) #select from main list remove in main list append in mine list

    #making grid
    grid = [0]*(Total_positions); player_grid = ["U"]*(Total_positions)
    for each in Mine_list: grid[each] = "X" #plotting mines in grid

    Game_grid = np.array(grid).reshape(Grid_size);  Player_grid = np.array(player_grid).reshape(Grid_size)

    for idx_row,each_row in enumerate(Game_grid):
        for idx_column in list(range(len(each_row))):
            if Game_grid[idx_row][idx_column] != "X":
                mine_count = 0
                for each in generate_8_side_index(idx_row,idx_column,Grid_size):
                    if Game_grid[each[0]][each[1]] == "X":mine_count +=1
                Game_grid[idx_row][idx_column] =  mine_count
                if mine_count == 0:Zero_list.append((idx_row,idx_column))

    return Game_grid,Player_grid,Zero_list

def Activate_AI():
    global Player_grid,Grid_size,button_by_index,Winner,mines_left
    
    def Test_tank_algo():
        global Player_grid,Grid_size,button_by_index,Winner,mines_left
        def for_side_analysis_and_pop(MY_Bfs_8,AI_grid):
            global Player_grid,Grid_size,button_by_index,Winner,mines_left

            for list_of_effective_numbers in MY_Bfs_8: 
                flag,prob,index = main_method(list_of_effective_numbers)
                for each_prob,each_index in zip(prob,index):
                    if each_index in Total_index:
                        index_of_common = Total_index.index(each_index)
                        Total_prob[index_of_common] = round((Total_prob[index_of_common] + each_prob)/2,2)
                    else:
                        Total_index.append(each_index)
                        Total_prob.append(each_prob)
            if flag == False:
                min_index = []
                # print("_____________final______________")
                # print(Total_index)
                # print(Total_prob)
                if Total_prob != []:
                    min = np.min(Total_prob)
                    for each_index,each_prob in zip(Total_index,Total_prob):
                        if each_prob == min:min_index.append(each_index)

                    total = 0
                    for each_row in AI_grid:total += each_row.count("U")
                    
                    unknown_indexes = []
                    for idx_row,each_row in enumerate(AI_grid):
                        for idx_column,each_column in enumerate(each_row):
                            if each_column == "U" and [idx_row,idx_column] not in Total_index:
                                unknown_indexes.append([idx_row,idx_column])
                    if unknown_indexes != [] and (mines_left - math.floor(sum(Total_prob)))/(total + 1 - len(Total_index)) < min:
                        choice = random.choice(unknown_indexes)
                        print("Guess pop on unknown button =",choice)
                            
                    else:                   
                        choice = random.choice(min_index)
                        print("Guess pop button =",choice)
                    
                    pop_button(choice)


        def main_method(list_of_effective_numbers):
            global Player_grid,Grid_size,button_by_index,Winner,mines_left,frame
            list_of_influenced_unknown = []
            for each in list_of_effective_numbers:
                for every in generate_8_side_index(each[0],each[1],Grid_size):
                    if AI_grid[every[0]][every[1]] == "U":
                        if every not in list_of_influenced_unknown: list_of_influenced_unknown.append(every)

            popped_flag = False
            n = len(list_of_influenced_unknown)        

            # print("\n\n______________________Values obtained___________________________\n")
            # print(list_of_effective_numbers)
            # print(list_of_influenced_unknown)
            # print("_______________________processing ___________________________\n")
            
            c = 0
            answers = []
            combination = [0]*n
            for i in range(2**n):
                print("-",2**n - i,"-",end="\r")
                c =1
                for idx,value in enumerate(combination):
                    if c == 1 and value == 0:combination[idx]=1;c = 0
                    elif c == 0 and value == 0:combination[idx]=0;c = 0
                    elif c == 0 and value == 1:combination[idx]=1;c = 0
                    elif c == 1 and value == 1:combination[idx]=0;c = 1

                count_1 = combination.count(1)
                if count_1<=mines_left:
                    append_flag = True 
                    for each_value,each_position in zip(combination,list_of_influenced_unknown): 
                        if each_value == 1 :AI_grid[each_position[0]][each_position[1]] = "M"
                        else:AI_grid[each_position[0]][each_position[1]] = "U"

                    for each in list_of_effective_numbers:
                        Marked_count = 0
                        for each_surr_index in generate_8_side_index(each[0],each[1],Grid_size):
                            if AI_grid[each_surr_index[0]][each_surr_index[1]] == "M":Marked_count +=1
                        if AI_grid[each[0]][each[1]] != Marked_count:append_flag = False;break
                    Append_answer = combination.copy()
                    if append_flag:answers.append(Append_answer)

                

            if answers != []:
                answer_probability = np.array(np.round(np.average(answers,axis=0),2)).tolist()
                for each_prob,each_index in zip(np.round(answer_probability,2),list_of_influenced_unknown):
                    if each_prob == 0:pop_button(each_index);popped_flag = True
                    elif each_prob == 1:mark_button(each_index);popped_flag = True
                return popped_flag,answer_probability,list_of_influenced_unknown
            else:
                print("no possible combinnation found")
                return popped_flag,[],[]                

        print("_______________________answers  tank algo___________________________\n")
        AI_grid = []
        for each_row in Player_grid:
            row =[]
            for each_column in each_row:
                if each_column == "U":row.append("U")
                else:row.append(0)
            AI_grid.append(row)
        
        set_of_effective_numbers = []
        for idx_row,each_row in enumerate(AI_grid):
            for idx_column,each_column in enumerate(each_row):
                if each_column == "U":
                    for each in generate_8_side_index(idx_row,idx_column,Grid_size):
                        if Player_grid[each[0]][each[1]] == 0:pass
                        elif Player_grid[each[0]][each[1]] == "F":AI_grid[each[0]][each[1]] = "F"
                        elif Player_grid[each[0]][each[1]] != "U" and each not in set_of_effective_numbers:
                            count = 0
                            for each1 in generate_8_side_index(each[0],each[1],Grid_size):
                                if Player_grid[each1[0]][each1[1]] == "F":count += 1
                            AI_grid[each[0]][each[1]] = int(Player_grid[each[0]][each[1]]) - count
                            if [each[0],each[1]] not in set_of_effective_numbers:
                                set_of_effective_numbers.append(each)

        """Main tank algo starts here"""
        if mines_left == 0 and len(set_of_effective_numbers) == 0:
                for idx_row,each_row in enumerate(Player_grid):
                    for idx_column,each_column in enumerate(each_row):
                        if each_column == "U": pop_button([idx_row,idx_column])

        elif len(set_of_effective_numbers) == 0:print("no data in unknown indexes")
        else:
            print("_____________________grid to evaluate______________________")

            print(np.array(AI_grid))
            print(set_of_effective_numbers)
            MY_Bfs_8 = BFS(set_of_effective_numbers.copy(),"8 sides")()#;print(MY_Bfs_8)
            MY_Bfs_4 = BFS(set_of_effective_numbers.copy(),"4 sides")()#;print(MY_Bfs_4)

            Total_prob = []
            Total_index = []

            if len(MY_Bfs_4) == len(MY_Bfs_8):for_side_analysis_and_pop(MY_Bfs_4,AI_grid)
            else: 
                for list_of_effective_numbers in MY_Bfs_4: work_flag,prob,index = main_method(list_of_effective_numbers)
                
                if not work_flag:
                    print("_________searching 4 sides didnt work so searching 8 sides___________________")
                    for_side_analysis_and_pop(MY_Bfs_8,AI_grid)
                    
                                  

    def marking_and_popping_search(): 
        print("_____________________answer normal algo___________________________\n")
        return_value = False  
        for idx_row,each_row in enumerate(Player_grid):
            for idx_column,each_column in enumerate(each_row):

                if each_column not in "UF0X":
                    count_u = 0 ; count_f = 0
                    for each in generate_8_side_index(idx_row,idx_column,Grid_size):
                        if Player_grid[each[0],each[1]] == "U":count_u += 1
                        if Player_grid[each[0],each[1]] == "F":count_f += 1

                    if count_u == 0:pass
                    elif int(each_column) == count_u + count_f:
                        for each in generate_8_side_index(idx_row,idx_column,Grid_size):
                            mark_button(each)
                            return_value = True

                    if int(each_column) == count_f and count_u >0:
                        for each in generate_8_side_index(idx_row,idx_column,Grid_size):
                            if Player_grid[each[0]][each[1]] != "F":
                                pop_button(each)
                                return_value = True
        return return_value

    if not Winner:
        update_frame("AI working please wait")
        pop_one_zero()
        if not marking_and_popping_search():goal_condition();Test_tank_algo()
        goal_condition() 
        update_frame("Game in progress")


def goal_condition():
    global Player_grid,Total_mines,Winner,Mine_left,MarKed_count,mines_left

    if not Winner:
        MarKed_count = 0; Unknown_count = 0;X_count = 0
        for each in Player_grid: MarKed_count += list(each).count("F");Unknown_count += list(each).count("U");X_count+=list(each).count("X")
        Total_count = MarKed_count + Unknown_count + X_count
        if Total_count == Total_mines:
            Mine_left.configure(text="mine=0");frame.configure(text = "!!!!!!!!!!!!!!!!!!!!!!!!! You win !!!!!!!!!!!!!!!!!!!!!!!!!!!")
            for each in frame.winfo_children():
                if each.cget("bg") == color_info["Bdefault"]: each.configure(state = DISABLED,bg="#6565d4",text="X",disabledforeground="Black")
            Winner = True
        else:
            mines_left = Total_mines-MarKed_count
            Mine_left.configure(text="mine="+str(mines_left))


"""defining buttons in dictionary so that it is easy to call"""
button_by_index = {}

"""pop one 0 indexed button if help is pressed"""
def pop_one_zero():
    global Zero_list,Initial_help_button,button_by_index,Help_needed
    if Initial_help_button.cget("state") == "normal":
        print("_____________one random zero popped_____________________\n")
        frame.configure(text = "Game in progress")
        choice = random.choice(Zero_list)
        pop_button(choice)
        Initial_help_button.configure(state=DISABLED)
        Initial_help_button.pack_forget()
        Help_needed = False

"""changing level and resetting"""
def Level_change():
    global Level_index
    Level_index = (Level_index + 1) % 3  
    reset_command()

"""well its a reset button whaat ya expect"""
def reset_command():
    global Total_mines,Game_grid,Player_grid,Level_index,Grid_size,Initial_help_button,Zero_list,Winner ,information,Help_needed

    Winner = False
    Help_needed = True
    """removing buttons"""
    for each in frame.winfo_children():each.destroy()

    if Level_index == 0:Level_button.configure(text="Beginner");Game_grid,Player_grid,Zero_list = Grid_generator("b");Total_mines = information["b"][0];Grid_size = information["b"][1];Beginner()
    elif Level_index == 1:Level_button.configure(text="Intermediate");Game_grid,Player_grid,Zero_list = Grid_generator("i");Total_mines = information["i"][0];Grid_size = information["i"][1];Intermediate()
    elif Level_index == 2 :Level_button.configure(text="Advanced");Game_grid,Player_grid,Zero_list = Grid_generator("a");Total_mines = information["a"][0];Grid_size = information["a"][1];Advanced()

    Initial_help_button.pack()
    Initial_help_button.configure(state=NORMAL)

    Mine_left.configure(text="mine="+str(Total_mines))
    frame.configure(text = "Grid Set")

"""Generates the index of all 8 sides from a spot like in flood fill"""
def generate_8_side_index(row,column,Grid_size=Grid_size):
    My_list = []
    for each in [[row-1,column-1],[row-1,column],[row-1,column+1],[row,column-1],[row,column+1],[row+1,column-1],[row+1,column],[row+1,column+1]]:
        if each[0] >= 0  and each[0] < Grid_size[0] and each[1] >= 0  and each[1] < Grid_size[1]:
            My_list.append([each[0],each[1]])
    return My_list

"""Generates the index of all 4 linear sides from a spot like in flood fill"""
def generate_4_side_index(row,column,Grid_size=Grid_size):
    My_list = []
    for each in [[row-1,column],[row,column-1],[row,column+1],[row+1,column]]:
        if each[0] >= 0  and each[0] < Grid_size[0] and each[1] >= 0  and each[1] < Grid_size[1]:
            My_list.append([each[0],each[1]])
    return My_list



"""Generating grid and needed grid information"""
Game_grid,Player_grid,Zero_list = Grid_generator("b")

"""Main program starts from here"""
root = Tk()
root.title("MLproductions")
root.resizable(False,False)

design_label = Label(root,text="Minesweeper",font="Times 20 bold")
Mine_left = Label(root,text="mine="+str(Total_mines),bg = "Black",fg = "White") 
frame = LabelFrame(root,text="Game started") 
reset_button = Button(root,text="Reset",command=reset_command) 
Level_button = Button(root,text="Beginner",command=Level_change)
AI_button = Button(root,text="AI",command= Activate_AI)
Initial_help_button = Button(root,text="Help?",command = pop_one_zero)

"""creating Button object such that it is easier to assign to multiple spots"""
class My_button():

    def __init__(self,row,column) -> None:
        self.button = Button(frame,height=0,width = 2,font="Times 8 bold",command = self.button_clicked)
        self.button.bind("<Button-3>",self.put_mark)
        self.row_position = row
        self.column_position = column
        self.check_help_needed = True        
    
    def button_clicked(self):
        global Grid_size,Player_grid,Game_grid,Winner,Help_needed
        if not Winner:
            
            if not Help_needed:Initial_help_button.pack_forget();update_frame("Game in progress")

            if self.button.cget("state") == "normal":
                if self.button.cget("text") == "F":
                    self.button.configure(text="")
                    Player_grid[self.row_position][self.column_position] = "U"
                else:
                    Player_grid[self.row_position][self.column_position] = Game_grid[self.row_position][self.column_position]
                    if Game_grid[self.row_position][self.column_position] == "0":
                        self.button.configure(state=DISABLED,bg="#9e9a9a")
                        for each in generate_8_side_index(self.row_position,self.column_position,Grid_size):pop_button(each)

                    elif Game_grid[self.row_position][self.column_position] in "12345678":
                        print(f"{[self.row_position,self.column_position]} button_pressed")
                        self.button.configure(state=DISABLED,bg="#9e9a9a",disabledforeground=color_info[Game_grid[self.row_position][self.column_position]],text=str(Game_grid[self.row_position][self.column_position]))

                    elif Game_grid[self.row_position][self.column_position] == "X":
                        print(f"{[self.row_position,self.column_position]} button_pressed")
                        frame.configure(text="You lost")
                        for idx_row,each_row in enumerate(Game_grid):
                            for idx_column,each_column in enumerate(each_row):
                                if each_column == "X": button_by_index[f"{idx_row}_{idx_column}"].button.configure(state=DISABLED,bg="red",text="X",disabledforeground="black")
                                else : button_by_index[f"{idx_row}_{idx_column}"].button.configure(state=DISABLED)
            goal_condition()

    def put_mark(self,event=0):
        global Player_grid,Mine_left,Winner
        if not Winner:
            update_frame("Game in progress")
            if self.button.cget("state") == "normal": 
                print(f"{[self.row_position,self.column_position]} button_marked")
                self.button.configure(text="F",fg = "Black")
                Player_grid[self.row_position][self.column_position] = "F"
            goal_condition()

    def put_in_frame(self): self.button.grid(column=self.column_position,row=self.row_position)

def pop_button(each):
    global button_by_index
    button_by_index[f"{each[0]}_{each[1]}"].button_clicked()

def mark_button(each):
    global button_by_index
    button_by_index[f"{each[0]}_{each[1]}"].put_mark()

def update_frame(text_inp):
    global frame
    frame.configure(text=text_inp)

"""function for which button to insert"""
def Advanced():
    global button_by_index
    for row in range(16):
        for column in range(30):
            button_by_index[f"{row}_{column}"] = My_button(row,column); button_by_index[f"{row}_{column}"].put_in_frame()

def Intermediate():
    global button_by_index
    for row in range(16):
        for column in range(16):
            button_by_index[f"{row}_{column}"] = My_button(row,column); button_by_index[f"{row}_{column}"].put_in_frame()

def Beginner():
    global button_by_index
    for row in range(9):
        for column in range(9):
            button_by_index[f"{row}_{column}"] = My_button(row,column); button_by_index[f"{row}_{column}"].put_in_frame()

"""inserting button and label in app"""
design_label.pack()
frame.pack(padx=0,pady=0)
reset_button.pack(side=RIGHT,padx=1)
AI_button.pack(side=LEFT,padx=1)
Level_button.pack(side=RIGHT)
Mine_left.pack(side=LEFT,padx=2)
Initial_help_button.pack()

"""defining button and click functions and inserting according to difficulty"""
Beginner()
root.mainloop()