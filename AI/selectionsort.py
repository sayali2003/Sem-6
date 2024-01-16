def selectionSort(arr):
    for i in range(len(arr)):
        for j in range(i + 1, len(arr)):
            if arr[i] > arr[j]:
                arr[i], arr[j] = arr[j], arr[i]
    return arr

n = int(input("Enter number of entries: "))  # Added a missing closing parenthesis
s = []

for i in range(n):
    x = int(input("Enter number: "))  # Added a missing closing parenthesis
    s.append(x)

print("Original array:", s)
print("Sorted array:", selectionSort(s))

