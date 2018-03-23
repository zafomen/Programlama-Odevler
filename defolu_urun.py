gU=200
dU=0
tDU=0
i=0
while(dU<=gU*0.20):
    dU=int(input("Defolu Ürün sayisini giriniz"))
    tDU=tDU+dU   
    i=i+1
    if(dU>gU*0.20):
        print("Defolu ürün sayısı limitine ulaşıldı")
        break
    print(i,"Günlük defolu ürün sayisi",tDU)
