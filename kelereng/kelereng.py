"""
Modul Logika Permainan Kelereng
"""

def cek_ganjil_genap(jumlah):
    """
    Mengembalikan 'G' jika ganjil, 'J' jika genap
    """
    return "G" if jumlah % 2 else "J"

def mainkan_ronde(pemain1, pemain2):
    """
    Melakukan satu ronde permainan antara dua pemain
    """
    print(f"\nGiliran: {pemain1.nama} bertaruh kelereng, {pemain2.nama} menebak.")
    taruhan = pemain1.taruhan()
    tebakan = pemain2.tebakan()
    hasil = cek_ganjil_genap(taruhan)

    print(f"{pemain1.nama} mempertaruhkan {taruhan} kelereng. Jumlah ini {'GANJIL' if hasil == 'G' else 'GENAP'}.")

    if tebakan == hasil:
        print(f"Tebakan {pemain2.nama} BENAR! {pemain2.nama} mendapatkan {taruhan} kelereng dari {pemain1.nama}.")
        pemain2.kelereng += taruhan
        pemain1.kelereng -= taruhan
    else:
        print(f"Tebakan {pemain2.nama} SALAH! {pemain1.nama} tetap menyimpan kelereng.")

def status_pemain(p1, p2):
    """
    Menampilkan status kelereng kedua pemain
    """
    print(f"\nStatus Kelereng: {p1} | {p2}")

def akhir_permainan(p1, p2, max_ronde=None, ronde_ke=None):
    """
    Mengecek apakah permainan harus diakhiri. Return True jika selesai.
    """
    if p1.kelereng == 0:
        print(f"\n{p1.nama} kehabisan kelereng! {p2.nama} menang!")
        return True
    elif p2.kelereng == 0:
        print(f"\n{p2.nama} kehabisan kelereng! {p1.nama} menang!")
        return True
    elif max_ronde is not None and ronde_ke is not None and ronde_ke >= max_ronde:
        if p1.kelereng > p2.kelereng:
            menang = p1
        elif p1.kelereng < p2.kelereng:
            menang = p2
        else:
            print("\nPermainan berakhir SERI!")
            return True
        print(f"\nPermainan selesai! Pemenang: {menang.nama} ({menang.kelereng} kelereng)")
        return True
    return False