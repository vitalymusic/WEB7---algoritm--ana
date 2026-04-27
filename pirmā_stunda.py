# print("Hello World!!!")
# vards = input("ka tevi sauc?")
# print("Labdien, "+ vards)

#komentārs

skaitlis1 = 15 #int
skaitlis2 = 12.5 #float
bool1 = True
bool2 = False
teksts1 = "Te nāks teksts 1"
teksts2 = 'Te nāks teksts 2'

mēneši = ["Janvāris","Februāris","Marts","Aprīlis"] #saraksts (masīvs)
dzīvoklis1 = {
    "stāvs":3,
    "istabu_skaits":4,
    "platība":75,
    "saimnieks":"Jānis"
} #Vārdnīca, jeb objekts

print(mēneši[3])
print(dzīvoklis1["saimnieks"])
print(type(dzīvoklis1))
print(2+2)
print(2**3)
print(2*(3+5))
# skaitlis1 = input("Ievadi Pirmo skaitli: ")
# skaitlis2 = input("Ievadi Otru skaitli: ")
# print(float(skaitlis1)+float(skaitlis2))
# print(skaitlis1<skaitlis2)
# print(vards=="Jānis")


# print(type(skaitlis1))
skaitlis3 = 5
print(2<skaitlis3 and 3>skaitlis3) #and
print(2<skaitlis3 or 3>skaitlis3) #and
# print(not 2>skaitlis3) #and

skaitlis4 = 0
# skaitlis4 = skaitlis4+2
skaitlis4+=2
skaitlis4*=3
# skaitlis4

print(skaitlis4)
print("Janvāris" in mēneši)
