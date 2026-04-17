#TO RUN USE CTRL+SHIFT+B ONLY
#----------------------------
# PYTHON OUTPUT

#1. Count Digits in a Number

def countDigit(Mnum):
    print("1. Count Digits in a Number"'\n')
    temp_num = Mnum

    one = len(str(temp_num))

    count = 0
    while temp_num > 0:
        temp_num = temp_num // 10
        count += 1

    print(f"Digit: {Mnum}\nCount: {one}")

    print("\n"'Alternate Method'"\n")
    print(f"Digit: {Mnum}\nCount: {count}")

#2. Reversing a Number

def reverseNum(Mnum):
    print("2. Reverse a Number")
    ans = 0
    temp_num = Mnum
    while temp_num > 0:
        ans = ans * 10 + (temp_num % 10)
        temp_num = temp_num // 10
    print(f"Digit: {Mnum}\nReverse: {ans}")

    print("Palindrome Detected." if Mnum == ans else "Palindrome Not Detected.")

#3. Calculating HCF

def calc_hcf(a,b):
    print("3. Finding HCF of a Number")
    dividend = max(a,b)
    divisor = min(a,b)
    rem = 0
    while dividend % divisor != 0:
        rem = dividend % divisor
        dividend = divisor
        divisor = rem
    print(f"HCF of {a,b} is {divisor}")

#print("\n4. Armstrong Number\n")


#-------MAIN--------
Mnum = int(input())
a = int(input())
b = int(input())
if __name__ == "__main__":

    print("Basic Math Implementations\n")
    #Run The functions by uncommenting them...

    #countDigit(Mnum)
    #reverseNum(Mnum)
    #calc_hcf(a, b)