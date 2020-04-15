from Tkinter import *

class Board(Frame):

    def __init__(self):
        Frame.__init__(self)

        self.initUI()

            


    def initUI(self):

        self.master.title("Checkers")
        self.pack(fill=BOTH, expand=1)

        canvas = Canvas(self)

        #### ROW 1 ####
        canvas.create_rectangle(30, 10, 90, 80, outline="black", fill="black")
        canvas.create_rectangle(90, 10, 150, 80, outline="white", fill="white")
        canvas.create_rectangle(150, 10, 210, 80, outline="black", fill="black")
        canvas.create_rectangle(210, 10, 270, 80, outline="white", fill="white")
        canvas.create_rectangle(270, 10, 330, 80, outline="black", fill="black")
        canvas.create_rectangle(330, 10, 390, 80, outline="white", fill="white")
        canvas.create_rectangle(390, 10, 450, 80, outline="black", fill="black")
        canvas.create_rectangle(450, 10, 510, 80, outline="white", fill="white")
        

        #### ROW 2 ####
        canvas.create_rectangle(30, 80, 90, 150, outline="white", fill="white")
        canvas.create_rectangle(90, 80, 150, 150, outline="black", fill="black")
        canvas.create_rectangle(150, 80, 210, 150, outline="white", fill="white")
        canvas.create_rectangle(210, 80, 270, 150, outline="black", fill="black")
        canvas.create_rectangle(270, 80, 330, 150, outline="white", fill="white")
        canvas.create_rectangle(330, 80, 390, 150, outline="black", fill="black")
        canvas.create_rectangle(390, 80, 450, 150, outline="white", fill="white")
        canvas.create_rectangle(450, 80, 510, 150, outline="black", fill="black")


        #### ROW 3 ####
        canvas.create_rectangle(30, 150, 90, 220, outline="black", fill="black")
        canvas.create_rectangle(90, 150, 150, 220, outline="white", fill="white")
        canvas.create_rectangle(150, 150, 210, 220, outline="black", fill="black")
        canvas.create_rectangle(210, 150, 270, 220, outline="white", fill="white")
        canvas.create_rectangle(270, 150, 330, 220, outline="black", fill="black")
        canvas.create_rectangle(330, 150, 390, 220, outline="white", fill="white")
        canvas.create_rectangle(390, 150, 450, 220, outline="black", fill="black")
        canvas.create_rectangle(450, 150, 510, 220, outline="white", fill="white")

        #### ROW 4 ####
        canvas.create_rectangle(30, 220, 90, 290, outline="white", fill="white")
        canvas.create_rectangle(90, 220, 150, 290, outline="black", fill="black")
        canvas.create_rectangle(150, 220, 210, 290, outline="white", fill="white")
        canvas.create_rectangle(210, 220, 270, 290, outline="black", fill="black")
        canvas.create_rectangle(270, 220, 330, 290, outline="white", fill="white")
        canvas.create_rectangle(330, 220, 390, 290, outline="black", fill="black")
        canvas.create_rectangle(390, 220, 450, 290, outline="white", fill="white")
        canvas.create_rectangle(450, 220, 510, 290, outline="black", fill="black")

        #### ROW 5 ####
        canvas.create_rectangle(30, 290, 90, 360, outline="black", fill="black")
        canvas.create_rectangle(90, 290, 150, 360, outline="white", fill="white")
        canvas.create_rectangle(150, 290, 210, 360, outline="black", fill="black")
        canvas.create_rectangle(210, 290, 270, 360, outline="white", fill="white")
        canvas.create_rectangle(270, 290, 330, 360, outline="black", fill="black")
        canvas.create_rectangle(330, 290, 390, 360, outline="white", fill="white")
        canvas.create_rectangle(390, 290, 450, 360, outline="black", fill="black")
        canvas.create_rectangle(450, 290, 510, 360, outline="white", fill="white")

        #### ROW 6 ####
        canvas.create_rectangle(30, 360, 90, 430, outline="white", fill="white")
        canvas.create_rectangle(90, 360, 150, 430, outline="black", fill="black")
        canvas.create_rectangle(150, 360, 210, 430, outline="white", fill="white")
        canvas.create_rectangle(210, 360, 270, 430, outline="black", fill="black")
        canvas.create_rectangle(270, 360, 330, 430, outline="white", fill="white")
        canvas.create_rectangle(330, 360, 390, 430, outline="black", fill="black")
        canvas.create_rectangle(390, 360, 450, 430, outline="white", fill="white")
        canvas.create_rectangle(450, 360, 510, 430, outline="black", fill="black")

        #### ROW 7 ####
        canvas.create_rectangle(30, 430, 90, 500, outline="black", fill="black")
        canvas.create_rectangle(90, 430, 150, 500, outline="white", fill="white")
        canvas.create_rectangle(150, 430, 210, 500, outline="black", fill="black")
        canvas.create_rectangle(210, 430, 270, 500, outline="white", fill="white")
        canvas.create_rectangle(270, 430, 330, 500, outline="black", fill="black")
        canvas.create_rectangle(330, 430, 390, 500, outline="white", fill="white")
        canvas.create_rectangle(390, 430, 450, 500, outline="black", fill="black")
        canvas.create_rectangle(450, 430, 510, 500, outline="white", fill="white")


        #### ROW 8 ####
        canvas.create_rectangle(30, 500, 90, 570, outline="white", fill="white")
        canvas.create_rectangle(90, 500, 150, 570, outline="black", fill="black")
        canvas.create_rectangle(150, 500, 210, 570, outline="white", fill="white")
        canvas.create_rectangle(210, 500, 270, 570, outline="black", fill="black")
        canvas.create_rectangle(270, 500, 330, 570, outline="white", fill="white")
        canvas.create_rectangle(330, 500, 390, 570, outline="black", fill="black")
        canvas.create_rectangle(390, 500, 450, 570, outline="white", fill="white")
        canvas.create_rectangle(450, 500, 510, 570, outline="black", fill="black")


        canvas.pack(fill=BOTH, expand=1)


        





def main():

    root = Tk()
    ex = Board()
    root.geometry("540x600+200+200")
    root.mainloop()


if __name__ == '__main__':
    main()
