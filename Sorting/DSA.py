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

#-------MAIN--------
arr = list(map(int, input().split()))
if __name__ == "__main__":

    print("SORTING IMPLEMENTATIONS\nArray: ", arr, "\n")
    #Run The functions by uncommenting them...

    #b_sort(arr)
    b_sort_alt(arr)