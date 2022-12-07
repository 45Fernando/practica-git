import tkinter as tk
import tkinter.font as tkFont

class App:
    def __init__(self, root):
        #setting title
        root.title("PROGRAMA")
        #setting window size
        width=600
        height=500
        screenwidth = root.winfo_screenwidth()
        screenheight = root.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        root.geometry(alignstr)
        root.resizable(width=False, height=False)

        GButton_538=tk.Button(root)
        GButton_538["bg"] = "#1e9fff"
        ft = tkFont.Font(family='Times',size=10)
        GButton_538["font"] = ft
        GButton_538["fg"] = "#000000"
        GButton_538["justify"] = "center"
        GButton_538["text"] = "Comprar"
        GButton_538["relief"] = "ridge"
        GButton_538.place(x=380,y=100,width=70,height=25)
        GButton_538["command"] = self.GButton_538_command

        GButton_579=tk.Button(root)
        GButton_579["bg"] = "#ff5722"
        ft = tkFont.Font(family='Times',size=10)
        GButton_579["font"] = ft
        GButton_579["fg"] = "#000000"
        GButton_579["justify"] = "center"
        GButton_579["text"] = "Cancelar"
        GButton_579.place(x=380,y=140,width=70,height=25)
        GButton_579["command"] = self.GButton_579_command

    def GButton_538_command(self):
        print("COMPRAR")


    def GButton_579_command(self):
        print("CANCELAR")

if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()
