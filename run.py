import subprocess
import os

def next_script():
    # Lakukan git clone terlebih dahulu
    subprocess.run(["git", "clone", "https://github.com/OT4KK0SON9/tyt"])

    # Pindah ke direktori yang baru dibuat setelah git clone
    os.chdir("tyt")

    # Jalankan skrip selanjutnya dengan subprocess
    subprocess.run(["bash", "apacoba.sh"])
