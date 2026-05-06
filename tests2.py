def funkcija1(*dati):

    vidējais  = sum(dati) / len(dati)
    return vidējais

print(f"{funkcija1(1,2,3,4,5,6,7,6,5,4,3,2,1,2,3,4,5,6,5,54,4):.2f}")

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
