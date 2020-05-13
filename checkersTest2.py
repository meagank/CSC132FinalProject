from Tkinter import *


root = Tk()
root.title("Checkers")
canvas = Canvas(root, width = 300 , height = 300)
canvas.pack()
background_image = PhotoImage(file="images/CheckerBoard.gif")
background_label = Label(image = background_image)
background_label.place(x=0, y=0, relwidth=1,relheight=1)
##    canvas.create_image(20, 20, anchor = NW, image = img)
##    photo = PhotoImage(file="images/Red piece.gif")
##    Button(root, image = photo).pack(side = TOP)
##    photo1 = PhotoImage(file="images/Black piece.gif")
##    Button(root, image = photo1).pack(side = TOP)
##


##window = Tk()

mainloop()

