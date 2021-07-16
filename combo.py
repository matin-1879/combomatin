# By Matin
import random, colorama
print(f"{colorama.Style.BRIGHT}{colorama.Fore.GREEN}")
count = 0
Domain = "gmail.com","outlook.com","mail.ru","yahoo.com","mailgano.com","trashmail.es","lycos.com","hushmail.com","hush.com","hushmail.me","mac.hush.com","hush.ai","Graphic-Designer.com","ie.petlover.com","mail.com","email.com","usa.com","myself.com","consulatn.com","post.com","dr.com","execs.com","europe.com","engineer.com","asia.com","writeme.com","iname.com","techie.com","contractor.com","accountant.com","workmail.com","musician.org","artlover.com","cheerful.com","hackermail.com","homemail.com","planetmail.com","housemail.com","activist.com","chef.net","toke.com","gmx.com","Facebook.com","Yandex.com","Shortmail.com","aol.com","hotmail.co.uk","hotmail.fr","msn.com","yahoo.fr","wanadoo.fr","orange.fr","comcast.net","yahoo.co.uk","yahoo.com.br","yahoo.co.in","live.com","rediffmail.com","free.fr","gmx.de","web.de","yandex.ru","ymail.com","libero.it","uol.com.br","bol.com.br","cox.net","hotmail.it","sbcglobal.net","verizon.net","bigpond.com","terra.com.br","alice.it","yahoo.in","rambler.ru","tiscali.it"
nfc = "0123456789"
IQ = "0770","0780","0750"
EG = "15","10","12","11"
nfc1 = "6","7","8","9"
em="Ali","Omar","Osama","Hussain","Amar","Amir","Rim","Rima","Zainab","Fatma","Zahraa","Abbas","Mustafa","Rashd","Gmal","Kadim","Mohammed","Bakr","Othman","Saud","Fahad","lena","somia","Safa","Tala","Safwan","Bahaa","Heba","Abeer","Afaf","Aisha","Aliya","Amina","Amira","Arwa","Asma","Aya","Azhar","Bushra","Saleh","Salem","Salman","Naif","Basm","Bassam","Nawaf","Mussab","Olivia","Liam","Noah","Oliver","Elijah","William","James","Benjamin","Lucas","Henry","Alexander","Mia","Khalifa"
com = ""
mode = input("DANAYAK DABNE: \n\n [1] NUMBER:NUMBER \n\n[2] EMAIL:PASS \n   \n [3] JUST PASSWORD     : ")
print("")
lecn = "2","3","4","5"
lenlast = 7,8,9
len = int(random.choice(lecn))
lecn1 = "5","6","7"
len1 = int(random.choice(lecn1))
user = "" 
sim = "qwertyuiopasdfghjklzxcvbnmqwertyuiopasdfghjklzxcvbnmqwertyuiopasdfghjklzxcvbnmqwertyuiopasdfghjklzxcvbnmqwertyuiopasdfghjklzxcvbnmqwertyuiopasdfghjklzxcvbnmqwertyuiopasdfghjklzxcvbn123456789123456789123456789123456789123456789"
length = int(7)
length1 = int(random.choice(nfc1))
nfc = "0123456789"
chars = "123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890"
def nccc():
             while True:
                 pas = ""
                 for me in range(length1):
                   c = random.choice(chars)
                   pas += c
                 return pas
def ncc():
             while True:
                 pas = ""
                 for me in range(len):
                   c = random.choice(chars)
                   pas += c
                 return pas
if mode == "1":
    c = input("HALLBZHERA:\n \n [1] IRAQ\n \n:  ")
    if c == "1":
        hmn = int(input("CHAND DANA:  "))
        print("")
        while True:
            if count < hmn:
                count += 1
                for item in range(length):
                    v = random.choice(nfc)
                    bg = random.choice(chars)
                    rs = random.choice(IQ)
                    user += bg
                with open("combo.txt", "a") as m:
                    m.write(f"\n{rs}{v}{user}:{rs}{v}{user}")
                    print("TAWAW", count)
                    user = ""
    if c == "2":
        hmn = int(input("CHAND DANA:  "))
        print("")
        while True:
            if count < hmn:
                count += 1
                for item in range(length):
                    v = random.choice(nfc)
                    bg = random.choice(chars)
                    rs = random.choice(EG)
                    user += bg
                with open("Phone number [EG].txt", "a") as m:
                    m.write(f"\n{rs}{v}{user}:{rs}{v}{user}")
                    print("TAWAW", count)
                    user = ""
elif mode == "2":
    Aom = input("\n [1] RONDOM\n\n    [2] BA NAME EXOT \n\n [3] TANHA EMAIL:  ")
    if Aom == "1":
        hmn = int(input("CHAND DANA:  "))
        while True:
            if count < hmn:
                count += 1
                for item in range(1):
                     l = random.choice(em)
                     com += l
                with open("combo.txt", "a") as m:
                    m.write(f"{com}{ncc()}@gmail.com:{com}{nccc()}\n")
                    print("TAWAW", count)
                    pas = ""
                    com = ""
                if count >= hmn:
                    print(f"""EMAIL GENERATED:{count}\nPASSWORD GENERATED:{count}""")
    elif Aom == "2":
        tn = input("NAWEK DANE KA ATAWE BAW BEHENE:  ")
        hmn = int(input("CHAND DANA:  "))
        num = int(input("CHAND RAQAMT AWET KA LANAW EMAILAKA BET:  "))
        def nyc():
             while True:
                 pas = ""
                 for me in range(num):
                   c = random.choice(chars)
                   pas += c
                 return pas
        def ncvc():
            while True:
                 pas = ""
                 for me in range(len1):
                   c = random.choice(sim)
                   pas += c
                 return pas
        while True:
            if count < hmn:
                count += 1
                for item in range(1):
                     l = random.choice(chars)
                     com += l
                with open("combo.txt", "a") as m:
                    m.write(f"{tn}{nyc()}@gmail.com:{ncvc()}\n")
                    print("TAWAW", count)
                    pas = ""
                    com = ""
                if count >= hmn:
                    print(f"""EMAIL:{count}\nPASS{count}""")
    elif Aom == "3":
        tn = input("NAWEK DANE KA ATAWE BAW BEHENE:  ")
        num = int(input("CHAND DANA RAQAMT AWET LANAW EMAIL:  "))
        hmn = int(input("CHAND DANA:"))
        sdfu = input("HALLBZHERA \n \n[1] BA TARGET DOMAIM \n\n[2] RONDOM DOMAIN\n:  ")
        if sdfu == "1":
            do = input("DOMAIN BNUSA WAKU {gmail.com}:  ")
            def nyc():
                 while True:
                     pas = ""
                     for me in range(num):
                       c = random.choice(chars)
                       pas += c
                     return pas
            while True:
                if count < hmn:
                    count += 1
                    with open("Combo.txt", "a") as m:
                       m.write(f"{tn}{nyc()}{do}\n")
                       print("TAWAW", count)
                       pas = ""
                       com = ""
                    if count >= hmn:
                        print(f"""EMAIL:{count}\nPASS{count}""")
        elif sdfu == "2":
            def nyc():
                 while True:
                     pas = ""
                     for me in range(num):
                       c = random.choice(chars)
                       pas += c
                     return pas
            def select_domain():
                 while True:
                     domano = ""
                     for me in range(1):
                       c = random.choice(Domain)
                       domano += c
                     return domano
            while True:
                if count < hmn:
                    count += 1
                    with open("Combo.txt", "a") as m:
                       m.write(f"{tn}{nyc()}@{select_domain()}\n")
                       print("TAWAW", count)
                       pas = ""
                       com = ""
                    if count >= hmn:
                        print(f"EMAIL:{count}")
elif mode == "3":
    re = int(input("CHAND PASSWORDT AWE:  "))
    while True:
        if re > count:
            count += 1
            thislist=""
            for ko in range(random.choice(lenlast)):
                lpass = random.choice(sim)
                thislist += lpass
            with open("pass.txt", "a") as s:
                s.write(f"\n{thislist}")          
                thislist=""
                print(f"TAWAW {count}")
                if count >= re:
                    print(f"PASS:{count}")
else:
    print("BAD")
