import random
import math
from tkinter import *

def key_pressed_event(event):
    global App_dict
    if not App_dict["start flag"]:
        try:
            App_dict["Depth_limit"] = int(App_dict["Depth entry"].get())
            show_depth()
        except:
            App_dict["label frame"].configure(text = "Enter integer")
            App_dict["root"].after(1000,show_depth)

def generate_surr_indexes(row,column):
    global App_dict
    return_list = []
    if App_dict["sides to use"] == 8:
        for each in [[row-1,column],[row-1,column+1],[row,column+1],[row+1,column+1],[row+1,column],[row+1,column-1],[row,column-1],[row-1,column-1]]:
            if 0 <= each[0] < App_dict["Grid size [x,y]"][0] and 0 <= each[1] < App_dict["Grid size [x,y]"][1]:
                return_list.append(each)
        return return_list
    
    elif App_dict["sides to use"] == 4:
        for each in [[row-1,column],[row,column+1],[row+1,column],[row,column-1]]:
            if 0 <= each[0] < App_dict["Grid size [x,y]"][0] and 0 <= each[1] < App_dict["Grid size [x,y]"][1]:
                return_list.append(each)
        return return_list

class bidirectional:
    def __init__(self) -> None:
        pass



class AStar:
    def __init__(self) -> None:
        global App_dict
        self.input = App_dict["start node"].copy()
        self.end = App_dict["end node"].copy()
        self.present_distance = abs(self.input[0] - self.end[0]) + abs(self.input[1] - self.end[1])
        self.previous_distance = math.inf
        self.queue = []
        self.visited = []

    def __call__(self,cost = 0):
        global App_dict
        if self.end in self.visited:App_dict["answer list"] = self.visited.copy();visit_answers()
        else:
            list_of_nodes = []
            heuretics = []
            self.visited.append(self.input)
            for each in generate_surr_indexes(self.input[0],self.input[1]):
                if each not in self.visited and App_dict["evaluation_grid"][each[0]][each[1]] != "B":
                    list_of_nodes.append(each)
                    heuretics.append(abs(each[0] - self.end[0]) + abs(each[1] - self.end[1]) + cost)

            pseudo_cost = cost + 1
            if heuretics != []:
                list_of_choice = []
                self.previous_distance = self.present_distance
                min_heuretics = min(heuretics)
                self.present_distance = min_heuretics
                if heuretics.count(min_heuretics) != 1:
                    for each_heu,each_index in zip(heuretics,list_of_nodes):
                        if each_heu == min_heuretics :list_of_choice.append(each_index)
                    self.input = random.choice(list_of_choice)
                    for each,each1 in zip(list_of_nodes,heuretics):
                        if each not in self.queue and each != self.input: self.queue.insert(0,[each,cost])
                    self.__call__(pseudo_cost)

                elif heuretics.count(min_heuretics) == 1:
                    index_to_send = heuretics.index(min_heuretics)
                    self.input = list_of_nodes[index_to_send]
                    for each,each1 in zip(list_of_nodes,heuretics):
                        if each not in self.queue and each != self.input: self.queue.insert(0,[each,cost])
                    self.__call__(pseudo_cost)
            else:
                if self.queue != []:
                    for each in self.visited:
                        for [index,cost] in self.queue:
                            if each == index:self.queue.remove([index,cost])

                    self.input = self.queue[0][0]
                    cost = self.queue[0][1]
                    self.queue.pop(0)
                    self.__call__(cost)
                else:
                    App_dict["answer list"] = self.visited.copy();visit_answers()

class IDLS:
    def __init__(self) -> None:
        global App_dict
        self.queue = []
        self.input= App_dict["start node"].copy()
        self.visited = []
        self.cost_limit = App_dict["Depth_limit"]

    def __call__(self,cost = 0):
        if cost > self.cost_limit: 
            if self.input not in self.queue:self.queue.append(self.input)
        elif App_dict["end node"] in self.visited :self.exit_flag = True
        elif cost <= self.cost_limit:
            self.visited.append(self.input)
            for each in generate_surr_indexes(self.input[0],self.input[1]):
                if each not in self.visited and App_dict["evaluation_grid"][each[0]][each[1]] != "B":
                    self.input = each
                    pseeudo_cost = cost+1
                    self.__call__(pseeudo_cost)
        
    def empty_queue(self):
        if self.queue != []:
            for each in self.queue:
                self.input = each
                self.__call__(1)

class DLS:
    def __init__(self) -> None:
        global App_dict
        self.input= App_dict["start node"].copy()
        self.visited = []
        self.cost_limit = App_dict["Depth_limit"]
        self.exit_flag = False

    def __call__(self,cost = 0):
        if not self.exit_flag:
            if App_dict["end node"] in self.visited:self.exit_flag = True
            elif cost > self.cost_limit:pass
            else:
                self.visited.append(self.input)
                for each in generate_surr_indexes(self.input[0],self.input[1]):
                    if each not in self.visited and App_dict["evaluation_grid"][each[0]][each[1]] != "B":
                        self.input = each
                        pseeudo_cost = cost+1
                        self.__call__(pseeudo_cost)

class DFS:
    def __init__(self) -> None:
        self.input= App_dict["start node"].copy()
        self.visited = []
        self.stop = False
        self.print = False
        self.record = []
        self.record.append(self.input)
    def __call__(self):
        if not self.stop:
            if self.input == App_dict["end node"]:self.visited.append(self.input);App_dict["answer list"] = self.visited.copy();visit_answers();self.stop=True
            else:
                self.record.remove(self.input)
                self.visited.append(self.input)
                for each in generate_surr_indexes(self.input[0],self.input[1]):
                    if each not in self.visited and App_dict["evaluation_grid"][each[0]][each[1]] != "B" and each not in self.record:
                        self.record.append(each)
                for each in generate_surr_indexes(self.input[0],self.input[1]):
                    if each not in self.visited and App_dict["evaluation_grid"][each[0]][each[1]] != "B":
                        self.input = each
                        self.__call__()
                if self.record == [] and not self.print:
                    self.print = True
                    App_dict["answer list"] = self.visited.copy()
                    visit_answers()


class BFS:
    def __init__(self) -> None:
        self.queue = []
        self.queue.append(App_dict["start node"].copy())
    def __call__(self):
        for each in self.queue:
            for every in generate_surr_indexes(each[0],each[1]):
                if every not in self.queue and App_dict["evaluation_grid"][every[0]][every[1]] != "B" and App_dict["end node"] not in self.queue:self.queue.append(every)
        App_dict["answer list"] = self.queue.copy()
        visit_answers()

def visit_answers():
    global App_dict
    if App_dict["start flag"] and len(App_dict["answer list"]) != 0:
        [i,j] = App_dict["answer list"][0]
        App_dict[f"label {i} {j}"].visit()
        App_dict["answer used list"].append([i,j])
        App_dict["answer list"].remove([i,j])
        App_dict["root"].after(100,visit_answers)
    elif len(App_dict["answer list"]) == 0:
        start_command()

def put_block_command():
    global App_dict
    if not App_dict["start flag"]:
        if not App_dict["block plot flag"]:
            App_dict["block plot button"].configure(text = "+blocks")
            App_dict["block plot flag"] = True
        else:
            App_dict["block plot button"].configure(text = "-blocks")
            App_dict["block plot flag"] = False

def algo_use(input="BFS"):
    global App_dict
    if "DLS" == input or "IDLS" == input:
        App_dict["search algo"] = input
        App_dict["Option menu"].configure(text = input)
        App_dict["Depth entry"].pack(side="right")
        App_dict["root"].bind("<Return>",key_pressed_event)
        show_depth()

    else:
        App_dict["search algo"] = input
        App_dict["Option menu"].configure(text = input)
        App_dict["Depth entry"].pack_forget()
        App_dict["root"].unbind("<Return>")
        show_grid_size()


def side_to_use(input=4):
    global App_dict
    App_dict["sides to use"] = input
    App_dict["Top label"].configure(text = f"Search Simulation {input}")

def show_grid_size():
    global App_dict
    App_dict["label frame"].configure(text = f"size = {App_dict['Grid size [x,y]'][0]} * {App_dict['Grid size [x,y]'][1]}")
    if App_dict["search algo"] == "IDLS" or App_dict["search algo"] == "DLS":App_dict["label frame"].configure(text = f"Depth = {App_dict['Depth_limit']}")

def show_depth():
    global App_dict
    App_dict["label frame"].configure(text = f"Depth = {App_dict['Depth_limit']}")

def start_command():
    global App_dict
    if not App_dict["start flag"] and App_dict["start node"] != [] and App_dict["end node"] != [] :

        App_dict["start flag"] = True

        if len(App_dict["answer used list"]) != []:
            for each in App_dict["answer used list"]:App_dict[f"label {each[0]} {each[1]}"].unvisit()
            App_dict["answer used list"] = []
        App_dict["start"].configure(text = "Stop")

        if App_dict["search algo"] == "DLS":
            DLS_ans = Search_algo_dict[App_dict["search algo"]]()
            DLS_ans(); App_dict["answer list"] = DLS_ans.visited.copy(); visit_answers()
        elif App_dict["search algo"] == "IDLS":
            IDLS_ans = Search_algo_dict[App_dict["search algo"]]();IDLS_ans()
            if IDLS_ans.queue != [] or App_dict["end node"] not in IDLS_ans.visited:IDLS_ans.empty_queue()
            App_dict["answer list"] = IDLS_ans.visited.copy(); visit_answers()
        else:Search_algo_dict[App_dict["search algo"]]()()

    elif App_dict["start flag"] and App_dict["start node"] != [] and App_dict["end node"] != [] :
        App_dict["start flag"] = False
        App_dict["start"].configure(text = "Start")
    
    else:
        App_dict["label frame"].configure(text = "Start and end nodes?")
        App_dict["start"].after(1000,show_grid_size)
        

def pop_up_search_menu(event):
    global App_dict
    if not App_dict["start flag"]:App_dict["search menu"].tk_popup(event.x_root,event.y_root,0)

def pop_up_side_menu(event):
    global App_dict
    if not App_dict["start flag"]:App_dict["sides menu"].tk_popup(event.x_root,event.y_root,0)

def reset_command():
    global App_dict
    App_dict["Depth_limit"] = 5
    if App_dict["search algo"] == "IDLS" or App_dict["search algo"] == "DLS":show_depth()
    App_dict["block plot button"].configure(text = "-blocks")
    App_dict["start"].configure(text = "Start")
    App_dict["Grid size [x,y]"]=[10,10]
    App_dict["start flag"]=False
    App_dict["start node"] = []
    App_dict["end node"] = []
    App_dict["block plot flag"] = False
    App_dict["search index"] = 0
    App_dict["answer list"]= []
    App_dict["evaluation_grid"] =  []
    App_dict["answer used list"] = []
    removing_label()
    defining_labels()

color_dict = {"starting" : "green","ending":"red","block":"black","visiting":"yellow","Bdefault":"SystemlabelFace","nothing":"grey","end node visited":"blue"}
search_algo = ["BFS","DFS"]
Search_algo_dict = {"BFS":BFS,"DFS":DFS,"DLS":DLS,"IDLS":IDLS,"A*":AStar}

App_dict = {}

App_dict["Depth_limit"] = 5
App_dict["Grid size [x,y]"]=[10,10]
App_dict["start flag"]=False
App_dict["start node"] = []
App_dict["end node"] = []
App_dict["block plot flag"] = False
App_dict["search index"] = 0
App_dict["answer list"]= []
App_dict["evaluation_grid"] =  []
App_dict["answer used list"] = []
App_dict["sides to use"] = 4
App_dict["search algo"] = "BFS"

App_dict["root"] = Tk()
App_dict["root"].title("ML productions")
App_dict["root"].resizable(0,0)


App_dict["Top label"] = Label(App_dict["root"],text="Search Simulation 4",font=("Times", 20 ,"bold"))
App_dict["label frame"] = LabelFrame(App_dict["root"]);show_grid_size()
App_dict["block plot button"] = Button(App_dict["root"],text = "-blocks",command = put_block_command)
App_dict["Reset"] = Button(App_dict["root"],text="Reset",command=reset_command)
App_dict["start"] = Button(App_dict["root"],text="Start",command=start_command)
App_dict["Option menu"] = Label(App_dict["root"],text="BFS",bg = "black",fg = "white",padx=3)
App_dict["Depth entry"] = Entry(App_dict["root"],width=3,background="#dbc2c2")

App_dict["Option menu"].bind("<Button>",pop_up_search_menu)
App_dict["search menu"] = Menu(App_dict["Option menu"],tearoff=0)

App_dict["search menu"].add_command(label="A*",command=lambda:algo_use("A*"))
App_dict["search menu"].add_command(label="DLS",command=lambda:algo_use("DLS"))
App_dict["search menu"].add_command(label="DFS",command=lambda:algo_use("DFS"))
App_dict["search menu"].add_command(label="BFS",command=lambda:algo_use("BFS"))
App_dict["search menu"].add_command(label="IDLS",command=lambda:algo_use("IDLS"))
App_dict["search menu"].add_command(label="Close")

App_dict["Top label"].bind("<Button-3>",pop_up_side_menu)
App_dict["sides menu"] = Menu(App_dict["Top label"],tearoff=0)
App_dict["sides menu"].add_command(label="use 4 sides",command=lambda:side_to_use(4))
App_dict["sides menu"].add_command(label="use 8 sides",command=lambda:side_to_use(8))
App_dict["sides menu"].add_command(label="Close")



class My_label:
    def __init__(self,row,column) -> None:
        self.main_label = Label(App_dict["label frame"],height=0,width=2,bg="grey",borderwidth=2,highlightthickness=1,highlightcolor="white")
        self.row_position = row
        self.column_position = column
        self.menu = Menu(self.main_label,tearoff=0)
        self.main_label.bind("<Button-3>",self.popup)
        self.main_label.bind("<Button>",self.main_label_clicked)

    def main_label_clicked(self,event = 0): 
        global App_dict
        if not App_dict["start flag"]:
            if App_dict["start node"] != [self.row_position,self.column_position] and App_dict["end node"] != [self.row_position,self.column_position]:
                if App_dict["block plot flag"]: 
                    self.main_label.configure(bg=color_dict["block"])
                    App_dict["evaluation_grid"][self.row_position][self.column_position] = "B"
                elif not App_dict["block plot flag"]: 
                    App_dict["evaluation_grid"][self.row_position][self.column_position] = 0
                    self.main_label.configure(bg=color_dict["nothing"])  
   

    def put_in_frame(self): self.main_label.grid(row=self.row_position,column=self.column_position)

    def popup(self,event):
        if not App_dict["start flag"]:self.menu_edited();self.menu.tk_popup(event.x_root, event.y_root, 0)

    def visit(self):
        if App_dict["start node"] == [self.row_position,self.column_position]:pass
        elif App_dict["end node"] == [self.row_position,self.column_position]:self.main_label.configure(bg=color_dict["end node visited"])
        else: self.main_label.configure(bg=color_dict["visiting"])

    def unvisit(self):
        if App_dict["start node"] == [self.row_position,self.column_position]:pass
        elif App_dict["evaluation_grid"][self.row_position][self.column_position] == "B":pass
        elif App_dict["end node"] == [self.row_position,self.column_position]:self.main_label.configure(bg=color_dict["ending"])
        else: self.main_label.configure(bg=color_dict["nothing"])

    def mark_as_start(self):
        self.main_label.configure(bg=color_dict["starting"])
        App_dict["start node"]=[self.row_position,self.column_position]
        App_dict["evaluation_grid"][self.row_position][self.column_position] = "S"

    def remove_as_start(self):
        self.main_label.configure(bg=color_dict["nothing"]) 
        App_dict["start node"]=[]
        App_dict["evaluation_grid"][self.row_position][self.column_position] = 0

    def mark_as_end(self):
        self.main_label.configure(bg=color_dict["ending"])
        App_dict["end node"]=[self.row_position,self.column_position]
        App_dict["evaluation_grid"][self.row_position][self.column_position] = "F"

    def remove_as_end(self):
        self.main_label.configure(bg=color_dict["nothing"])
        App_dict["end node"]=[]
        App_dict["evaluation_grid"][self.row_position][self.column_position] = 0

    def menu_edited(self):
        self.menu.destroy()
        self.menu = Menu(self.main_label,tearoff= 0)

        if App_dict["start node"] == [] and App_dict["end node"]!= [self.row_position,self.column_position]:self.menu.add_command(label="Mark as start",command=self.mark_as_start)
        elif App_dict["start node"] == [self.row_position,self.column_position]:self.menu.add_command(label="Remove as start",command=self.remove_as_start)

        if App_dict["end node"] == [] and App_dict["start node"] != [self.row_position,self.column_position]:self.menu.add_command(label="Mark as end",command=self.mark_as_end)
        elif App_dict["end node"] == [self.row_position,self.column_position]:self.menu.add_command(label="Remove as end",command=self.remove_as_end)

        if App_dict["start node"] ==[] or App_dict["end node"] == [] or App_dict["end node"] == [self.row_position,self.column_position] or App_dict["start node"] == [self.row_position,self.column_position]:
            self.menu.add_command(label="close")



def removing_label():
    global App_dict
    for each in App_dict["label frame"].winfo_children(): each.destroy()


def defining_labels(x=App_dict["Grid size [x,y]"][0],y=App_dict["Grid size [x,y]"][1]):
    global App_dict
    for i in range(y):
        row =[]
        for j in range(x):
            row.append(0)
            App_dict[f"label {i} {j}"] = My_label(i,j)
            App_dict[f"label {i} {j}"].put_in_frame()
        App_dict["evaluation_grid"].append(row)
        

App_dict["Top label"].pack()
App_dict["label frame"].pack()
defining_labels()
App_dict["block plot button"].pack(side="left")
App_dict["Reset"].pack(side="right")
App_dict["start"].pack(side = "right")
App_dict["Option menu"].pack(side = "right",padx=5)


App_dict["root"].mainloop()
