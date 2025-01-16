import tkinter as tk
from tkinter import filedialog
import subprocess

def select_pdf_file():
    filepath = filedialog.askopenfilename(title="Select PDF File", filetypes=[("PDF files", "*.pdf")])
    if filepath:
        entry_pdf.delete(0, tk.END)
        entry_pdf.insert(tk.END, filepath)

def add_password():
    input_pdf = entry_pdf.get()
    output_pdf = entry_output_pdf.get() + ".pdf" if entry_output_pdf.get() else input_pdf[:-4] + "_encrypted.pdf"
    user_password = entry_user_password.get()
    owner_password = entry_owner_password.get()
    
    command = f"qpdf --encrypt {user_password} {owner_password} 256 -- {input_pdf} {output_pdf}"
    
    process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    stdout, stderr = process.communicate()
    
    if stderr:
        tk.messagebox.showerror("Error", "Failed to add password.")
    else:
        tk.messagebox.showinfo("Success", "Password added successfully!")

#window
root = tk.Tk()
root.title("PDF Password Adder")

#labels and widgets
label_pdf = tk.Label(root, text="Select PDF File:")
label_pdf.grid(row=0, column=0, padx=5, pady=5, sticky="w")

entry_pdf = tk.Entry(root, width=60)
entry_pdf.grid(row=0, column=1, padx=5, pady=5, columnspan=2, sticky="ew")

button_browse = tk.Button(root, text="Browse", command=select_pdf_file)
button_browse.grid(row=0, column=3, padx=5, pady=5)

label_output_pdf = tk.Label(root, text="Output PDF Name (optional):")
label_output_pdf.grid(row=1, column=0, padx=5, pady=5, sticky="w")

entry_output_pdf = tk.Entry(root, width=45)
entry_output_pdf.grid(row=1, column=1, padx=5, pady=5, columnspan=2, sticky="ew")

label_user_password = tk.Label(root, text="User Password:")
label_user_password.grid(row=2, column=0, padx=5, pady=5, sticky="w")

entry_user_password = tk.Entry(root, show="*", width=27)
entry_user_password.grid(row=2, column=1, padx=5, pady=5, sticky="ew")

label_owner_password = tk.Label(root, text="Owner Password:")
label_owner_password.grid(row=3, column=0, padx=5, pady=5, sticky="w")

entry_owner_password = tk.Entry(root, show="*", width=27)
entry_owner_password.grid(row=3, column=1, padx=5, pady=5, sticky="ew")

#button
button_add_password = tk.Button(root, text="Add Password", command=add_password, width=int(15*1.2), bg="beige", activebackground="lightyellow")
button_add_password.grid(row=4, column=1, columnspan=2, padx=5, pady=5)

#row and column weights
root.grid_rowconfigure((0, 1, 2, 3), weight=1)
root.grid_columnconfigure((1, 2), weight=1)

#run
root.mainloop()

