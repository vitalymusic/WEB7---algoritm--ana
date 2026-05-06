# 1. Kalkulators 
# Tēma: Funkcijas un zarošanās (if/elif/else).
# Uzraksti funkciju kalkulators(a, b, darbiba), kas pieņem divus skaitļus un darbību (kā tekstu: "+", "-", "*", "/").
# •	Ja tiek padota darbība, ko funkcija neatpazīst, tai jāatgriež paziņojums: "Nezināma darbība".
# •	Neaizmirsti par drošību — programmā nedrīkst pieļaut dalīšanu ar nulli!

def kalkulators(a,b,darbība):
    if darbība=="+":
        return a + b
    elif darbība=="-":
        return a - b
    elif darbība=="*":
        return a * b
    elif darbība=="/":
        if b == 0:
            return "Nedrīkst dalīt ar 0"
        return a / b
    else: 
        return "Nezināma darbība"
    
# print(kalkulators(2,6,"+"))
# print(kalkulators(2,6,"-"))
# print(kalkulators(2,6,"*"))
# print(kalkulators(2,6,"/"))
# print(kalkulators(2,0,"/"))
# print(kalkulators(2,0,":"))


# 2. Pāra skaitļu filtrs
# Tēma: Cikli (for) un zarošanās.
# Izveido funkciju atlasit_para_skaitlus(saraksts), kura saņem skaitļu sarakstu un atgriež jaunu sarakstu, kurā ir tikai pāra skaitļi.
# •	Piemērs: Ja ievada [1, 2, 3, 4, 5, 6], rezultātam jābūt [2, 4, 6].
# •	Padoms: Izmanto modulo operatoru %, lai pārbaudītu atlikumu.



def atlasit_para_skaitlus(saraksts):
    jauns_saraksts = []
    for x in saraksts:
        if x%2==0:
           jauns_saraksts.append(x)
    return jauns_saraksts


# skaitļi = []
# for x in range(10):
#     skaitļi.append(int(input("Ievadi skaitli: ")))
# print(atlasit_para_skaitlus(skaitļi))




# 3. "Mainīgs skaits" grozā (Lielveikala kase)
# Tēma: Funkcijas ar *args un cikli.
# Izmanto savas zināšanas par mainīgu argumentu skaitu! Uzraksti funkciju aprekinat_summu(*cenas), kas saskaita visas padotās preču cenas.
# •	Ja kopējā summa pārsniedz 100 EUR, piemēro 10% atlaidi.
# •	Atgriez gala summu, noapaļotu līdz 2 zīmēm aiz komata.


def aprekinat_summu(*cenas):
    summa = 0
    for x in cenas:
        summa+=x
    if summa>100:
        summa = summa-summa*0.1
    return f"Gala summa ir: {summa:.2f}"

# print(aprekinat_summu(12.5,6.55,4.50,100))


# 4. Paroļu sargs
# Tēma: Cikli, if un teksta apstrāde.
# Uzraksti funkciju parbaudit_paroli(parole), kas pārbauda, vai parole ir pietiekami droša. Droša parole atbilst šādiem kritērijiem:
# 1.	Garums ir vismaz 8 rakstzīmes.
# 2.	Tā satur vismaz vienu ciparu (izmanto ciklu, lai izietu cauri simboliem un char.isdigit()).
# 3.	Tā satur vismaz vienu speciālo simbolu, piemēram, @, # vai !.
# Funkcijai jāatgriež True vai False.

def parbaudit_paroli(parole):
    garums = len(parole)
    ir_cipars = False
    ir_specialais_simbols = False

    for simbols in parole:
        if simbols.isdigit():
           ir_cipars=True
        if simbols=="@":
            ir_specialais_simbols=True
        elif simbols=="#":
            ir_specialais_simbols=True 
        elif simbols=="!":
            ir_specialais_simbols=True

    if garums>=8 and ir_cipars and ir_specialais_simbols:
        return "Parole Droša"
    else:
        return "Parole nav droša"

print(parbaudit_paroli("Vitaly12345"))
print(parbaudit_paroli("Qwerty12345"))             
print(parbaudit_paroli("Qwerty!12345"))           



# Tēma: Viss kopā (Funkcijas, cikli, zarošanās).
# Izveido programmu, kas prasa lietotājam ievadīt skaitļus vienu pēc otra.
# •	Ja lietotājs ievada "stop", cikls apstājas.
# •	Pēc tam programma izsauc funkciju, kas aprēķina vidējo aritmētisko no visiem ievadītajiem skaitļiem.
# •	Vidējā aritmētiskā formula:
# •	Izvadi rezultātu un paziņojumu: "Liels vidējais", ja tas ir virs 50, vai "Mazs vidējais", ja zem

def vidējais(skaitļi):
    summa = 0
    for x in skaitļi:
        summa+=x
    vidējais =  summa / len(skaitļi)
    if vidējais >50:
        return f"Rezultāts ir: {vidējais} Liels vidējais"
    else: return f"Rezultāts ir: {vidējais} Mazs vidējais"

atbilde = ""
skaitļi = []
while atbilde!="stop":
    atbilde = input("Ievadi skaitļi: ")
    if atbilde != "stop":
        skaitļi.append(int(atbilde))

print(vidējais(skaitļi))

    







