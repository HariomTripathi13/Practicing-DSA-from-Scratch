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

#4. Fibonacci Series

def fib_loop(a,b,rng):
    print("Fibonacci Series with Loop: ")
    for fibo in range(rng):
        print(a, end = " ")
        newfibo = a + b
        a = b
        b = newfibo

def fib_alt(a, b, rng):
    print("Fibonacci Series with Reccursion: ")
    count = 1
    def fib_rec(a, b, rng, count):
        if count <= rng:
            print(a, end = " ")
            newfibo = a + b
            a = b
            b = newfibo
            count += 1
            fib_rec(a, b, rng, count)
        else:
            return
    
    fib_rec(a, b, rng, count)


#-------MAIN--------
Mnum = int(input())
a = int(input())
b = int(input())
rng = int(input())
if __name__ == "__main__":

    print("Basic Math Implementations\n")
    #Run The functions by uncommenting them...

    #countDigit(Mnum)
    #reverseNum(Mnum)
    #calc_hcf(a, b)
    
    #fib_loop(a,b,rng)
    #fib_alt(a, b, rng)