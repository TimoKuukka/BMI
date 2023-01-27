# SOVELLUS PAINOINDEKSIN JA KEHON RASVAPROSENTIN LASKEMISEEN
# ==========================================================

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

# Määritellään funktio aikuisen kehonrasvaprosentin laskemiseen
def aikuisen_rasvaprosentti(bmi, ika, sukupuoli):
    """Laskee aikuisen kehon rasvaprosentin 

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

# Määritellään funktio lapsen kehonrasvaprosentin laskemiseen
def lapsen_rasvaprosentti(bmi, ika, sukupuoli):
    """Laskee lapsen kehon rasvaprosentin

    Args:
        bmi (float): painoindeksi
        ika (float): henkilön ikä
        sukupuoli (float): 1 -> poika, 0 -> tyttö

    Returns:
        float: kehon rasvaprosentti (lapsi)
    """
    
    rasvaprosentti = 1.51 * bmi - 0.70 * ika - 3.6 * sukupuoli + 1.4
    return rasvaprosentti

# Suoritetaan seuraavat rivit vain, jos tämä tiedosto on pääohjelma
# Mahdollistaa funktioiden lataamisen toisiin ohjelmiin
# Kun koodi ladataan toiseen tiedostoon,
#  if __name__ == "__main__": alapuolella olevaa koodia ei suoriteta
if __name__ == "__main__":
    
    # Kysytään käyttäjältä tiedot
    pituus_teksti = input("Kuinka pitkä olet (cm)?: ")
    paino_teksti = input ("Kuinka paljon painat (kg)?: ")
    ika_teksti = input("Kuinka vanha olet?:")
    sukupuoli_teksti = input("Anna sukupuoli. Mies vastaa: 1, nainen vastaa 0: ")

    # Muutetaan vastaukset liukuluvuiksi
    pituus = float(pituus_teksti)
    paino = float(paino_teksti)
    ika = float(ika_teksti)
    sukupuoli = float(sukupuoli_teksti)

    # Lasketaan painoindeksi funktiolla laske_bmi
    oma_bmi = laske_bmi(pituus, paino)

    # Yli 18 vuotiailla käytetään aikusten kaavaa
    if ika >= 18:
        oma_rasvaprosentti = aikuisen_rasvaprosentti(oma_bmi, ika, sukupuoli)

    # Muussa tapauksessa käytetään lapsen kaavaa
    else:
        oma_rasvaprosentti = lapsen_rasvaprosentti(oma_bmi, ika, sukupuoli)
        
    print("Painoindeksisi on", oma_bmi, "ja kehon rasvaprosentti on", oma_rasvaprosentti)
