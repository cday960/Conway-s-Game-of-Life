import tkinter as tk
import matrix
from time import sleep
from tkinter import ttk
from tkinter.messagebox import showinfo

#Root app class, tk.Tk() object
class App(tk.Tk):
    def __init__(self):
        super().__init__()
        
        #configures root window
        self.title('Game of Life')
        self.geometry('700x800')
        self.grid_anchor(tk.CENTER)
        self._frame = titleFrame(self)
        
    #Function to change the frame
    def switch_frame(self, frame_class):
        new_frame = frame_class(self)
        if self._frame is not None:
            self._frame.destroy()
        self._frame = new_frame
        self._frame.grid()


#Title frame class, first frame displayed when the app is launched
class titleFrame(ttk.Frame):
    def __init__(self, master):
        super().__init__(master)
        
        #root window settings
        self.grid()

        #styling
        style = ttk.Style()
        style.theme_use('aqua')
        style.configure('title.TLabel', background='#2b2b2b')
        
        #title label
        self.label = ttk.Label(self, 
                                text='The Game Of Life.', 
                                style='title.TLabel')
        self.label.grid()
        
        #start button
        self.button = ttk.Button(self, text='Start',
                                 command=lambda: master.switch_frame(lifeFrame))
        self.button.grid()
        

#Game frame, holds the actual game and the buttons to control it
class lifeFrame(tk.Frame):
    def __init__(self, App):
        super().__init__(App)

        #centers all of the grid placements
        self.grid_anchor(tk.CENTER)
        
        #creating the matrix
        self.matrix = matrix.Matrix(width=125, height=125)
        
        #scale for the cells that are drawn. higher scale = bigger cells
        self.scale = 5.6
        self.running = False
        self.generation = 1
        
        #setting up the canvas
        self.canvas = tk.Canvas(self, 
                                width=700, 
                                height=700, 
                                )
        self.canvas.grid(row=1, column=0, columnspan=3)
        
        #start button to begin the game
        self.startButton = tk.Button(self, text="Start", command=lambda: self.start())
        self.startButton.grid(row=0, column=1, sticky="E")
        
        #stop button
        self.stopButton = tk.Button(self, text="Stop", command=lambda: self.stop())
        self.stopButton.grid(row=0, column=2, sticky="W")
        
        #label that shows that number generation the game is on
        self.genLabel = tk.Label(self, text="Generation: 0")
        self.genLabel.grid(row=0, column=0)
        
        #draws the initial matrix onto the canvas
        for row in range(len(self.matrix.m)):
            for col in range(len(self.matrix.m[row])):
                if self.matrix.m[row][col] == 1:
                    y0 = row-1 if row != 0 else 0
                    x0 = col-1 if col != 0 else 0
                    self.canvas.create_rectangle(x0*self.scale, 
                                                 y0*self.scale,
                                                 col*self.scale,
                                                 row*self.scale,
                                                 fill="blue")
                    
       
    
    #starts the actual game
    def nextGen(self):
        if self.running:
            self.startButton.configure(state='disabled') #disables the start button since it can't be pressed during the game
            
            #loop that makes each new generation and draws it onto the canvas
            # for i in range(generations):
            self.canvas.delete('all')
            self.matrix.m = matrix.nextGeneration(self.matrix) #updates the matrix to the next generation
            
            for row in range(self.matrix.height):
                for col in range(self.matrix.width):
                    if self.matrix.m[row][col] == 1:
                        y0 = row-1 if row != 0 else 0
                        x0 = col-1 if col != 0 else 0
                        self.canvas.create_rectangle(x0*self.scale,
                                                    y0*self.scale,
                                                    col*self.scale,
                                                    row*self.scale,
                                                    fill="blue")
        
        #to optimize this I could assign a tag to each rectangle and only redraw it if it's value is different from the previous generation, but that would require a lot more logic
        #I'm not sure if the limitation is actually drawing the rectangles or generating the next generation, but if the matrix size goes over 125 it slows down significantly
            self.update()
            self.genLabel.configure(text="Generation: " + str(self.generation))
            self.generation += 1
            self.after(5, self.nextGen())
            #region
            # new_mat = "\n".join([" ".join([str(x) for x in y]) for y in self.matrix.m])
            # self.label.configure(text=new_mat)
            # self.genCounter.configure(text="Generation: "+str(i+1))
            #endregion
    
    def start(self):
        self.running = True
        self.nextGen()
    
    def stop(self):
        self.running = False
        self.startButton.configure(state='normal')

if __name__ == '__main__':
    app = App()
    app.mainloop()
