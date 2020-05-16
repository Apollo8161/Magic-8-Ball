import tkinter as tk
import random
import time

HEIGHT = 600
WIDTH = 600

responses = {
    1:'It is certain.',
    2:'It is decidedly so.',
    3:'Without a doubt.',
    4:'Yes - definitely.',
    5:'You may rely on it',
    6:'As I see it, yes.',
    7:'Most likely.',
    8:'Outlook good.',
    9:'Yes.',
    10:'Signs point to yes.',
    11:'Reply hazy, try agin.',
    12:'Ask again later.',
    13:'Better not tell you now.',
    14:'Cannot predict now.',
    15:'Concentrate and ask again.',
    16:'Don\'t count on it.',
    17:'My reply is no.',
    18:'My sources say no.',
    19:'Outlook not so good.',
    20:'Very doubtful.',
}

#main ball functionality
def ball():
    num = random.randint(1,20)
    text = tk.Label(canvas, text=responses[num], bg='#00154f', fg='white')
    text.place(x=WIDTH/2, y=HEIGHT/2, anchor='center')

root = tk.Tk()
root.title('Magic 8 Ball')
root.resizable(False, False)

frame = tk.Frame(root, bg='#00154f', height=HEIGHT, width=WIDTH)
frame.pack()

canvas = tk.Canvas(frame, bg='#00154f', height=HEIGHT, width=WIDTH)

#first two values are the x and y of the top left  and next two are the x and y of bottom rigth of square containing the circle
circle= canvas.create_oval(0, 0, WIDTH, HEIGHT, fill='black')

# first 2 first corner x and y, next 2 second corner x and y, next 2 third conrner x and y
triangle_coords = [40, HEIGHT/4, WIDTH-40, HEIGHT/4, WIDTH/2, HEIGHT]
triangle = canvas.create_polygon(triangle_coords, width=5, outline='#00154f', fill='#00154f')

button = tk.Button(canvas, text='SHAKE', command=ball, bg='#00154f', fg='white')
button.place(x=WIDTH/2, y=(HEIGHT*3)/4, anchor='center')
ext = tk.Button(canvas, text='Exit', command=quit, bg='red', fg='white')
ext.place(x=WIDTH/2,y=HEIGHT-40, anchor='center')

canvas.pack()

root.mainloop()