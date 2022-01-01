import random
cikansayi = []
rakamlar = [1,2,3,4,5,6]
random.shuffle(rakamlar)
for sayi in range(0,1):
    zar = random.choice(rakamlar)
    cikansayi.append(zar)
print(cikansayi)