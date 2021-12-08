import tkinter as tk
WINDOW_WIDTH, WINDOW_HEIGHT = 600, 400
root = tk.Tk()
window = tk.Canvas(root, width = WINDOW_WIDTH, height = WINDOW_HEIGHT, bg = "white")

def createaction(l):
    def enter_letter():
        pass
    return enter_letter

alpha = ('A', 'B', 'C', 'D', 'E', 'F', 'H', 'I', 'J', 'K' ,'L' ,'M' ,'N' ,'O' ,'P' ,'Q', 'R', 'S','T' ,'U' ,'V', 'W', 'X', 'Y', 'Z')
for i,l in enumerate (alpha):
    bouton = tk.Button (root, text=l, command = createaction(l), bg="white")
    bouton.grid (row = 1+i//25, column = i%25)
root.title("Jeu du pendu")
window.grid (row = 0, column = 0, columnspan = 27)

root.mainloop()
    
