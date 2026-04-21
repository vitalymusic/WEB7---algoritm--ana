def binara_meklesana(sakartots_saraksts, meklejamais_elements):
    sakums = 0
    beigas = len(sakartots_saraksts) - 1
    
    while sakums <= beigas:
        # Izmantojam //, lai iegūtu veselu skaitli
        vidus = (sakums + beigas) // 2
        pasreizeja_vertiba = sakartots_saraksts[vidus]
        
        if pasreizeja_vertiba == meklejamais_elements:
            return vidus
        
        if pasreizeja_vertiba > meklejamais_elements:
            beigas = vidus - 1
        else:
            sakums = vidus + 1
            
    return -1

# Pārbaude
dati = [1, 3, 5, 7, 9, 11, 13]
pozicija = binara_meklesana(dati, 7)
print(f"Skaitlis 7 atrodas indeksā: {pozicija}")
