from Tkinter import *
import numpy as np


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

        ##self.canvas.create_oval(100, 100, 150, 150, outline="red", fill="red")
        ##self.createToken(1, 1, "red")
        ##self.draw(1,1)

        self.canvas.pack(fill=BOTH, expand=1)
        ##self.draw(1,1)


    


    def draw(self, top, left):

        mx = top + 26
        my = left + 46
        self.createToken(my, mx, "red")
        ##createToken(my, mx, "red")
        ##self.canvas.create_oval(100, 100, 150, 150, outline="red", fill="red")

    def createToken(self, x, y, color):
        ##print x
        # create a checker piece at given coord
        aOval = self.canvas.create_oval(x - 25, y - 25,x + 25 , y + 25, outline="red", fill="red")
##        return aOval
##        self.canvas.create_oval(1, 1, x + 25, y + 25, outline=color, fill=color,tags=("token",),)


class Square:

    def __init__(self):
        self.top = 1
        self.bottom = 10
        self.left = 1
        self.right = 10
        content = 99


    def setUpSquare(self, counter):

        # based off of place in list, determines top and bottom x - coord
        if (counter < 9):
            self.top = 10
            self.bottom = 62
        elif (counter < 17):
            self.top = 62
            self.bottom = 114
        elif (counter < 25):
            self.top = 114
            self.bottom = 166
        elif (counter < 33):
            self.top = 166
            self.bottom = 218
        elif (counter < 41):
            self.top = 218
            self.bottom = 270
        elif (counter < 49):
            self.top = 270
            self.bottom = 322
        elif (counter < 57):
            self.top = 322
            self.bottom = 374
        else:
            self.top = 374
            self.bottom = 424

        
        # based off of place in list, determines left and right y - coord
        if (counter % 8 == 1):
            self.left = 30
            self.right = 122
        elif (counter % 8 == 2):
            self.left = 122
            self.right = 214
        elif (counter % 8 == 3):
            self.left = 214
            self.right = 306
        elif (counter % 8 == 4):
            self.left = 306
            self.right = 398
        elif (counter % 8 == 5):
            self.left = 398
            self.right = 490
        elif (counter % 8 == 6):
            self.left = 490
            self.right = 582
        elif (counter % 8 == 7):
            self.left = 582
            self.right = 674
        else:
            self.left = 674
            self.right = 766


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

       ## print "SETUPSQ: counter, top, bottom, left, right, content:  " + str(counter) +", " + str(top) + ", " + str(bottom)+", " + str(left)+", "+str(right)+", "+str(content)
        

    def getleft(self):
      #  print "getleft === " + str(self.left)
        return self.left

    def getright(self):
      #  print "getright === " + str(self.right)
        return self.right

    def gettop(self):
      #  print "gettop === " + str(self.top)
        return self.top

    def getbottom(self):
      #  print "getbottom === " + str(self.bottom)
        return self.bottom
       

class Pieces:

    def __init__(self):
        # 1 = red, 0 = blue
        color = 1
        king = False
        life = True
        self.square = 1
        self.token = 1

    def color(self, x):
        if (x < 13):
            color = 1
        elif (x < 25):
            color = 0


    def getLocation(self):
         # print "getLocation === " + str(self.square)
        return self.square

    def setLocation(self, x, lastCounter):
        print "SETLOCATION:  x, lastcounter " + str(x)+", "+str(lastCounter)
        if (x < 12):
            NotSet = True
            counter = lastCounter
            while (counter < 25 and NotSet == True):
                if counter < 9:
                    if (counter % 2 == 1):
                        print "Counter === " + str(counter)
                        return counter
                    else:
                        counter += 1
                elif (counter < 17):
                    if (counter % 2 == 0):
                        print "Counter === " + str(counter)
                        return counter
                    else:
                        counter += 1
                elif (counter < 25):
                    if (counter % 2 == 1):
                        print "Counter === " + str(counter)
                        return counter
                    else:
                        counter += 1
                else:
                    print "Error"
        elif (x < 24):
            if lastCounter < 41:
                counter = 41
            else:
                counter = lastCounter
            while (counter < 65):
                if counter < 49:
                    if counter % 2 == 0:
                       # print "Counter === " + str(counter)
                        return counter
                    else:
                        counter += 1
                elif (counter < 57):
                    if counter % 2 == 1:
                       # print "Counter === " + str(counter)
                        return counter
                    else:
                        counter += 1
                elif (counter < 65):
                    if counter % 2 == 0:
                        return counter
                    else:
                        counter += 1
                else:
                    print "Error"


            
    
############### MAIN ###############
def main():
    root = Tk()
    root.geometry("800x450+200+200")
    s = Square()
    p = Pieces()
    b = Background(root)
##    root.mainloop()

        
    counter = 1
    squares = []
    i = 0

    while counter < 65:
        tmp = Square()
        squares.append(tmp)
        squares[i].setUpSquare(counter)
       # print "in whule counter=== " + str(counter) + ", i=== " + str(i)
        counter += 1
        i += 1

##    counter = 1
##    i = 0
##    while counter < 65:
##        s.setUpSquare(counter)
##        squares[i].setUpSquare(counter)
##
##        counter += 1
##        i += 1

    x = 1
    pieces = []
    i = 0
    lastCounter = 1
    while x < 25:
        tmp2 = Pieces()
        pieces.append(tmp2)
        pieces[i].color(x)
        startSquare = tmp2.setLocation(i, lastCounter)
        print "LASTCOUNTER, startSquare ===== " + str(lastCounter) +", " + str(startSquare)
        pieces[i].square = startSquare
        lastCounter = startSquare + 1
        x += 1
        i += 1

        


##    x = 1
##    i = 0
##    while x < 25:
##        p.color(x)
##        pieces[i].color(x)
##        x += 1
##        i += 1

        


    for counter in range(len(pieces)):
        location = pieces[counter].getLocation()
        left = squares[location - 1].getleft()
        right = squares[location - 1].getright()
        top = squares[location - 1].gettop()
        bottom = squares[location - 1].getbottom()
        color = pieces[counter].color
        print (" location = {}, top = {}, bottom = {}, left = {}, right = {}").format(location, top, bottom, left, right)
        ##b.createToken(top, left, "red")
        b.draw(top,left)


    root.mainloop()  



if __name__ == "__main__":
    main()
        
