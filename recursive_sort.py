def merge_sort_recursive(arr):
    if len(arr) <= 1:
        return arr, 0, 0, 1
    mid = len(arr) // 2
    left_half, c1, a1, r1 = merge_sort_recursive(arr[:mid])
    right_half, c2, a2, r2 = merge_sort_recursive(arr[mid:])
    merged, c_merge, a_merge = merge(left_half, right_half)
    return merged, c1 + c2 + c_merge, a1 + a2 + a_merge, r1 + r2 + 1

def merge(left, right):
    merged = []
    i = j = 0
    comparisons = 0
    assignments = 0
    while i < len(left) and j < len(right):
        comparisons += 1
        if left[i] <= right[j]:
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            j += 1
        assignments += 1
    while i < len(left):
        merged.append(left[i])
        i += 1
        assignments += 1
    while j < len(right):
        merged.append(right[j])
        j += 1
        assignments += 1
    return merged, comparisons, assignments

# Приклад використання
my_list = [10, 90, 95, 30, 45, 60, 57, 28, 5]
print("Оригінальний список:", my_list)
sorted_list, comps, assigs, rec_calls = merge_sort_recursive(my_list)
print("Відсортований список:", sorted_list)
print(f"Загальна кількість порівнянь: {comps}")
print(f"Загальна кількість присвоювань: {assigs}")
print(f"Загальна кількість рекурсивних викликів: {rec_calls}")
