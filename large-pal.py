def gen_pal(input, midDig = None):
    #returns next highest palindromic number
    numString = str(input)
    palString = str()
    if midDig == None:
        palString = numString + numString[2] + numString[1] + numString[0]
    else:
        palString = numString + str(midDig) + numString[1] + numString[0]

    return int(palString)

def test_div(input):
    #returns True if two 3-digit divisors can be found
    print("testing", input)
    for i in range(100, 1000, 1):
        if (input / i) < 100 or (input/i) > 999:
            continue
        elif ((input % i) == 0):
            print(input/i, "and", i, "make a palindromic number")
            return True
    return False

def findLargePal():
    #returns the first number returned by gen_pal() returns True for test_div
    for i in range(999, 99, -1):
        if test_div(gen_pal(i)) == True:
            return gen_pal(i)
    for j in range(99, 9, -1):
        print("testing five digit numbers")
        for k in range(9, -1, -1):
            if test_div(gen_pal(j,k)) == True:
                return gen_pal(j,k)

            #if test_div(i) == True:
            #    return i

print(findLargePal(), "is the largest palindromic number that is a product of two 3-digit integers")
