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


