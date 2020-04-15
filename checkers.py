from Tkinter import *

class Board(Frame):

    def __init__(self):
        Frame.__init__(self)

        self.initUI()

            


    def initUI(self):

        self.master.title("Checkers")
        self.pack(fill=BOTH, expand=1)

        canvas = Canvas(self)

        #### ROW 1 ###
        canvas.create_rectangle(30, 10, 90, 80, outline="black", fill="black")
        canvas.create_rectangle(90, 10, 150, 80, outline="white", fill="white")
        canvas.create_rectangle(150, 10, 210, 80, outline="black", fill="black")
        canvas.create_rectangle(210, 10, 270, 80, outline="white", fill="white")
        canvas.create_rectangle(270, 10, 330, 80, outline="black", fill="black")
        canvas.create_rectangle(330, 10, 390, 80, outline="white", fill="white")
        canvas.create_rectangle(390, 10, 450, 80, outline="black", fill="black")
        canvas.create_rectangle(450, 10, 510, 80, outline="white", fill="white")
        canvas.pack(fill=BOTH, expand=1)





def main():

    root = Tk()
    ex = Board()
    root.geometry("540x460+200+200")
    root.mainloop()


if __name__ == '__main__':
    main()
