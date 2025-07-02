#boy,kilo,beden kitle indeksi hesapla,sonuc normal,kilolu,zayıf veya obez,boy bilgisi cm veya metre girilecek.

a=int(input('boy biliginizi giriniz:'))
b=int(input('kilo bilginizi giriniz:'))

bki=b/(a*a)
print('bki:',bki)
if bki<18.50:
    print('zayıf')
elif 18.50<bki<24.99:
    print('saglikli')
elif 25<bki<29.99:
    print('asiri kilolu')

