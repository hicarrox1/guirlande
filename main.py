import microbit as mb
import neopixel
from random import randint

text = {"a": [["010","101","101"]],"t": [["111","010","010"]],"p": [["111","110","100"]],"u": [["101","101","111"]],"e": [["111","100","111"]],
"o": [["111","101","111"]],"l": [["001","001","111"]],"2": [["011","010","110"]]," ": [["000","000","000"]],"/": [["100","010","001"]]}



def affiche_liste(liste_led: list[neopixel], liste_patern: list, time: int):

    liste_led = liste_led
    liste_patern = liste_patern

    decal = 0

    while True:

        n = decal
        for i in range(30):

            n+= 1
            
            if n >= len(liste_patern[0]):
                n = 0
            
            for j in range(len(liste_led)):
                liste_led[j][i] = liste_patern[j][n]
                
        for np in liste_led:
            np.show()

        decal += 1

        if decal >= len(liste_patern[0]):
            decal = 0

        mb.sleep(time)


#project 
def detect_luminosity():
    
    np = neopixel.NeoPixel(mb.pin0, 30)

    while True:
            signal = mb.pin1.read_analog()
            percent(signal/600, np)
            mb.sleep(500)

def test_luminosity_stroboscope():

    np = neopixel.NeoPixel(mb.pin0, 30)

    while True:
            signal = mb.pin1.read_analog()
            if signal < 100:
                stroboscope(np)
            else:
                allume_all_led((0,0,200),np)
            mb.sleep(500)
            

def test_luminosity():

    np = neopixel.NeoPixel(mb.pin0, 30)

    while True:
        signal = mb.pin1.read_analog()
        if signal < 100:
            allume_all_led((255,0,0),np)
        else:
            allume_all_led((0,0,200),np)
        mb.sleep(500)
        
        #mb.pin2.write_digital(1)

def guirlande_francaise():

    np = neopixel.NeoPixel(mb.pin0, 30)

    liste = [(0,0,200),(60,60,60),(200,0,0)]

    affiche_liste([np],[liste,],150)

def afiche_text(texte:str,liste_bande: list):

    matrice = []
    
    for i in range(3):
        bande = "0000"

        for i_l in texte:
            #print(text[i_l])
            bande += text[i_l][0][i]
            bande += "0"
        bande += "0000"

        matrice.append([bande])

        print(matrice)

    test = []


    for li in matrice:

            all_patern_led = []

            for ligne in li:

                patern_led = []
                
                for el in ligne:

                    if el == "0":
                        patern_led.append((0,0,0))
                    else:
                        patern_led.append((60,60,60))

                all_patern_led.append(patern_led)

                test.extend(all_patern_led)

                all_patern_led = []
            
                patern_led = []

    affiche_liste(liste_bande,test,400)
    
    
np1= neopixel.NeoPixel(mb.pin0, 30)
np2 = neopixel.NeoPixel(mb.pin1, 30)
np3 = neopixel.NeoPixel(mb.pin2, 30)
liste_bande = [np1,np2,np3]

afiche_text("o2/o2",liste_bande)


