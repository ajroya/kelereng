"""
Program Utama Permainan Kelereng (Modular)
"""

from player import Player
import kelereng

def main():
    print("=== PERMAINAN KELERENG SEDERHANA ===")
    nama1 = input("Masukkan nama Pemain 1: ")
    nama2 = input("Masukkan nama Pemain 2: ")
    kelereng_awal = 10
    p1 = Player(nama1, kelereng_awal)
    p2 = Player(nama2, kelereng_awal)

    try:
        max_ronde = int(input("Bermain berapa ronde maksimal? (0 untuk tak terbatas): "))
    except ValueError:
        max_ronde = 0

    ronde = 1
    while True:
        print(f"\n=== Ronde {ronde} ===")
        # P1 bertaruh, P2 menebak
        kelereng.mainkan_ronde(p1, p2)
        kelereng.status_pemain(p1, p2)
        if kelereng.akhir_permainan(p1, p2, max_ronde if max_ronde > 0 else None, ronde):
            break

        # Tukar giliran: P2 bertaruh, P1 menebak
        ronde += 1
        print(f"\n=== Ronde {ronde} ===")
        kelereng.mainkan_ronde(p2, p1)
        kelereng.status_pemain(p1, p2)
        if kelereng.akhir_permainan(p1, p2, max_ronde if max_ronde > 0 else None, ronde):
            break

        ronde += 1

if __name__ == "__main__":
    main()