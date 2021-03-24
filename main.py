import time
import datetime
now = datetime.datetime.now()
ini = now.strftime("%A")
aloha = now.strftime("%Y-%m-%d")
if ini == "Sunday":
    hari = "Senin"
elif ini == "Tuesday":
    hari = "Selasa"
if ini == "Wednesday":
    hari = "Rabu"
elif ini == "Thursday":
    hari = "Kamis"
elif ini == "Friday":
    hari = "Jumat"
print(aloha + " " + hari)


def tanya1(tanya):
    if tanya == "senin":
        print(" Jadwal hari senin: \n | 7: 30 - 09: 00  PKN |\n | 09: 30 - 10: 00 IPS | ")
    elif tanya == "selasa":
        print(" Jadwal hari selasa: \n | 7: 30 - 09: 00  Indonesia |\n | 09: 30 - 10: 00 Inggris | ")
    elif tanya == "rabu":
        print(" Jadwal hari rabu: \n | 7: 00 - 08: 30  IPA |\n | 09: 00 - 10: 30 MTK |\n | 10.30 - 12.00 PJOK | ")
    elif tanya == "kamis":
        print(" Jadwal hari kamis: \n | 7: 30 - 09: 00  Sunda |\n | 09: 30 - 11: 00 TIK | ")
    elif tanya == "jumat":
        print(
            " Jadwal hari jumat: \n | 7: 30 - 09: 00  PAI |\n | 09: 30 - 11: 00 Senbud | ")
    elif tanya == "pkn":
        print("|Senin 7:30 - 09:00 PKN |")
    elif tanya == "ips":
        print("|Senin 09:30 - 10:00 IPS |")
    elif tanya == "indo":
        print("|Selasa 7: 30 - 09: 00  Indonesia |")
    elif tanya == "inggris":
        print("|Selasa 09: 30 - 10: 00 Inggris |")
    elif tanya == "ipa":
        print("|Rabu 7: 00 - 08: 30  IPA |")
    elif tanya == "mtk":
        print("|Rabu 09: 00 - 10: 30 MTK |")
    elif tanya == "pjok":
        print("|Rabu 10.30 - 12.00 PJOK |")
    elif tanya == "sunda":
        print("|Kamis 7: 30 - 09: 00  Sunda |")
    elif tanya == "tik":
        print("|Kamis 09: 30 - 11: 00 TIK |")
    elif tanya == "PAI":
        print("|Jumat 7: 30 - 09: 00  PAI |")
    elif tanya == "senbud":
        print("|Jumat 09: 30 - 11: 00 Senbud |")
    elif tanya == "bk":
        print("|Rabu 11: 00 - 12: 00  BK |")
    elif tanya == "exit":
        exit()
    else:
        print(f'Tidak ada perintah {tanya}')


print('Jadwal Pelajaran Kelas 9 SMP 34 Bandung')
while True:
    tanya = input("Hari / pelajaran: ")
    tanya1(tanya)
