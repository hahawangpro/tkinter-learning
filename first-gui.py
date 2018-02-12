import tkinter as tk
import time
app = tk.Tk()
app.title("Hello")
myImage = tk.PhotoImage(file="hello.gif")
imageLable=tk.Label(app,
                    compound = tk.TOP,
                    image=myImage,
                    text="Hello Steemians!",
                    fg="white",bg="black",
                    font=("Times", "30", "bold"),
                     )
imageLable.pack()
app.mainloop()
