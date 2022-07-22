
#Primera forma
series = ('Lucifer','Blacklist','Los 100','La casa de papel')


for i in range(0,len(series)):
    print(series[i])

#Segunda forma

for i in range(0,len(series)):
    print(i,series[i])

#Tercera forma
# 
for i in series:
    print(i)  

#Cuarta forma
for i,dato in enumerate(series):
    print(i,dato)