#TO RUN USE CTRL+SHIFT+B ONLY
#----------------------------
# PYTHON OUTPUT
"""
print("Hello! Hariom.")
x = 5
y = 10
print(x, "+", y, "=", x + y)
"""

#-1----------------------------
def question1(y):
    print('\n'"Question 1")
    for i in range(y, 0, -1):
        print("*"*i)

#-2-----------------------------
def question2(x, y):
    print('\n'"Question 2")
    while x<= y:
        print("*"*x)
        x += 1

#-3-----------------------------
def question3(y):
    print('\n'"Question 3")
    third_string = ""  # Start empty

    for i in range(1, y + 1):
        third_string += str(i) # Just add the new number to the end
        print(third_string)

#-4-----------------------------
def question4(y):
    print('\n'"Question 4")
    fourth_string = ""

    for i in range(y, 0, -1):
        fourth_string += str(i)

    for i in range(y):
        print(fourth_string[i:])

#-5------------------------------
def question5(y):
    print('\n'"Question 5")

    for i in range(1, y+1):
        print(i*str(i))

#-6------------------------------
def question6(y):
    print('\n'"Question 6")

    for i in range(y, 0, -1):
        print(i*str(i))

#-7-------------------------------
def question7(y):
    print('\n'"Question 7")
    seventh_string = ""

    for i in range(1, y+1):
        seventh_string += str(i)

    for k in range(1, y + 1):
        print(seventh_string[:k])

#-8-------------------------------
def question8(y):
    print('\n'"Question 8")

    for i in range(y):
        spaces = " " * (y-1-i)
        stars = "*" * (2*i+1)
        print(spaces+stars)

#-9-------------------------------
def question9(y):
    print('\n'"Question 9")

    for i in range(y):
        spaces = " " * i
        stars = "*" * (2*(y-i)-1)
        print(spaces+stars)

#-10------------------------------
def question10(y):
    print('\n'"Question 10")

    for i in range(y-1):
        space1 = " " * (y-i-1)
        stars1 = "*" * (2*i+1)
        print(space1+stars1)

    for i in range(y):
        space2 = " " * i
        stars2 = "*" * (2*(y-i)-1)
        print(space2+stars2)

#-11------------------------------
def question11(y):
    print('\n'"Question 11")

    for i in range(1, y+1):
        eleventh = "*" * i
        print(eleventh)
    for i in range(y-1):
        eleventh = "*" * y
        print(eleventh[i+1:])

#-12------------------------------
def question12(y):
    print('\n'"Question 12")

    for i in range(y):
        twelveth = "*" * y
        print(twelveth[i:])
    for i in range(2, y+1):
        twelveth = "*" * i
        print(twelveth)

#-13-------------------------------
def question13(y):
    print('\n'"Questioin 13")
    print('\n''--The String Slicing Way--')
    thirteen = []
    for i in range(2*y):
        if i % 2 == 0:
            thirteen.append(1)
        else:
            thirteen.append(0)
    print(thirteen)

    for i in range(y):
        row = thirteen[i:i+i+1]
        print(*row)

    print('\n''--The Mathematicall Way--')

    for i in range(y):
        for j in range(i + 1):
            print((i + j + 1) % 2, end = " ")
            #if (i+j) % 2 == 0:
            #    print(1, end = " ")
            #else:
            #    print(0, end = " ")
        print()

#-14------------------------------------
def question14(y):
    print('\n'"Question 14")

    for i in range(1, y + 1):
        for j in range(1, i + 1):
            string1 = j
            print(str(string1), end = " ")
        space = " " * (2 * (y - i))
        print(2*space, end = " ")
        for k in range(i, 0, -1):
            print(k, end = " ")
        print()

def question15(y):
    print('\n'"Question 15")

    k = 1
    for i in range(1, y+1):
        for j in range(i):
            print(k, end =" ")
            k += 1
        print()

def numTochr(num):
    return chr(num + 65)

def question16(y):
    print('\n' "Question 16")
    for i in range(1, y + 1):
        for j in range(i):
            print(numTochr(j), end = " ")
        print()

def question17(y):
    print('\n' "Question 17")

    for i in range(y):
        for j in range(y - i):
            print(numTochr(j), end = " ")
        print()

def question18(y):
    print('\n' "Question 18")

    for i in range(y):
        for j in range(i + 1):
            print(numTochr(i) , end = " ")
        print()

def question19(y):
    print('\n' "Question 19")

    for i in range(y - 1):
        for j in range(y - i - 1):
            print(" ", end = " ")
    
        for k in range(i):
            print(numTochr(k) , end = " ")
    
        for l in range(i, -1, -1):
            print(numTochr(l) , end = " ")

        for m in range(y - i - 1):
            print(" " , end = " ")

        print()

def question20(y):
    print('\n' "Question 20")

    twenty = y - 1

    for i in range(y):
        for j in range(i + 1):
            print(numTochr(j + twenty), end = " ")
        twenty = twenty - 1
        print()

def question21(y):
    print('\n' "Question 21")

    for i in range(y):
        for j in range(y - i):
            print("*", end = " ")

        for k in range(i * 2):
            print(" ", end = " ")

        for m in range(y - 1 - i, -1, -1):
            print("*", end = " ")
        print()

    for n in range(y):
        for o in range(n + 1):
            print("*", end = " ")
    
        for p in range((y - n - 1) * 2):
            print(" ", end = " ")

        for q in range(n + 1):
            print("*", end = " ")
        print()

def question22(y):
    print('\n' "Question 22")

    for i in range(2*y - 1):
        for j in range(2*y - 1):
            row = min(i, 2*y-2-i)
            col = min(j, 2*y-2-j)
            ans = min(row, col)
            ans = min(row, col)
            print(y - ans, end = " ")
        print()

if __name__ == "__main__":
    try:
        print("Pattern Problem")
        x = int(input())
        y = int(input())
        #x = 1
        #y = 5

        #2. Call the Question function here by uncommenting
        #question1(y)
        #question2(x, y)
        #question3(y)
        #question4(y)
        #question5(y)
        #question6(y)
        #question7(y)
        #question8(y)
        #question9(y)
        #question10(y)
        #question11(y)
        #question12(y)
        #question13(y)
        #question14(y)
        #question15(y)
        #question16(y)
        #question17(y)
        #question18(y)
        #question19(y)
        #question20(y)
        #question21(y)
        #question22(y)

    except EOFError:
        print("Error detected...Review everything.")