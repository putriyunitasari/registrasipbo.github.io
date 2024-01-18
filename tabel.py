from tkinter import *
from tkinter import ttk

class AplikasiTkinter:
    def __init__(self, root):
        self.root = root
        self.root.title("Contoh Treeview")
        self.root.geometry("800x300")

        self.judul = Label(root, text='Data Siswa')
        self.judul.pack()

        # Membuat Treeview
        self.tree = ttk.Treeview(root, columns=("NIS", "Nama", "Kelas"))

        # Menetapkan heading untuk kolom
        self.tree.heading("NIS", text="NIS")
        self.tree.heading("Nama", text="Nama")
        self.tree.heading("Kelas", text="Kelas")

        # Menetapkan lebar kolom
        self.tree.column("NIS", width=100)
        self.tree.column("Nama", width=150)
        self.tree.column("Kelas", width=100)

        # Menambahkan data ke Treeview
        self.tree.insert('', "end", values=("001", "John Doe", "RPL 2"))
        self.tree.insert('', "end", values=("002", "Jane Doe", "RPL 2"))
        self.tree.insert('', "end", values=("003", "Bob Smith", "RPL 2"))
        # Menampilkan Treeview
        self.tree.pack()

if __name__ == "__main__":
    root = Tk()
    app = AplikasiTkinter(root)
    root.mainloop()