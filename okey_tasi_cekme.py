#okey taşı uygulaması.

import random #random taş gelmesi için random kütüphanesi tanımlıyoruz.buradaki fonksiyonuu kullanıcaz

taslar=[[renk+str(sayi)] for renk in ["t","k","m","s"]for sayi in range(1,14)]*2
#renge göre sayı cekicez ki renklerin yanında sayılar yazsın. 1,14 arası olmasının sebebi 13 taş olması ve *2 de her taştan 2 tane bulunduğu icin 2 kere döngü dönecek.

def tasCek():
    while taslar:
        yield taslar.pop(random.randint(0,len(taslar)-1))
        #yield ile döngü döndükce bir sonraki değer yazılacak.pop ise yazılan elemanı indexten siler.randint verdiğimiz aralıkta rastgele sayılar üretir.
        #0 ile her taş çekiminde taşların sayısının 1 eksiği aralığında randint sayı üretir.

for tas in tasCek():
    print(tas,end=' ')
    #her yazılan sayi ve renk ikilisinden sonra alt satıra geçmeden aralarında bir boşluk kalsın diye kullanılır.