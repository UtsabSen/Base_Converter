from tkinter import *
from tkinter import messagebox

root = Tk()

label_1 = Label(root, text="Enter value: ")
label_1.grid(row=0, sticky=W)

label_space = Label(root, text=" ")
label_space.grid(row=0, column=1)

entry = Entry(root, bd=3)
entry.grid(row=0, column=1, columnspan=2, ipadx=30, ipady=10)


def backspace():
    entry.delete(entry.index(INSERT) - 1)


btn_backspace = Button(root, text="<--", bd=5, relief="groove", bg="#E5EB39", width=15, command=backspace)
btn_backspace.grid(row=0, column=4)

def reset():
    entry.delete(0, END)
    entry.insert(0, "")

    label_space1 = Label(root, text="                   ")
    label_space2 = Label(root, text="                   ")
    label_space3 = Label(root, text="                   ")
    label_space4 = Label(root, text="                   ")
    label_space1.grid(row=9, column=2)
    label_space2.grid(row=10, column=2)
    label_space3.grid(row=11, column=2)
    label_space4.grid(row=12, column=2)

    label_NIL1 = Label(root, text="              NIL               ")
    label_NIL2 = Label(root, text="              NIL               ")
    label_NIL3 = Label(root, text="              NIL               ")
    label_NIL4 = Label(root, text="              NIL               ")
    label_NIL1.grid(row=9, column=2)
    label_NIL2.grid(row=10, column=2)
    label_NIL3.grid(row=11, column=2)
    label_NIL4.grid(row=12, column=2)

    for i in range(4):
        var_a[i].set(0)
        var_b[i].set(0)


label_space.grid(row=0, column=3)

button_reset = Button(root, text="RESET", bd=5, relief="groove", bg="#F24B4B",width=15, command=reset)
button_reset.grid(row=1, column=4)

label_space.grid(row=1)

label_2 = Label(root, text="Convert Base From:")
label_2.grid(row=2)

label_3 = Label(root, text="Convert Base To:")
label_3.grid(row=2, column=2)


# ********************* ALL CONVERTING FUNCTIONS START *************************


def bin_to_bin(b):
    return (bin(int(str(b), 2)))


def bin_to_dec(b):
    return int(str(b), 2)


def bin_to_oct(b):
    return oct(int(str(b), 2))


def bin_to_hex(b):
    return hex(int(str(b), 2))


def dec_to_bin(d):
    return bin(int(d))


def dec_to_dec(d):
    return int(d)


def dec_to_oct(d):
    return oct(int(d))


def dec_to_hex(d):
    return hex(int(d))


def oct_to_bin(o):
    return bin(int(str(o), 8))


def oct_to_dec(o):
    return int(str(o), 8)


def oct_to_oct(o):
    return oct(int(str(o), 8))


def oct_to_hex(o):
    return hex(int(str(o), 8))


def hex_to_bin(h):
    return bin(int(str(h), 16))


def hex_to_dec(h):
    return int(str(h), 16)


def hex_to_oct(h):
    return oct(int(str(h), 16))


def hex_to_hex(h):
    return hex(int(str(h), 16))


# ********************* ALL CONVERTING FUNCTIONS STOP *************************

def convert():
    filename = "HISTORY.txt"
    label_space: Label = Label(root, text="                   ")
    label_NIL_a = Label(root, text="              NIL               ")
    label_NIL_b = Label(root, text="              NIL               ")
    label_NIL_c = Label(root, text="              NIL               ")

    if entry.get() == "":
        messagebox.showinfo("EMPTY", "Please enter value.")

    elif var_a[0].get() == 1 and var_b[0].get() == 1:
        try:
            label_answer = Label(root, text=bin_to_bin(entry.get())[2:])
            label_space.grid(row=9, column=2)
            label_NIL_a.grid(row=10, column=2)
            label_NIL_b.grid(row=11, column=2)
            label_NIL_c.grid(row=12, column=2)
            label_answer.grid(row=9, column=2)
            file = open(filename,"a")
            file.write("Binary To Binary: "+str(entry.get())+" => "+str(bin_to_bin(entry.get())[2:])+"\n")
            file.close()
        except:
            messagebox.showinfo("ERROR INPUT", "You have entered invalid input.\nOnly '0' and '1' are accepted.")

    elif var_a[0].get() == 1 and var_b[1].get() == 1:
        try:
            label_answer = Label(root, text=bin_to_dec(entry.get()))
            label_NIL_a.grid(row=9, column=2)
            label_space.grid(row=10, column=2)
            label_NIL_b.grid(row=11, column=2)
            label_NIL_c.grid(row=12, column=2)
            label_answer.grid(row=10, column=2)
            file = open(filename, "a")
            file.write("Binary To Decimal: " + str(entry.get()) + " => " + str(bin_to_dec(entry.get()))+"\n")
            file.close()
        except:
            messagebox.showinfo("ERROR INPUT", "You have entered invalid input.\nOnly '0' and '1' are accepted.")

    elif var_a[0].get() == 1 and var_b[2].get() == 1:
        try:
            label_answer = Label(root, text=bin_to_oct(entry.get())[2:])
            label_NIL_a.grid(row=9, column=2)
            label_NIL_b.grid(row=10, column=2)
            label_space.grid(row=11, column=2)
            label_NIL_c.grid(row=12, column=2)
            label_answer.grid(row=11, column=2)
            file = open(filename, "a")
            file.write("Binary To Octal: " + str(entry.get()) + " => " + str(bin_to_oct(entry.get())[2:])+"\n")
            file.close()
        except:
            messagebox.showinfo("ERROR INPUT", "You have entered invalid input.\nOnly '0' and '1' are accepted.")
    elif var_a[0].get() == 1 and var_b[3].get() == 1:
        try:
            label_answer = Label(root, text=bin_to_hex(entry.get()).upper()[2:])
            label_NIL_c.grid(row=9, column=2)
            label_NIL_a.grid(row=10, column=2)
            label_NIL_b.grid(row=11, column=2)
            label_space.grid(row=12, column=2)
            label_answer.grid(row=12, column=2)
            file = open(filename, "a")
            file.write("Binary To Hexa Decimal: " + str(entry.get()) + " => " + str(bin_to_hex(entry.get()).upper()[2:])+"\n")
            file.close()
        except:
            messagebox.showinfo("ERROR INPUT", "You have entered invalid input.\nOnly '0' and '1' are accepted.")

    elif var_a[1].get() == 1 and var_b[0].get() == 1:
        try:
            label_answer = Label(root, text=dec_to_bin(entry.get())[2:])
            label_space.grid(row=9, column=2)
            label_NIL_a.grid(row=10, column=2)
            label_NIL_b.grid(row=11, column=2)
            label_NIL_c.grid(row=12, column=2)
            label_answer.grid(row=9, column=2)
            file = open(filename, "a")
            file.write("Decimal To Binary: " + str(entry.get()) + " => " + str(dec_to_bin(entry.get())[2:])+"\n")
            file.close()
        except:
            messagebox.showinfo("ERROR INPUT", "You have entered invalid input.\nOnly numbers are accepted.")

    elif var_a[1].get() == 1 and var_b[1].get() == 1:
        try:
            label_answer = Label(root, text=dec_to_dec(entry.get()))
            label_NIL_a.grid(row=9, column=2)
            label_space.grid(row=10, column=2)
            label_NIL_b.grid(row=11, column=2)
            label_NIL_c.grid(row=12, column=2)
            label_answer.grid(row=10, column=2)
            file = open(filename, "a")
            file.write("Decimal To Decimal: " + str(entry.get()) + " => " + str(dec_to_dec(entry.get()))+"\n")
            file.close()
        except:
            messagebox.showinfo("ERROR INPUT", "You have entered invalid input.\nOnly numbers are accepted.")

    elif var_a[1].get() == 1 and var_b[2].get() == 1:
        try:
            label_answer = Label(root, text=dec_to_oct(entry.get())[2:])
            label_NIL_a.grid(row=9, column=2)
            label_NIL_b.grid(row=10, column=2)
            label_space.grid(row=11, column=2)
            label_NIL_c.grid(row=12, column=2)
            label_answer.grid(row=11, column=2)
            file = open(filename, "a")
            file.write("Decimal To Octal: " + str(entry.get()) + " => " + str(dec_to_oct(entry.get())[2:])+"\n")
            file.close()
        except:
            messagebox.showinfo("ERROR INPUT", "You have entered invalid input.\nOnly numbers are accepted")

    elif var_a[1].get() == 1 and var_b[3].get() == 1:
        try:
            label_answer = Label(root, text=dec_to_hex(entry.get()).upper()[2:])
            label_NIL_c.grid(row=9, column=2)
            label_NIL_a.grid(row=10, column=2)
            label_NIL_b.grid(row=11, column=2)
            label_space.grid(row=12, column=2)
            label_answer.grid(row=12, column=2)
            file = open(filename, "a")
            file.write("Decimal To Hexa Decimal: " + str(entry.get()) + " => " + str(dec_to_hex(entry.get()).upper()[2:])+"\n")
            file.close()
        except:
            messagebox.showinfo("ERROR INPUT", "You have entered invalid input.\nOnly numbers are accepted.")

    elif var_a[2].get() == 1 and var_b[0].get() == 1:
        try:
            label_answer = Label(root, text=oct_to_bin(entry.get())[2:])
            label_space.grid(row=9, column=2)
            label_NIL_a.grid(row=10, column=2)
            label_NIL_b.grid(row=11, column=2)
            label_NIL_c.grid(row=12, column=2)
            label_answer.grid(row=9, column=2)
            file = open(filename, "a")
            file.write("Octal To Binary: " + str(entry.get()) + " => " + str(oct_to_bin(entry.get())[2:])+"\n")
            file.close()
        except:
            messagebox.showinfo("ERROR INPUT", "You have entered invalid input.\nOnly 0 to 7 numbers are accepted.")

    elif var_a[2].get() == 1 and var_b[1].get() == 1:
        try:
            label_answer = Label(root, text=oct_to_dec(entry.get()))
            label_NIL_a.grid(row=9, column=2)
            label_space.grid(row=10, column=2)
            label_NIL_b.grid(row=11, column=2)
            label_NIL_c.grid(row=12, column=2)
            label_answer.grid(row=10, column=2)
            file = open(filename, "a")
            file.write("Octal To Decimal: " + str(entry.get()) + " => " + str(oct_to_dec(entry.get()))+"\n")
            file.close()
        except:
            messagebox.showinfo("ERROR INPUT", "You have entered invalid input.\nOnly 0 to 7 numbers are accepted.")

    elif var_a[2].get() == 1 and var_b[2].get() == 1:
        try:
            label_answer = Label(root, text=oct_to_oct(entry.get())[2:])
            label_NIL_a.grid(row=9, column=2)
            label_NIL_b.grid(row=10, column=2)
            label_space.grid(row=11, column=2)
            label_NIL_c.grid(row=12, column=2)
            label_answer.grid(row=11, column=2)
            file = open(filename, "a")
            file.write("Octal To Ocatl: " + str(entry.get()) + " => " + str(oct_to_oct(entry.get())[2:])+"\n")
            file.close()
        except:
            messagebox.showinfo("ERROR INPUT", "You have entered invalid input.\nOnly 0 to 7 numbers are accepted.")

    elif var_a[2].get() == 1 and var_b[3].get() == 1:
        try:
            label_answer = Label(root, text=oct_to_hex(entry.get()).upper()[2:])
            label_NIL_c.grid(row=9, column=2)
            label_NIL_a.grid(row=10, column=2)
            label_NIL_b.grid(row=11, column=2)
            label_space.grid(row=12, column=2)
            label_answer.grid(row=12, column=2)
            file = open(filename, "a")
            file.write("Octal To Hexa Decimal: " + str(entry.get()) + " => " + str(oct_to_hex(entry.get()).upper()[2:])+"\n")
            file.close()
        except:
            messagebox.showinfo("ERROR INPUT", "You have entered invalid input.\nOnly 0 to 7 numbers are accepted.")

    elif var_a[3].get() == 1 and var_b[0].get() == 1:
        try:
            label_answer = Label(root, text=hex_to_bin(entry.get())[2:])
            label_space.grid(row=9, column=2)
            label_NIL_a.grid(row=10, column=2)
            label_NIL_b.grid(row=11, column=2)
            label_NIL_c.grid(row=12, column=2)
            label_answer.grid(row=9, column=2)
            file = open(filename, "a")
            file.write("Hexa Decimal To Binary: " + str(entry.get()) + " => " + str(hex_to_bin(entry.get())[2:])+"\n")
            file.close()
        except:
            messagebox.showinfo("ERROR INPUT",
                                "You have entered invalid input.\nOnly 0 to 9 and 'A' to 'F' are accepted.")

    elif var_a[3].get() == 1 and var_b[1].get() == 1:
        try:
            label_answer = Label(root, text=hex_to_dec(entry.get()))
            label_NIL_a.grid(row=9, column=2)
            label_space.grid(row=10, column=2)
            label_NIL_b.grid(row=11, column=2)
            label_NIL_c.grid(row=12, column=2)
            label_answer.grid(row=10, column=2)
            file = open(filename, "a")
            file.write("Hexa Decimal To Decimal: " + str(entry.get()) + " => " + str(hex_to_dec(entry.get()))+"\n")
            file.close()
        except:
            messagebox.showinfo("ERROR INPUT",
                                "You have entered invalid input.\nOnly 0 to 9 and 'A' to 'F' are accepted.")

    elif var_a[3].get() == 1 and var_b[2].get() == 1:
        try:
            label_answer = Label(root, text=hex_to_oct(entry.get())[2:])
            label_NIL_a.grid(row=9, column=2)
            label_NIL_b.grid(row=10, column=2)
            label_space.grid(row=11, column=2)
            label_NIL_c.grid(row=12, column=2)
            label_answer.grid(row=11, column=2)
            file = open(filename, "a")
            file.write("Hexa Decimal To Octal: " + str(entry.get()) + " => " + str(hex_to_oct(entry.get())[2:])+"\n")
            file.close()
        except:
            messagebox.showinfo("ERROR INPUT",
                                "You have entered invalid input.\nOnly 0 to 9 and 'A' to 'F' are accepted.")

    elif var_a[3].get() == 1 and var_b[3].get() == 1:
        try:
            label_answer = Label(root, text=hex_to_hex(entry.get()).upper()[2:])
            label_NIL_c.grid(row=9, column=2)
            label_NIL_a.grid(row=10, column=2)
            label_NIL_b.grid(row=11, column=2)
            label_space.grid(row=12, column=2)
            label_answer.grid(row=12, column=2)
            file = open(filename, "a")
            file.write("Hexa Decimal To Hexa Decimal: " + str(entry.get()) + " => " + str(hex_to_hex(entry.get()).upper()[2:])+"\n")
            file.close()
        except:
            messagebox.showinfo("ERROR INPUT","You have entered invalid input.\nOnly 0 to 9 and 'A' to 'F' are accepted.")

    else:
        messagebox.showinfo("REQUIREMENT", "Choose options on the both side")


# ***************************************************** LOOP ON GRID START ****************************************

now_a = None
buttons_a = None
var_a1 = IntVar()
var_a2 = IntVar()
var_a3 = IntVar()
var_a4 = IntVar()

var_a = [var_a1, var_a2, var_a3, var_a4]


def cb_a():
    global now_a, buttons_a
    if None != now_a:
        buttons_a[now_a].deselect()
    vals_a = [var_a[i].get() for i in range(4)]
    try:
        now_a = vals_a.index(1)
    except ValueError:
        now_a = None


x_a = ["Binary", "Decimal", "Octal", "Hexa Decimal"]
y_a = 3
buttons_a = [Checkbutton(root, text=x_a[i], variable=var_a[i], command=cb_a) for i in range(4)]
for b in buttons_a:
    b.grid(row=y_a, sticky=W)
    y_a = y_a + 1

# *************** A SEPERATES B ***************

now_b = None
buttons_b = None
var_a1 = IntVar()
var_a2 = IntVar()
var_a3 = IntVar()
var_a4 = IntVar()

var_b = [var_a1, var_a2, var_a3, var_a4]


def cb_b():
    global now_b, buttons_b
    if None != now_b:
        buttons_b[now_b].deselect()
    vals_b = [var_b[i].get() for i in range(4)]
    try:
        now_b = vals_b.index(1)
    except ValueError:
        now_b = None


x_b = ["Binary", "Decimal", "Octal", "Hexa Decimal"]
y_b = 3
buttons_b = [Checkbutton(root, text=x_b[i], variable=var_b[i], command=cb_b) for i in range(4)]
for b in buttons_b:
    b.grid(row=y_b, column=2, sticky=W)
    y_b = y_b + 1

# ***************************************************** LOOP ON GRID STOP ****************************************
# ***************************************************** STSRT OF RESULT SECTION ***************************************

button_convert = Button(root, text="CONVERT", bd=5, relief="groove", bg="#0BD72D", width=15,  command=convert)
button_convert.grid(row=7, columnspan=3)


label_space.grid(row=8)

l_bin = Label(root, text="Binary: ")
l_bin.grid(row=9, sticky=W)
l_bin_ans = Label(root, text="                  NIL                   ", borderwidth=3, height=2, relief="groove")
l_bin_ans.grid(row=9, column=2)

l_dec = Label(root, text="Decimal: ")
l_dec.grid(row=10, sticky=W)
l_dec_ans = Label(root, text="                  NIL                   ", borderwidth=3, height=2, relief="groove")
l_dec_ans.grid(row=10, column=2)

l_oct = Label(root, text="Octal: ")
l_oct.grid(row=11, sticky=W)
l_oct_ans = Label(root, text="                  NIL                   ", borderwidth=3, height=2, relief="groove")
l_oct_ans.grid(row=11, column=2)

l_hex = Label(root, text="Hexa Decimal: ")
l_hex.grid(row=12, sticky=W)
l_hex_ans = Label(root, text="                  NIL                   ", borderwidth=3, height=2, relief="groove")
l_hex_ans.grid(row=12, column=2)

root.title("Base Converter")
try:
    root.iconbitmap("convert.ico")
except:
    pass


# ***************************************************** END OF RESULT SECTION ***************************************
# ********************** CALCULATOR *******************


def calculator():
    root_calculator = Tk()

    label_expression = Label(root_calculator, text="Enter expression: ")
    label_expression.grid(row=0, sticky=W)

    entry_cal = Entry(root_calculator, bd=3)
    entry_cal.grid(row=0, column=1, columnspan=2, ipadx=30, ipady=10)

    def backspace():
        entry_cal.delete(entry_cal.index(INSERT) - 1)

    btn_backspace = Button(root_calculator, text="<--", bd=5, bg="#E5EB39", width=14, height=2, relief="groove", command=backspace)
    btn_backspace.grid(row=0, column=3)

    label_answer = Label(root_calculator, text="Answer: ")
    label_answer.grid(row=3, column=0, sticky=W)

    label_space_cal=Label(root_calculator, text=" ", bd=2, width=17, height=2, relief="groove")
    label_space_cal.grid(row=3, column=1, columnspan=2, ipadx=30)

    def reset_cal():
        entry_cal.delete(0, END)
        entry_cal.insert(0, "")
        label_space_cal: Label = Label(root_calculator, text="                                         ")
        label_space_cal.grid(row=3, column=1, columnspan=2)

    def bracket_start():
        entry_cal.insert(entry_cal.index(INSERT), "(")

    def bracket_end():
        entry_cal.insert(entry_cal.index(INSERT), ")")

    def entry_divide():
        entry_cal.insert(entry_cal.index(INSERT), "/")

    btn_reset = Button(root_calculator, text="RESET", width=15, height=2, bg="#F24B4B", command=reset_cal)
    btn_reset.grid(row=4)

    btn_bracket_start = Button(root_calculator, text="(", width=15, height=2, bg="cyan", command=bracket_start)
    btn_bracket_start.grid(row=4, column=1)

    btn_bracket_end = Button(root_calculator, text=")", width=15, height=2, bg="cyan", command=bracket_end)
    btn_bracket_end.grid(row=4, column=2)

    btn_divide = Button(root_calculator, text="/", width=15, height=2, bg="pink", command=entry_divide)
    btn_divide.grid(row=4, column=3)


    def entry_7():
        entry_cal.insert(entry_cal.index(INSERT), "7")

    def entry_8():
        entry_cal.insert(entry_cal.index(INSERT), "8")

    def entry_9():
        entry_cal.insert(entry_cal.index(INSERT), "9")

    def entry_multiply():
        entry_cal.insert(entry_cal.index(INSERT), "*")

    btn_7 = Button(root_calculator, text="7",  width=15, height=2, bg="white", command=entry_7)
    btn_7.grid(row=5)

    btn_8 = Button(root_calculator, text="8",  width=15, height=2, bg="white", command=entry_8)
    btn_8.grid(row=5, column=1)

    btn_9 = Button(root_calculator, text="9",  width=15, height=2, bg="white", command=entry_9)
    btn_9.grid(row=5, column=2)

    btn_multiply = Button(root_calculator, text="*",  width=15, height=2, bg="pink", command=entry_multiply)
    btn_multiply.grid(row=5, column=3)

    def entry_4():
        entry_cal.insert(entry_cal.index(INSERT), "4")

    def entry_5():
        entry_cal.insert(entry_cal.index(INSERT), "5")

    def entry_6():
        entry_cal.insert(entry_cal.index(INSERT), "6")

    def entry_minus():
        entry_cal.insert(entry_cal.index(INSERT), "-")

    btn_4 = Button(root_calculator, text="4",  width=15, height=2, bg="white", command=entry_4)
    btn_4.grid(row=6)

    btn_5 = Button(root_calculator, text="5",  width=15, height=2, bg="white", command=entry_5)
    btn_5.grid(row=6, column=1)

    btn_6 = Button(root_calculator, text="6",  width=15, height=2, bg="white", command=entry_6)
    btn_6.grid(row=6, column=2)

    btn_minus = Button(root_calculator, text="-",  width=15, height=2, bg="pink", command=entry_minus)
    btn_minus.grid(row=6, column=3)

    def entry_1():
        entry_cal.insert(entry_cal.index(INSERT), "1")

    def entry_2():
        entry_cal.insert(entry_cal.index(INSERT), "2")

    def entry_3():
        entry_cal.insert(entry_cal.index(INSERT), "3")

    def entry_plus():
        entry_cal.insert(entry_cal.index(INSERT), "+")

    btn_1 = Button(root_calculator, text="1",  width=15, bg="white", height=2, command=entry_1)
    btn_1.grid(row=7)

    btn_2 = Button(root_calculator, text="2",  width=15, bg="white", height=2, command=entry_2)
    btn_2.grid(row=7, column=1)

    btn_3 = Button(root_calculator, text="3",  width=15, height=2, bg="white", command=entry_3)
    btn_3.grid(row=7, column=2)

    btn_plus = Button(root_calculator, text="+",  width=15, height=2, bg="pink", command=entry_plus)
    btn_plus.grid(row=7, column=3)

    def entry_0():
        entry_cal.insert(entry_cal.index(INSERT), "0")

    def entry_decimal():
        entry_cal.insert(entry_cal.index(INSERT), ".")

    def result():
        try:
            if entry_cal.get()== "":
                messagebox.showinfo("INVALID", "Please enter expression")
            else:
                res = eval(str(entry_cal.get()))
                label_result = Label(root_calculator, text=res)
                label_result.grid(row=3, column=1, columnspan=2)
        except ZeroDivisionError:
            messagebox.showinfo("ERROR", "Can not divisible by zero")
        except SyntaxError:
            messagebox.showinfo("ERROR", "You have entered invalid syntax")
        except NameError:
            messagebox.showinfo("ERROR", "Only numbers are allowed")

    btn_exit = Button(root_calculator, text="EXIT",  width=15, height=2, bg="red", command=root_calculator.destroy)
    btn_exit.grid(row=8)

    btn_0 = Button(root_calculator, text="0",  width=15, height=2, bg="white", command=entry_0)
    btn_0.grid(row=8, column=1)

    btn_decimal = Button(root_calculator, text=".",  width=15, height=2, bg="cyan", command=entry_decimal)
    btn_decimal.grid(row=8, column=2)

    btn_result = Button(root_calculator, text="=",  width=15, height=2, bg="#0BD72D", command=result)
    btn_result.grid(row=8, column=3)

    root_calculator.title("CALCULATOR")
    try:
        root_calculator.iconbitmap("calculator.ico")
    except:
        pass
    root_calculator.mainloop()


btn_calculator = Button(root, text="CALCULATOR", bd=5, width=15, bg="#2B00FF", relief="groove", command=calculator)
btn_calculator.grid(row=2, column=4)


def explanation():
    if var_a[0].get() == 1 and var_b[0].get() == 1:
        messagebox.showinfo("Binary Number System", "Binary number represents any number using 2 digits.\nBinary number system contains 0 and 1.")
    elif var_a[0].get() == 1 and var_b[1].get() == 1:
        messagebox.showinfo("Binary To Decimal", "1. Start the decimal result at 0.\n2. Remove the most significant binary digit (leftmost) and add it to the result.\n3. If all binary digits have been removed, you’re done. Stop.\n4. Otherwise, multiply the result by 2.\n5. Go to step 2.")
    elif var_a[0].get() == 1 and var_b[2].get() == 1:
        messagebox.showinfo("Binary To Octal", "An easy way to convert from binary to octal is to group binary digits into sets of three, starting with the least significant (rightmost) digits.")
    elif var_a[0].get() == 1 and var_b[3].get() == 1:
        messagebox.showinfo("Binary To Hexa Decimal", "An easy way to convert from binary to hexadecimal is to group binary digits into sets of four, starting with the least significant (rightmost) digits.")
    elif var_a[1].get() == 1 and var_b[0].get() == 1:
        messagebox.showinfo("Decimal To Binary", "1. Divide the decimal number by the desired target radix 2.\n2. Append the remainder as the next most significant digit.\n3. Repeat until the decimal number has reached zero.")
    elif var_a[1].get() == 1 and var_b[1].get() == 1:
        messagebox.showinfo("Decimal Number System", "Decimal number represents any number using 10 digits.\nDecimal number system contains 0, 1, 2, 3, 4, 5, 6, 7, 8 and 9.")
    elif var_a[1].get() == 1 and var_b[2].get() == 1:
        messagebox.showinfo("Decimal To Octal", "1. Divide the decimal number by the desired target radix 8.\n2. Append the remainder as the next most significant digit.\n3. Repeat until the decimal number has reached zero.")
    elif var_a[1].get() == 1 and var_b[3].get() == 1:
        messagebox.showinfo("Decimal To Hexa Decimal", "1. Divide the decimal number by the desired target radix 16.\n2. Append the remainder as the next most significant digit.\n3. Repeat until the decimal number has reached zero.\n4. If any remainder exceed 9 then replace the digits with the corresponding alphabetical letters.")
    elif var_a[2].get() == 1 and var_b[0].get() == 1:
        messagebox.showinfo("Octal To Binary", "Converting from octal to binary is as easy as converting from binary to octal.\nSimply look up each octal digit to obtain the equivalent group of three binary digits.")
    elif var_a[2].get() == 1 and var_b[1].get() == 1:
        messagebox.showinfo("Octal To Decimal", "1. Start the decimal result at 0.\n2.Remove the most significant octal digit (leftmost) and add it to the result.\n3. If all octal digits have been removed, you’re done. Stop.\n4. Otherwise, multiply the result by 8.\n5. Go to step 2.")
    elif var_a[2].get() == 1 and var_b[2].get() == 1:
        messagebox.showinfo("Octal Number Syatem", "Octal number represents any number using 8 digits.\nOctal number system contains 0, 1, 2, 3, 4, 5, 6, 7 and 8.")
    elif var_a[2].get() == 1 and var_b[3].get() == 1:
        messagebox.showinfo("Octal To Hexa Decimal", "When converting from octal to hexadecimal, it is often easier to first convert the octal number into binary and then from binary into hexadecimal.")
    elif var_a[3].get() == 1 and var_b[0].get() == 1:
        messagebox.showinfo("Hexa Decimal To Binary", "Converting from hexadecimal to binary is as easy as converting from binary to hexadecimal.\nSimply look up each hexadecimal digit to obtain the equivalent group of four binary digits.")
    elif var_a[3].get() == 1 and var_b[1].get() == 1:
        messagebox.showinfo("Hexa Decimal To Decimal", "Converting hexadecimal to decimal can be performed in the conventional mathematical way, by showing each digit place as an increasing power of 16.\nOf course, hexadecimal letter values need to be converted to decimal values before performing the math.")
    elif var_a[3].get() == 1 and var_b[2].get() == 1:
        messagebox.showinfo("Hexa Decimal To Octal", "When converting from hexadecimal to octal, it is often easier to first convert the hexadecimal number into binary and then from binary into octal.")
    elif var_a[3].get() == 1 and var_b[3].get() == 1:
        messagebox.showinfo("Hecxa Decimal Number System", "Hexa Decimal number represents any number using 10 digits and 6 alphabetical letters.\nHexa Decimal number system contains 0, 1, 2, 3, 4, 5, 6, 7, 8 and 9 as digits and A, B, C, D, E and F as alphabetical letters.")
    else:
        messagebox.showinfo("REQUIREMENT", "Choose options on the both side")


btn_explanation = Button(root, text="EXPLANATION", bd=5, width=15, bg="#CC00CC", relief="groove", command=explanation)
btn_explanation.grid(row=3, column=4)


def history():
    try:
        filename = "HISTORY.txt"
        file = open(filename, "r")
        data = file.readlines()
        m = ""
        for i in data:
            m = m + str(i) + "\n"
        messagebox.showinfo("HISTORY", str(m))
        file.close()
    except:
        messagebox.showinfo("EMPTY","There are no histoty recorded.")


btn_history = Button(root, text="HISTORY", bd=5, width=15, bg="cyan", relief="groove", command=history)
btn_history.grid(row=4, column=4)


def about():
    messagebox.showinfo("ABOUT","Name: Utsab Sen\nEmail: utsabsen1999@gmail.com\nLOVELY PROFESSIONAL UNIVERSITY\n  <3 INDIA <3")

btn_about = Button(root, text="ABOUT", bd=5, width=15, bg="grey", relief="groove", command=about)
btn_about.grid(row=5, column=4)

btn_exit = Button(root, text="EXIT", bd=5, width=15, bg="red", relief="groove", command=root.destroy)
btn_exit.grid(row=6, column=4)

root.mainloop()
