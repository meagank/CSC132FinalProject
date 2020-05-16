from Tkinter import *


class Background(Frame):
    

    def __init__(self,parent):
        Frame.__init__(self, parent)
        self.initUI()

        self._drag_data = {"x": 0, "y": 0, "item": None}
        
    def initUI(self):
        self.master.title("Checkers")
        self.pack(fill=BOTH, expand=1)
        self.canvas = Canvas(self)
        


        drag_data = {"x": 0, "y": 0, "item": None}
        init_data = {"x": 0, "y": 0, "item": None}   

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


    def draw(self, top, left, color):

        mx = top + 26
        my = left + 46

        if (color == 1):
            self.createToken(my, mx, "red")
        elif (color == 0):
            self.createToken(my, mx, "blue")


    def createToken(self, x, y, color):
        # create a checker piece at given coord
        aOval = self.canvas.create_oval(x - 25, y - 25,x + 25 , y + 25, outline= color , fill=color)
        # add bindings for clicking, dragging and releasing the pieces
        self.canvas.tag_bind(aOval, "<ButtonPress-1>", self.startDrag)
        self.canvas.tag_bind(aOval, "<ButtonRelease-1>", self.stopDrag)
        self.canvas.tag_bind(aOval, "<B1-Motion>", self.drag)
        
    def startDrag(self, event):
        # begin drag of a checker piece and record location
        self._drag_data["item"] = self.canvas.find_closest(event.x, event.y)[0]
        self._drag_data["x"] = event.x
        self._drag_data["y"] = event.y

    def stopDrag(self, event):
        # end drag of an object and information
        self._drag_data["item"] = None
        self._drag_data["x"] = 0
        self._drag_data["y"] = 0

    def drag(self, event):
        dimensionVert = [36, 88, 140, 192, 244, 296, 348, 400]
        dimensionHor = [76, 168, 260, 352, 444, 536, 628, 720]
        # handle dragging of an object 
        # determine move distance
        delta_x = event.x - self._drag_data["x"]
        delta_y = event.y - self._drag_data["y"]
        # move the object 
        self.canvas.move(self._drag_data["item"], delta_x, delta_y)
        offsetx = 999
        offsety = 999
        finalVert = 1
        finalHor = 1
        finalSquare = 1
        x = 0
        for vert in range(len(dimensionVert)):
            VCoord = dimensionVert[vert]
            if (abs(VCoord - event.y) < offsetx):
                # print " VCoord ===== {}, event.y ====== {}, offsety ===== {}, vert ==== {}".format(VCoord, event.x, offsetx, vert)
                finalVert =  vert
                offsetx = abs(VCoord - event.y)
        for horiz in range(len(dimensionHor)):
            HCoord = dimensionHor[horiz]
            if (abs(HCoord - event.x) < offsety):
                # print " HCoord ===== {}, event.x ====== {}, offsetx ===== {}, horiz===== {}".format(HCoord, event.y, offsety, horiz)
                finalHor = horiz
                offsety = abs(HCoord - event.x)
                # print "offsety ==== {}".format(offsety)

        #event.x = dimensionVert[finalVert]
        #event.y = dimensionHor[finalHor]
        finalSquare = (finalVert * 8) + finalHor + 1

        # print "finalSquare === {}, finalVert === {}, finalHor === {}".format(finalSquare, finalVert, finalHor)


        
        # record the new position
        self._drag_data["x"] = event.x
        self._drag_data["y"] = event.y

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
        self.color = 1
        king = False
        life = True
        self.square = 1
        self.token = 1

    def setColor(self, x):
        if (x < 13):
            return 1
        elif (x < 25):
            return 0

    def getColor(self):
        return self.color


    def getLocation(self):
         # print "getLocation === " + str(self.square)
        return self.square

    def setLocation(self, x, lastCounter):
        # print "SETLOCATION:  x, lastcounter " + str(x)+", "+str(lastCounter)
        if (x < 12):
            NotSet = True
            counter = lastCounter
            while (counter < 25 and NotSet == True):
                if counter < 9:
                    if (counter % 2 == 1):
                        # print "Counter === " + str(counter)
                        return counter
                    else:
                        counter += 1
                elif (counter < 17):
                    if (counter % 2 == 0):
                        # print "Counter === " + str(counter)
                        return counter
                    else:
                        counter += 1
                elif (counter < 25):
                    if (counter % 2 == 1):
                        # print "Counter === " + str(counter)
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
        pieces[i].color = tmp2.setColor(x)
        startSquare = tmp2.setLocation(i, lastCounter)
        # print "LASTCOUNTER, startSquare ===== " + str(lastCounter) +", " + str(startSquare)
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
        color = pieces[counter].getColor()
        # print (" location = {}, top = {}, bottom = {}, left = {}, right = {}").format(location, top, bottom, left, right)
        ##b.createToken(top, left, "red")
        b.draw(top,left, color)


    root.mainloop()  



if __name__ == "__main__":
    main()
        