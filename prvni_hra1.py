import time
import random


pravidla = input(f"Chete si přečíst pravidla a úvod? (ano, ne): ")
if pravidla == "ano":
    print(f"Vítejte na spawnu, jmenuji si Bukaj a jsem tvůrcem této minihry.")
    time.sleep(3)
    print(f"Princip této hry je velice jednoduchý.")
    time.sleep(3)
    print(f"Aby jste hru dokončili musíte přejít přes 3 levely. V každém levelu vás čekají různé hry. Na konci každého levelu se vám odhalí jedno písmenko.")
    time.sleep(5)
    print(f"Na konci levelu 3, pak budete dotázán na hledané slovo. Hru dokončíte tak, že toto slovo úspěšně zadáte.")
    time.sleep(5)
    print(f"Pozor! Je důležité levely dělat postupně! Začněte lvl. 1 a skončete lvl. 3!")
    time.sleep(4)
    print(f"To je vše na úvod, nyní se můžete do hry vrhnout, hodně štěstí.")
    level = int(input("Zvolte číslo levelu: "))
elif pravidla == "ne":
    level = int(input("Zvolte číslo levelu: "))

if level == 1:
    print(f"Vítejte, právě jste se ocitl v Quizlandu. Vašim úkolem je dostat se přes 5 jednoduchých otázek.")
    time.sleep(4)
    print(f"Na otázky odpovídejte odpovědmi a, b nebo c")
    time.sleep(3)
    print(f"Avšak POZOR! Každá špatná odpověď pro vás znamená začit celý lvl. od znova!")
    time.sleep(4)
    print(f"Pojďme tedy začít.")
    time.sleep(3)
    print(f"1. otázka: ")
    time.sleep(1)
    print(f"Pod jakou přezdívkou se autor prezentuje?")
    time.sleep(2)
    print(f"a) Žukov")
    time.sleep(1)
    print(f"b) Bukovec")
    time.sleep(1)
    print(f"c) Bukaj")
    time.sleep(1)
    odpoved1 = input("Odpověď: ")
    if odpoved1 == "c":
        print(f"To je správná odpověď, to bylo celkem jednoduché, pojďme na 2. otázku.")
        time.sleep(1)
        print(f"2. otázka: ")
        time.sleep(1)
        print(f"Kdo je kapitánem týmu HC Olomouc?")
        time.sleep(2)
        print(f"a) Jan Knotek")
        time.sleep(1)
        print(f"b) Jakub Navrátil")
        time.sleep(1)
        print(f"c) Jiří Ondrušek")
        time.sleep(1)
        odpoved2 = input("Odpověď: ")
        if odpoved2 == "c":
            print(f"To je správná odpověď, vidím, že hokej sledujete, pojďme dále.")
            time.sleep(1)
            print(f"3. otázka: ")
            time.sleep(1)
            print(f"Co byla operace Barbarossa?")
            time.sleep(2)
            print(f"a) Invaze Nacistického Německa do Sovětského svazu")
            time.sleep(1)
            print(f"b) Atentát na Heydricha")
            time.sleep(1)
            print(f"c) Krycí jméno pro spojenecké bombardování německého průmyslu")
            time.sleep(1)
            odpoved3 = input("Odpověď: ")
            if odpoved3 == "a":
                print(f"To je správná odpověď, vidím, že historie vám jde, tím pádem další otázka bude pro vás zadarmo.")
                time.sleep(1)
                print(f"4. otázka: ")
                time.sleep(1)
                print(f"Jak se jmenovali vojáci, kteří úspěšně provedli atentát na zastupujícího říšského protektora Reinharda Heydricha?")
                time.sleep(4)
                print(f"a) Karel Čurda a Jan Kubiš")
                time.sleep(1)
                print(f"b) Jan Kubiš a Jozef Gabčík ")
                time.sleep(1)
                print(f"c) Jozef Gabčík a Karel Svoboda")
                time.sleep(1)
                odpoved4 = input("Odpověď: ")
                if odpoved4 == "b":
                    print(f"To je správná odpověď, poslední otázka prověří vaše znalosti v zeměpisu.")
                    time.sleep(3)
                    print(f"5. otázka: ")
                    time.sleep(1)
                    print(f"Jaký z těchto státu se NACHÁZÍ v Jižní Americe")
                    time.sleep(4)
                    print(f"a) Suriname")
                    time.sleep(1)
                    print(f"b) Belize")
                    time.sleep(1)
                    print(f"c) Ghana")
                    time.sleep(1)
                    odpoved5 = input("Odpověď: ") 
                    if odpoved5 == "a":
                        print(f"A máte naprostou pravdu!!!")
                        time.sleep(1)
                        print(f"Gratuluji k dokončení lvl. 1, první písmeno do tajenky je 'f'.")
                        time.sleep(3)
                        print(f"Zachvíly budete vrácen na spawn.")
                        time.sleep(3)
                    elif odpoved5 == "b":
                        print(f"Špatná odpověď. Musíte začít od začátku.")
                    elif odpoved5 == "c":
                        print(f"Špatná odpověď. Musíte začít od začátku.!")
                    else:
                        print(f"Tady ta možnost tu ani není pro kristovy rány")
                elif odpoved4 == "a":
                    print(f"Špatná odpověď. Musíte začít od začátku.") 
                elif odpoved4 == "c":
                    print(f"Špatná odpověď. Musíte začít od začátku.") 
                else:
                    print(f"Tady ta možnost tu ani není pro kristovy rány")
            elif odpoved3 == "b":
                print(f"Špatná odpověď. Musíte začít od začátku.")
            elif odpoved3 == "c":
                print(f"Špatná odpověď. Musíte začít od začátku.") 
            else:
                print(f"Tady ta možnost tu ani není pro kristovy rány")
        elif odpoved2 == "a":
            print(f"Špatná odpověď. Musíte začít od začátku.")
        elif odpoved2 == "b":
            print(f"Špatná odpověď. Musíte začít od začátku.")
        else:
            print(f"Tady ta možnost tu ani není pro kristovy rány")
    elif odpoved1 == "a":
        print(f"Špatná odpověď. Musíte začít od začátku.!")
    elif odpoved1 == "b":
        print(f"Špatná odpověď. Musíte začít od začátku.")
    else:
        print(f"Tady ta možnost tu ani není pro kristovy rány")
if level == 2:
    print(f"Ocitl jste se v bludišti, vašim úkolem je najít únikovou cestu, v bludišti je možné i zemřít! Pokud zemřete musíte začít celý lvl. od začátku.")
    time.sleep(4)
    print(F"Před každou cestou vám bude řečena nápověda, vždy se zamyslete nad podstatou věty či stavbou věty.")
    time.sleep(3)
    print(f"Bludiště berte z pohledu první osoby!")
    time.sleep(2)
    print(f"legenda: ")
    time.sleep(2)
    print(f"w = rovno")
    time.sleep(1)
    print(f"a = vlevo")
    time.sleep(1)
    print(f"d = vpravo")
    time.sleep(3)
    print(f"Nápověda: Anička absolvovala akademii a dodržela denní docházku.")
    trasa = input("Vyberte první cestu: ")
    if trasa == "w":
        print(f"Nápověda: Vpravo dobri, rovno dobri, vlevo blbý")
        trasa1_1 = input("Jak budete pokračovat dál: ")
        if trasa1_1 == "d":
            print(f"Narazily jste na velkého SMEGRA, který vás snědl, musíte začít znova.")
            time.sleep(1)
        elif trasa1_1 == "w":
            print(f"Zhroutila se pod vámi podlaha, musíte začít znova.")
            time.sleep(1)
        elif trasa1_1 == "a":
            print(f"Nápověda: Vpravo kámen, rovno vejce, vlevo asi cesta")
            trasa1_2 = input("Zvolte vaší další cestu: ")
            if trasa1_2 == "d":
                print(f"Vstupní cesta byla zasypána, jste v pasti, musíte začít znova.")
                time.sleep(1)
            elif trasa1_2 == "w":
                print(f"Našel jste easter egg, hra teď sice končí, ale do cíle se dostanete pomocí zkratky 's' ")
                time.sleep(1)
            elif trasa1_2 == "a":
                print(f"Nápověda: vpravo jste nebyl, vlevo to už znáte, WoW!")
                trasa1_3 = input("Zvolte cestu: ")
                if trasa1_3 == "a":
                    print(f"Ocitl jste se na začátku, můžete začít znovu :).")
                    time.sleep(1)
                elif trasa1_3 == "d":
                    print(f"Ocitl jste se v BACKROOMS, musíte začít znova.")
                    time.sleep(1)
                elif trasa1_3 == "w":
                    print(f"Nápověda: Skočíte na to levárnu?")
                    trasa1_4 = input("Vyberte cestu, jeste blíž než si myslíte: ")
                    if trasa1_4 == "d":
                        print(f"Ocitl jste se v BACKROOMS, musíte začít znova.")
                        time.sleep(1)
                    elif trasa1_4 == "w":
                        print(f"V místnosti se objevilo spostu jedovatých hadů, tady končíte, musíte znova.")
                        time.sleep(1)
                    elif trasa1_4 == "a":
                        print(f"Našel jste cíl, gratuluji! Dokončil jste lvl. 2, druhé písmenko tajenky je 'i'. Za pár sekund budete vrácen zpět na spawn.")
                        time.sleep(5)
    elif trasa == "a":
        print(f"Nápověda: Tak ještě jednou, Anička absolvovala")
        trasa2_1 = input("Jak chcete pokračovat: ")
        if trasa2_1 == "w":
            print(f"Ocitl jste se v BACKROOMS, musíte začít znova.")
            time.sleep(1)
        elif trasa2_1 == "a":
            print(f"Nápověda: Anička")
            trasa2_2 = input("Zvolte dalši cestu: ")
            if trasa2_2 == "d":
                print(f"Ocitl jste se v BACKROOMS, musíte začít znova.")
                time.sleep(1) 
            elif trasa2_2 == "w":
                print(f"V místnosti se objevilo spostu jedovatých hadů, tady končíte, musíte znova.")
                time.sleep(1)
            elif trasa2_2 == "a":
                print(f"Našel jste cíl, gratuluji! Dokončil jste lvl. 2, druhé písmenko tajenky je 'i'. Za pár sekund budete vrácen zpět na spawn.")
                time.sleep(5) 
        elif trasa2_1 == "d":
            print(f"Nápověda: no, nevim no, moc to tu hezký není.")
            trasa2_3 = input("Zvolte vaši dálší cestu: ")
            if trasa2_3 == "a":
                print(f"Našel jste easter egg, hra teď sice končí, ale do cíle se dostanete pomocí zkratky 'd' ")
                time.sleep(1)
            elif trasa2_3 == "w":
                print(f"Vstupní cesta byla zasypána, jste v pasti, musíte začít znova.")
                time.sleep(1)
            elif trasa2_3 == "d":
                print(f"Nápověda: A to jste v pasti.")
                trasa2_4 = input("Jakou cestu zvolíte: ")
                if trasa2_4 == "a":
                    print(f"Zhroutila se pod vámi podlaha, musíte začít znova.")
                    time.sleep(1)
                elif trasa2_4 == "w":
                    print(f"Narazily jste na velkého SMEGRA, který vás snědl, musíte začít znova.")
                    time.sleep(1)
                elif trasa2_4 == "d":
                    print(f"Ocitl jste se na zažátku, můžete začít znovu :).")
                    time.sleep(1)
    elif trasa == "d":
        print(f"Nápověda: Dodržela docházku!")
        trasa3_1 = input("Zvolte jak chcete pokračovat: ")
        if trasa3_1 == "a":
            print(f"Narazily jste na velkého SMEGRA, který vás snědl, musíte začít znova.")
            time.sleep(1)
        elif trasa3_1 == "w":
            print(f"Ocitl jste se v BACKROOMS, musíte začít znova.")
            time.sleep(1) 
        elif trasa3_1 == "d":
            print(f"dnes je nádherný Den.")
            trasa3_2 = input("Jakou cestu zvolíte: ")
            if trasa3_2 == "w":
                print(f"Místnost se začíná plnit vodou, tady cesta nevede, musíte zonva.")
            elif trasa3_2 == "a":
                print(f"Ocitl jste se v BACKROOMS, musíte začít znova.")
                time.sleep(1)
            elif trasa3_2 == "d":
                print(f"Našel jste cíl, gratuluji! Dokončil jste lvl. 2, druhé písmenko tajenky je 'i'. Za pár sekund budete vrácen zpět na spawn.")
                time.sleep(5)
    elif trasa == "s":
        print(f"Dorazil jste do cíle, ano tak jednoduché to bylo, gratuluji k dokončení lvl. 2 druhé písmenko tajenky je 'i', zachvíly budete vrácen zpět na spawn.")
        time.sleep(6)
if level == 3:
    print(f"Vítejte v posledním lvl.")
    time.sleep(2)
    print(f"Ocitl jste se na hradě Rohlík.")
    time.sleep(2)
    print(f"Vašim úkolem je se dostat pryč z hradu, ale hlavní brána je zavřená, avšak jsou tu tajné dveře. Kde se však klíč skrývá ví pouze samotný král, ale také hradní paní.")
    time.sleep(6)
    print(f"Král vám jistě klíč nedá, ale hradní paní ano. Kde se však skrývá? To musíte zjistit.")
    time.sleep(4)
    print(f"*Příběh začíná*")
    time.sleep(2)
    print(f"*Jdete chodbou a potkáváte sluhu krále*")
    time.sleep(3)
    print(f"Sluha: 'Zdravím tě, Co tu pohledáváš? Hradní paní? Tak to tě zklamu, nevím kde by mohla být, ale možná vím někoho kdo by o ní něco věděl, ale potřebuji pomoc.'")
    time.sleep(6)
    print(f"Sluha: 'Mám tu matematický příklad a když mi ho vypočítáš, tak ti pomohu. Tak hele ten příklad zní: 8*5-20+10+100-50+60-110'")

    odpoved_hrad1 = int(input("Výsledek je: "))
    while odpoved_hrad1 < 30 or odpoved_hrad1 > 30:
        print(f"To není správně, zkus to znova")
        odpoved_hrad1 = int(input("Výsledek je: "))
    print(f"Sluha: 'Páni jsi fakt dobrej, no dobrá, zajdi za šéfkuchařem, on by vědět mohl.'")
    time.sleep(4)
    print(f"*Docházíš do kuchyně*")
    time.sleep(2)
    print(f"Šéfkuchař: 'Heeej, co tady pohledáváš!'")
    time.sleep(2)
    print(f"Šéfkuchař: 'Jooo hradní paní. Nevidím důvod proč bych ti to měl říkat. Ikdyž víš co, mám pro tebe návrh.'")
    time.sleep(5)
    print(f"Šéfkuchař: 'Vidíš na tom stole ty misky s jídlem, v každé misce je surovina, která mezi ostatní nepatří, pomož mi je najít a řeknu ti co chceš slyšet'")
    time.sleep(5)
    pec = ["chleba", "paprika", "houska", "vánočka", "preclík"]
    zel = ["okurek", "rajče", "salát", "cibule", "malina"]
    ovo = ["banán", "jablko", "hruška", "mrkev", "broskev"]
    print(pec)
    print(zel)
    print(ovo)

    prvni_miska = input(f"Do první misky nepatří: ")
    while not "paprika" in prvni_miska:
        print(f"Tohle tam patří!")
        prvni_miska = input(f"Do první misky nepatří: ")
    print(f"Ano, paprika do této misky nepatří.")


    druha_miska = input(f"Do druhé misky nepatří: ")
    while not "malina" in druha_miska:
        print(f"Tahle věc tam patří!")
        druha_miska = input(f"Do druhé misky nepatří: ")
    print(f"Správně, malina v této misce nemá co dělat.")
    
    
    treti_miska = input(f"Do třetí misky nepatří: ")
    while not "mrkev" in treti_miska:
        print(f"Nene, tohle tam patří!")
        treti_miska = input(f"Do třetí misky nepatří: ")
    print(f"Ano, mrkev je tu navíc.")
    time.sleep(1)
    print(f"Šéfkuchař: 'Páni, děkuji ti, hodně jsi mi pomohl, na oplátku ti tedy také pomohu. Hradní paní se nachází v pravé přední věži.'")
    time.sleep(5)
    print(f"*Pricházíš do věže hradní paní*")
    time.sleep(2)
    print(f"Hradní paní: 'Kdo jsi a co tě ke mně přivádí? '")
    time.sleep(3)
    print(f"Hradní paní: 'Tak ty by jsi rád klíč k tajnému vchodu, no musím uznat že je úctyhodné, že jsi se dostal až sem.'")
    time.sleep(5)
    print(f"Hradní Paní: 'Klíč ti tedy dám, ale pouze když uhodneš mojí hádanku.'")
    time.sleep(4)
    print(f"Hradní Paní: 'Tak tedy poslouchej.'")
    time.sleep(2)
    print(f"Hradní paní: 'Když mě máš, chceš mě sdílet. Když mě sdílíš, tak mě nemáš. Co jsem?'")
    
    hadanka = input("Odpověď na hádanku: ")
    while "tajemství" not in hadanka:
        print(f"Hradní paní: 'To není správně, zkus to ještě jednou.'")
        hadanka = input("Odpověď na hádanku: ")

    print(f"Hradní paní: 'Správně, Uhodl jsi mojí hádanku, tady máš svůj klíč, dveře se nachází v tunelu pod hlavní bránou, sbohem poutníku.'")
    time.sleep(5)
    print(f"*Procházíš hradem až k tunelu*")
    time.sleep(2)
    print(f"*Před dveřmi se objeví strážce.*")
    time.sleep(2)
    print(f"Strážce: 'Ha a mám tě! Celou dobu jsem tě pronásledoval. Dál tě nenechám udělat ani krok!'")
    time.sleep(4)
    print(f"Strážce: 'Leda, že by jsi mě porazil ve hře, která prověří zda máš právo na to utéct!'")
    time.sleep(4)
    print(f"Strážce: 'Kámen, nůžky, papír!'")
    time.sleep(2)

    možnostiRPS = ("kámen", "nůžky", "papír")
    prubeh = True
   

    while prubeh:
        volba = ""
        strazce = random.choice(možnostiRPS)

        while volba not in možnostiRPS:
            volba = input("Zvolte možnost (kámen, nůžky, papír): ")


        print(f"Vaše volba: {volba}")
        print(f"Volba strážce: {strazce}")   


        if strazce == volba:
            print(f"Strážce: 'Hah remíza ti je k ničemu! Tak znova!'")
        elif strazce == "kámen" and volba == "nůžky":
            print(f"Strážce: 'Jsem neporazitelný, pojď klidně znova! Mně nikdy neporazíš, hahaha.'")
        elif strazce == "nůžky" and volba == "papír":
            print(f"Strážce: 'Jsem neporazitelný, pojď klidně znova! Mně nikdy neporazíš, hahaha.'")
        elif strazce == "papír" and volba == "kámen":
            print(f"Strážce: 'Jsem neporazitelný, pojď klidně znova! Mně nikdy neporazíš, hahaha.'")

        else:
            prubeh = False
            print(f"Strážce: 'Ty, ty.. jsi mě porazil, ale jaaak. To není možné, ještě nikdy jsem předtím neprohrál.'")
            time.sleep(4)
            print(f"Strážce: 'No dobrá, tak běž!'")
            time.sleep(2)
            print(f"*Otevíráš dveře a odcházíš z hradu.*")
            time.sleep(2)
            print(f"Gratuluji k dokončení lvl. 3. Poslední písmenko tajenky je 'n'.")
            time.sleep(3)
            print(f"Nyní jste připraven uhodnout slovo, tak s chutí do toho.")
            time.sleep(2)
            tajenka = input("Slovo tajenky je: ")
            while not "fin" == tajenka:
                print(f"To je špatně, nekde jsi se musel seknout, zkus to znovu.")
                tajenka = input("Slovo tajenky je: ")
            print(f"Výborně! To je správně!")
            time.sleep(2)
            print(F"Ano slovo fin znamená konec a na tom se právě nacházíte.")
            time.sleep(3)
            print(f"Gratuluji za dokončení hry a zároveň za zahrání hry.")