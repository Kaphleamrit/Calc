from tkinter import *

root = Tk()                           # window
root.title("Simple Calculator")       # window title

e = Entry(root, width = 35, borderwidth = 10, bg ="white", fg="black")      # defines input field
e.grid(row=0, column = 0, columnspan = 3, padx = 10 , pady = 0)           # places the input field in the screen


# inserts the pressed numbers in the input field
def button_click(param):
    # e.delete(0, END)
    current = e.get()
    e.delete(0, END)
    e.insert(0, str(current)+str(param))


# clears the numbers from the input field
def clear():
    e.delete(0, END)


# stores the first number t0 the global variable f_num, assign the pressed arthematic operators to the global
# variable sign and clears the input field
def math(operator):
    first_number = e.get()
    global f_num, sign
    f_num = int(first_number)
    sign = operator
    e.delete(0, END)


# inserts the appropriate value into the input field after evaluation according to the value of the global variable sign
def equal():
    second_number = e.get()
    e.delete(0, END)
    if sign=='+':
        e.insert(0, f_num + int(second_number))
    elif sign=='-':
        e.insert(0, f_num - int(second_number))
    elif sign=='X':
        e.insert(0, f_num * int(second_number))
    else:
        e.insert(0, f_num/int(second_number))


# defines buttons
button_1 = Button(root, text ="1", padx = 40, pady =20, bg ="white", fg="black",  command =lambda: button_click(1))
button_2 = Button(root, text ="2", padx = 40, pady =20,  bg ="white", fg="black",  command =lambda: button_click(2))
button_3 = Button(root, text ="3", padx = 40, pady =20, bg ="white", fg="black",   command = lambda: button_click(3))
button_4 = Button(root, text ="4", padx = 40, pady =20,  bg ="white", fg="black",  command = lambda: button_click(4))
button_5= Button(root, text ="5", padx = 40, pady =20,  bg ="white", fg="black",  command = lambda: button_click(5))
button_6 = Button(root, text ="6", padx = 40, pady =20, bg ="white", fg="black",   command = lambda: button_click(6))
button_7 = Button(root, text ="7", padx = 40, pady =20,  bg ="white", fg="black",  command = lambda: button_click(7))
button_8= Button(root, text ="8", padx = 40, pady =20, bg ="white", fg="black",   command = lambda: button_click(8))
button_9 = Button(root, text ="9", padx = 40, pady =20, bg ="white", fg="black",   command = lambda: button_click(9))
button_0 = Button(root, text ="0", padx = 40, pady =20,  bg ="white", fg="black",  command = lambda: button_click(0))

button_plus = Button(root, text = "+" , padx =40, pady=15, bg= "#dddddd", fg="black", command =lambda: math('+'))
button_subtract = Button(root, text = "-", padx = 40, pady =10,   bg= "#dddddd", fg="black", command = lambda: math('-'))
button_multiply = Button(root, text = "X" , padx = 40, pady =10,   bg= "#dddddd", fg="black", command =lambda: math('X'))
button_divide = Button(root, text = "/" , padx = 40, pady =10,   bg= "#dddddd", fg="black", command =lambda: math('/'))

button_equal = Button(root, text = "=" , padx =90, pady=15, bg="green", command = lambda: equal())
button_clear = Button(root, text = "clear", padx =80, pady=15, bg= "red", command = clear)




# puts the buttons on the screen
button_1.grid(row =3, column =0)
button_2.grid(row =3, column =1)
button_3.grid(row =3, column =2)

button_4.grid(row =2, column =0)
button_5.grid(row =2, column =1)
button_6.grid(row =2, column =2)

button_7.grid(row =1, column =0)
button_8.grid(row =1, column =1)
button_9.grid(row =1, column =2)

button_0.grid(row =4, column =0)
button_clear.grid(row=4, column = 1 , columnspan = 2)

button_plus.grid(row =5, column = 0)
button_equal.grid(row= 5, column = 1, columnspan= 2)

button_multiply.grid(row =6, column =0)
button_subtract.grid(row =6, column =1)
button_divide.grid(row =6, column =2)

# keeps the program running until the window is closed itself
root.mainloop()

