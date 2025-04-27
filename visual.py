from tkinter import Tk, BOTH, Canvas

class Window():

    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.root = Tk()
        self.root.title("root widget")
        self.canvas = Canvas(self.root)

        self.canvas.pack()

        self.isRunning = False
        self.root.protocol("WM_DELETE_WINDOW", self.close)


    def redraw(self):
        self.root.update_idletasks()
        self.root.update()


    def wait_for_close(self):
        self.isRunning = True
        while self.isRunning:
            self.redraw()


    def close(self):
        self.isRunning = False

