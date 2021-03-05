from tkinter import *
import math

starting_input = "Start your To-Do List here"
recent_forget = list()

def eleminator(butt, tex):
    butt.pack_forget()
    recent_forget = tex

def undo():
    global recent_forget
    try:
        e.insert(0, recent_forget[-1])
        recent_forget = recent_forget[:-1]
        stopgap()
    except:
        pass

def makeChecker(t):
    global recent_forget
    b = Button()
    b = Button(root, text=t, command=lambda:[b.pack_forget(),recent_forget.append(t)], height=2,padx=1000, bg='black', fg='white', font='sans 16 bold', wraplength=300)
    #make_draggable(b)
    b.pack()
    e.focus_set()

def stopgap():
    if e.get() and e.get() != starting_input:
        makeChecker(e.get().upper())
        e.delete(0, "end")

def some_callback(event): # note that you must include the event as an arg, even if you don't use it.
    e.delete(0, "end")
    return None

def key_pressed(event):
    if event.char == '`':
        e.delete(0,'end')
        undo()
    if event.char == '\r':
        stopgap()
        
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

#Run EventLoop
if __name__ == "__main__":
    root.mainloop()




#https://www.youtube.com/watch?v=YXPyB4XeYLA
#YOU WERE DOING WINDOW POSITIONING W/ ".geometry()
