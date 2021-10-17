import tkinter as tk
from tkinter.constants import BOTH

class App(tk.Tk):
    def __init__(self):
        super().__init__()

        self.geometry("500x500+300+300")
        self.canvas = tk.Canvas(self, bg="white")
        self.canvas.pack(fill=BOTH, expand=1)
        # self.update()

        self.headers = ['a', 'b', 'c', 'd']
        self.circle_positions =  {4 : [(0, 0, 333, 333), (167, 0, 500, 333), (0, 167, 333, 500), (167, 167, 500, 500)],
            3 : [(0, 0, 333, 333), (0, 167, 333, 500), (167, 84, 500, 417)],
            2 : [(0, 0, 400, 400), (100, 100, 500, 500)]
            }
        self.headers_position = {4 : [(30, 30), (470, 30), (30, 470), (470, 470)],
            3 : [(30, 30), (417, 84), (30, 470)],
            2 : [(30, 30), (470, 470)]
        }
        
        for i in self.circle_positions[len(self.headers)]:
            self.canvas.create_oval(i)

        for i in range(len(self.headers)):
            self.canvas.create_text(self.headers_position[len(self.headers)][i], text=f'{self.headers[i]}', font='24')

        # self.canvas.create_arc(10, 10, 190, 190, 
        #      start=200, extent=100, 
        #      style=tk.CHORD, fill='green')

if __name__ == "__main__":
    App().mainloop()