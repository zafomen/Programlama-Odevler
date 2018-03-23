def mobilya():
    kS=50
    yS=50
    dS=50
    dBS=kS+yS+dS
    print("Bu dönem 25 koltuk , 20 yatak ve 10 dolap satılmıştır ve 10 koltuk,15 yatak,5 dolap alınmıştır")
    kS1=kS-25+10
    yS1=yS-20+15
    dS1=dS-10+5
    dSS=kS1+yS1+dS1
    print("Sene başındaki stok sayisi",dBS)
    print("Kalan stok sayisi = ",dSS)
    ortS=(dBS+dSS)/2
    print("Ortalama Stok = ",ortS)
