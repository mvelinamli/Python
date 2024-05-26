import tkinter as tk

def yeni_not_ekle():
    not_metni = entry.get()
    if not_metni.strip():
        listbox.insert(tk.END, not_metni)
        entry.delete(0, tk.END)
        dosyaya_kaydet()

def dosyaya_kaydet():
    with open("uygulamalarlaPython/notlar.txt", "w") as dosya:
        notlar.listbox.get(0, tk.END)
        for not_ in notlar:
            dosya.write(not_ + "\n")
    
def notlari_yukle():
    try:
            
        with open("ugulamalarlaPython/notlar.txt", "r") as dosya:
            notlar = dosya.readlines()
        for not_ in notlar:
            listbox.insert(tk.END, not_.strip())
    except FileNotFoundError:
        pass

root = tk.Tk()
root.title("Notepad")

frame = tk.Frame(root)
frame.pack(padx=10, pady=10)

listbox = tk.Listbox(frame, width=50, height=50)
listbox.grid(row=0, column=0, padx=5, pady=5)

scrollbar = tk.Scrollbar(frame, orient=tk.VERTICAL)
scrollbar.grid(row=0, column=1, sticky=tk.NS)
scrollbar.config(command=listbox.yview)
listbox.config(yscrollcommand=scrollbar.set)

entry = tk.Entry(frame, width=50)
entry.grid(row=1, column=0, padx=5, pady=5)

ekle_button = tk.Button(frame, text="Yeni Not Ekle", command=yeni_not_ekle)
ekle_button.grid(row=2, column=0, padx=5, pady=5)

notlari_yukle()

root.mainloop()



