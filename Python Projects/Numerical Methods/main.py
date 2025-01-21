import os

import pandas as pd
import tkinter as tk
from tkinter import ttk, Button, filedialog, messagebox
from lagrange import lagrange
from plot import plot, plot_approximate

data_sets = []
file_names = []


# append imported data to data set list
def append(x, y, file_path):
    data_sets.append((x, y))
    file_names.append(os.path.basename(file_path))
    update_combobox()


# browse for Excel file
def browse_file():
    file_path = filedialog.askopenfilename(filetypes=[("Excel Files", "*.xlsx;*.xls")])

    load_data(file_path)
    x, y = data_sets[-1]

    plot(x, y)


# load excel file
def load_data(file_path):
    # df = pd.read_excel(file_path)
    # df = df.iloc[-100:]

    # x = df["Date"].values
    # y = df["Open"].values

    y = [14460, 14220, 13820, 13440, 13090, 12740, 12420, 12110, 11810, 11530, 11260, 11010, 10770, 10530, 10300, 10080, 9860, 9660, 9460, 9270, 9080, 8900, 8730, 8570, 8410, 8250, 8110, 7960, 7820, 7690, 7560, 7430, 7300, 7180, 7070, 6950, 6840, 6730, 6630, 6530, 6410]
    x = [i for i in range(len(y))]

    append(x, y, file_path)


# calculate interpolation/extrapolation using app
def main():
    num_data_points = int(slider.get())

    if not data_sets:
        messagebox.showerror("Error", "No data sets loaded. Please open a file.")
        return

    try:
        date_string = entry_box.get().split()
        dates = [pd.to_datetime(date_str, format="%Y-%m-%d") for date_str in date_string]

        selected_data_set = data_set_combobox.current()

        if selected_data_set == -1:
            messagebox.showerror("Error", "No data set selected. Please choose a data set.")
            return

        x, y = data_sets[selected_data_set]

        if num_data_points > len(x):
            messagebox.showerror("Error", "Number of data points selected exceeds available data.")

        for date in dates:
            output = lagrange(x, y, date, num_data_points)
            plot_approximate(x, y, date, output)

            if date >= max(x):
                print("Extrapolated value on {}: {}".format(date, output))
            else:
                print("Interpolated value on {}: {}".format(date, output))

    except ValueError:
        messagebox.showerror("Error", "Invalid input. Please enter a valid date in the format YYYY-MM-DD.")
        return


# update slider event
def slider_changed(event):
    current_value = int(slider.get())
    slider_value_label.config(text=f"Data Points Selected: {current_value}")


# update combobox function
def update_combobox():
    data_set_combobox["values"] = file_names
    data_set_combobox.current(len(file_names) - 1)


# plot data set function
def plot_data_set():
    selected_data_set = data_set_combobox.current()

    if selected_data_set == -1:
        messagebox.showerror("Error", "No data set selected. Please choose a data set.")
        return

    x, y = data_sets[selected_data_set]
    plot(x, y)


app = tk.Tk()
app.geometry("400x200")
app.resizable(False, False)
app.title("STOCK PREDICTION")

# slider
slider_label = ttk.Label(app, text="Data Points:")
slider_label.grid(column=0, row=0, pady=10, padx=10, sticky="w")
slider = ttk.Scale(app, from_=1, to=100, orient="horizontal", command=slider_changed)
slider.grid(column=1, row=0, pady=10, padx=10, sticky="we")
app.columnconfigure(0, weight=1)
app.columnconfigure(1, weight=3)
slider_value_label = ttk.Label(app, text="Data Points Selected: 1")
slider_value_label.grid(column=1, row=1, pady=5, padx=10, sticky="w")

# entry box
entry_label = ttk.Label(app, text="Enter Point:")
entry_label.grid(column=0, row=2, pady=10, padx=10, sticky="w")
entry_box = ttk.Entry(app)
entry_box.grid(column=1, row=2, pady=10, padx=10, sticky="we")

# calculate button
calculate_button = Button(app, text="Calculate", command=main)
calculate_button.grid(column=2, row=2, pady=10, padx=10, sticky="w")

# combo box
data_set_combobox = ttk.Combobox(app)
data_set_combobox.grid(column=1, row=4, pady=10, padx=10, sticky="we")
data_set_combobox_label = ttk.Label(app, text="Select data set:")
data_set_combobox_label.grid(column=0, row=4, pady=10, padx=10, sticky="w")

# plot from combobox button
plot_button = Button(app, text="Plot", command=plot_data_set)
plot_button.grid(column=2, row=4, pady=10, padx=10, sticky="w")

# menu bar
menu_bar = tk.Menu(app)
file_menu = tk.Menu(menu_bar, tearoff=0)
file_menu.add_command(label="Open", command=browse_file)
file_menu.add_separator()
file_menu.add_command(label="Exit", command=app.quit)
menu_bar.add_cascade(label="File", menu=file_menu)

app.config(menu=menu_bar)

app.mainloop()
