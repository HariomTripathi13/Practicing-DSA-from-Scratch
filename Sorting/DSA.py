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
    
    print("Insertion Sort(Improved): ", arr)

#4. Quick Sort

def partition(arr, low, high):
    pivot = arr[high]
    i = low - 1

    for j in range(low, high):
        if arr[j] <= pivot:
            arr[i + 1], arr[j] = arr[j], arr[i + 1]
            i += 1
    
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1

def _q_sort(arr, low, high):
    if low < high:
        pivot_index = partition(arr, low, high)
        _q_sort(arr, low, pivot_index - 1)
        _q_sort(arr, pivot_index + 1, high)
    
def q_sort(arr, high = None):
    if high is None:
        high = len(arr) - 1
    _q_sort(arr, 0, len(arr) - 1)
    print("Quick Sort: ", arr)


#-------MAIN--------
arr = list(map(int, input().split()))
if __name__ == "__main__":

    print("SORTING IMPLEMENTATIONS\nArray: ", arr, "\n")
    #Run The functions by uncommenting them...

    #b_sort(arr)
    #b_sort_alt(arr)
    #s_sort(arr)
    #i_sort(arr)
    #i_sort_alt(arr)
    q_sort(arr)