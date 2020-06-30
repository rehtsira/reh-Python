import tkinter, random
import tkinter.messagebox
from time import time
from time import ctime

#Create root window
root = tkinter.Tk()

#Change root window background color
root.configure(bg="white")

#Change title
root.title("aerDo")

#Change the window size
root.geometry("300x275")

#Create an empty list
tasks =[]

#Creating functions
def update_listbox():
    #clear the current list
    clear_listbox()
    #populate the listbox
    for task in tasks:
        lb_tasks.insert("end", task)

def print_time():
    #print current time
    t = time()
    print(ctime(t))
    return ctime(t)


def clear_listbox():
    lb_tasks.delete(0,"end")

def add_task():
    #get the task to add
    task = txt_input.get()
    #don't let duplicate task to pass
    if task in tasks:
        tkinter.messagebox.showwarning("Warning","You have already entered this task.")
        tasks.remove(task)
    #make sure the task is not empty
    if task != "":
        #append to the list
        tasks.append(task + " - " + str(print_time()))
        #update the listbox
        update_listbox()
    else:
        tkinter.messagebox.showwarning("Warning","You need to enter a task.")
    txt_input.delete(0,"end")

def del_all():
    #send a prompt for verification
    confirmed = tkinter.messagebox.askyesno("Please confirm", "Do you really want to delete all?")
    if confirmed == True:
        #changing the list requires it to be global
        global tasks
        #clear the task list
        tasks = []
        #update the listbox
        update_listbox()

def del_one():
    #get the text of the currently selected item
    task = lb_tasks.get("active")
    #confirm it is on the list"
    if task in tasks:
        tasks.remove(task)
    #update the listbox
    update_listbox()

def sort_asc():
    #sort the list in ascending manner
    tasks.sort()
    #update the listbox
    update_listbox()

def sort_dsc():
    #sort the list in descending manner
    tasks.sort()
    #reverse the list
    tasks.reverse()
    #update the listbox
    update_listbox()

def choose_random():
    #Choose a random taks
    task = random.choice(tasks)
    #Update the display label
    lbl_display["text"]=task

def show_number_of_tasks():
    #get number of tasks
    number_of_tasks = len(tasks)
    #create and format the message
    msg = "Number of tasks: %s" %number_of_tasks
    #display the message
    lbl_display["text"]=msg


lbl_title = tkinter.Label(root, text="To-Do-List", bg="white")
lbl_title.grid(row=0,column=0)

lbl_display = tkinter.Label(root, text="", bg="white")
lbl_display.grid(row=0,column=1)

txt_input = tkinter.Entry(root, width=15)
txt_input.grid(row=1,column=1)

btn_add_task = tkinter.Button(root, text="Add task", fg="green", bg="white", command=add_task)
btn_add_task.grid(row=1,column=0)

btn_del_all = tkinter.Button(root, text="Delete All", fg="green", bg="white", command=del_all)
btn_del_all.grid(row=2,column=0)

btn_del_one = tkinter.Button(root, text="Delete", fg="green", bg="white", command=del_one)
btn_del_one.grid(row=3,column=0)

btn_sort_asc = tkinter.Button(root, text="Sort Ascending", fg="green", bg="white", command=sort_asc)
btn_sort_asc.grid(row=4,column=0)

btn_sort_dsc = tkinter.Button(root, text="Sort Descending", fg="green", bg="white", command=sort_dsc)
btn_sort_dsc.grid(row=5,column=0)

btn_choose_random = tkinter.Button(root, text="Choose Random", fg="green", bg="white", command=choose_random)
btn_choose_random.grid(row=6,column=0)

btn_number_of_tasks = tkinter.Button(root, text="Number of tasks", fg="green", bg="white", command=show_number_of_tasks)
btn_number_of_tasks.grid(row=7,column=0)

btn_exit = tkinter.Button(root, text="Quit", fg="green", bg="white", command=exit)
btn_exit.grid(row=8,column=0)

lb_tasks = tkinter.Listbox(root)
lb_tasks.grid(row=2,column=1, rowspan=7)


root.mainloop()
