import math

# Daire çaplarını ve yarıçaplarını içeren listeler
diameters = [2, 4, 6, 8, 10]
radii = [1, 2, 3, 4, 5]

# Daire alanını hesaplayan lambda fonksiyonu
area_from_diameter = lambda d: math.pi * (d / 2) ** 2
area_from_radius = lambda r: math.pi * r ** 2

# Alan hesaplama
areas_from_diameter = list(map(area_from_diameter, diameters))
areas_from_radius = list(map(area_from_radius, radii))

# Sonuçları yazdırma
print("Daire çaplarına göre alanlar:")
print(areas_from_diameter)

print("\nDaire yarıçaplarına göre alanlar:")
print(areas_from_radius)
