def laske_bmi(pituus, paino):
    bmi = paino / (pituus*pituus)
    print("Painoindeksisi on")
    print(round(bmi, 2))	

pituus = float(input("Syötä pituutesi: "))
paino = float(input("Syötä painosi: "))

laske_bmi(pituus, paino)
