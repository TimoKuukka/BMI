# SOVELLUS PAINOINDEKSIN JA KEHON RASVAPROSENTIN LASKEMISEEN
# ==========================================================

# Muuttujat

# Kysytään käyttäjältä tiedot
pituus_teksti = input("Kuinka pitkä olet (cm)?: ")
paino_teksti = input ("Kuinka paljon painat (kg)?: ")
ika_teksti = input("Kuinka vanha olet?:")
sukupuoli_teksti = input("Anna sukupuoli. Mies vastaa: 1, nainen vastaa: 0: ")

# Muutetaan vastaukset liukuluvuiksi
pituus = float(pituus_teksti)
paino = float(paino_teksti)
ika = float(ika_teksti)
sukupuoli = float(sukupuoli_teksti)


# Määritellään funktio painoindeksin laskentaan
def laske_bmi(pituus, paino):
    """Laskee painoindeksin(BMI)

    Args:
        paino (float): paino (kg)
        pituus (float): pituus (cm)

    Returns:
        float: painoindeksi desimaalin tarkkuudella
    """
    pituus = pituus / 100 # Muutetaan pituus metreiksi
    bmi = paino / pituus**2
    bmi = round(bmi, 1)
    return bmi

bmi = laske_bmi(pituus, paino)

def aikuisen_rasvaprosentti(bmi, ika, sukupuoli):
    """summa

    Args:
        bmi (float): painoindeksi
        ika (float): henkilön ikä
        sukupuoli (float): 1 -> mies, 0 -> nainen

    Returns:
        float: kehon rasvaprosentti (aikuinen)
    """

    rasvaprosentti = 1.20 * bmi + 0.23 * ika - 10.8 * sukupuoli - 5.4
    rasvaprosentti = round(rasvaprosentti)
    return rasvaprosentti

oma_bmi = laske_bmi(pituus, paino)
oma_rasvaprosentti = aikuisen_rasvaprosentti(oma_bmi, ika, sukupuoli)

print("Painoindeksisi on", oma_bmi, "ja kehon rasvaprosenti on", oma_rasvaprosentti)
