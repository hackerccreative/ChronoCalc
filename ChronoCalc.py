import tkinter as tk
from tkinter import messagebox
import datetime
def current_day():
    today = datetime.datetime.now()
    return today.strftime("%A")

def large_number_mod(large_num_str, mod): 
    result = 0
    for char in large_num_str:
        result = (result * 10 + int(char)) % mod
    return result

def mod_exp(base, power, mod):
    return pow(base, power, mod)

def update_result(day):
    result_label.config(text=f"The day will be: {day}")

def integer_choice():
    days = entry.get()
    if days.isdigit():
        result = (large_number_mod(days, 7) + current_day_index) % 7
        update_result(week_days[result])
    else:
        messagebox.showerror("Invalid input", "Please enter a valid integer.")

def power_choice():
    base = entry.get()
    power = entry_power.get()
    if base.isdigit() and power.isdigit():
        c_base = large_number_mod(base, 7)
        c_power = large_number_mod(power, 6)
        result = (mod_exp(c_base, c_power, 7) + current_day_index) % 7
        update_result(week_days[result])
    else:
        messagebox.showerror("Invalid input", "Please enter valid integers for base and power.")

def show_integer_input():
    entry_label.config(text="Enter the number of days:")
    entry.pack(pady=5)
    entry_power.pack_forget()
    submit_button.config(command=integer_choice)
    
def show_power_input():
    entry_label.config(text="Enter the base:")
    entry.pack(pady=5)
    entry_power.pack(pady=5)
    submit_button.config(command=power_choice)

def handle_choice():
    choice = var.get()
    if choice == 1:
        show_integer_input()
    elif choice == 2:
        show_power_input()

week_days = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
current_day_index = week_days.index(current_day())

root = tk.Tk()
root.title("ChronoCalc")
root.geometry("400x350")
root.config(bg="black")

heading_label = tk.Label(root, text="ChronoCalc", font=("Courier", 24, "bold"), bg="black", fg="cyan")
heading_label.pack(pady=10)

current_day_label = tk.Label(root, text=f"Today is: {week_days[current_day_index]}", font=("Arial", 12), bg="black", fg="white")
current_day_label.pack(pady=5)

var = tk.IntVar()

int_radio = tk.Radiobutton(root, text="Enter Days (Integer)", variable=var, value=1, font=("Arial", 12), bg="black", fg="cyan", command=handle_choice)
int_radio.pack(pady=5)

power_radio = tk.Radiobutton(root, text="Enter Base and Power", variable=var, value=2, font=("Arial", 12), bg="black", fg="cyan", command=handle_choice)
power_radio.pack(pady=5)

entry_label = tk.Label(root, text="", font=("Arial", 12), bg="black", fg="white")
entry_label.pack(pady=5)

entry = tk.Entry(root, font=("Arial", 14))
entry_power = tk.Entry(root, font=("Arial", 14))

submit_button = tk.Button(root, text="Submit", font=("Arial", 12), bg="cyan", fg="black")
submit_button.pack(pady=10)

result_label = tk.Label(root, text="", font=("Arial", 14, "bold"), bg="black", fg="lime")
result_label.pack(pady=10)

root.mainloop()
