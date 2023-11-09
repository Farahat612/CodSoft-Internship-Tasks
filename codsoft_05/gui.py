import tkinter as tk
from tkinter import messagebox

class Contact:
    def __init__(self, name, phone_number, email, address):
        self.name = name
        self.phone_number = phone_number
        self.email = email
        self.address = address

class ContactBookGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Contact Book")
        self.root.geometry("500x600")
        self.root.configure(bg="#212529")

        self.contacts = []

        self.create_widgets()

    def create_widgets(self):
        self.title_label = tk.Label(self.root, text="Contact Book", font=("Arial", 20), fg="#ffffff", bg="#212529")
        self.title_label.pack(pady=20)
        
        
        self.name_frame = tk.Frame(self.root, bg="#212529")
        self.name_frame.pack(pady=20)

        self.name_label = tk.Label(self.name_frame, text="Name:", font=("Arial", 12), fg="#ffffff", bg="#212529")
        self.name_label.pack(side=tk.LEFT, padx=10)
        self.name_entry = tk.Entry(self.name_frame, font=("Arial", 12))
        self.name_entry.pack(side=tk.LEFT, padx=10)
        
        
        
        self.phone_frame = tk.Frame(self.root, bg="#212529")
        self.phone_frame.pack(pady=20)

        self.phone_label = tk.Label(self.phone_frame, text="Phone:", font=("Arial", 12), fg="#ffffff", bg="#212529")
        self.phone_label.pack(side=tk.LEFT, padx=10)
        self.phone_entry = tk.Entry(self.phone_frame, font=("Arial", 12))
        self.phone_entry.pack(side=tk.LEFT, padx=10)
        
        
        
        self.email_frame = tk.Frame(self.root, bg="#212529")
        self.email_frame.pack(pady=20)

        self.email_label = tk.Label(self.email_frame, text="Email:", font=("Arial", 12), fg="#ffffff", bg="#212529")
        self.email_label.pack(side=tk.LEFT, padx=10)
        self.email_entry = tk.Entry(self.email_frame, font=("Arial", 12))
        self.email_entry.pack(side=tk.LEFT, padx=10)
        
        
        
        self.address_frame = tk.Frame(self.root, bg="#212529")
        self.address_frame.pack(pady=20)

        self.address_label = tk.Label(self.address_frame, text="Address:", font=("Arial", 12), fg="#ffffff", bg="#212529")
        self.address_label.pack(side=tk.LEFT, padx=5)
        self.address_entry = tk.Entry(self.address_frame, font=("Arial", 12))
        self.address_entry.pack(side=tk.LEFT, padx=10)
        
        

        self.button_frame = tk.Frame(self.root, bg="#212529")
        self.button_frame.pack(pady=20)

        self.add_button = tk.Button(self.button_frame, text="Add Contact", font=("Arial", 12), fg="#ffffff", bg="#0d6efd", command=self.add_contact)
        self.add_button.pack(side=tk.LEFT, padx=10)
        self.view_button = tk.Button(self.button_frame, text="View Contact List", font=("Arial", 12), fg="#ffffff", bg="#0d6efd", command=self.view_contact_list)
        self.view_button.pack(side=tk.LEFT, padx=10)
        
        
        
        self.search_frame = tk.Frame(self.root, bg="#212529")
        self.search_frame.pack(pady=20)

        self.search_label = tk.Label(self.search_frame, text="Search:", font=("Arial", 12), fg="#ffffff", bg="#212529")
        self.search_label.pack(side=tk.LEFT, padx=10)
        self.search_entry = tk.Entry(self.search_frame, font=("Arial", 12))
        self.search_entry.pack(side=tk.LEFT, padx=10)

        self.search_button = tk.Button(self.root, text="Search", font=("Arial", 12), fg="#ffffff", bg="#0d6efd", command=self.search_contact)
        self.search_button.pack(pady=10)
        
       
        
    def show_contact_details(self, contact):
        contact_details_window = tk.Toplevel(self.root)
        contact_details_window.title("Contact Details")
        self.center_window(contact_details_window)

        contact_info = f"Name: {contact.name}\nPhone Number: {contact.phone_number}\nEmail: {contact.email}\nAddress: {contact.address}"
        contact_label = tk.Label(contact_details_window, text=contact_info)
        contact_label.pack()

        delete_button = tk.Button(contact_details_window, text="Delete", command=self.delete_contact(contact))
        delete_button.pack()

        update_button = tk.Button(contact_details_window, text="Update", command=lambda c=contact: self.update_contact_window(c))
        update_button.pack()

    def add_contact(self):
        name = self.name_entry.get()
        phone_number = self.phone_entry.get()
        email = self.email_entry.get()
        address = self.address_entry.get()

        contact = Contact(name, phone_number, email, address)
        self.contacts.append(contact)

        messagebox.showinfo("Success", "Contact added successfully!")

        self.clear_entries()

    def view_contact_list(self):
        if self.contacts:
            contact_list_window = tk.Toplevel(self.root)
            contact_list_window.title("Contact List")
            self.center_window(contact_list_window)

            contact_frame = tk.Frame(contact_list_window)
            contact_frame.pack()

            for contact in self.contacts:
                contact_info = f"Name: {contact.name}, Phone Number: {contact.phone_number}"
                contact_label = tk.Label(contact_frame, text=contact_info)
                contact_label.pack()

                details_button = tk.Button(contact_frame, text="Details", command=lambda c=contact: self.show_contact_details(c))
                details_button.pack()
        else:
            messagebox.showinfo("Contact List", "No contacts found.")
            
        
    def search_contact(self):
        search_term = self.search_entry.get()
        found_contacts = []

        for contact in self.contacts:
            if search_term.lower() in contact.name.lower() or search_term in contact.phone_number:
                found_contacts.append(contact)

        if found_contacts:
            search_results_window = tk.Toplevel(self.root)
            search_results_window.title("Search Results")
            self.center_window(search_results_window)

            search_frame = tk.Frame(search_results_window)
            search_frame.pack()

            for contact in found_contacts:
                contact_info = f"Name: {contact.name}, Phone Number: {contact.phone_number}"
                contact_label = tk.Label(search_frame, text=contact_info)
                contact_label.pack()

                details_button = tk.Button(search_frame, text="Details", command=lambda c=contact: self.show_contact_details(c))
                details_button.pack()
        else:
            messagebox.showinfo("Search Results", "No contacts found.")

    def update_contact(self):
        search_term = self.search_entry.get()
        found_contacts = []

        for contact in self.contacts:
            if search_term.lower() in contact.name.lower() or search_term in contact.phone_number:
                found_contacts.append(contact)

        if found_contacts:
            contact = found_contacts[0]
            name = self.name_entry.get()
            phone_number = self.phone_entry.get()
            email = self.email_entry.get()
            address = self.address_entry.get()

            contact.name = name
            contact.phone_number = phone_number
            contact.email = email
            contact.address = address

            messagebox.showinfo("Success", "Contact updated successfully!")

            self.clear_entries()
        else:
            messagebox.showinfo("Error", "Contact not found.")

    def delete_contact(self, contact):
        def delete():
            self.contacts.remove(contact)
            messagebox.showinfo("Success", "Contact deleted successfully!")
            contact_details_window.destroy()

        return delete
       
        
    def update_contact_window(self, contact):
        update_window = tk.Toplevel(self.root)
        update_window.title("Update Contact")
        self.center_window(update_window)

        name_label = tk.Label(update_window, text="Name:", font=("Arial", 12))
        name_label.pack()
        name_entry = tk.Entry(update_window, font=("Arial", 12))
        name_entry.insert(tk.END, contact.name)
        name_entry.pack()

        phone_label = tk.Label(update_window, text="Phone Number:", font=("Arial", 12))
        phone_label.pack()
        phone_entry = tk.Entry(update_window, font=("Arial", 12))
        phone_entry.insert(tk.END, contact.phone_number)
        phone_entry.pack()

        email_label = tk.Label(update_window, text="Email:", font=("Arial", 12))
        email_label.pack()
        email_entry = tk.Entry(update_window, font=("Arial", 12))
        email_entry.insert(tk.END, contact.email)
        email_entry.pack()

        address_label = tk.Label(update_window, text="Address:", font=("Arial", 12))
        address_label.pack()
        address_entry = tk.Entry(update_window, font=("Arial", 12))
        address_entry.insert(tk.END, contact.address)
        address_entry.pack()

        save_button = tk.Button(update_window, text="Save", command=lambda: self.save_updated_contact(contact, name_entry.get(), phone_entry.get(), email_entry.get(), address_entry.get(), update_window))
        save_button.pack()

    def save_updated_contact(self, contact, name, phone_number, email, address, update_window):
        contact.name = name
        contact.phone_number = phone_number
        contact.email = email
        contact.address = address
        messagebox.showinfo("Success", "Contact updated successfully!")
        update_window.destroy()

    def clear_entries(self):
        self.name_entry.delete(0, tk.END)
        self.phone_entry.delete(0, tk.END)
        self.email_entry.delete(0, tk.END)
        self.address_entry.delete(0, tk.END)
        self.search_entry.delete(0, tk.END)
        
    
    def center_window(self, win, min_width=400, min_height=400):
        win.update_idletasks()
        width = max(win.winfo_reqwidth(), min_width)
        height = max(win.winfo_reqheight(), min_height)
        x = (win.winfo_screenwidth() // 2) - (width // 2)
        y = (win.winfo_screenheight() // 2) - (height // 2)
        win.geometry(f"{width}x{height}+{x}+{y}")

def main():
    root = tk.Tk()
    root.configure(bg="#0d6efd")
    contact_book_gui = ContactBookGUI(root)
    contact_book_gui.center_window(root)
    root.mainloop()

if __name__ == "__main__":
    main()
    