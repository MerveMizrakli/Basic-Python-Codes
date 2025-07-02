#boy,kilo,beden kitle indeksi hesapla,sonuc normal,kilolu,zayıf veya aşırı kilolu,boy bilgisi cm veya metre girilecek.

a=int(input('boy biliginizi giriniz:'))  #kullanıcıdan string olarak alınan boy bilgisi integer yapılır.
b=int(input('kilo bilginizi giriniz:'))

bki=b/(a*a)  #beden kitle endeksi hesaplama formulü
print('bki:',bki)
if bki<18.50:
    print('zayıf')
elif 18.50<bki<24.99:
    print('saglikli')
elif 25<bki<29.99:
    print('asiri kilolu')

#boy ölçüsünün metre cinsinden girilmesi gerekmektedir.
