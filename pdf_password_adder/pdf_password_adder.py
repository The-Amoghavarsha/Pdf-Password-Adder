import tkinter as tk
from tkinter import filedialog, messagebox
import subprocess

# Modularized with a main() function for better maintainability and reuse.

def select_pdf_file():
    filepath = filedialog.askopenfilename(
        title="Select PDF File", filetypes=[("PDF files", "*.pdf")]
    )
    if filepath:
        entry_pdf.delete(0, tk.END)
        entry_pdf.insert(tk.END, filepath)


def toggle_widgets(state):
    entry_pdf.config(state=state)
    entry_output_pdf.config(state=state)
    entry_user_password.config(state=state)
    entry_owner_password.config(state=state)
    button_browse.config(state=state)
    button_add_password.config(state=state)


def add_password():
    input_pdf = entry_pdf.get()
    if not input_pdf or input_pdf == "Select a PDF file...":
        messagebox.showerror("Error", "Please select a valid PDF file.")
        return

    output_pdf = (
        entry_output_pdf.get() + ".pdf"
        if entry_output_pdf.get()
        else input_pdf[:-4] + "_encrypted.pdf"
    )
    user_password = entry_user_password.get()
    owner_password = entry_owner_password.get()

    if not user_password:
        messagebox.showerror("Error", "User password cannot be empty.")
        return
    if not owner_password:
        messagebox.showerror("Error", "Owner password cannot be empty.")
        return

    command = [
        "qpdf", "--encrypt", user_password, owner_password, "256", "--", input_pdf, output_pdf
    ]

    toggle_widgets("disabled")
    try:
        process = subprocess.Popen(
            command, stdout=subprocess.PIPE, stderr=subprocess.PIPE
        )
        stdout, stderr = process.communicate()

        if process.returncode != 0:
            messagebox.showerror("Error", f"Failed to add password.\n{stderr.decode().strip()}")
        else:
            messagebox.showinfo("Success", "Password added successfully!")
    finally:
        toggle_widgets("normal")


def main():
    global root, entry_pdf, entry_output_pdf, entry_user_password, entry_owner_password, button_browse, button_add_password
    
    # GUI Setup
    root = tk.Tk()
    root.title("PDF Password Adder")

    # Labels and Widgets
    label_pdf = tk.Label(root, text="Select PDF File:")
    label_pdf.grid(row=0, column=0, padx=5, pady=5, sticky="w")

    entry_pdf = tk.Entry(root, width=60)
    entry_pdf.grid(row=0, column=1, padx=5, pady=5, columnspan=2, sticky="ew")
    entry_pdf.insert(0, "Select a PDF file...")

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

    # Button
    button_add_password = tk.Button(
        root, text="Add Password", command=add_password, width=int(15 * 1.2), bg="beige", activebackground="lightyellow"
    )
    button_add_password.grid(row=4, column=1, columnspan=2, padx=5, pady=5)

    # Run the Application
    root.mainloop()


if __name__ == "__main__":
    main()
