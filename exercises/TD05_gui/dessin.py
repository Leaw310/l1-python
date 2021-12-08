from tkinter import*

CANVAS_WIDTH, CANVAS_HEIGHT = 600, 400
if __name__ == '__main__':
   
    root = Tk()
    canvas = Canvas(root, width = CANVAS_WIDTH, height = CANVAS_HEIGHT)

    # Début de votre code
    x0 = 100
    x1 = CANVAS_WIDTH - 300
    y = CANVAS_HEIGHT /2
    canvas.create_line(y, x1, y, x0)
    canvas.create_oval(y - 50, x0 + 50, y + 50, x0 - 50)
    canvas.create_oval(y - 50, x1 + 50, y + 50, x1 - 50)
    canvas.create_oval((x0 + x1) / 2 - 50, y + 50, (x0 + x1) / 2 + 50, y - 50)
    
    # Fin de votre code

    canvas.pack()
    root.mainloop()