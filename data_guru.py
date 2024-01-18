from tkinter import *
from tkinter import ttk

class Data_Guru:
    def __init__(self, root):
        self.root = root
        self.root.title("Data Guru SMK KRIAN 1")
        self.root.geometry("800x300")

        self.judul = Label(root, text='Data Guru')
        self.judul.pack()

        # Membuat Treeview
        self.tree = ttk.Treeview(root, columns=("Kode Guru", "Nama", "Mata Pelajaran", "Kelas", "Jadwal"))

        # Menetapkan heading untuk kolom
        self.tree.heading("Kode Guru", text="Kode Guru")
        self.tree.heading("Nama", text="Nama")
        self.tree.heading("Mata Pelajaran", text="Mata Pelajaran")
        self.tree.heading("Kelas", text="Kelas")
        self.tree.heading("Jadwal", text="Jadwal")

        # Menetapkan lebar kolom
        self.tree.column("Kode Guru", width=100)
        self.tree.column("Nama", width=150)
        self.tree.column("Mata Pelajaran", width=100)
        self.tree.column("Kelas", width=100)
        self.tree.column("Jadwal", width=150)


        # Menambahkan data ke Treeview
        self.tree.insert('', "end", values=("20", "Pak Onny", "WEB", "RPL 4", "Senin"))
        self.tree.insert('', "end", values=("05", "Pak Robby", "BD", "RPL 4", "Selasa"))
        self.tree.insert('', "end", values=("63", "Bu Nia", "PBO", "RPL 4", "Kamis"))
        self.tree.insert('', "end", values=("51", "Pak Fachri", "PKK", "RPL 4", "Rabu"))
        self.tree.insert('', "end", values=("35", "Bu Rinda", "MTK", "RPL 4", "Kamis"))
        # Menampilkan Treeview
        self.tree.pack()

if __name__ == "__main__":
    root = Tk()
    app = Data_Guru(root)
    root.mainloop()