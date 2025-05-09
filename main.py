import tkinter as tk
from tkinter import ttk, messagebox, simpledialog
import os
import sys

# Add the project directory to the path so we can import from utils
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from password_manager.utils.helpers import (
    initialize_database, 
    add_password, 
    get_all_passwords, 
    delete_password
)

class PasswordManager:
    def __init__(self, root):
        self.root = root
        self.root.title("Password Manager")
        self.root.geometry("700x500")
        self.root.resizable(True, True)
        
        # Initialize the database
        self.db_path = initialize_database()
        
        # Create main frame
        self.main_frame = ttk.Frame(root, padding="10")
        self.main_frame.pack(fill=tk.BOTH, expand=True)
        
        # Create form frame for adding passwords
        self.form_frame = ttk.LabelFrame(self.main_frame, text="Add New Password", padding="10")
        self.form_frame.pack(fill=tk.X, padx=5, pady=5)
        
        # Website entry
        ttk.Label(self.form_frame, text="Website:").grid(row=0, column=0, sticky=tk.W, pady=5)
        self.website_var = tk.StringVar()
        ttk.Entry(self.form_frame, textvariable=self.website_var, width=30).grid(row=0, column=1, sticky=tk.W, padx=5, pady=5)
        
        # Username entry
        ttk.Label(self.form_frame, text="Username:").grid(row=1, column=0, sticky=tk.W, pady=5)
        self.username_var = tk.StringVar()
        ttk.Entry(self.form_frame, textvariable=self.username_var, width=30).grid(row=1, column=1, sticky=tk.W, padx=5, pady=5)
        
        # Password entry
        ttk.Label(self.form_frame, text="Password:").grid(row=2, column=0, sticky=tk.W, pady=5)
        self.password_var = tk.StringVar()
        ttk.Entry(self.form_frame, textvariable=self.password_var, show="*", width=30).grid(row=2, column=1, sticky=tk.W, padx=5, pady=5)
        
        # Add button
        ttk.Button(self.form_frame, text="Add Password", command=self.add_new_password).grid(row=3, column=0, columnspan=2, pady=10)
        
        # Create table frame
        self.table_frame = ttk.LabelFrame(self.main_frame, text="Saved Passwords", padding="10")
        self.table_frame.pack(fill=tk.BOTH, expand=True, padx=5, pady=5)
        
        # Create treeview for passwords
        columns = ("id", "website", "username", "date_added")
        self.tree = ttk.Treeview(self.table_frame, columns=columns, show="headings", selectmode="browse")
        
        # Define column headings
        self.tree.heading("id", text="ID")
        self.tree.heading("website", text="Website")
        self.tree.heading("username", text="Username")
        self.tree.heading("date_added", text="Date Added")
        
        # Define column widths
        self.tree.column("id", width=50)
        self.tree.column("website", width=150)
        self.tree.column("username", width=150)
        self.tree.column("date_added", width=150)
        
        # Add scrollbar
        scrollbar = ttk.Scrollbar(self.table_frame, orient=tk.VERTICAL, command=self.tree.yview)
        self.tree.configure(yscroll=scrollbar.set)
        
        # Pack the tree and scrollbar
        self.tree.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        
        # Add right-click menu
        self.context_menu = tk.Menu(self.tree, tearoff=0)
        self.context_menu.add_command(label="Delete", command=self.delete_selected_password)
        
        # Bind right-click event
        self.tree.bind("<Button-3>", self.show_context_menu)
        
        # Load existing passwords
        self.load_passwords()
    
    def load_passwords(self):
        # Clear existing items
        for item in self.tree.get_children():
            self.tree.delete(item)
        
        # Get all passwords
        passwords = get_all_passwords(self.db_path)
        
        # Add to treeview
        for password in passwords:
            self.tree.insert("", tk.END, values=(
                password["id"],
                password["website"],
                password["username"],
                password["date_added"]
            ))
    
    def add_new_password(self):
        website = self.website_var.get().strip()
        username = self.username_var.get().strip()
        password = self.password_var.get().strip()
        
        # Validate inputs
        if not website or not username or not password:
            messagebox.showerror("Error", "All fields are required")
            return
        
        # Add to database
        add_password(self.db_path, website, username, password)
        
        # Clear inputs
        self.website_var.set("")
        self.username_var.set("")
        self.password_var.set("")
        
        # Update treeview
        self.load_passwords()
        
        messagebox.showinfo("Success", "Password added successfully")
    
    def show_context_menu(self, event):
        # Select the item under the cursor
        item = self.tree.identify_row(event.y)
        if item:
            self.tree.selection_set(item)
            self.context_menu.post(event.x_root, event.y_root)
    
    def delete_selected_password(self):
        # Get selected item
        selected_item = self.tree.selection()
        if not selected_item:
            return
        
        # Get the ID of the selected password
        password_id = self.tree.item(selected_item, "values")[0]
        
        # Confirm deletion
        if messagebox.askyesno("Confirm", "Are you sure you want to delete this password?"):
            # Delete from database
            delete_password(self.db_path, password_id)
            
            # Update treeview
            self.load_passwords()
            
            messagebox.showinfo("Success", "Password deleted successfully")

if __name__ == "__main__":
    root = tk.Tk()
    app = PasswordManager(root)
    root.mainloop() 
