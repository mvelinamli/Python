# 1) TR_Bileşenleri içeri aktarma.EN_Importing the components.
import tkinter as tk
from tkinter import messagebox

# 2) TR_Ana pencereyi oluşturma.EN_Creating the main window.
root = tk.Tk()
root.title("To-Do List")
root.geometry("400x400")

# 3)TR_Liste kutusu ve kaydırma çubuğu ekleme.EN_Add a list box and scroll bar.

    #Listbox
listbox = tk.Listbox(root, width=50, height=15)
listbox.pack(pady=10)

    #Scrollbar
scrollbar = tk.Scrollbar(root)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
listbox.config(yscrollcommand=scrollbar.set)
scrollbar.config(command=listbox.yview)

# 4)TR_Giriş alanı ve düğmeler ekleme.EN_Add an input field and buttons.

    #input field
entry = tk.Entry(root, width=45)
entry.pack(pady=10)

    #button frame
button_frame = tk.Frame(root)
button_frame.pack(pady=10)

    #buttons
add_button = tk.Button(button_frame, text="Add", command=lambda: add_task)
add_button.grid(row=0, column=0, padx=5)

delete_button = tk.Button(button_frame, text="Delete", command=lambda: delete_task)
delete_button.grid(row=0, column=1, padx=5)

clear_button = tk.Button(button_frame, text="Clear", command=lambda: clear_tasks)
clear_button.grid(row=0, column=2, padx=5)

# 5)TR_Fonksiyon tanımlama.EN_Function definition.

def add_task():
    task = entry.get()
    if task:
        listbox.insert(tk.END, task)
        entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Uyarı", "Lütfen bir iş seçin!")

def delete_task():
    try:
        selected_task_index = listbox.curselection()[0]
        listbox.delete(selected_task_index)
    except IndexError:
        messagebox.showwarning("Error", "Please select a task to delete")
def clear_tasks():
    listbox.delete(0, tk.END)

root.mainloop()