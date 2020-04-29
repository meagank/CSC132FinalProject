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

        
        self._drag_data = {"x": 0, "y": 0, "item": None}

    ##### RED CHECKER PIECES #####
        
        #### ROW 1 ####
        r1 = canvas.create_oval(50, 12, 102, 60, outline="red", fill="red", tags = "oval")
        r2 = canvas.create_oval(234, 12, 286, 60, outline="red", fill="red", tags = "oval")
        r3 = canvas.create_oval(418, 12, 470, 60, outline="red", fill="red", tags = "oval")
        r4 = canvas.create_oval(602, 12, 654, 60, outline="red", fill="red", tags = "oval")
        
        

        #### ROW 2 ####
        r5 = canvas.create_oval(142, 64, 194, 112, outline="red", fill="red", tags = "oval")
        r6 = canvas.create_oval(326, 64, 378, 112, outline="red", fill="red", tags = "oval")
        r7 = canvas.create_oval(510, 64, 562, 112, outline="red", fill="red", tags = "oval")
        r8 = canvas.create_oval(694, 64, 746, 112, outline="red", fill="red", tags = "oval")
        


        #### ROW 3 ####
        r9 = canvas.create_oval(50, 116, 102, 164, outline="red", fill="red", tags = "oval")
        r10 = canvas.create_oval(234, 116, 286, 164, outline="red", fill="red", tags = "oval")
        r11 = canvas.create_oval(418, 116, 470, 164, outline="red", fill="red", tags = "oval")
        r12 = canvas.create_oval(602, 116, 654, 164, outline="red", fill="red", tags = "oval")


    ##### BLUE CHECKER PIECES #####
        
        #### ROW 6 ####
        b1 = canvas.create_oval(142, 272, 194, 320, outline="blue", fill="blue", tags = "oval")
        b2 = canvas.create_oval(326, 272, 378, 320, outline="blue", fill="blue", tags = "oval")
        b3 = canvas.create_oval(510, 272, 562, 320, outline="blue", fill="blue", tags = "oval")
        b4 = canvas.create_oval(694, 272, 746, 320, outline="blue", fill="blue", tags = "oval")
        
        

        #### ROW 7 ####
        b5 = canvas.create_oval(50, 324, 102, 372, outline="blue", fill="blue", tags = "oval")
        b6 = canvas.create_oval(234, 324, 286, 372, outline="blue", fill="blue", tags = "oval")
        b7 = canvas.create_oval(418, 324, 470, 372, outline="blue", fill="blue", tags = "oval")
        b8 = canvas.create_oval(602, 324, 654, 372, outline="blue", fill="blue", tags = "oval")
        


        #### ROW 8 ####
        b9 = canvas.create_oval(142, 376, 194, 422, outline="blue", fill="blue", tags = "oval")
        b10 = canvas.create_oval(326, 376, 378, 422, outline="blue", fill="blue", tags = "oval")
        b11 = canvas.create_oval(510, 376, 562, 422, outline="blue", fill="blue", tags = "oval")
        b12 = canvas.create_oval(694, 376, 746, 422, outline="blue", fill="blue", tags = "oval")


               
        canvas.pack(fill=BOTH, expand=1)

        # add bindings for clicking, dragging, and releasing
        canvas.tag_bind("oval", "<ButtonPress-1>", self.strtdrag)
        canvas.tag_bind("oval", "<ButtonRelease-1>", self.stpdrag)
        canvas.tag_bind("oval", "<B1-Motion>", self.drag)
        
    def create_token(self, x, y, color):
        ###Create a token at the given coordinate in the given color###
        self.canvas.create_oval(
            x - 25,
            y - 25,
            x + 25,
            y + 25,
            outline = color,
            fill = color,
            tags = ("oval",),
        )

    def strtdrag(self, event):
        ###Begining drag of an object###
        # record the item and its location
        canvas._drag_data["item"] = self.canvas.find_closest(event.x, event.y)[0]
        canvas._drag_data["x"] = event.x
        canvas._drag_data["y"] = event.y

    def stpdrag(self, event):
        ###End drag of an object###
        # reset the drag information
        self._drag_data["item"] = None
        self._drag_data["x"] = 0
        self._drag_data["y"] = 0

    def drag(self, event):
        ###Handle dragging of an object###
        # compute how much the mouse has moved
        delta_x = event.x - self._drag_data["x"]
        delta_y = event.y - self._drag_data["y"]
        # move the object the appropriate amount
        self.canvas.move(self._drag_data["item"], delta_x, delta_y)
        # record the new position
        self._drag_data["x"] = event.x
        self._drag_data["y"] = event.y

# determines player's turn        
def playerTurn():
    # initialize counter to help determine player's turn
    counter = 0
    if (counter % 2 == 0):
        # display label with "Player 1's Turn"
        r = Label(root, text="Player 1's Turn (Red)")
        r.pack()
        # wait for player to move checker piece
        # increase counter by 1
        counter += 1

    else:
        # display label with "Player 1's Turn"
        b = Label(root, text="Player 2's Turn (Blue)")
        b.pack()
        # wait for player to move checker piece
        # increase counter by 1
        counter += 1
    
def main():

    global root
    root = Tk()
    ex = Board()
    root.geometry("800x450+200+200")
    playerTurn()
    root.mainloop()


if __name__ == '__main__':
    main()
