def milia(arabnum):
    global mil

    mil = (arabnum // 1000)
    return(mil)

def centum(arabnum):
    global mil
    global cent

    if (mil == 0):
        cent = (arabnum // 100)
    elif (mil == 1):
        cent = ((arabnum - 1000) // 100)
    elif (mil == 2):
        cent = ((arabnum - 2000) // 100)
    elif (mil == 3):
        cent = ((arabnum - 3000) // 100)
    return(cent)

def decem(arabnum):
    global mil
    global cent
    global dec

    if (mil == 0):
        dec = ((arabnum - cent * 100) // 10)
    elif (mil == 1):
        dec = (((arabnum - 1000) - cent * 100) // 10)
    elif (mil == 2):
        dec = (((arabnum - 2000) - cent * 100) // 10)
    elif (mil == 3):
        dec = (((arabnum - 3000) - cent * 100) // 10)
    return(dec)

def romannumDec(arabnum):
    global mil
    global cent
    global dec
    global resultDec

    if (dec == 0) and (dec != 10):
        if (0 <= (arabnum - mil * 1000 - cent * 100 - dec * 10) <= 3):
            resultDec = 'I' * (arabnum - mil * 1000 - cent * 100 - dec * 10)
        elif ((arabnum - mil * 1000 - cent * 100 - dec * 10) == 4):
            resultDec = 'IV'
        elif (5 <= (arabnum - mil * 1000 - cent * 100 - dec * 10) <= 8):
            resultDec = 'V' + 'I' * (-(5 - (arabnum - mil * 1000 - cent * 100 - dec * 10)))
        elif ((arabnum - mil * 1000 - cent * 100 - dec * 10) == 9):
            resultDec = 'IX'
    elif (dec in (1, 2, 3)):
        if (0 <= (arabnum - mil * 1000 - cent * 100 - dec * 10) <= 3):
            resultDec = 'X' * dec + 'I' * (-(0 - (arabnum - mil * 1000 - cent * 100 - dec * 10)))
        elif ((arabnum - mil * 1000 - cent * 100 - dec * 10) == 4):
            resultDec = 'X' * dec + 'IV'
        elif (5 <= (arabnum - mil * 1000 - cent * 100 - dec * 10) <= 8):
            resultDec = 'X' * dec + 'V' + 'I' * (-(5 - (arabnum - mil * 1000 - cent * 100 - dec * 10)))
        elif ((arabnum - mil * 1000 - cent * 100 - dec * 10) == 9):
            resultDec = 'X' * dec + 'IX'
    elif (dec == 4):
        if (0 <= (arabnum - mil * 1000 - cent * 100 - dec * 10) <= 3):
            resultDec = 'XL' + 'I' * (-(0 - (arabnum - mil * 1000 - cent * 100 - dec * 10)))
        elif ((arabnum - mil * 1000 - cent * 100 - dec * 10) == 4):
            resultDec = 'XL' + 'IV'
        elif (5 <= (arabnum - mil * 1000 - cent * 100 - dec * 10) <= 8):
            resultDec = 'XL' + 'V' + 'I' * (-(5 - (arabnum - mil * 1000 - cent * 100 - dec * 10)))
        elif ((arabnum - mil * 1000 - cent * 100 - dec * 10) == 9):
            resultDec = 'XL' + 'IX'
    elif (dec in (5, 6, 7, 8)):
        if (0 <= (arabnum - mil * 1000 - cent * 100 - dec * 10) <= 3):
            resultDec = 'L' + 'X' * (dec - 5) + 'I' * (-(0 - (arabnum - mil * 1000 - cent * 100 - dec * 10)))
        elif ((arabnum - mil * 1000 - cent * 100 - dec * 10) == 4):
            resultDec = 'L' + 'X' * (dec - 5) + 'IV'
        elif (5 <= (arabnum - mil * 1000 - cent * 100 - dec * 10) <= 8):
            resultDec = 'L' + 'X' * (dec - 5) + 'V' + 'I' * (-(5 - (arabnum - mil * 1000 - cent * 100 - dec * 10)))
        elif ((arabnum - mil * 1000 - cent * 100 - dec * 10) == 9):
            resultDec = 'L' + 'X' * (dec - 5) + 'IX'
    elif (dec == 9):
        if (0 <= (arabnum - mil * 1000 - cent * 100 - dec * 10) <= 3):
            resultDec = 'XC' + 'I' * (-(0 - (arabnum - mil * 1000 - cent * 100 - dec * 10)))
        elif ((arabnum - mil * 1000 - cent * 100 - dec * 10) == 4):
            resultDec = 'XC' + 'IV'
        elif (5 <= (arabnum - mil * 1000 - cent * 100 - dec * 10) <= 8):
            resultDec = 'XC' + 'V' + 'I' * (-(5 - (arabnum - mil * 1000 - cent * 100 - dec * 10)))
        elif ((arabnum - mil * 1000 - cent * 100 - dec * 10) == 9):
            resultDec = 'XC' + 'IX'
    elif (dec == 10):
        resultDec = ''
    return(resultDec)

def romannumCent(arabnum):
    global mil
    global cent
    global dec
    global resultDec
    global resultCent

    if (cent == 0):
        resultCent = resultDec
    elif (cent in (1, 2, 3)):
        resultCent = 'C' * cent + resultDec
    elif (cent == 4):
        resultCent = 'CD' + resultDec
    elif (cent == 5):
        resultCent = 'D' + resultDec
    elif (cent in (6, 7, 8)):
        resultCent = 'D'+'C' * (cent - 5) + resultDec
    elif (cent == 9):
        resultCent = 'CM' + resultDec
    elif (cent == 10):
        resultCent = ''
    return(resultCent)

def romannumMil(arabnum):
    global mil
    global cent
    global dec
    global resultDec
    global resultCent
    global resultMil

    resultMil = 'M' * mil + resultCent

    return(resultMil)

arabnum = int(input('Введите число '))
#result = 'a'
#mil = 'x'
#cent = 'y'
#dec = 'z'
if (0 < arabnum < 4000):
    milia(arabnum)
    centum(arabnum)
    decem(arabnum)
    romannumDec(arabnum)
    romannumCent(arabnum)
    romannumMil(arabnum)
    print(resultMil)
    print('3999 = MMMCMXCIX')
    print(resultDec)
else:
    print('Out of conditions')
