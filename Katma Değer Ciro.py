def katmaDeğer():
    print("Katma Değer Cirosu Bulan Programa Hoşgeldiniz")
    x=int(input("Toplam Satış Miktarınıı Giriniz"))
    y=int(input("Hammadde Maliyetini Giriniz"))
    z=int(input("Bakım Onarım Giderlerini Giriniz"))
    t=int(input("Sevkiyat Değerlerini Giriniz"))
    w=int(input("Satın Alınan Hizmet Giderlerini Giriniz"))
    kdc=x-(y+z+t+w)
    if(kdc>1000):
        print("Katma Değer Cirosu Yüksek",kdc)
    elif(500<kdc<999):
        print("Katma Değer Cirosu Normal" , kdc)
    else:
        print("Katma Değer Cirosu Düşük" , kdc)








    

      
