# summa = 0
# for x in range(5):
#     summa += float(input("Ievadi skaitli: "))
# print(f"Jūsu ievadīto skautļu summa ir: {summa}!")

# for x in range(1,101):
#     if x%2 ==0:
#         print(x)

# skaitlis = 0
# while skaitlis<=100:
#     if skaitlis%2 ==0:
#         print(skaitlis)
#     skaitlis +=1   


# vards = ""
# while len(vards)<=3:
#     vards = input("Ievadi savu vārdu: ")

sk1=40
sk2=67

def saskaitišana():
   return sk1+sk2
sk1=0
def reizināšana():
   return sk1*sk2
# print(sk1,sk2)
print(saskaitišana())
print(reizināšana())


def laika_prognoze(temperatūra,mitrums,nokrišņi):
   if temperatūra>15 and mitrums<40 and nokrišņi==False:
      print(f"Ārā ir ļoti silts un saulains laiks!")
   elif temperatūra>15 and mitrums<40 and nokrišņi==True:
      print(f"Ārā ir ļoti silts, bet ir lietus. Paņem lietussargu")
   elif temperatūra>5 and temperatūra<14 and mitrums>=30 and nokrišņi==False:
      print(f"Ārā ir auksti, bez nokrišņiem.")
   elif temperatūra>-4 and temperatūra<2 and mitrums>=40 and nokrišņi==True:
      print(f"Ārā ir auksti, un iet sniegs")
   else: print(f"Jūsu datiem neatbilst neviens nosacījums")

# Palūgt lietotājam ievadīt 3 vērtības un pēc tam programma atbild par gaidāmo laiku 


laika_prognoze(
   int(input("Ievadiet temperatūru: ")),
   int(input("Ievadiet mitrumu: ")),
   True if input("Ievadiet nokrišņus (jā/nē): ")=="jā" else False
)