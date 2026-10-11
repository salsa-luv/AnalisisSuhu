def baca_data(nama_file):
    data = []

    try:
        with open(nama_file, "r") as file:
            for baris in file:
                try:
                    hari, suhu = baris.strip().split(";")
                    suhu = int(suhu)

                    data.append({
                        "hari": hari,
                        "suhu": suhu
                    })

                except ValueError:
                    print(f"Data tidak valid, baris dilewati: {baris.strip()}"
                          )

    except FileNotFoundError:
        print(f"File {nama_file} belum ditemukan."
              )

    return data

def hitung_rata_rata(*suhu):
    if not suhu:
        return 0

    return sum(suhu) / len(suhu)

def analisis_suhu(data):
    if not data:
        return None

    daftar_suhu = [item["suhu"] for item in data]

    rata_rata = hitung_rata_rata(*daftar_suhu)

    suhu_tertinggi = max(data, key=lambda item: item["suhu"])
    suhu_terendah = min(data, key=lambda item: item["suhu"])

    jumlah_panas = 0

    for item in data:
        if item["suhu"] >= 32:
            item["kategori"] = "Panas"
            jumlah_panas += 1
        else:
            item["kategori"] = "Normal"

    return rata_rata, suhu_tertinggi, suhu_terendah, jumlah_panas

def tulis_laporan(
    data,
    rata_rata,
    suhu_tertinggi,
    suhu_terendah,
    jumlah_panas,
    nama_file="laporan_suhu.txt"
):
    with open(nama_file, "w") as file:
        file.write("===== LAPORAN SUHU HARIAN =====\n")
        file.write(f"Rata-rata suhu: {rata_rata:.2f} derajat C\n")
        file.write(
            f"Suhu tertinggi: {suhu_tertinggi['suhu']} derajat C "
            f"({suhu_tertinggi['hari']})\n"
        )
        file.write(
            f"Suhu terendah: {suhu_terendah['suhu']} derajat C "
            f"({suhu_terendah['hari']})\n"
        )
        file.write(f"Jumlah hari Panas: {jumlah_panas}\n\n")

        file.write("Data suhu harian:\n")

        for item in data:
            file.write(
                f"{item['hari']}: {item['suhu']} derajat C - "
                f"{item['kategori']}\n"
            )

if __name__ == "__main__":
    data = baca_data("suhu.txt")

    if data:
        hasil = analisis_suhu(data)

        if hasil is not None:
            rata_rata, tertinggi, terendah, jumlah_panas = hasil

            tulis_laporan(
                data,
                rata_rata=rata_rata,
                suhu_tertinggi=tertinggi,
                suhu_terendah=terendah,
                jumlah_panas=jumlah_panas
            )

            print("Laporan berhasil dibuat.\n")

            with open("laporan_suhu.txt", "r") as file:
                for baris in file:
                    print(baris, end="")
    else:
        print("Tidak ada data suhu yang dapat dianalisis.")

