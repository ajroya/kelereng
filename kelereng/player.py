"""
Modul Player
Berisi kelas dan fungsi terkait pemain pada permainan kelereng
"""

class Player:
    def __init__(self, nama, jumlah_kelereng):
        """
        Membuat pemain dengan nama dan kelereng awal
        """
        self.nama = nama
        self.kelereng = jumlah_kelereng

    def taruhan(self):
        """
        Meminta pemain memasukkan jumlah kelereng yang ingin dipertaruhkan
        """
        while True:
            try:
                jumlah = int(input(f"{self.nama}, berapa kelereng yang ingin kamu pertaruhkan? (1-{self.kelereng}): "))
                if 1 <= jumlah <= self.kelereng:
                    return jumlah
                else:
                    print("Jumlah taruhan tidak valid!")
            except ValueError:
                print("Masukkan angka yang valid!")

    def tebakan(self):
        """
        Meminta pemain menebak (ganjil/genap)
        """
        while True:
            tebakan = input(f"{self.nama}, tebak kelereng lawan GANJIL atau GENAP? (G/J): ").strip().upper()
            if tebakan in ["G", "J"]:
                return tebakan
            else:
                print("Input tidak valid! Masukkan 'G' untuk Ganjil atau 'J' untuk Genap.")

    def __str__(self):
        return f"{self.nama}: {self.kelereng} kelereng"