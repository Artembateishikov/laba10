# первое решение
def merge_sorted(a, b):
    return sorted(a+b)

print(merge_sorted([1, 3], [2, 4]))
print(merge_sorted([], [1, 2]))
print(merge_sorted([1, 1], [1]))

# второе решение
def merge_sorted(a,b):
    result = []
    i = 0
    j = 0

    while i < len(a) and j < len(b):
        if a[i] < b[j]:
            result.append(a[i])
            i += 1
        else:
            result.append(b[j])
            j += 1

    result += a[i:]
    result += b[j:]

    return result
