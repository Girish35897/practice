from tkinter import *

#r = int(input('No. of inputs:'))

windows = Tk()
windows.title('Sperare')
windows.config(padx=50, pady=50, bg='#F6D7A7')

# Labels
layer = Label(text='Layer', font=('Courier', 20, 'bold'))
layer.grid(row=0, column=0, columnspan=2)

thickness_o = Label(text='Thickness', font=('Courier', 20, 'bold'), pady=15)
thickness_o.grid(column=2, row=0, rowspan=2)

input_cp = Label(text='Input', font=('Courier', 20, 'bold'))
input_cp.grid(column=3, row=0, columnspan=2)

weighted_avg = Label(text='Weighted average',font=('Courier', 20, 'bold') )
weighted_avg.grid(row=0,column=5, columnspan=2)

from_i = Label(text='From', font=('Courier', 15, 'bold'))
from_i.grid(column=0, row=1)

to_i = Label(text='To', font=('Courier', 15, 'bold'), padx=2)
to_i.grid(column=1, row=1)

c_i = Label(text='C', font=('Courier', 15, 'bold'), padx=10)
c_i.grid(column=3, row=1)

phi_i = Label(text='Phi', font=('Courier', 15, 'bold'), padx=5)
phi_i.grid(column=4, row=1)

c_o = Label(text='C', font=('Courier', 15, 'bold'), padx=51)
c_o.grid(column=5, row=1)

phi_o = Label(text='Phi', font=('Courier', 15, 'bold'), padx=52, borderwidth=2)
phi_o.grid(column=6, row=1)

l = list(range(2,50))

def add_row():
    for i in range(7):
        global lf
        lf = Entry(windows,width=8)
        lf.grid(row=l[0], column=0)
        lf.insert(0,0)

        global lto
        lto = Entry(windows,width=4)
        lto.grid(row=l[0], column=1)
        lto.insert(0, 0)

        global th_o
        th_o = Entry(windows, width=24)
        th_o.grid(row=l[0], column=2)

        global c_in
        c_in = Entry(windows, width=5)
        c_in.grid(row=l[0], column=3)

        global phi
        phi = Entry(windows, width=7)
        phi.grid(row=l[0], column=4)

        global c_out
        c_out = Entry(windows, width=19)
        c_out.grid(row=l[0], column=5)

        global phi_out
        phi_out = Entry(windows, width=23)
        phi_out.grid(row=l[0], column=6)

        calculate_button = Button(windows, text='Calculate', command=calc, fg='green')
        calculate_button.grid(row=l[0], column=7)

        add_button.grid(row=l[0], column=8)
    l.pop(0)


def calc():
    th_o.delete(0, END)
    c_out.delete(0, END)
    phi_out.delete(0, END)
    result_thickness = float(lto.get())-float(lf.get())
    th_o.insert(0, result_thickness)

    c = float(c_in.get())
    p = float(phi.get())
    l1 = float(lf.get())
    l2 = float(lto.get())
    res_c = (((result_thickness*c*l1)+(result_thickness*c*l2))/+(l1+l2))
    res_phi = (((result_thickness*p*l1)+(result_thickness*p*l2))/+(l1+l2))

    c_out.insert(0, res_c)
    phi_out.insert(0, res_phi)


# Button
add_button = Button(windows, text='+', command=add_row, fg='green')
add_button.grid(row=1, column=8)

windows.mainloop()