# kullanıcıdan vize ve final notları alacak
vizeNotu = input()
finalNotu = input()
floatVize = float(vizeNotu)
floatFinal = float(finalNotu)

vizeYüzde = floatVize * 0.4
finalYüzde = floatFinal * 0.6

print(f"vize yüzdesi: {vizeYüzde}")
print(f"final yüzdesi: {finalYüzde}")


notOrtalaması = (vizeYüzde + finalYüzde)
intNot = int(notOrtalaması)

print(f"Not ortalamanız : {intNot}")
if intNot < 49:
    print("FF")
elif intNot >= 50 and intNot < 60:
    print("DD")
elif intNot >= 60 and intNot < 70:
    print("CC")
elif intNot >= 70 and intNot < 80:
    print("BB")
elif intNot >= 80 and intNot < 100:
    print("AA")
else:
    print("Yanlış not girdiniz!")