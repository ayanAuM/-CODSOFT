import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk  #Import PIL for Image handling

# Create a dictionary to store contacts
contacts = {}

# Function to add a new contact
def add_contact():
    name = name_entry.get()
    phone = phone_entry.get()
    email = email_entry.get()
    address = address_entry.get()

    if name and phone:
        contacts[name] = {"Phone": phone, "Email": email, "Address": address}
        clear_fields()
        update_contact_list()
    else:
        messagebox.showwarning("Warning", "Name and Phone are required fields.")

# Function to update the contact list
def update_contact_list():
    contact_list.delete(0, tk.END)
    for name in contacts:
        contact_list.insert(tk.END, name)

# Function to display contact details when a contact is selected
def show_contact_details(event):
    selected_contact = contact_list.get(contact_list.curselection())
    if selected_contact in contacts:
        contact_details = contacts[selected_contact]
        details_label.config(text=f"Phone: {contact_details['Phone']}\nEmail: {contact_details['Email']}\nAddress: {contact_details['Address']}")

# Function to search for a contact by name or phone number
def search_contact():
    query = search_entry.get().lower()
    search_results = [name for name in contacts if query in name.lower() or query in contacts[name]['Phone']]
    contact_list.delete(0, tk.END)
    for name in search_results:
        contact_list.insert(tk.END, name)

# Function to update contact details
def update_contact():
    selected_contact = contact_list.get(contact_list.curselection())
    if selected_contact in contacts:
        name = name_entry.get()
        phone = phone_entry.get()
        email = email_entry.get()
        address = address_entry.get()

        if name and phone:
            contacts[selected_contact] = {"Phone": phone, "Email": email, "Address": address}
            clear_fields()
            update_contact_list()
        else:
            messagebox.showwarning("Warning", "Name and Phone are required fields.")
    else:
        messagebox.showerror("Error", "Select a contact to update.")

# Function to delete a contact
def delete_contact():
    selected_contact = contact_list.get(contact_list.curselection())
    if selected_contact in contacts:
        del contacts[selected_contact]
        clear_fields()
        update_contact_list()
    else:
        messagebox.showerror("Error", "Select a contact to delete.")

# Function to clear input fields
def clear_fields():
    name_entry.delete(0, tk.END)
    phone_entry.delete(0, tk.END)
    email_entry.delete(0, tk.END)
    address_entry.delete(0, tk.END)
    details_label.config(text="")

# Create the main window
root = tk.Tk()
root.title("Contact Book App")

# Loading the background image
background_image = Image.open("C:/Users/123ay/Downloads/background.jpg") # Providing the path of the image
background_photo =ImageTk.PhotoImage(background_image)

# Creating a canvas to display the background image
canvas = tk.Canvas(root)#width, height=background_image.height()#)

# Placing the background image on the canvas
canvas.create_image(0, 0, image= background_photo,  anchor = tk.NW)

# Create and configure widgets
name_label = tk.Label(root, text="Name:")
name_label.grid(row=0, column=0)
name_entry = tk.Entry(root)
name_entry.grid(row=0, column=1)

phone_label = tk.Label(root, text="Phone:")
phone_label.grid(row=1, column=0)
phone_entry = tk.Entry(root)
phone_entry.grid(row=1, column=1)

email_label = tk.Label(root, text="Email:")
email_label.grid(row=2, column=0)
email_entry = tk.Entry(root)
email_entry.grid(row=2, column=1)

address_label = tk.Label(root, text="Address:")
address_label.grid(row=3, column=0)
address_entry = tk.Entry(root)
address_entry.grid(row=3, column=1)

add_button = tk.Button(root, text="Add Contact", command=add_contact, bg='LightGreen')
add_button.grid(row=4, column=0, columnspan=2)

search_label = tk.Label(root, text="Search:")
search_label.grid(row=5, column=0)
search_entry = tk.Entry(root)
search_entry.grid(row=5, column=1)

search_button = tk.Button(root, text="Search", command=search_contact,bg ='red')
search_button.grid(row=6, column=0, columnspan=2)

update_button = tk.Button(root, text="Update Contact", command=update_contact)
update_button.grid(row=7, column=0, columnspan=2)

delete_button = tk.Button(root, text="Delete Contact", command=delete_contact, bg="red")
delete_button.grid(row=8, column=0, columnspan=2)

contact_list = tk.Listbox(root, selectmode=tk.SINGLE)
contact_list.grid(row=0, column=2, rowspan=9)
contact_list.bind('<<ListboxSelect>>', show_contact_details)

details_label = tk.Label(root, text="", justify=tk.LEFT)
details_label.grid(row=9, column=0, columnspan=3)

# Start the application
update_contact_list()
root.mainloop()
