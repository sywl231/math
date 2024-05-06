import pyautogui
import time

# Buka Microsoft Word
pyautogui.hotkey('winleft')
pyautogui.write('word')
pyautogui.press('enter')

# Tunggu Word terbuka
time.sleep(5)  # Sesuaikan jika perlu

# Tambahkan judul
pyautogui.write("Daftar Isi\n")

# Pindahkan ke baris berikutnya
pyautogui.press('enter')

# Tambahkan nomor dan judul
pyautogui.write("1. Judul Bab 1\n")

# Pindahkan ke baris berikutnya
pyautogui.press('enter')

# Tambahkan nomor dan judul
pyautogui.write("2. Judul Bab 2\n")

# Pindahkan ke baris berikutnya
pyautogui.press('enter')

# Tambahkan nomor dan judul
pyautogui.write("3. Judul Bab 3\n")

# Simpan dokumen
pyautogui.hotkey('ctrl', 's')
time.sleep(1)  # Tunggu dialog menyimpan muncul
pyautogui.write('document_with_toc.docx')
pyautogui.press('enter')
