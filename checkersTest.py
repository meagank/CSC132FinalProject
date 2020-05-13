######################################################################
# Name: Jakira Williams
# Date: March 13, 2020
# Description: Checkers python game using Tkinter
######################################################################

from Tkinter import *
import tkMessageBox

class Board(Frame):

    def __init__(self, parent, kcoord,last_itm, was_moved, red_king, blue_king, moved):
        Frame.__init__(self, parent)
        
        self.last_itm = last_itm
        self.was_moved = was_moved
        self.red_king = red_king
        self.blue_king = blue_king
        self.moved = moved
        self.kcoord = kcoord
        
        self.initUI()

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

        # keep track of the coordinates of the checker pieces
        self._drag_data = {"x": 0, "y": 0, "item": None}

        def Coords(objID):
            coordinate = []

            # row coordinate
            if (objID >= 57):
                coordinate.append(8)
            elif (objID >= 49):
                coordinate.append(7)
            elif (objID >= 41):
                coordinate.append(6)
            elif (objID >= 33):
                coordinate.append(5)
            elif (objID >= 25):
                coordinate.append(4)
            elif (objID >= 17):
                coordinate.append(3)
            elif (objID >= 9):
                coordinate.append(2)
            else:
                coordinate.append(1)


            # column coordinate
            temp = objID % 8
            if (temp == 1):
                coordinate.append(1)
            elif (temp == 2):
                coordinate.append(2)
            elif (temp == 3):
                coordinate.append(3)
            elif (temp == 4):
                coordinate.append(4)
            elif (temp == 5):
                coordinate.append(5)
            elif (temp == 6):
                coordinate.append(6)
            elif (temp == 7):
                coordinate.append(7)
            else:
                coordinate.append(8)

            return coordinate

            

        def RectDims(coordinate):
            dims = []
            x1 = 0
            x2 = 0
            y1 = 0
            y2 = 0
            i = 1

            #configure dimensions
            while i < 9:
                #y-coordinates
                if coordinate[1] == i:
                    if i == 1:
                        x1 = 30
                        x2 = 122
                    elif i == 2:
                        x1 = 122
                        x2 = 214
                    elif i == 3:
                        x1 = 214
                        x2 = 306
                    elif i == 4:
                        x1 = 306
                        x2 = 398
                    elif i == 5:
                        x1 = 398
                        x2 = 490
                    elif i == 6:
                        x1 = 490
                        x2 = 582
                    elif i == 7:
                        x1 = 582
                        x2 = 674
                    elif i == 8:
                        x1 = 674
                        x2 = 766

                #x-coordinates
                if coordinate[0] == i:
                    if i == 1:
                        y1 = 10
                        y2 = 62
                    elif i == 2:
                        y1 = 62
                        y2 = 114
                    elif i == 3:
                        y1 = 114
                        y2 = 166
                    elif i == 4:
                        y1 = 166
                        y2 = 218
                    elif i == 5:
                        y1 = 218
                        y2 = 270
                    elif i == 6:
                        y1 = 270
                        y2 = 322
                    elif i == 7:
                        y1 = 322
                        y2 = 374
                    elif i == 8:
                        y1 = 374
                        y2 = 424
                i += 1

            dims.append(x1)
            dims.append(y1)
            dims.append(x2)
            dims.append(y2)

            return dims

        # create the checker pieces
        ##### RED CHECKER PIECES #####
        
        #### ROW 1 ####
        r1 = self.createToken(76, 36, "red")
        r2 = self.createToken(260, 36, "red")
        r3 = self.createToken(444, 36, "red")
        r4 = self.createToken(628, 36, "red")

        #### ROW 2 ####
        r5 = self.createToken(168, 88, "red")
        r6 = self.createToken(352, 88, "red")
        r7 = self.createToken(536, 88, "red")
        r8 = self.createToken(720, 88, "red")
        
        #### ROW 3 ####
        r9 = self.createToken(76, 140, "red")
        r10 = self.createToken(260, 140, "red")
        r11 = self.createToken(444, 140, "red")
        r12 = self.createToken(628, 140, "red")
        

        ##### BLUE CHECKER PIECES #####

        #### ROW 6 ####
        b1 = self.createToken(168, 296, "blue")
        b2 = self.createToken(352, 296, "blue")
        b3 = self.createToken(536, 296, "blue")
        b4 = self.createToken(720, 296, "blue")

        #### ROW 7 ####
        b5 = self.createToken(76, 348, "blue")
        b6 = self.createToken(260, 348, "blue")
        b7 = self.createToken(444, 348, "blue")
        b8 = self.createToken(628, 348, "blue")

        #### ROW 8 ####
        b9 = self.createToken(168, 399, "blue")
        b10 = self.createToken(352, 399, "blue")
        b11 = self.createToken(536, 399, "blue")
        b12 = self.createToken(720, 399, "blue")

        # add bindings for clicking, dragging and releasing the pieces
        self.canvas.tag_bind("token", "<ButtonPress-1>", self.startDrag)
        self.canvas.tag_bind("token", "<ButtonRelease-1>", self.stopDrag)
        self.canvas.tag_bind("token", "<B1-Motion>", self.drag)

    def initUI(self):
        self.master.title("Checkers")
        self.pack(fill=BOTH, expand=1)
        self.canvas = Canvas(self)


    '''

    def playerTurn(event):
        if self.was_moved == True:
            self.was_moved = False
            
        OnTokenButtonRelease(event)
        curr_itm = canvas.find_closest(event.x, event.y)[0]
        itm_below = canvas.find_overlapping(event.x, event.y, event.x, event.y)[0]
        itm_tuple = canvas.find_overlapping(event.x, event.y, event.x, event.y)

        same_color = False
        if ((self.last_itm > 64 and self.last_itm < 77) and (curr_itm > 64 and curr_itm < 77)) and self.illegal != True:
            same_color = True
            tkMessageBox.showinfo(title = None, message = "Player 1's Turn (Red)")
            if self.was_moved != True:
                delta_x = init_data["x"] - event.x
                delta_y = init_data["y"] - event.y
                canvas.move(init_data["item"], delta_x, delta_y)
                self.was_moved = True


        elif ((self.last_itm > 76 and self.last_itm < 90) and (curr_itm > 76 and curr_itm < 90)) and self.illegal != True:
            same_color = True
            tkMessageBox.showinfo(title = None, message = "Player 2's Turn (Blue)")
            if self.was_moved != True:
                delta_x = init_data["x"] - event.x
                delta_y = init_data["y"] - event.y
                canvas.move(init_data["item"], delta_x, delta_y)
                self.was_moved = True
                
    '''
    
    def createToken(self, x, y, color):
        # create a checker piece at given coord
        self.canvas.create_oval(x - 25, y - 25, x + 25, y + 25, outline=color, fill=color,tags=("token",),)

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
        # handle dragging of an object 
        # determine move distance
        delta_x = event.x - self._drag_data["x"]
        delta_y = event.y - self._drag_data["y"]
        # move the object 
        self.canvas.move(self._drag_data["item"], delta_x, delta_y)
        # record the new position
        self._drag_data["x"] = event.x
        self._drag_data["y"] = event.y

    '''
    def playerTurn():
        # initialize counter to help determine player's turn
        counter = 0
        if (counter % 2 == 0):
            # display label reading "Player 1's Turn"
            r = Label(root, text="Player 1's Turn (Red)")
            r.pack()
            # wait for player to complete turn
            ## something involving a button reading "Turn Completed" ##
            # increment counter by 1
            counter += 1
        else:
            # display label reading "Player 2's Turn"
            b = Label(root, text="Player 2's Turn (Blue)")
            b.pack()
            # wait for player to complete turn
            ## something involving a button reading "Turn Completed" ##
            # increment counter by 1
            counter += 1
    '''

    def PieceLogic(event):
        blackTags = canvas.find_withtag("black")
        current = canvas.find_closest(event.x,event.y)[0]
        iBelow = canvas.find_overlapping(event.x,event.y,event.x,event.y)[0]
        iTuple = canvas.find_overlapping(event.x,event.y,event.x,event.y)
        self.kcoord = Coords(iBelow)

        lastCoord = Coords(iBelow)

        dRow = abs(lastCoord[1] - self.kcoord[1])
        dCol = abs(lastCoord[0] - self.kcoord[0])
        
        for item in blackTags:
            if ((item == itemB) and (len(iTuple) == 2) and dRow > 0 and dCol > 0):
                s_dims = RectDims(lastCoord)
                self.moved += 1
                print "Moves: ", self.moved
                if lastCoord[0] == 1 and current < 76 and same_color != True:
                    canvas.itemconfig(current, fill = "orange", outline = "orange")
                    self.red_king.append(current)
                elif lastCoord[0] == 8 and current < 77 and same_color != True:
                    canvas.itemconfig(current, fill = "gray", outline = "gray")
                    self.blue_king.append(current)
                    
                        

def main():
    root = Tk()
    x = Board(root, [], 0, 0, False, [], [], False)
    root.geometry("800x450+200+200")
    root.mainloop()
    
if __name__ == "__main__":
    main()
