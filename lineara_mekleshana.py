def lineara_meklesana(elementu_saraksts, meklejamais_elements):
    # Ejam cauri katrai pozīcijai sarakstā
    for indekss in range(len(elementu_saraksts)):
        # Pārbaudām, vai pašreizējais elements ir tas, ko meklējam
        if elementu_saraksts[indekss] == meklejamais_elements:
            return indekss  # Atgriežam atrašanās vietu
            
    return -1  # Ja cikls beidzas un nekas nav atrasts

# Piemērs
cipari = [10, 5, 2, 8, 7]
pozicija = lineara_meklesana(cipari, 8)
print(f"Skaitlis 8 atrodas indeksā: {pozicija}")