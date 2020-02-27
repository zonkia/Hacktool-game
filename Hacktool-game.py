print("Witaj w narzędziu HACKTOOL v.1.0 - Złam klucz do tajnego szyfru tajemniczego wroga i zapobiegnij intergalaktycznej wojnie! Podaj dowolną CALKOWITĄ LICZBĘ, a oprogramowanie do łamania szyfrów wykryje, jak blisko shakowania klucza jesteś!")
print()
print("Masz tylko 20 szans, zanim wróg użyje tajnej broni i wysadzi w kosmos cały kosmos!")
print()
print("UWAGA WAŻNE:")
print("Im więcej plusów pokaże HACKTOOL, tym bliżej złamania kodu, im więcej minusów tym dalej - np. jeśli będziesz DOŚC BLISKO shakowania to zobaczysz \"0++\", a będąc BARDZO DALEKO zobaczysz \"------0\"")
print("Pierwsza informacja jaką zdobył Szeregowy Bomba brzmi: \"Mamy do czynienia z przeciwnikiem z antywymiaru - klucz szyfrowania MOZE BYC liczbą ujemną!\"")

import math
import time
import random
import os
import time
from datetime import datetime
from threading import Timer

wins = 0
loses = 0
bilans = 0
zapytanie = 1
iloscZagran = 0
poprzedniPrzegranyKod = "brak"
poprzedniZlamanyKod = "brak"
listaZlamanychKodow = []
listaPrzegranychKodow = []

def exitfunc():
    os._exit(0)

def rezygnacja():
    print("W porządku może uda się następnym razem! Jak zmienisz zdanie to znajdziesz mnie w Kantynie \"Laser\", w której będę zapijał (porządnie) naszą porażkę")
    global zapytanie
    zapytanie = 0
    Timer(5, exitfunc).start()
    while True:
        time.sleep(1)

def zagrania5():
    print("Kapitan Wieśniak przyniósł raport, który może Ciebie przybliżyć do rozwiązania - chcesz go poznać? TAK/NIE")
    odp = input().upper()
    if (odp == "TAK"):
        print("Liczba jest",znak)
    else:
        print("No dobra cwaniaku próbuj dalej. Kosmos i okolice trzymają kciuki")

def zagrania10():
    print("Sierżant Gigusław zameldował o kolejnych postępach wywiadu! Chcesz się dowiedzieć co zameldował? TAK/NIE")
    odp = input().upper()
    if (odp == "TAK"):
        zakresI = random.randrange(1, poziom * 10000)
        zakresII = poziom * 10000 - zakresI
        if x > poziom * 40000 or x < poziom * (-40000):
            if x > 0:
                print("Tajny kod mieści się w zakresie od :", poziom * 40000," do + ", poziom * 50000)
            else:
                print("Tajny kod mieści się w zakresie od :", poziom * (-40000)," do + ", poziom * (-50000))
        else:
            print("Tajny kod mieści się w zakresie od ",str(x-zakresI)," do ",str(x+zakresII))
    else:
        print("Widzę, że nie boisz się ryzyka! Próbuj dalej, ale pamiętaj o jednym: Cały kosmos jest zagrożony")

def zagrania15():
    print("Generał Hausztajn rzuca jakimiś papierami i wydziera się, że to Twoja ostatnia szansa! Chcesz poznać jakie informacje zdobył? TAK/NIE")
    odp = input().upper()
    if (odp == "TAK"):
        zakresA = random.randrange(1, poziom * 1000)
        zakresB = poziom * 1000 - zakresA
        if x > poziom * 49000 or x < poziom * (-49000):
            if x > 0:
                print("Tajny kod mieści się w zakresie od :", poziom * 49000," do + ", poziom * 50000)
            else:
                print("Tajny kod mieści się w zakresie od :", poziom * (-49000)," do + ", poziom * (-50000))
        else:
                print("Tajny kod mieści się w zakresie od ",str(x-zakresA)," do ",str(x+zakresB))
    else:
        print("Ty zwariowany wariacie! Wygląda na to, że już po kosmosie...")

def zagrania19():
    print("Doktor Queen wbiega w ostatniej chwili i krzyczy: \"KAPRALU! UDAŁO MI SIĘ ZDOBYĆ PIĘCIOLICZBOWY ZAKRES MOŻLIWYCH KLUCZY!\" Czy chcesz poznać ten zakres? TAK/NIE")
    odp = input().upper()
    if (odp == "TAK"):
        zakres1 = random.randrange(1,5)
        zakres2 = 5 - zakres1
        if x > poziom * 49995 or x < poziom * (-49995):
            if x > 0:
                print("Tajny kod mieści się w zakresie od :", poziom * 49995," do + ", poziom * 50000)
            else:
                print("Tajny kod mieści się w zakresie od :", poziom * (-49995)," do + ", poziom * (-50000))
        else:
                print("Tajny kod mieści się w zakresie od ",str(x-zakres1)," do ",str(x+zakres2),"- szansa 1/5. Prawie jak rosyjska ruletka! Powodzenia w imieniu całego kosmosu!")
    else:
        print("Myślę, że mogę śmiało stwierdzić, że kosmos jest już skonczony... Zegnaj kosmosie... i okolico!")

def zagrania20(loses):
    print("BUUUUUUUUUUUM!!!!!!!!!!! Nie żyjesz a kosmos legnął w gruzach. THE END. Prawidłowy klucz szyfrowania to :",x)
    print()
    loses += 1
    bilans = wins - loses   
    print("Ilość zwycięstw: ",wins," | Ilość porażek: ",loses," | BILANS: ",bilans)
    print("Doktor Queen właśnie mnie poinformowała, że każdorazowa podróż w czasie zmienia klucz szyfrowania. Kapralu, czy chcesz cofnąć się w czasie i spróbować uratować kosmos jeszcze raz? TAK/NIE")

def poziomyFunkcja():
    sprPoziomu = 1
    while sprPoziomu > 0:
        print()
        poziom = input("Wpisz poziom trudności: 1 - normalny, 2 - trudny, 3 - koszmarnie trudny: ")
        try:
            poziom = int(poziom)
            if (poziom == 1):
                poziomName = "normalny"
                print("Wybrano",poziomName,"poziom trudności. Ocalenie kosmosu na tym poziomie nadal jest wyzwaniem!")
                sprPoziomu -= 1
                return poziom
            elif (poziom == 2):
                poziomName = "trudny"
                print("Wybrano",poziomName,"poziom trudności. Ocalenie kosmosu na tym poziomie może przysporzyć bólu głowy!")
                sprPoziomu -= 1
                return poziom
            elif (poziom == 3):
                poziomName = "koszmarnie trudny"
                print("Wybrano",poziomName,"poziom trudności. Ocalenie kosmosu na tym poziomie jest prawie niemożliwe!")
                sprPoziomu -= 1
                return poziom
            else:
                print("Poziom trudności kosmosu może być tylko cyframi: \"1\", \"2\" lub \"3\"")
                continue
        except ValueError:
            print("Poziom trudności kosmosu może być tylko cyframi: \"1\", \"2\" lub \"3\"")
            continue

def xFunkcja():
    iteracjeZnak = 1
    while iteracjeZnak > 0:
        x = random.randrange(poziom * (-50000), poziom * 50000)
        if x != 0:
            iteracjeZnak -= 1
            return x

def znakFunkcja():
    if x > 0:
        znak = "dodatnia"
        return znak
    else:
        znak = "ujemna"
        return znak

def winsFunkcja(wins, loses):
    bilans = wins - loses
    print("Ilość zwycięstw: ",wins," | Ilość porażek: ",loses," | BILANS: ",bilans)

poziom = poziomyFunkcja()
x = xFunkcja()
znak = znakFunkcja()

"""
Main loop
"""

while zapytanie > 0:
    listaZlamanychKodow.append(poprzedniZlamanyKod)
    listaPrzegranychKodow.append(poprzedniPrzegranyKod)
    if (poprzedniPrzegranyKod == "brak") and (poprzedniZlamanyKod == "brak"):
        pass
    else:
        try:
            while "brak" in listaZlamanychKodow:
                listaZlamanychKodow.remove("brak")
        except:
            pass
        try:
            while "brak" in listaPrzegranychKodow:
                listaPrzegranychKodow.remove("brak")
        except:
            pass
        print("Dotychczas złamałane kody: ",listaZlamanychKodow," Dotychczas NIE złamane kody: ",listaPrzegranychKodow)
    if wins == 5:
        print("Kapralu Kox! Niesamowity wynik! Tak dalej, a otrzymacie najwyższe odznaczenie w kosmosie oraz dostąpicie niesamowitego zaszczytu z rąk samego Króla Kosmosu we własnej osobie!")
    elif wins == 10:
        print("Kapralu Kox! Wyrazy najwyższego uznania za odwagę i wierną służbę kosmosowi! Otrzymujecie order Pierduti Gilitari oraz UŚCISK DŁONI od samego Króla Kosmosu we własnej osobie! Królowa kosmosu puściła Tobie oczko - Hmmm")
    elif wins == 15:
        print("Przybywasz do pałacu Króla Kosmosu, po odbiór kolejnej nagrody, ale nie widać go w sali tronowej. Wtem pojawia się Królowa Kosmosu - \"Oh Kapralu Kox, jak Kosmos mógłby Ci się odwdzięczyć... Król Kosmosu pewnie dałby Ci kolejny medal, ale ja wolę dać Tobie coś czego nigdy nie zapomnisz.\" Jak powiedziała tak też zrobiła. Królowa obsłużyła Cię na iście królewskim poziomie i przez chwilę nawet się zakochałeś. Podczas wychodzenia z pałacu zauważasz 19-letnią córkę Królowej, która jest ostra jak żyleta i widać, że też lubi ruch. Wasze spojrzenia się spotkały. Postanawiasz podejść... Ale to już historia na zupełnie inną grę :) KONIEC")
        Timer(20, exitfunc).start()
        while True:
            time.sleep(1)
    iloscZagran += 1
    a = input("Twoja " + str(iloscZagran) + " próba: ")

    try:
        if (int(a) > poziom * 50000) or (int(a) < poziom * (-50000)):
            print("Zbyt duża liczba! Kosmici potrafią tylko liczyć od ", poziom * (-50000)," do +", poziom * 50000)
            if iloscZagran == 5:
                zagrania5()
                continue
            elif iloscZagran == 10:
                zagrania10()
                continue
            elif iloscZagran == 15:
                zagrania15()
                continue
            elif iloscZagran == 19:
                zagrania19()
                continue
            elif iloscZagran == 20:
                zagrania20(loses)
                reset = input().upper()
                if reset == "TAK":
                    poziom = poziomyFunkcja()
                    x = xFunkcja()
                    iloscZagran = 0
                    poprzedniPrzegranyKod = x
                    continue
                else:
                    rezygnacja()
            continue

    except ValueError:
        print("Musi być liczba całkowita")
        if iloscZagran == 5:
            zagrania5()
            continue
        elif iloscZagran == 10:
            zagrania10()
            continue
        elif iloscZagran == 15:
            zagrania15()
            continue
        elif iloscZagran == 19:
            zagrania19()
            continue
        elif iloscZagran == 20:
            zagrania20(loses)
            reset = input().upper()
            if reset == "TAK":
                poziom = poziomyFunkcja()
                x = xFunkcja()
                iloscZagran = 0
                poprzedniPrzegranyKod = x
                continue
            else:
                rezygnacja()
        continue

    try:
        a = int(a)
        if (a > x) or (a < x):
            if a * x < 0:
                roznica = math.fabs(a) + math.fabs(x)
                if roznica > poziom * 20000:
                    print("------------0")
                    if iloscZagran == 5:
                        zagrania5()
                        continue
                    elif iloscZagran == 10:
                        zagrania10()
                        continue
                    elif iloscZagran == 15:
                        zagrania15()
                        continue
                    elif iloscZagran == 19:
                        zagrania19()
                        continue
                    elif iloscZagran == 20:
                        zagrania20(loses)
                        reset = input().upper()
                        if reset == "TAK":
                            print()
                            poziom = poziomyFunkcja()
                            x = xFunkcja()
                            iloscZagran = 0
                            poprzedniPrzegranyKod = x
                            continue
                        else:
                            rezygnacja()

                elif (roznica <= poziom * 20000 and roznica > poziom * 10000):
                    print("------0")
                    if iloscZagran == 5:
                        zagrania5()
                        continue
                    elif iloscZagran == 10:
                        zagrania10()
                        continue
                    elif iloscZagran == 15:
                        zagrania15()
                        continue
                    elif iloscZagran == 19:
                        zagrania19()
                        continue
                    elif iloscZagran == 20:
                        zagrania20(loses)
                        reset = input().upper()
                        if reset == "TAK":
                            print()
                            poziom = poziomyFunkcja()
                            x = xFunkcja()
                            iloscZagran = 0
                            poprzedniPrzegranyKod = x
                            continue
                        else:
                            rezygnacja()

                elif (roznica <= poziom * 10000 and roznica > poziom * 5000):
                    print("---0")
                    if iloscZagran == 5:
                        zagrania5()
                        continue
                    elif iloscZagran == 10:
                        zagrania10()
                        continue
                    elif iloscZagran == 15:
                        zagrania15()
                        continue
                    elif iloscZagran == 19:
                        zagrania19()
                        continue
                    elif iloscZagran == 20:
                        zagrania20(loses)
                        reset = input().upper()
                        if reset == "TAK":
                            print()
                            poziom = poziomyFunkcja()
                            x = xFunkcja()
                            iloscZagran = 0
                            poprzedniPrzegranyKod = x
                            continue
                        else:
                            rezygnacja()

                elif (roznica <= poziom * 5000 and roznica > poziom * 2500):
                    print("--0")
                    if iloscZagran == 5:
                        zagrania5()
                        continue
                    elif iloscZagran == 10:
                        zagrania10()
                        continue
                    elif iloscZagran == 15:
                        zagrania15()
                        continue
                    elif iloscZagran == 19:
                        zagrania19()
                        continue
                    elif iloscZagran == 20:
                        zagrania20(loses)
                        reset = input().upper()
                        if reset == "TAK":
                            print()
                            poziom = poziomyFunkcja()
                            x = xFunkcja()
                            iloscZagran = 0
                            poprzedniPrzegranyKod = x
                            continue
                        else:
                            rezygnacja()

                elif (roznica <= poziom * 2500 and roznica > poziom * 1000):
                    print("-0")
                    if iloscZagran == 5:
                        zagrania5()
                        continue
                    elif iloscZagran == 10:
                        zagrania10()
                        continue
                    elif iloscZagran == 15:
                        zagrania15()
                        continue
                    elif iloscZagran == 19:
                        zagrania19()
                        continue
                    elif iloscZagran == 20:
                        zagrania20(loses)
                        reset = input().upper()
                        if reset == "TAK":
                            print()
                            poziom = poziomyFunkcja()
                            x = xFunkcja()
                            iloscZagran = 0
                            poprzedniPrzegranyKod = x
                            continue
                        else:
                            rezygnacja()

                elif (roznica <= poziom * 1000 and roznica > poziom * 500):
                    print("0")
                    if iloscZagran == 5:
                        zagrania5()
                        continue
                    elif iloscZagran == 10:
                        zagrania10()
                        continue
                    elif iloscZagran == 15:
                        zagrania15()
                        continue
                    elif iloscZagran == 19:
                        zagrania19()
                        continue
                    elif iloscZagran == 20:
                        zagrania20(loses)
                        reset = input().upper()
                        if reset == "TAK":
                            print()
                            poziom = poziomyFunkcja()
                            x = xFunkcja()
                            iloscZagran = 0
                            poprzedniPrzegranyKod = x
                            continue
                        else:
                            rezygnacja()

                elif (roznica <= poziom * 500 and roznica > poziom * 250):
                    print("0+")
                    if iloscZagran == 5:
                        zagrania5()
                        continue
                    elif iloscZagran == 10:
                        zagrania10()
                        continue
                    elif iloscZagran == 15:
                        zagrania15()
                        continue
                    elif iloscZagran == 19:
                        zagrania19()
                        continue
                    elif iloscZagran == 20:
                        zagrania20(loses)
                        reset = input().upper()
                        if reset == "TAK":
                            print()
                            poziom = poziomyFunkcja()
                            x = xFunkcja()
                            iloscZagran = 0
                            poprzedniPrzegranyKod = x
                            continue
                        else:
                            rezygnacja()

                elif (roznica <= poziom * 250 and roznica > poziom * 100):
                    print("0++")
                    if iloscZagran == 5:
                        zagrania5()
                        continue
                    elif iloscZagran == 10:
                        zagrania10()
                        continue
                    elif iloscZagran == 15:
                        zagrania15()
                        continue
                    elif iloscZagran == 19:
                        zagrania19()
                        continue
                    elif iloscZagran == 20:
                        zagrania20(loses)
                        reset = input().upper()
                        if reset == "TAK":
                            print()
                            poziom = poziomyFunkcja()
                            x = xFunkcja()
                            iloscZagran = 0
                            poprzedniPrzegranyKod = x
                            continue
                        else:
                            rezygnacja()

                elif (roznica <= poziom * 100 and roznica > poziom * 50):
                    print("0+++")
                    if iloscZagran == 5:
                        zagrania5()
                        continue
                    elif iloscZagran == 10:
                        zagrania10()
                        continue
                    elif iloscZagran == 15:
                        zagrania15()
                        continue
                    elif iloscZagran == 19:
                        zagrania19()
                        continue
                    elif iloscZagran == 20:
                        zagrania20(loses)
                        reset = input().upper()
                        if reset == "TAK":
                            print()
                            poziom = poziomyFunkcja()
                            x = xFunkcja()
                            iloscZagran = 0
                            poprzedniPrzegranyKod = x
                            continue
                        else:
                            rezygnacja()

                elif (roznica <= poziom * 50 and roznica > poziom * 25):
                    print("0++++")
                    if iloscZagran == 5:
                        zagrania5()
                        continue
                    elif iloscZagran == 10:
                        zagrania10()
                        continue
                    elif iloscZagran == 15:
                        zagrania15()
                        continue
                    elif iloscZagran == 19:
                        zagrania19()
                        continue
                    elif iloscZagran == 20:
                        zagrania20(loses)
                        reset = input().upper()
                        if reset == "TAK":
                            print()
                            poziom = poziomyFunkcja()
                            x = xFunkcja()
                            iloscZagran = 0
                            poprzedniPrzegranyKod = x
                            continue
                        else:
                            rezygnacja()

                elif (roznica <= poziom * 25 and roznica > poziom * 10):
                    print("0++++++")
                    if iloscZagran == 5:
                        zagrania5()
                        continue
                    elif iloscZagran == 10:
                        zagrania10()
                        continue
                    elif iloscZagran == 15:
                        zagrania15()
                        continue
                    elif iloscZagran == 19:
                        zagrania19()
                        continue
                    elif iloscZagran == 20:
                        zagrania20(loses)
                        reset = input().upper()
                        if reset == "TAK":
                            print()
                            poziom = poziomyFunkcja()
                            x = xFunkcja()
                            iloscZagran = 0
                            poprzedniPrzegranyKod = x
                            continue
                        else:
                            rezygnacja()

                elif (roznica <= poziom * 10 and roznica > poziom * 5):
                    print("0++++++++++++")
                    if iloscZagran == 5:
                        zagrania5()
                        continue
                    elif iloscZagran == 10:
                        zagrania10()
                        continue
                    elif iloscZagran == 15:
                        zagrania15()
                        continue
                    elif iloscZagran == 19:
                        zagrania19()
                        continue
                    elif iloscZagran == 20:
                        zagrania20(loses)
                        reset = input().upper()
                        if reset == "TAK":
                            print()
                            poziom = poziomyFunkcja()
                            x = xFunkcja()
                            iloscZagran = 0
                            poprzedniPrzegranyKod = x
                            continue
                        else:
                            rezygnacja()

                elif (roznica <= poziom * 5 and roznica > poziom * 3):
                    print("0++++++++++++++++++++++++")
                    if iloscZagran == 5:
                        zagrania5()
                        continue
                    elif iloscZagran == 10:
                        zagrania10()
                        continue
                    elif iloscZagran == 15:
                        zagrania15()
                        continue
                    elif iloscZagran == 19:
                        zagrania19()
                        continue
                    elif iloscZagran == 20:
                        zagrania20(loses)
                        reset = input().upper()
                        if reset == "TAK":
                            print()
                            poziom = poziomyFunkcja()
                            x = xFunkcja()
                            iloscZagran = 0
                            poprzedniPrzegranyKod = x
                            continue
                        else:
                            rezygnacja()

                elif (roznica <= poziom * 3 and roznica > poziom * 0):
                    print("0++++++++++++++++++++++++++++++++++++++++++++++++")
                    if iloscZagran == 5:
                        zagrania5()
                        continue
                    elif iloscZagran == 10:
                        zagrania10()
                        continue
                    elif iloscZagran == 15:
                        zagrania15()
                        continue
                    elif iloscZagran == 19:
                        zagrania19()
                        continue
                    elif iloscZagran == 20:
                        zagrania20(loses)
                        reset = input().upper()
                        if reset == "TAK":
                            print()
                            poziom = poziomyFunkcja()
                            x = xFunkcja()
                            iloscZagran = 0
                            poprzedniPrzegranyKod = x
                            continue
                        else:
                            rezygnacja()

            else:
                roznica = math.fabs(a - x)
                if roznica > poziom * 20000:
                    print("------------0")
                    if iloscZagran == 5:
                        zagrania5()
                        continue
                    elif iloscZagran == 10:
                        zagrania10()
                        continue
                    elif iloscZagran == 15:
                        zagrania15()
                        continue
                    elif iloscZagran == 19:
                        zagrania19()
                        continue
                    elif iloscZagran == 20:
                        zagrania20(loses)
                        reset = input().upper()
                        if reset == "TAK":
                            print()
                            poziom = poziomyFunkcja()
                            x = xFunkcja()
                            iloscZagran = 0
                            poprzedniPrzegranyKod = x
                            continue
                        else:
                            rezygnacja()

                elif (roznica <= poziom * 20000 and roznica > poziom * 10000):
                    print("------0")
                    if iloscZagran == 5:
                        zagrania5()
                        continue
                    elif iloscZagran == 10:
                        zagrania10()
                        continue
                    elif iloscZagran == 15:
                        zagrania15()
                        continue
                    elif iloscZagran == 19:
                        zagrania19()
                        continue
                    elif iloscZagran == 20:
                        zagrania20(loses)
                        reset = input().upper()
                        if reset == "TAK":
                            print()
                            poziom = poziomyFunkcja()
                            x = xFunkcja()
                            iloscZagran = 0
                            poprzedniPrzegranyKod = x
                            continue
                        else:
                            rezygnacja()

                elif (roznica <= poziom * 10000 and roznica > poziom * 5000):
                    print("---0")
                    if iloscZagran == 5:
                        zagrania5()
                        continue
                    elif iloscZagran == 10:
                        zagrania10()
                        continue
                    elif iloscZagran == 15:
                        zagrania15()
                        continue
                    elif iloscZagran == 19:
                        zagrania19()
                        continue
                    elif iloscZagran == 20:
                        zagrania20(loses)
                        reset = input().upper()
                        if reset == "TAK":
                            print()
                            poziom = poziomyFunkcja()
                            x = xFunkcja()
                            iloscZagran = 0
                            poprzedniPrzegranyKod = x
                            continue
                        else:
                            rezygnacja()

                elif (roznica <= poziom * 5000 and roznica > poziom * 2500):
                    print("--0")
                    if iloscZagran == 5:
                        zagrania5()
                        continue
                    elif iloscZagran == 10:
                        zagrania10()
                        continue
                    elif iloscZagran == 15:
                        zagrania15()
                        continue
                    elif iloscZagran == 19:
                        zagrania19()
                        continue
                    elif iloscZagran == 20:
                        zagrania20(loses)
                        reset = input().upper()
                        if reset == "TAK":
                            print()
                            poziom = poziomyFunkcja()
                            x = xFunkcja()
                            iloscZagran = 0
                            poprzedniPrzegranyKod = x
                            continue
                        else:
                            rezygnacja()

                elif (roznica <= poziom * 2500 and roznica > poziom * 1000):
                    print("-0")
                    if iloscZagran == 5:
                        zagrania5()
                        continue
                    elif iloscZagran == 10:
                        zagrania10()
                        continue
                    elif iloscZagran == 15:
                        zagrania15()
                        continue
                    elif iloscZagran == 19:
                        zagrania19()
                        continue
                    elif iloscZagran == 20:
                        zagrania20(loses)
                        reset = input().upper()
                        if reset == "TAK":
                            print()
                            poziom = poziomyFunkcja()
                            x = xFunkcja()
                            iloscZagran = 0
                            poprzedniPrzegranyKod = x
                            continue
                        else:
                            rezygnacja()

                elif (roznica <= poziom * 1000 and roznica > poziom * 500):
                    print("0")
                    if iloscZagran == 5:
                        zagrania5()
                        continue
                    elif iloscZagran == 10:
                        zagrania10()
                        continue
                    elif iloscZagran == 15:
                        zagrania15()
                        continue
                    elif iloscZagran == 19:
                        zagrania19()
                        continue
                    elif iloscZagran == 20:
                        zagrania20(loses)
                        reset = input().upper()
                        if reset == "TAK":
                            print()
                            poziom = poziomyFunkcja()
                            x = xFunkcja()
                            iloscZagran = 0
                            poprzedniPrzegranyKod = x
                            continue
                        else:
                            rezygnacja()

                elif (roznica <= poziom * 500 and roznica > poziom * 250):
                    print("0+")
                    if iloscZagran == 5:
                        zagrania5()
                        continue
                    elif iloscZagran == 10:
                        zagrania10()
                        continue
                    elif iloscZagran == 15:
                        zagrania15()
                        continue
                    elif iloscZagran == 19:
                        zagrania19()
                        continue
                    elif iloscZagran == 20:
                        zagrania20(loses)
                        reset = input().upper()
                        if reset == "TAK":
                            print()
                            poziom = poziomyFunkcja()
                            x = xFunkcja()
                            iloscZagran = 0
                            poprzedniPrzegranyKod = x
                            continue
                        else:
                            rezygnacja()

                elif (roznica <= poziom * 250 and roznica > poziom * 100):
                    print("0++")
                    if iloscZagran == 5:
                        zagrania5()
                        continue
                    elif iloscZagran == 10:
                        zagrania10()
                        continue
                    elif iloscZagran == 15:
                        zagrania15()
                        continue
                    elif iloscZagran == 19:
                        zagrania19()
                        continue
                    elif iloscZagran == 20:
                        zagrania20(loses)
                        reset = input().upper()
                        if reset == "TAK":
                            print()
                            poziom = poziomyFunkcja()
                            x = xFunkcja()
                            iloscZagran = 0
                            poprzedniPrzegranyKod = x
                            continue
                        else:
                            rezygnacja()

                elif (roznica <= poziom * 100 and roznica > poziom * 50):
                    print("0+++")
                    if iloscZagran == 5:
                        zagrania5()
                        continue
                    elif iloscZagran == 10:
                        zagrania10()
                        continue
                    elif iloscZagran == 15:
                        zagrania15()
                        continue
                    elif iloscZagran == 19:
                        zagrania19()
                        continue
                    elif iloscZagran == 20:
                        zagrania20(loses)
                        reset = input().upper()
                        if reset == "TAK":
                            print()
                            poziom = poziomyFunkcja()
                            x = xFunkcja()
                            iloscZagran = 0
                            poprzedniPrzegranyKod = x
                            continue
                        else:
                            rezygnacja()

                elif (roznica <= poziom * 50 and roznica > poziom * 25):
                    print("0++++")
                    if iloscZagran == 5:
                        zagrania5()
                        continue
                    elif iloscZagran == 10:
                        zagrania10()
                        continue
                    elif iloscZagran == 15:
                        zagrania15()
                        continue
                    elif iloscZagran == 19:
                        zagrania19()
                        continue
                    elif iloscZagran == 20:
                        zagrania20(loses)
                        reset = input().upper()
                        if reset == "TAK":
                            print()
                            poziomyFunkcja()
                        
                            znakFunkcja()
                            iloscZagran = 0
                            poprzedniPrzegranyKod = x
                            continue
                        else:
                            rezygnacja()

                elif (roznica <= poziom * 25 and roznica > poziom * 10):
                    print("0++++++")
                    if iloscZagran == 5:
                        zagrania5()
                        continue
                    elif iloscZagran == 10:
                        zagrania10()
                        continue
                    elif iloscZagran == 15:
                        zagrania15()
                        continue
                    elif iloscZagran == 19:
                        zagrania19()
                        continue
                    elif iloscZagran == 20:
                        zagrania20(loses)
                        reset = input().upper()
                        if reset == "TAK":
                            print()
                            poziom = poziomyFunkcja()
                            x = xFunkcja()
                            iloscZagran = 0
                            poprzedniPrzegranyKod = x
                            continue
                        else:
                            rezygnacja()

                elif (roznica <= poziom * 10 and roznica > poziom * 5):
                    print("0++++++++++++")
                    if iloscZagran == 5:
                        zagrania5()
                        continue
                    elif iloscZagran == 10:
                        zagrania10()
                        continue
                    elif iloscZagran == 15:
                        zagrania15()
                        continue
                    elif iloscZagran == 19:
                        zagrania19()
                        continue
                    elif iloscZagran == 20:
                        zagrania20(loses)
                        reset = input().upper()
                        if reset == "TAK":
                            print()
                            poziom = poziomyFunkcja()
                            x = xFunkcja()
                            iloscZagran = 0
                            poprzedniPrzegranyKod = x
                            continue
                        else:
                            rezygnacja()

                elif (roznica <= poziom * 5 and roznica > poziom * 3):
                    print("0++++++++++++++++++++++++")
                    if iloscZagran == 5:
                        zagrania5()
                        continue
                    elif iloscZagran == 10:
                        zagrania10()
                        continue
                    elif iloscZagran == 15:
                        zagrania15()
                        continue
                    elif iloscZagran == 19:
                        zagrania19()
                        continue
                    elif iloscZagran == 20:
                        zagrania20(loses)
                        reset = input().upper()
                        if reset == "TAK":
                            print()
                            poziom = poziomyFunkcja()
                            x = xFunkcja()
                            iloscZagran = 0
                            poprzedniPrzegranyKod = x
                            continue
                        else:
                            rezygnacja()

                elif (roznica <= poziom * 3 and roznica > poziom * 0):
                    print("0++++++++++++++++++++++++++++++++++++++++++++++++")
                    if iloscZagran == 5:
                        zagrania5()
                        continue
                    elif iloscZagran == 10:
                        zagrania10()
                        continue
                    elif iloscZagran == 15:
                        zagrania15()
                        continue
                    elif iloscZagran == 19:
                        zagrania19()
                        continue
                    elif iloscZagran == 20:
                        zagrania20(loses)
                        reset = input().upper()
                        if reset == "TAK":
                            print()
                            poziom = poziomyFunkcja()
                            x = xFunkcja()
                            iloscZagran = 0
                            poprzedniPrzegranyKod = x
                            continue
                        else:
                            rezygnacja()

        else:
            if (iloscZagran < 20):
                print("GRATULACJE Kapralu Kox!!! FANFARY!!! Potrzebowałeś tylko ", iloscZagran," prób by wygrać i ocalić kosmos oraz bezpośrednie okolice! Tak trzymać!")
                wins += 1
                poprzedniZlamanyKod = x
                print("Doktor Queen właśnie mnie poinformowała, że każdorazowa podróż w czasie zmienia klucz szyfrowania. Kapralu, czy chcesz cofnąć się w czasie i spróbować uratować kosmos jeszcze raz? TAK/NIE")
                reset = input().upper()
                if reset == "TAK":
                    winsFunkcja(wins, loses)
                    poziom = poziomyFunkcja()
                    x = xFunkcja()
                    iloscZagran = 0
                    continue
                else:
                    print("Rozumiem Kapralu - jeden heroiczny czyn na dzień wystarczy. Gdybyś jednak zmienił/a zdanie, to znajdziesz mnie w Kantynie \"Laser\", w której będę opijał (porządnie) nasze zwycięstwo!")
            else:
                print("GRATULACJE Kapralu Kox!!! FANFARY!!! BYŁO BLISKO! Zużyłeś wszystkie możliwe próby, ale i tak udało Ci się ocalić kosmos oraz bezpośrednie okolice! Następnym razem postaraj się ocalić kosmos szybciej!")
                wins += 1
                poprzedniZlamanyKod = x
                print("Doktor Queen właśnie mnie poinformowała, że każdorazowa podróż w czasie zmienia klucz szyfrowania. Kapralu, czy chcesz cofnąć się w czasie i spróbować uratować kosmos jeszcze raz? TAK/NIE")
                reset = input().upper()
                if reset == "TAK":
                    winsFunkcja(wins, loses)
                    poziom = poziomyFunkcja()
                    x = xFunkcja()
                    iloscZagran = 0
                    continue
                else:
                    print("Rozumiem Kapralu - jeden heroiczny czyn na dzień wystarczy. Gdybyś jednak zmienił/a zdanie, to znajdziesz mnie w Kantynie \"Laser\", w której będę opijał (porządnie) nasze zwycięstwo!")

            Timer(10, exitfunc).start()
            while True:
                time.sleep(1)


    except ValueError:
        print("Musi być liczba całkowita")
        continue