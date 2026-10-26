import sqlite3
import tkinter as tk
from tkinter import messagebox

# Konfigurasi Jendela Utama Tkinter
root = tk.Tk()
root.title("Aplikasi Prediksi Fakultas Pilihan")
root.geometry("500x550")
root.configure(bg="#f0f4f7")

root.mainloop()

# Inisialisasi Database dan Pembuatan Tabel
def init_db():
  conn = sqlite3.connect("prediksi_fakultas.db")
  cursor = conn.cursor()
  cursor.execute("""
        CREATE TABLE IF NOT EXISTS nilai_siswa (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nama_siswa TEXT NOT NULL,
            biologi REAL,
            fisika REAL,
            inggris REAL,
            prediksi_fakultas TEXT
        )
    """)
  conn.commit()
  conn.close()

# Fungsi untuk memproses prediksi dan menyimpan ke database
def submit_data():
  nama = entry_nama.get().strip()
  bio_str = entry_biologi.get().strip()
  fis_str = entry_fisika.get().strip()
  ing_str = entry_inggris.get().strip()

  # Validasi kolom kosong
  if not nama or not bio_str or not fis_str or not ing_str:
    messagebox.showwarning(
        "Peringatan", "Semua kolom data dan nilai harus diisi!"
    )
    return

  # Validasi input angka
  try:
    biologi = float(bio_str)
    fisika = float(fis_str)
    inggris = float(ing_str)
  except ValueError:
    messagebox.showerror(
        "Error", "Nilai Biologi, Fisika, dan Inggris harus berupa angka!"
    )
    return

  # Logika Penentuan Prediksi Berdasarkan Nilai Tertinggi
  nilai_dict = {"Kedokteran": biologi, "Teknik": fisika, "Bahasa": inggris}

  prediksi = max(nilai_dict, key=nilai_dict.get)

  # Simpan Data ke SQLite
  try:
    conn = sqlite3.connect("prediksi_fakultas.db")
    cursor = conn.cursor()
    cursor.execute(
        """
            INSERT INTO nilai_siswa (nama_siswa, biologi, fisika, inggris, prediksi_fakultas)
            VALUES (?, ?, ?, ?, ?)
        """,
        (nama, biologi, fisika, inggris, prediksi),
    )
    conn.commit()
    conn.close()

    # Tampilkan hasil prediksi ke GUI
    label_hasil.config(
        text=(
            f"Siswa: {nama}\n Hasil Prediksi Fakultas: {prediksi}\n(Data"
            " berhasil disimpan ke SQLite!)"
        )
    )
    messagebox.showinfo("Sukses", "Data berhasil disimpan ke database!")

    # Kosongkan form input setelah submit
    entry_nama.delete(0, tk.END)
    entry_biologi.delete(0, tk.END)
    entry_fisika.delete(0, tk.END)
    entry_inggris.delete(0, tk.END)

  except Exception as e:
    messagebox.showerror("Error Database", f"Terjadi kesalahan: {e}")


# Panggil inisialisasi database saat program dijalankan
init_db()

# Konfigurasi Jendela Utama Tkinter
root = tk.Tk()
root.title("Aplikasi Prediksi Fakultas Pilihan")
root.geometry("500x550")
root.configure(bg="#f0f4f7")

# Judul Aplikasi
judul = tk.Label(
    root,
    text="Aplikasi Prediksi Fakultas",
    font=("Helvetica", 18, "bold"),
    bg="#f0f4f7",
    fg="#333",
)
judul.pack(pady=20)

# Frame untuk Input Form
input_frame = tk.Frame(root, bg="#f0f4f7")
input_frame.pack(pady=10)

