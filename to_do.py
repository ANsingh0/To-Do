from tkinter import *
from tkinter import messagebox

#globsl lidt for storing all the task
tasks_list = []

#globsl variable for counting tasks
counter = 1

#function for checking input error when empty input is goven in task fiels
def inputError():
    if enterTaskField.get() == "":
        #show the error message
        messagebox.showerror("Input Error")
        return 0
    return 1

#Function for clearing the contents of task number tect field
def clear_taskNumberField():
    taskNumberField.delete(0.0, END)

def clear_taskField():
    enterTaskField.delete(0, END)

def insertTask():
    global counter

    #check for error
    value = inputError()
    if value == 0:
        return
    #get the task strng concatenating with new line character
    content = enterTaskField.get() + "\n"

    tasks_list.append(content)
    TextArea.insert("end -1 chars", "[" +str(counter)+ "]" + content)
    counter += 1

    clear_taskField()

def delete():
     global counter

     #handling the empty task error
     if len(tasks_list) == 0:
         messagebox.showerror("No task")
         return
     
     #get the task number, which is required to delete
     number = taskNumberField.get(1.0, END)

     #checking for input error when empty input in task number field
     if number == "\n":
         messagebox.showerror("input error")
         return
     else:
         task_no = int(number)
         
     clear_taskNumberField()
     
     tasks_list.pop(task_no - 1)
     counter -= 1
     TextArea.delete(1.0,END)

     #rewriting the task after ddeleting one task at a time
     for i in range(len(tasks_list)):
         TextArea.insert("end -1 chars", "[" + str(i+1) +"]" + tasks_list[i])

# Driver code
if __name__ == "__main__":
    gui = Tk()

    gui.configure(background= "white")
    gui.title("ToDo App")
    gui.geometry("250x300")

    #create a label: Enter Your Task
    enterTask = Label(gui, text = "Enter Your Task", bg = "light green")
    enterTaskField = Entry(gui)
    Submit = Button(gui, text = "Submit", fg = "Black", bg = "blue", command = insertTask)
    TextArea = Text(gui, height = 5, width = 25, font = "lucida 13")
    taskNumber = Label(gui, text = "Delete Task Number", bg = "blue")
    taskNumberField = Text(gui, height = 1, width= 2, font = "lucida 13")
    delete_ = Button(gui, text="Delete", fg ="Black", bg = "Red", command = delete)
    Exit = Button(gui, text = "Exit", fg = "Black", bg = "Red", command = exit)

    #SPECIFY Grid
    Grid.rowconfigure(gui, 0, weight= 1)
    Grid.columnconfigure(gui, 0, weight = 1)
    Grid.rowconfigure(gui, 1, weight = 1)

    enterTask.grid(row = 0, column = 2)
    enterTaskField.grid(row = 1, column = 2, ipadx = 50) #ipadx attributed set the entry box horizontal size
    Submit.grid(row=2, column = 2)
    TextArea.grid(row= 3, column =2, padx = 10, sticky = NSEW) #padx attributed provide  x-xis margin from the root window to the widget
    taskNumber.grid(row = 4, column = 2, pady = 5)# pady attribute provide y-axis margin from the widget.
    taskNumberField.grid(row = 5, column = 2)
    delete_.grid(row=6, column = 2, pady = 5)

    Exit.grid(row= 7, column =2)
    
    #start the GUI
    gui.mainloop()




    



