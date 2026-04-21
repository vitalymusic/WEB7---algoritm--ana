def insertion_sort(saraksts):
    for i in range(1, len(saraksts)):
        atslega = saraksts[i]
        j = i - 1
        # Pārvietojam elementus, kas ir lielāki par atslēgu, par vienu pozīciju uz priekšu
        while j >= 0 and atslega < saraksts[j]:
            saraksts[j + 1] = saraksts[j]
            j -= 1
        saraksts[j + 1] = atslega
    return saraksts

skaitli = [12, 11, 13, 5, 6]
print(f"Insertion Sort: {insertion_sort(skaitli)}")
