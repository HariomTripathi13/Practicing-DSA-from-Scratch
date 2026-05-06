#TO RUN USE CTRL+SHIFT+B ONLY
#----------------------------
# PYTHON OUTPUT

#1. Bubble Sort
def b_sort(arr):
    n = len(arr)
    for i in range(n - 1):
        for j in range(n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    
    print("Bubble Sort: ", arr)

# Improved Bubble Sort------------

def b_sort_alt(arr):
    n = len(arr)
    for i in range(n - 1):
        swaped = False
        for j in range(n - 1 - i):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swaped = True
        if not swaped:
            break
    
    print("Bubble Sort(Improved): ", arr)

#2. Selection Sort
def s_sort(arr):
    n = len(arr)
    for i in range(n - 1):
        min_index = i
        for j in range(i + 1, n):
            if arr[min_index] > arr[j]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]
    print("Selection Sort: ", arr)

#3. Insertion Sort
def i_sort(arr):
    n = len(arr)
    for i in range(1, n):
        insert_index = i
        current_val = arr.pop(i)
        for j in range(i - 1, -1, -1):
            if arr[j] > current_val:
                insert_index = j
        arr.insert(insert_index, current_val)
    
    print("Insertion Sort: ", arr)

# Insertion Sort Improvement-------

def i_sort_alt(arr):
    n = len(arr)
    for i in range(1, n):
        # Pocketing the current value
        current_val = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > current_val:
            # Shifting the value
            arr[j + 1] = arr[j]
            j -= 1
            
        # Assigning the current value
        arr[j + 1] = current_val
    
    print("Insertion Sort: ", arr)

#-------MAIN--------
arr = list(map(int, input().split()))
if __name__ == "__main__":

    print("SORTING IMPLEMENTATIONS\nArray: ", arr, "\n")
    #Run The functions by uncommenting them...

    #b_sort(arr)
    #b_sort_alt(arr)
    #s_sort(arr)
    #i_sort(arr)
    i_sort_alt(arr)