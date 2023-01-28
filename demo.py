# https://www.thepythoncode.com/article/spreadsheet-app-using-tkinter-in-python
# Imports
from tkinter import *
import string, csv

# Define X and Y Axis Lists
# Gives the first 8 letters in lower case
xAxis = string.ascii_uppercase[0:4]
# Creates columns of 12 fields
yAxis = range(0, 12)

# Cells will hold the strings vars and the labels 
cells = {}

# Make a new Top Level Element (Window)
root = Tk()
# Set the the title to also mention the given file name
# if there is one
title = "Spreadsheet App"
root.title(title)

# Display the Y-axis labels
# Labels each row
for y in yAxis:
    label = Label(root, text = y, width=5, background='white')
    label.grid(row=y + 1, column=0)

# Display the X-axis labels with enumerate
# Enumerate takes a string of letters and turns them into an iterable
for i, x in enumerate(xAxis):
    label = Label(root, text = x, width=35, background='white')
    label.grid(row=0, column=i + 1, sticky='n')

# Display the Cells, by using a nested loop
for y in yAxis:
    for xcoor, x in enumerate(xAxis):
        # Generate a Unique ID for the cell with the coordinates
        id = f'{x}{y}'
         # Make String Var associated with the Cell - initialized to be blank
        var = StringVar(root, '', id)
         # Make Entry and label, offset each axis by one because of the lables
        e = Entry(root, textvariable=var, width=30)
        e.grid(row=y + 1, column=xcoor + 1)
        # Save the string var and a reference to the labels in the dictionary
        cells[id] = [var]

def get_data():
    for key, value in cells.items():
        print(key, ':', value[0].get())

        

def generate_csv():
    header = xAxis
    csv_data = []
    for key, value in cells.items():
        csv_data.append(value[0].get())
    counter = 0
    main_array = []
    for y in yAxis:
        inner_array = []
        for x in xAxis:
            inner_array.append(csv_data[counter])
            counter += 1
        main_array.append(inner_array)
    print(main_array)

    file = open('data.csv', 'w', encoding='UTF8', newline='')
    writer = csv.writer(file)
    # write the header
    writer.writerow(header)
    # write multiple rows
    writer.writerows(main_array)
    file.close()
    

submit_button = Button(root, text="Submit", command=get_data)
submit_button.grid(column=1, row=14)

generate_csv_button = Button(root, text="Generate CSV", command=generate_csv)
generate_csv_button.grid(column=2, row=14)

# Run the Mainloop
root.mainloop()
