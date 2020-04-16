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
        canvas.create_rectangle(30, 10, 122, 62, outline="black", fill="black")
        canvas.create_rectangle(122, 10, 214, 62, outline="white", fill="white")
        canvas.create_rectangle(214, 10, 306, 62, outline="black", fill="black")
        canvas.create_rectangle(306, 10, 398, 62, outline="white", fill="white")
        canvas.create_rectangle(398, 10, 490, 62, outline="black", fill="black")
        canvas.create_rectangle(490, 10, 582, 62, outline="white", fill="white")
        canvas.create_rectangle(582, 10, 674, 62, outline="black", fill="black")
        canvas.create_rectangle(674, 10, 766, 62, outline="white", fill="white")
        

        #### ROW 2 ####
        canvas.create_rectangle(30, 62, 122, 114, outline="white", fill="white")
        canvas.create_rectangle(122, 62, 214, 114, outline="black", fill="black")
        canvas.create_rectangle(214, 62, 306, 114, outline="white", fill="white")
        canvas.create_rectangle(306, 62, 398, 114, outline="black", fill="black")
        canvas.create_rectangle(398, 62, 490, 114, outline="white", fill="white")
        canvas.create_rectangle(490, 62, 582, 114, outline="black", fill="black")
        canvas.create_rectangle(582, 62, 674, 114, outline="white", fill="white")
        canvas.create_rectangle(674, 62, 766, 114, outline="black", fill="black")


        #### ROW 3 ####
        canvas.create_rectangle(30, 114, 122, 166, outline="black", fill="black")
        canvas.create_rectangle(122, 114, 214, 166, outline="white", fill="white")
        canvas.create_rectangle(214, 114, 306, 166, outline="black", fill="black")
        canvas.create_rectangle(306, 114, 398, 166, outline="white", fill="white")
        canvas.create_rectangle(398, 114, 490, 166, outline="black", fill="black")
        canvas.create_rectangle(490, 114, 582, 166, outline="white", fill="white")
        canvas.create_rectangle(582, 114, 674, 166, outline="black", fill="black")
        canvas.create_rectangle(674, 114, 766, 166, outline="white", fill="white")

        #### ROW 4 ####
        canvas.create_rectangle(30, 166, 122, 218, outline="white", fill="white")
        canvas.create_rectangle(122, 166, 214, 218, outline="black", fill="black")
        canvas.create_rectangle(214, 166, 306, 218, outline="white", fill="white")
        canvas.create_rectangle(306, 166, 398, 218, outline="black", fill="black")
        canvas.create_rectangle(398, 166, 490, 218, outline="white", fill="white")
        canvas.create_rectangle(490, 166, 582, 218, outline="black", fill="black")
        canvas.create_rectangle(582, 166, 674, 218, outline="white", fill="white")
        canvas.create_rectangle(674, 166, 766, 218, outline="black", fill="black")

        #### ROW 5 ####
        canvas.create_rectangle(30, 218, 122, 270, outline="black", fill="black")
        canvas.create_rectangle(122, 218, 214, 270, outline="white", fill="white")
        canvas.create_rectangle(214, 218, 306, 270, outline="black", fill="black")
        canvas.create_rectangle(306, 218, 398, 270, outline="white", fill="white")
        canvas.create_rectangle(398, 218, 490, 270, outline="black", fill="black")
        canvas.create_rectangle(490, 218, 582, 270, outline="white", fill="white")
        canvas.create_rectangle(582, 218, 674, 270, outline="black", fill="black")
        canvas.create_rectangle(674, 218, 766, 270, outline="white", fill="white")

        #### ROW 6 ####
        canvas.create_rectangle(30, 270, 122, 322, outline="white", fill="white")
        canvas.create_rectangle(122, 270, 214, 322, outline="black", fill="black")
        canvas.create_rectangle(214, 270, 306, 322, outline="white", fill="white")
        canvas.create_rectangle(306, 270, 398, 322, outline="black", fill="black")
        canvas.create_rectangle(398, 270, 490, 322, outline="white", fill="white")
        canvas.create_rectangle(490, 270, 582, 322, outline="black", fill="black")
        canvas.create_rectangle(582, 270, 674, 322, outline="white", fill="white")
        canvas.create_rectangle(674, 270, 766, 322, outline="black", fill="black")

        #### ROW 7 ####
        canvas.create_rectangle(30, 322, 122, 374, outline="black", fill="black")
        canvas.create_rectangle(122, 322, 214, 374, outline="white", fill="white")
        canvas.create_rectangle(214, 322, 306, 374, outline="black", fill="black")
        canvas.create_rectangle(306, 322, 398, 374, outline="white", fill="white")
        canvas.create_rectangle(398, 322, 490, 374, outline="black", fill="black")
        canvas.create_rectangle(490, 322, 582, 374, outline="white", fill="white")
        canvas.create_rectangle(582, 322, 674, 374, outline="black", fill="black")
        canvas.create_rectangle(674, 322, 766, 374, outline="white", fill="white")


        #### ROW 8 ####
        canvas.create_rectangle(30, 374, 122, 424, outline="white", fill="white")
        canvas.create_rectangle(122, 374, 214, 424, outline="black", fill="black")
        canvas.create_rectangle(214, 374, 306, 424, outline="white", fill="white")
        canvas.create_rectangle(306, 374, 398, 424, outline="black", fill="black")
        canvas.create_rectangle(398, 374, 490, 424, outline="white", fill="white")
        canvas.create_rectangle(490, 374, 582, 424, outline="black", fill="black")
        canvas.create_rectangle(582, 374, 674, 424, outline="white", fill="white")
        canvas.create_rectangle(674, 374, 766, 424, outline="black", fill="black")

        canvas.pack(fill=BOTH, expand=1)
    

def main():

    root = Tk()
    ex = Board()
    root.geometry("800x425+200+200")
    root.mainloop()


if __name__ == '__main__':
    main()
