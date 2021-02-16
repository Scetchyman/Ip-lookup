import pygeoip
from tkinter import *
from tkinter import messagebox

root = Tk()
root.geometry("150x100")

frame = Frame(root)
frame.pack()


entry1 = Entry(frame, width=20)
entry1.insert(0, 'Insert IP')
entry1.pack()
entry1.get()

Button = Button(frame, text="Run", command=are_you_sure())
Button.pack()

gip = pygeoip.GeoIP("GeoLiteCity.dat")
res = gip.record_by_addr("")
for key, val in res.items():
    print('%s : %s' % (key, val))


root.mainloop()