import sqlite3
from tkinter import *
from tkinter import ttk, messagebox
from datetime import datetime

class AplikasiKunjunganKerja:
    def __init__(self, root):
        self.root = root
        self.root.title("Aplikasi Data Kunjungan Kerja Instansi")
        self.root.geometry("800x600")
        self.root.configure(bg="#f0f8ff")

        # Koneksi database
        self.conn = sqlite3.connect('kunjungan_kerja.db')
        self.c = self.conn.cursor()
        self.c.execute('''
            CREATE TABLE IF NOT EXISTS kunjungan (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nama_instansi TEXT NOT NULL,
                tanggal TEXT NOT NULL,
                tujuan TEXT NOT NULL,
                penanggung_jawab TEXT,
                jumlah_peserta INTEGER
            )
        ''')

        # Style
        self.style = ttk.Style()
        self.style.configure("TFrame", background="#f0f8ff")
        self.style.configure("TButton", font=("Helvetica", 10), padding=5)
        self.style.configure("TLabel", background="#f0f8ff", font=("Helvetica", 10))
        self.style.configure("Header.TLabel", font=("Helvetica", 16, "bold"))

        self.create_widgets()
        self.tampilkan_data()

    def create_widgets(self):
        # Header
        header_frame = ttk.Frame(self.root)
        header_frame.pack(pady=10)

        ttk.Label(header_frame, text="DATA KUNJUNGAN KERJA INSTANSI", style="Header.TLabel").pack()

        # Form Input
        form_frame = ttk.Frame(self.root)
        form_frame.pack(pady=20, padx=10, fill=X)

        # Nama Instansi
        ttk.Label(form_frame, text="Nama Instansi:").grid(row=0, column=0, padx=5, pady=5, sticky=W)
        self.entry_instansi = ttk.Entry(form_frame, width=40)
        self.entry_instansi.grid(row=0, column=1, padx=5, pady=5)

        # Tanggal
        ttk.Label(form_frame, text="Tanggal Kunjungan:").grid(row=1, column=0, padx=5, pady=5, sticky=W)
        self.entry_tanggal = ttk.Entry(form_frame, width=40)
        self.entry_tanggal.grid(row=1, column=1, padx=5, pady=5)
        self.entry_tanggal.insert(0, datetime.now().strftime("%Y-%m-%d"))

        # Tujuan
        ttk.Label(form_frame, text="Tujuan Kunjungan:").grid(row=2, column=0, padx=5, pady=5, sticky=W)
        self.entry_tujuan = ttk.Entry(form_frame, width=40)
        self.entry_tujuan.grid(row=2, column=1, padx=5, pady=5)

        # Penanggung Jawab
        ttk.Label(form_frame, text="Penanggung Jawab:").grid(row=3, column=0, padx=5, pady=5, sticky=W)
        self.entry_penanggung_jawab = ttk.Entry(form_frame, width=40)
        self.entry_penanggung_jawab.grid(row=3, column=1, padx=5, pady=5)

        # Jumlah Peserta
        ttk.Label(form_frame, text="Jumlah Peserta:").grid(row=4, column=0, padx=5, pady=5, sticky=W)
        self.entry_jumlah_peserta = ttk.Entry(form_frame, width=40)
        self.entry_jumlah_peserta.grid(row=4, column=1, padx=5, pady=5)

        # Button Frame
        button_frame = ttk.Frame(self.root)
        button_frame.pack(pady=10)

        ttk.Button(button_frame, text="Tambah Data", command=self.tambah_data).pack(side=LEFT, padx=5)
        ttk.Button(button_frame, text="Refresh Data", command=self.tampilkan_data).pack(side=LEFT, padx=5)
        ttk.Button(button_frame, text="Hapus Data", command=self.hapus_data).pack(side=LEFT, padx=5)

        # Treeview untuk menampilkan data
        self.tree_frame = ttk.Frame(self.root)
        self.tree_frame.pack(pady=10, padx=10, fill=BOTH, expand=True)

        self.tree = ttk.Treeview(self.tree_frame, columns=("ID", "Instansi", "Tanggal", "Tujuan", "Penanggung Jawab", "Jumlah"), show="headings")

        # Scrollbar
        scrollbar = ttk.Scrollbar(self.tree_frame, orient="vertical", command=self.tree.yview)
        scrollbar.pack(side=RIGHT, fill=Y)
        self.tree.configure(yscrollcommand=scrollbar.set)

        # Kolom Treeview
        self.tree.heading("ID", text="ID")
        self.tree.heading("Instansi", text="Instansi")
        self.tree.heading("Tanggal", text="Tanggal")
        self.tree.heading("Tujuan", text="Tujuan")
        self.tree.heading("Penanggung Jawab", text="Penanggung Jawab")
        self.tree.heading("Jumlah", text="Jumlah Peserta")

        self.tree.column("ID", width=50, anchor=CENTER)
        self.tree.column("Instansi", width=150)
        self.tree.column("Tanggal", width=100)
        self.tree.column("Tujuan", width=200)
        self.tree.column("Penanggung Jawab", width=150)
        self.tree.column("Jumlah", width=100, anchor=CENTER)

        self.tree.pack(fill=BOTH, expand=True)

    def tambah_data(self):
        instansi = self.entry_instansi.get()
        tanggal = self.entry_tanggal.get()
        tujuan = self.entry_tujuan.get()
        penanggung_jawab = self.entry_penanggung_jawab.get()
        jumlah_peserta = self.entry_jumlah_peserta.get()

        if not instansi or not tanggal or not tujuan:
            messagebox.showwarning("Peringatan", "Harap isi semua field yang diperlukan!")
            return

        try:
            self.c.execute('''
                INSERT INTO kunjungan (nama_instansi, tanggal, tujuan, penanggung_jawab, jumlah_peserta)
                VALUES (?, ?, ?, ?, ?)
            ''', (instansi, tanggal, tujuan, penanggung_jawab, jumlah_peserta))
            self.conn.commit()
            messagebox.showinfo("Sukses", "Data kunjungan berhasil ditambahkan!")
            self.clear_form()
            self.tampilkan_data()
        except Exception as e:
            messagebox.showerror("Error", f"Terjadi kesalahan: {str(e)}")

    def tampilkan_data(self):
        for item in self.tree.get_children():
            self.tree.delete(item)

        self.c.execute('SELECT * FROM kunjungan ORDER BY tanggal DESC')
        data = self.c.fetchall()

        for row in data:
            self.tree.insert("", "end", values=row)

    def hapus_data(self):
        selected_item = self.tree.selection()
        if not selected_item:
            messagebox.showwarning("Peringatan", "Pilih data yang akan dihapus!")
            return

        confirm = messagebox.askyesno("Konfirmasi", "Yakin ingin menghapus data ini?")
        if confirm:
            item_id = self.tree.item(selected_item)['values'][0]
            try:
                self.c.execute('DELETE FROM kunjungan WHERE id = ?', (item_id,))
                self.conn.commit()
                messagebox.showinfo("Sukses", "Data berhasil dihapus!")
                self.tampilkan_data()
            except Exception as e:
                messagebox.showerror("Error", f"Terjadi kesalahan: {str(e)}")

    def clear_form(self):
        self.entry_instansi.delete(0, END)
        self.entry_tanggal.delete(0, END)
        self.entry_tanggal.insert(0, datetime.now().strftime("%Y-%m-%d"))
        self.entry_tujuan.delete(0, END)
        self.entry_penanggung_jawab.delete(0, END)
        self.entry_jumlah_peserta.delete(0, END)

    def __del__(self):
        self.conn.close()

if __name__ == "__main__":
    root = Tk()
    app = AplikasiKunjunganKerja(root)
    root.mainloop()
