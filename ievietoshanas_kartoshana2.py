# Ievietosanas kārtošana (INSERTION SORT)
import time
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


skaitli2 = [5, 12, 78, 3, 89, 23, 67, 1, 90, 34,
56, 2, 99, 17, 28, 65, 41, 8, 73, 19,
84, 6, 92, 31, 57, 14, 76, 25, 38, 60,
5, 88, 21, 49, 70, 11, 95, 33, 62, 27,
80, 4, 69, 15, 52, 36, 97, 18, 74, 29,
63, 9, 82, 24, 55, 40, 93, 7, 68, 20,
86, 13, 71, 30, 58, 43, 98, 16, 77, 26,
61, 10, 83, 22, 54, 39, 91, 35, 66, 44,
87, 32, 72, 47, 59, 42, 96, 37, 64, 50,
79, 46, 85, 48, 53, 51, 94, 81, 75, 100, -5]
start = time.perf_counter()
print(f"Insertion Sort: {insertion_sort(skaitli2)}")
end =time.perf_counter()
print(f"izpildes laiks: {end-start:.6f} sekundes")