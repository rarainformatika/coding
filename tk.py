import tkinter as tk
from tkinter import messagebox

def hitung():
    try:
        panjang = float(input_panjang.get())
        lebar = float(input_lebar.get())

        luas = panjang * lebar
        keliling = 2 * (panjang + lebar)

        hasil_luas.config(text=f"Luas: {luas:.2f}")
        hasil_keliling.config(text=f"Keliling: {keliling:.2f}")
    except ValueError:
        messagebox.showerror("Error", "Masukkan angka yang valid")

# Membuat window utama
window = tk.Tk()
window.title("Kalkulator Persegi Panjang")
window.geometry("300x200")

# Label dan Entry untuk panjang
label_panjang = tk.Label(window, text="Panjang:")
label_panjang.pack()
input_panjang = tk.Entry(window)
input_panjang.pack()

# Label dan Entry untuk lebar
label_lebar = tk.Label(window, text="Lebar:")
label_lebar.pack()
input_lebar = tk.Entry(window)
input_lebar.pack()

# Tombol hitung
button_hitung = tk.Button(window, text="Hitung", command=hitung)
button_hitung.pack()

# Label untuk menampilkan hasil
hasil_luas = tk.Label(window, text="Luas: ")
hasil_luas.pack()
hasil_keliling = tk.Label(window, text="Keliling: ")
hasil_keliling.pack()

# Menjalankan aplikasi
window.mainloop()