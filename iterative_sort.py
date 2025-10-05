def merge_sort_iterative(a):
    n = len(a)
    comparisons = 0
    assignments = 0
    i = 1
    while i < n:
        j = 0
        while j < n - i:
            left = j
            mid = j + i
            right = min(j + 2 * i, n)
            c, a_count = merge(a, left, mid, right)
            comparisons += c
            assignments += a_count
            j += 2 * i
        i *= 2
    return a, comparisons, assignments

def merge(a, left, mid, right):
    comparisons = 0
    assignments = 0
    L = a[left:mid]
    R = a[mid:right]
    assignments += len(L) + len(R)
    i = 0
    j = 0
    k = left
    while i < len(L) and j < len(R):
        comparisons += 1
        if L[i] < R[j]:
            a[k] = L[i]
            i += 1
        else:
            a[k] = R[j]
            j += 1
        k += 1
        assignments += 1
    while i < len(L):
        a[k] = L[i]
        i += 1
        k += 1
        assignments += 1
    while j < len(R):
        a[k] = R[j]
        j += 1
        k += 1
        assignments += 1
    return comparisons, assignments

# Приклад використання
my_list = [10, 90, 95, 30, 45, 60, 57, 28, 5]
print("Оригінальний список:", my_list)
sorted_list, comps, assigs = merge_sort_iterative(my_list.copy())
print("Відсортований список:", sorted_list)
print(f"Кількість порівнянь: {comps}")
print(f"Кількість присвоювань: {assigs}")
