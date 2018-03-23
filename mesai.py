saat=1
aylikmesai=1
while aylikmesai<=22:
    saat=int(input("haftalik personel çalışma saati giriniz ="))
    mesai=saat-40
    aylikmesai=mesai*4
    toplammaas=50*(40*90+(mesai*9))
    aylik=toplammaas*4
    print("ödenecek maaş = ",aylik)
else:
    print("aylik 22 saatten fazla personele mesai yaptırılamaz.")
