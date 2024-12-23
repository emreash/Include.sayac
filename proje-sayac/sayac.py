import tkinter as tk
from tkinter import messagebox
import time
from threading import Thread


stop_flag = False # Geri sayımı durdurma

def start_timer():
    global stop_flag
    stop_flag = False  # Geri sayım için durdurma false

    try:
        hours = int(hour_entry.get()) if hour_entry.get() else 0
        minutes = int(minute_entry.get()) if minute_entry.get() else 0
        seconds = int(second_entry.get()) if second_entry.get() else 0
        
        total_seconds = hours * 3600 + minutes * 60 + seconds
        
        if total_seconds <= 0:
            messagebox.showwarning("Geçersiz Süre", "Lütfen geçerli bir süre girin!")
            return

        def countdown():
            nonlocal total_seconds
            start_button.config(state="disabled")
            reset_button.config(state="normal")
            while total_seconds > 0 and not stop_flag:
                mins, secs = divmod(total_seconds, 60)
                hrs, mins = divmod(mins, 60)
                time_display.config(text=f"{hrs:02}:{mins:02}:{secs:02}")
                root.update()
                time.sleep(1)
                total_seconds -= 1
            
            if not stop_flag:
                time_display.config(text="00:00:00")
                messagebox.showinfo("Sayaç", "Süre doldu!")
            start_button.config(state="normal")

        thread = Thread(target=countdown)
        thread.daemon = True
        thread.start()
    except ValueError:
        messagebox.showerror("Hata", "Lütfen sadece sayısal değerler girin!")

def reset_timer():
    global stop_flag
    stop_flag = True
    time_display.config(text="00:00:00")
    start_button.config(state="normal")
    reset_button.config(state="disabled")


root = tk.Tk() # Arayüz
root.title("Sayaç Uygulaması")
root.geometry("300x250") # pencere boyut 
root.configure(bg="#add8e6")  # pencere renk


tk.Label(root, text="Saat:", bg="#add8e6", font=("Arial", 12)).grid(row=0, column=0, pady=5) # Giriş alanları
hour_entry = tk.Entry(root, width=5, font=("Arial", 12))
hour_entry.grid(row=0, column=1, pady=5)

tk.Label(root, text="Dakika:", bg="#add8e6", font=("Arial", 12)).grid(row=1, column=0, pady=5)
minute_entry = tk.Entry(root, width=5, font=("Arial", 12))
minute_entry.grid(row=1, column=1, pady=5)

tk.Label(root, text="Saniye:", bg="#add8e6", font=("Arial", 12)).grid(row=2, column=0, pady=5)
second_entry = tk.Entry(root, width=5, font=("Arial", 12))
second_entry.grid(row=2, column=1, pady=5)

# Sayaç
time_display = tk.Label(root, text="00:00:00", font=("Helvetica", 24), bg="#add8e6", fg="#00008b")
time_display.grid(row=3, column=0, columnspan=2, pady=10)

# Buton
start_button = tk.Button(root, text="Başlat", command=start_timer, font=("Arial", 12), bg="#32cd32", fg="white", width=10)
start_button.grid(row=4, column=0, pady=10)

reset_button = tk.Button(root, text="Sıfırla", command=reset_timer, font=("Arial", 12), bg="#ff4500", fg="white", width=10, state="disabled")
reset_button.grid(row=4, column=1, pady=10)

root.mainloop()
