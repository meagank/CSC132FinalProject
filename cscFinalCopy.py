from Tkinter import *



class Background(Frame):
    

    def __init__(self,parent):
        Frame.__init__(self, parent)
        self.initUI()

    def initUI(self):
        self.master.title("Checkers")
        self.pack(fill=BOTH, expand=1)
        self.canvas = Canvas(self)


        drag_data = {"x": 0, "y": 0, "item": None}
        init_data = {"x": 0, "y": 0, "item": None}
        final_coord = [0,0]    

        # create the checkerboard
        #### ROW 1 ####
        self.canvas.create_rectangle(30, 10, 122, 62, outline="black", fill="black", tags = "black")
        self.canvas.create_rectangle(122, 10, 214, 62, outline="white", fill="white")
        self.canvas.create_rectangle(214, 10, 306, 62, outline="black", fill="black", tags = "black")
        self.canvas.create_rectangle(306, 10, 398, 62, outline="white", fill="white")
        self.canvas.create_rectangle(398, 10, 490, 62, outline="black", fill="black", tags = "black")
        self.canvas.create_rectangle(490, 10, 582, 62, outline="white", fill="white")
        self.canvas.create_rectangle(582, 10, 674, 62, outline="black", fill="black", tags = "black")
        self.canvas.create_rectangle(674, 10, 766, 62, outline="white", fill="white")

        #### ROW 2 ####
        self.canvas.create_rectangle(30, 62, 122, 114, outline="white", fill="white")
        self.canvas.create_rectangle(122, 62, 214, 114, outline="black", fill="black", tags = "black")
        self.canvas.create_rectangle(214, 62, 306, 114, outline="white", fill="white")
        self.canvas.create_rectangle(306, 62, 398, 114, outline="black", fill="black", tags = "black")
        self.canvas.create_rectangle(398, 62, 490, 114, outline="white", fill="white")
        self.canvas.create_rectangle(490, 62, 582, 114, outline="black", fill="black", tags = "black")
        self.canvas.create_rectangle(582, 62, 674, 114, outline="white", fill="white")
        self.canvas.create_rectangle(674, 62, 766, 114, outline="black", fill="black", tags = "black")


        #### ROW 3 ####
        self.canvas.create_rectangle(30, 114, 122, 166, outline="black", fill="black", tags = "black")
        self.canvas.create_rectangle(122, 114, 214, 166, outline="white", fill="white")
        self.canvas.create_rectangle(214, 114, 306, 166, outline="black", fill="black", tags = "black")
        self.canvas.create_rectangle(306, 114, 398, 166, outline="white", fill="white")
        self.canvas.create_rectangle(398, 114, 490, 166, outline="black", fill="black", tags = "black")
        self.canvas.create_rectangle(490, 114, 582, 166, outline="white", fill="white")
        self.canvas.create_rectangle(582, 114, 674, 166, outline="black", fill="black", tags = "black")
        self.canvas.create_rectangle(674, 114, 766, 166, outline="white", fill="white")

        #### ROW 4 ####
        self.canvas.create_rectangle(30, 166, 122, 218, outline="white", fill="white")
        self.canvas.create_rectangle(122, 166, 214, 218, outline="black", fill="black", tags = "black")
        self.canvas.create_rectangle(214, 166, 306, 218, outline="white", fill="white")
        self.canvas.create_rectangle(306, 166, 398, 218, outline="black", fill="black", tags = "black")
        self.canvas.create_rectangle(398, 166, 490, 218, outline="white", fill="white")
        self.canvas.create_rectangle(490, 166, 582, 218, outline="black", fill="black", tags = "black")
        self.canvas.create_rectangle(582, 166, 674, 218, outline="white", fill="white")
        self.canvas.create_rectangle(674, 166, 766, 218, outline="black", fill="black", tags = "black")

        #### ROW 5 ####
        self.canvas.create_rectangle(30, 218, 122, 270, outline="black", fill="black", tags = "black")
        self.canvas.create_rectangle(122, 218, 214, 270, outline="white", fill="white")
        self.canvas.create_rectangle(214, 218, 306, 270, outline="black", fill="black", tags = "black")
        self.canvas.create_rectangle(306, 218, 398, 270, outline="white", fill="white")
        self.canvas.create_rectangle(398, 218, 490, 270, outline="black", fill="black", tags = "black")
        self.canvas.create_rectangle(490, 218, 582, 270, outline="white", fill="white")
        self.canvas.create_rectangle(582, 218, 674, 270, outline="black", fill="black", tags = "black")
        self.canvas.create_rectangle(674, 218, 766, 270, outline="white", fill="white")

        #### ROW 6 ####
        self.canvas.create_rectangle(30, 270, 122, 322, outline="white", fill="white")
        self.canvas.create_rectangle(122, 270, 214, 322, outline="black", fill="black", tags = "black")
        self.canvas.create_rectangle(214, 270, 306, 322, outline="white", fill="white")
        self.canvas.create_rectangle(306, 270, 398, 322, outline="black", fill="black", tags = "black")
        self.canvas.create_rectangle(398, 270, 490, 322, outline="white", fill="white")
        self.canvas.create_rectangle(490, 270, 582, 322, outline="black", fill="black", tags = "black")
        self.canvas.create_rectangle(582, 270, 674, 322, outline="white", fill="white")
        self.canvas.create_rectangle(674, 270, 766, 322, outline="black", fill="black", tags = "black")

        #### ROW 7 ####
        self.canvas.create_rectangle(30, 322, 122, 374, outline="black", fill="black", tags = "black")
        self.canvas.create_rectangle(122, 322, 214, 374, outline="white", fill="white")
        self.canvas.create_rectangle(214, 322, 306, 374, outline="black", fill="black", tags = "black")
        self.canvas.create_rectangle(306, 322, 398, 374, outline="white", fill="white")
        self.canvas.create_rectangle(398, 322, 490, 374, outline="black", fill="black", tags = "black")
        self.canvas.create_rectangle(490, 322, 582, 374, outline="white", fill="white")
        self.canvas.create_rectangle(582, 322, 674, 374, outline="black", fill="black", tags = "black")
        self.canvas.create_rectangle(674, 322, 766, 374, outline="white", fill="white")


        #### ROW 8 ####
        self.canvas.create_rectangle(30, 374, 122, 424, outline="white", fill="white")
        self.canvas.create_rectangle(122, 374, 214, 424, outline="black", fill="black", tags = "black")
        self.canvas.create_rectangle(214, 374, 306, 424, outline="white", fill="white")
        self.canvas.create_rectangle(306, 374, 398, 424, outline="black", fill="black", tags = "black")
        self.canvas.create_rectangle(398, 374, 490, 424, outline="white", fill="white")
        self.canvas.create_rectangle(490, 374, 582, 424, outline="black", fill="black", tags = "black")
        self.canvas.create_rectangle(582, 374, 674, 424, outline="white", fill="white")
        self.canvas.create_rectangle(674, 374, 766, 424, outline="black", fill="black", tags = "black")

        self.canvas.pack(fill=BOTH, expand=1)  


class Square:

    def __init__(self):
        top = 1
        bottom = 10
        left = 1
        right = 10
        content = 99

    def setUpSquare(self, counter):


        if (counter < 9):
            top = 10
            bottom = 62
        elif (counter < 17):
            top = 62
            bottom = 114
        elif (counter < 25):
            top = 114
            bottom = 166
        elif (counter < 33):
            top = 166
            bottom = 218
        elif (counter < 41):
            top = 218
            bottom = 270
        elif (counter < 49):
            top = 270
            bottom = 322
        elif (counter < 57):
            top = 322
            bottom = 374
        else:
            top = 374
            bottom = 424


        if (counter % 8 == 1):
            left = 30
            right = 122
        elif (counter % 8 == 2):
            left = 122
            right = 214
        elif (counter % 8 == 3):
            left = 214
            right = 306
        elif (counter % 8 == 4):
            left = 306
            right = 398
        elif (counter % 8 == 5):
            left = 398
            right = 490
        elif (counter % 8 == 6):
            left = 490
            right = 582
        elif (counter % 8 == 7):
            left = 582
            right = 674
        else:
            left = 674
            right = 766


        if (counter < 9):
            if counter % 2 == 0:
                content = counter / 2
        elif (counter < 17):
            if counter % 2 == 1:
                content = counter / 2
        elif (counter < 25):
            if counter % 2 == 0:
                content = counter / 2
        elif (counter > 40 and counter < 49):
            if counter % 2 == 1:
                content = counter / 2
        elif (counter > 48 and counter < 57):
            if counter % 2 == 0:
                content = counter / 2
        elif (counter > 56 and counter <= 64):
            if counter % 2 == 1:
                content = counter / 2

    def getleft(self):
        return left

    def getright(self):
        return right

    def gettop(self):
        return top

    def getbottom(self):
        return bottom
       

class Pieces:

    def __init__(self):
        # 1 = red, 0 = blue
        color = 1
        king = False
        life = True
        square = 1

    def color(self, x):
        if (x < 13):
            color = 1
        elif (x < 25):
            color = 0


        
    
############### MAIN ###############
def main():
    root = Tk()
    root.geometry("800x450+200+200")
    s = Square()
    p = Pieces()
    b = Background(root)
    root.mainloop()

        
    counter = 1
    squares = []

    while counter < 65:
        tmp = Square()
        squares.append(tmp)
        counter += 1

    counter = 1
    i = 0
    while counter < 65:
        s.setUpSquare(counter)
        squares[i]

        counter += 1
        i += 1

    x = 1
    pieces = []
    while x < 25:
        tmp2 = Pieces()
        pieces.append(tmp2)
        x += 1

    x = 1
    while x < 25:
        p.color(x)
        x += 1

########### Create board and pieces ###########
    for counter in range(len(pieces)):
        location = pieces[counter].square
        left = squares[location].left
        right = squares[location].right
        top = squares[location].top
        bottom = squares[location].bottom
        color = pieces[counter].color



if __name__ == "__main__":
    main()
        


