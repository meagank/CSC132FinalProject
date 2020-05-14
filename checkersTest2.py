from Tkinter import *

root = Tk()
root.title("Checkers")

canvas = Canvas(root, width = 300 , height = 300)
canvas.pack()
background_image = PhotoImage(file="images/CheckerBoard.gif")
background_label = Label(image = background_image)
background_label.place(x=0, y=0, relwidth=1,relheight=1)


img = PhotoImage(file="images/Red piece.gif")
label = Label(root, image = img).place(x=3,y=100)

photo = PhotoImage(file="images/Black piece.gif")
label = Label(root, image = photo).place(x=100,y=50)




##window = Tk()

mainloop()
