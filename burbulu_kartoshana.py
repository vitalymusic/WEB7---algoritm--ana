def bubble_sort(saraksts):
    n = len(saraksts)
    # Ejam cauri visiem saraksta elementiem
    for i in range(n):
        # Pēdējie i elementi jau ir savās vietās
        for j in range(0, n - i - 1):
            # Ja tekošais elements ir lielāks par nākamo, mainām tos vietām
            if saraksts[j] > saraksts[j + 1]:
                saraksts[j], saraksts[j + 1] = saraksts[j + 1], saraksts[j]
    return saraksts

skaitli = [64, 34, 25, 12, 22, 11, 90]
print(f"Bubble Sort: {bubble_sort(skaitli)}")