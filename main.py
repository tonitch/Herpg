from tkinter import Tk, Frame, Canvas


class Window(Frame):
    def __init__(self, master):
        super().__init__(master)
        self.height = 800
        self.width = 1000
        self.DrawGUI()
        self.mainloop()

    def DrawGUI(self):
        self.ToolsFrame = Frame(self.master, width=200, height=self.height+100)
        self.ToolsFrame.grid(column=0, row=0, rowspan=3)

        self.TilesFrame = Frame(self.master, width=self.width, height=50)
        self.TilesFrame.grid(column=1, row=0)

        self.PlyFrame = Frame(self.master, width=self.width, height=50)
        self.PlyFrame.grid(column=1, row=2)

        self.TockensFrame = Frame(self.master, width=200, height=self.height+100)
        self.TockensFrame.grid(column=2, row=0, rowspan=3)

        self.MainCanvas = Canvas(self.master, height=self.height, width=self.width)
        self.MainCanvas.grid(column=1, row=1)


def main():
    root = Tk()
    Window(root)


if __name__ == "__main__":
    main()
