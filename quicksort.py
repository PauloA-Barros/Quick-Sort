def quicksort(arr):
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[len(arr) // 2]  # Escolhe o elemento do meio como pivô
        left = [x for x in arr if x < pivot]  # Elementos menores que o pivô
        middle = [x for x in arr if x == pivot]  # Elementos iguais ao pivô
        right = [x for x in arr if x > pivot]  # Elementos maiores que o pivô
        return quicksort(left) + middle + quicksort(right) # Aplica o método
        # recursivamente as sublistas left e right

# Exemplo de uso
L = [15, 48, 84, 89, 2, 60, 10, 42, 17, 13]
sorted_L = quicksort(L)
print(sorted_L)