# FITNESS-MODULIN TESTIT
#-----------------------

# KIRJASTOJEN JA MODULIEN LATAUKSET
import fitness

def test_laske_bmi():
    assert fitness.laske_bmi(170, 64.7) == 22.4
    assert fitness.laske_bmi(170, 40) == 13.8
    assert fitness.laske_bmi(170, 100) == 34.6

def test_aikuisen_rasvaprosentti():
    # Testejä aikuisia miehiä
    assert fitness.aikuisen_rasvaprosentti(22.4, 20, 1) == 15.3 
    assert fitness.aikuisen_rasvaprosentti(13.8, 40, 1) == 9.6
    assert fitness.aikuisen_rasvaprosentti(34.6, 70, 1) == 41.4

    # Testejä aikuisia naisia
    assert fitness.aikuisen_rasvaprosentti(20.8, 20, 0) == 24.2
    assert fitness.aikuisen_rasvaprosentti(13.8, 40, 0) == 20.4
    assert fitness.aikuisen_rasvaprosentti(34.6, 50, 0) == 47.6

def test_lapsen_rasvaprosentti():
    # Testejä lapsia
    assert fitness.lapsen_rasvaprosentti() == 