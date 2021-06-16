from tkinter import *
import math
import json
import os

starting_input = "Start your To-Do List here"
startFlag= False
recent_forget = list()
box = {'todo': [],
       'forget':[]}
List_folder = "checklist.json"

'''
def eleminator(butt, tex):
    butt.pack_forget()
    recent_forget = tex
'''

def undo():
    global box
    try:
        e.insert(0, box['forget'][-1])
        box['forget'] = box['forget'][:-1]
        stopgap()
    except:
        pass

def dumper(dat):
    with open(List_folder, 'w')as lf:
        json.dump(dat,lf)

def makeChecker(t):
    global box
    b = Button()
    b = Button(root, text=t, command=lambda:[b.pack_forget(),
                                             box['forget'].append(t),
                                             box['todo'].remove(t),
                                             dumper(box)], height=2,padx=1000, bg='black', fg='white', font='sans 16 bold', wraplength=300)
    b.pack()
    e.focus_set()
    box['todo'].append(t)

def stopgap():
    global box
    if e.get() and e.get() != starting_input:
        makeChecker(e.get().upper())
        e.delete(0, "end")
        dumper(box)

def some_callback(event): 
    e.delete(0, "end")
    return None

def key_pressed(event):
    if event.char == '`':
        e.delete(0,'end')
        undo()
    if event.char == '\r':
        stopgap()
    '''
    if event.char == 'l':

    '''
    if starting_input in e.get():
        e.delete(0,'end')
        e.insert(0, event.char)

'''
def make_draggable(widget):
    widget.bind("<Button-1>", on_drag_start)
    widget.bind("<B1-Motion>", on_drag_motion)

def on_drag_start(event):
    widget = event.widget
    widget._drag_start_x = event.x
    widget._drag_start_y = event.y

def on_drag_motion(event):
    widget = event.widget
    x = widget.winfo_x() 
    y = widget.winfo_y() - widget._drag_start_y + event.y
    widget.place(x=x, y=y)
'''
#Initialize gui and pack
root = Tk()
root.config(background='black')
root.title("My Checklist")

screen_width = int(math.floor((root.winfo_screenwidth() - 6) / 5))
screen_height = root.winfo_screenheight() - 72
geostring = ""+str(screen_width+1)+"x"+str(screen_height)+"+"+str(screen_width*4)+"+"+str(0)
root.geometry(geostring)

#creating the entry box, initialized
e = Entry(root, text="Enter a todo", width= screen_width, bg='black', fg='white',font='sans 16 bold')
e.bind("<Button-1>", some_callback)

#creating the main button
but = Button(root, text="MAKE NEW", padx=500, pady=50, command=stopgap, bg='black', fg='white', font='sans 16 bold')

but.pack(side=BOTTOM)
e.pack(side=BOTTOM)

e.insert(0, starting_input)
e.focus_set()

root.bind("<Key>",key_pressed)

if box['todo'] == [] and box['forget'] == [] and os.path.exists(List_folder):
    with open(List_folder, 'r') as lf:
        tmp = json.load(lf)
    for i in tmp['todo']:
        makeChecker(i)
    box['forget'] = tmp['forget']

#Run EventLoop
if __name__ == "__main__":
    root.mainloop()




#https://www.youtube.com/watch?v=YXPyB4XeYLA
#YOU WERE DOING WINDOW POSITIONING W/ ".geometry()
