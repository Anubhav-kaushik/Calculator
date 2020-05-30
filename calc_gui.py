from tkinter import *
from tkinter import messagebox


# Functions
def get_num(number):
    """Show the input numbers on the screen."""
    global operator_holder
    if operator_holder == "empty":
        # This expression help in clear out the screen when user enter a number at the starting (when 0 is diplayed)
        # and when there comes a result.
        clear_display()
        operator_holder = None
    display_screen.insert(20, number)  # Handles only numbers whose length is less than or equal to 20.


def show_operator(operator: str):
    """Show the selected operator."""
    operators_screen.delete(0, END)
    operators_screen.insert(0, operator)


def show_cache_numbers(number):
    cache_screen.delete(0, END)
    cache_screen.insert(0, number)


def clear_display():
    """Delete all the digits displayed on the main screen."""
    display_screen.delete(0, END)


def del_digit():
    """Delete digit by digit."""
    dig_len = len(display_screen.get())
    display_screen.delete(dig_len - 1)


temp_var = "0"  # Save the updated result
operator_holder = "empty"  # Save the last operation executed


def operator_call_function(operator):
    global operator_holder, temp_var

    operator_function = None
    if operator == "+":
        operator_function = summation
    elif operator == "-":
        operator_function = subtraction
    elif operator == "x":
        operator_function = product
    elif operator == "/":
        operator_function = division
    elif operator == "=":
        operator_function = equal_to

    if operator_holder is None or operator_holder == "empty":
        try:
            temp_var = float(display_screen.get())
        except ValueError:
            messagebox.showerror(title="ERROR", message="Invalid Input!\nOnly operates on decimal numbers.")
            clear_display()
            operators_screen.delete(0, END)
            cache_screen.delete(0, END)
            return
        clear_display()
        operator_holder = operator_function
        show_operator(operator)
        show_cache_numbers(temp_var)
        return

    operator_holder()
    operator_holder = operator_function
    show_operator(operator)


def summation():
    """Add the numbers"""
    global temp_var, operator_holder

    try:
        temp = float(display_screen.get())
    except ValueError:
        messagebox.showerror(title="ERROR", message="Invalid Input!\nOnly operates on decimal numbers.")
        clear_display()
        operators_screen.delete(0, END)
        cache_screen.delete(0, END)
        operator_holder = None
        temp_var = "0"
        return

    clear_display()
    temp_var += temp
    show_cache_numbers(temp_var)


def product():
    """Multiply the numbers"""
    global temp_var, operator_holder

    try:
        temp = float(display_screen.get())
    except ValueError:
        messagebox.showerror(title="ERROR", message="Invalid Input!\nOnly operates on decimal numbers.")
        clear_display()
        operators_screen.delete(0, END)
        cache_screen.delete(0, END)
        operator_holder = None
        temp_var = "0"
        return

    clear_display()
    temp_var *= temp
    show_cache_numbers(temp_var)


def subtraction():
    """Subtract the numbers"""
    global temp_var, operator_holder

    try:
        temp = float(display_screen.get())
    except ValueError:
        messagebox.showerror(title="ERROR", message="Invalid Input!\nOnly operates on decimal numbers.")
        clear_display()
        operators_screen.delete(0, END)
        cache_screen.delete(0, END)
        operator_holder = None
        temp_var = "0"
        return

    clear_display()
    temp_var -= temp
    show_cache_numbers(temp_var)


def division():
    """Divide the numbers."""
    global temp_var, operator_holder

    try:
        temp = float(display_screen.get())
    except ValueError:
        messagebox.showerror(title="ERROR", message="Invalid Input!\nOnly operates on decimal numbers.")
        clear_display()
        operators_screen.delete(0, END)
        cache_screen.delete(0, END)
        operator_holder = None
        temp_var = "0"
        return

    clear_display()
    try:
        temp_var /= temp
    except ZeroDivisionError:
        messagebox.showwarning(title="Infinity", message="Undefined number occured!")
        clear_display()
        operators_screen.delete(0, END)
        cache_screen.delete(0, END)
        operator_holder = None
        temp_var = "0"
        return
    show_cache_numbers(temp_var)


def equal_to():
    """Show the result on the screen."""
    global temp_var, operator_holder

    if operator_holder == equal_to or \
            operator_holder is None:  # Handles input without operator e.g. 4(input) = 4(output)
        temp_var = float(display_screen.get())

    operator_call_function("=")
    clear_display()
    operators_screen.delete(0, END)
    cache_screen.delete(0, END)
    try:
        if temp_var == int(temp_var):  # Differentiate between int and float values
            temp_var = int(temp_var)
    except ValueError:
        pass
    finally:
        display_screen.insert(0, temp_var)  # Display the result on the screen
        temp_var = "0"
        operator_holder = "empty"


if __name__ == '__main__':
    # GUI for calculator
    root = Tk()
    root.title("Calculator")

    # Background colors
    num_pad_bg = "#7777ff"
    operator_bg = "#4B0082"

    # Display for numbers (On the top-left corner a large display)
    display_screen = Entry(root, width=11, bd=2, font=["", "24", "bold"], bg="#ffffff", fg="#000000")
    display_screen.grid(row=0, column=0, columnspan=3, rowspan=3)
    display_screen.insert(0, 0)

    # Display for entered  numbers (On the top-right corner below the operator screen)
    cache_screen = Entry(root, width=5, font=["", "13", "bold"], bg="#ffffff", fg="#000000")
    cache_screen.grid(row=1, column=3, columnspan=1, rowspan=2)

    # Display for the Operators (On the top-right corner above the cached number screen)
    operators_screen = Entry(root, width=6, font=["", "11", "bold"], bg="#ffffff", fg="#000000")
    operators_screen.grid(row=0, column=3, columnspan=1, rowspan=1)

    # Frame for buttons
    frame1 = Frame(root, bg="#004593", relief=SUNKEN)
    frame1.grid(row=3, column=0, rowspan=5, columnspan=4)

    # Buttons
    button_1 = Button(frame1, text="1", padx=22, font="bold", pady=20,
                      bg=num_pad_bg, command=lambda: get_num(1))
    button_2 = Button(frame1, text="2", padx=21, font="bold", pady=20,
                      bg=num_pad_bg, command=lambda: get_num(2))
    button_3 = Button(frame1, text="3", padx=21, font="bold", pady=20,
                      bg=num_pad_bg, command=lambda: get_num(3))
    button_4 = Button(frame1, text="4", padx=22, font="bold", pady=20,
                      bg=num_pad_bg, command=lambda: get_num(4))
    button_5 = Button(frame1, text="5", padx=21, font="bold", pady=20,
                      bg=num_pad_bg, command=lambda: get_num(5))
    button_6 = Button(frame1, text="6", padx=21, font="bold", pady=20,
                      bg=num_pad_bg, command=lambda: get_num(6))
    button_7 = Button(frame1, text="7", padx=22, font="bold", pady=20,
                      bg=num_pad_bg, command=lambda: get_num(7))
    button_8 = Button(frame1, text="8", padx=21, font="bold", pady=20,
                      bg=num_pad_bg, command=lambda: get_num(8))
    button_9 = Button(frame1, text="9", padx=21, font="bold", pady=20,
                      bg=num_pad_bg, command=lambda: get_num(9))
    button_0 = Button(frame1, text="0", padx=21, font="bold", pady=20,
                      bg=num_pad_bg, command=lambda: get_num(0))
    button_clear = Button(frame1, text="Clear", font="bold", padx=40, pady=20,
                          bg="#ff0011", command=clear_display)
    button_del = Button(frame1, text="Del", font="bold", padx=13, pady=20,
                        bg="#ff0011", command=del_digit)
    button_equal2 = Button(frame1, text="=", font="bold", padx=52, pady=20,
                           bg="#9400D3", fg="white", command=equal_to)
    button_dot = Button(frame1, text=".", font="Helvetica 20 bold", padx=16, pady=8,
                        bg="#4b3fD3", command=lambda: get_num("."))
    button_add = Button(frame1, text="+", font="bold", padx=20, pady=20,
                        bg=operator_bg, fg="white", command=lambda: operator_call_function("+"))
    button_mul = Button(frame1, text="x", font="bold", padx=21, pady=20,
                        bg=operator_bg, fg="white", command=lambda: operator_call_function("x"))
    button_sub = Button(frame1, text="-", font="bold", padx=22, pady=20,
                        bg=operator_bg, fg="white", command=lambda: operator_call_function("-"))
    button_div = Button(frame1, text="/", font="bold", padx=23.2, pady=20,
                        bg=operator_bg, fg="white", command=lambda: operator_call_function("/"))

    # Set buttons on position
    button_1.grid(row=5, column=0)
    button_2.grid(row=5, column=1)
    button_3.grid(row=5, column=2)

    button_4.grid(row=4, column=0)
    button_5.grid(row=4, column=1)
    button_6.grid(row=4, column=2)

    button_7.grid(row=3, column=0)
    button_8.grid(row=3, column=1)
    button_9.grid(row=3, column=2)

    button_0.grid(row=6, column=1)

    button_clear.grid(row=7, column=0, columnspan=2)
    button_del.grid(row=6, column=2)
    button_equal2.grid(row=7, column=2, columnspan=2)
    button_dot.grid(row=6, column=0)

    button_add.grid(row=3, column=3)
    button_mul.grid(row=4, column=3)
    button_sub.grid(row=5, column=3)
    button_div.grid(row=6, column=3)

    root.mainloop()
