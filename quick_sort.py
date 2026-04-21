def quick_sort(saraksts):
    if len(saraksts) <= 1:
        return saraksts
    
    balsts = saraksts[len(saraksts) // 2] # Izvēlamies vidējo elementu
    kreisa_puse = [x for x in saraksts if x < balsts]
    vidus = [x for x in saraksts if x == balsts]
    laba_puse = [x for x in saraksts if x > balsts]
    
    # Rekursīvi kārtojam abas puses un savienojam
    return quick_sort(kreisa_puse) + vidus + quick_sort(laba_puse)

skaitli = [10, 7, 8, 9, 1, 5]
print(f"Quick Sort: {quick_sort(skaitli)}")
