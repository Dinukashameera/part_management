from tkinter import *
from tkinter import messagebox
from db import Databases


db = Databases()


def populate_List():
    part_List.delete(0, END)
    for row in db.fetch():
        part_List.insert(END, row)


def add_item():
    if(part_text.get() == '' or customer_text.get() == '' or retail_text.get() == '' or price_text.get() == ''):
        messagebox.showerror('Required Fields','Please Enter the Fields')
        return
    else:
        db.insert(part_text.get(), customer_text.get(),
              retail_text.get(), price_text.get())
    populate_List()

 



# creating a method
app = Tk()

# Part
part_text = StringVar()
part_label = Label(app, text='Part Name', font=('bold', 14), pady=20)
part_label.grid(row=0, column=0, sticky=W)
part_entry = Entry(app, textvariable=part_text)
part_entry.grid(row=0, column=1)

# customer
customer_text = StringVar()
customer_label = Label(app, text='Customer Name', font=('bold', 14))
customer_label.grid(row=0, column=2, sticky=W)
customer_entry = Entry(app, textvariable=customer_text)
customer_entry.grid(row=0, column=3)

# retailer Name
retail_text = StringVar()
retail_label = Label(app, text='Retailer  Name', font=('bold', 14))
retail_label.grid(row=1, column=0, sticky=W)
retail_entry = Entry(app, textvariable=retail_text)
retail_entry.grid(row=1, column=1)

# price
price_text = StringVar()
price_label = Label(app, text='Price', font=('bold', 14))
price_label.grid(row=1, column=2, sticky=W)
price_entry = Entry(app, textvariable=price_text)
price_entry.grid(row=1, column=3)


# part List, list box widget
part_List = Listbox(app, height=10, width=80)
part_List.grid(row=3, column=0, columnspan=8, rowspan=10, pady=20, padx=20)

# creating the scroll bar
scrollbar = Scrollbar(app)
scrollbar.grid(row=3, column=3)

# setting the scrol for the list box
part_List.configure(yscrollcommand=scrollbar.set)
scrollbar.configure(command=part_List.yview)


# creating the buttons
# add button
add_btn = Button(app, text='ADD PARTS', width=12, command=add_item)
add_btn.grid(row=2, column=0, pady=20)

remove_btn = Button(app, text='Remove PARTS', width=12, command=remove_item)
remove_btn.grid(row=2, column=1, pady=20)

update_btn = Button(app, text='Update PARTS', width=12, command=update_item)
update_btn.grid(row=2, column=2, pady=20)

clear_btn = Button(app, text='Clear PARTS', width=12, command=clear_item)
clear_btn.grid(row=2, column=3, pady=20)


# title of the project
app.title('Part Manager')
app.geometry('1000x800')

populate_List()

app.mainloop()
