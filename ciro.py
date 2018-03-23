sM=500
bS=20
ciro=5000
i=0
while(ciro<=500000):
    ciro=ciro+(sM*bS)
    sM=sM+200
    bS=bS+10
    i=i+1
print(i,". ayda ciro 500.000 den fazla olmustur...",ciro)
