def milia(arabnum):
    global mil
    if (arabnum // 1000) == 0:
        mil = 0
    elif (arabnum // 1000) == 1:
        mil = 1
    elif (arabnum // 1000) == 2:
        mil = 2
    elif (arabnum // 1000) == 3:
        mil = 3
    return(mil)

def centum(arabnum):
    global mil
    global cent
    if (arabnum > 99):
        cent = 0
    if (mil == 0):
        cent = (arabnum / 100)
    elif (mil == 1):
        cent = ((arabnum - 1000) / 100)
    elif (mil == 2):
        cent = ((arabnum - 2000) / 100)
    elif (mil == 3):
        cent = ((arabnum - 3000) / 100)
    return(cent)
    
def decem(arabnum):
    global mil
    global cent
    global dec
    if (mil == 0):
        dec = (arabnum - cent * 100
    elif (mil == 1):
        dec = ((arabnum - 1000) - cent * 100
    elif (mil == 2):
        dec = ((arabnum - 2000) - cent * 100
    elif (mil == 3):
        dec = ((arabnum - 3000) - cent * 100
    return(dec)

def pre(arabnum):
    global pres
    if ((arabnum // 5) < 1):
        pres = 1
    elif ((arabnum // 5) >= 1) and ((arabnum // 10) < 1):
        pres = 2
    elif ((arabnum // 10) >= 1) and ((arabnum // 40) < 1):
        pres = 3
    elif ((arabnum // 40) >= 1) and ((arabnum // 50) < 1):
        pres = 4
    elif ((arabnum // 50) >= 1) and ((arabnum // 90) < 1):
        pres = 5
    elif ((arabnum // 90) >= 1) and ((arabnum // 100) < 1):
        pres = 6
    elif ((arabnum // 100) >= 1) and ((arabnum // 400) < 1):
        pres = 7
    elif ((arabnum // 400) >= 1) and ((arabnum // 500) < 1):
        pres = 8
    elif ((arabnum // 500) >= 1) and ((arabnum // 600) < 1):
        pres = 9
    elif ((arabnum // 600) >= 1) and ((arabnum // 900) < 1):
        pres = 10
    elif ((arabnum // 900) >= 1) and ((arabnum // 1000) < 1):
        pres = 11
    elif ((arabnum // 1000) >= 1):
        pres = 12

    else:
        print('nope')
    return(pres)

def romannum(arabnum):
    global pres
    global result
    if (pres == 1):
        if (1 <= arabnum <= 3):
            result = 'I'*arabnum
        elif (arabnum == 4):
            result = 'IV'
    elif (pres == 2):
        if (5 <= arabnum <= 8):
            result = 'V' + 'I' * (-(5 - arabnum))
        elif (arabnum == 9):
            result = 'IX'
    elif (pres == 3):
        if (0 <= (arabnum % 10) <= 3):
            result = 'X' * (arabnum // 10) + 'I' * (-(0 - (arabnum % 10)))
        elif ((arabnum % 10) == 4):
            result = 'X' * (arabnum // 10) + 'IV'
        elif (5 <= (arabnum % 10) <= 8):
            result = 'X' * (arabnum // 10) + 'V' + 'I' * (-(5 - (arabnum % 10)))
    elif (pres == 4):
        if (0 <= (arabnum % 10) <= 3):
            result = 'XL' + 'I' * (-(0 - (arabnum % 10)))
        elif ((arabnum % 10) == 4):
            result = 'XL' + 'IV'
        elif (5 <= (arabnum % 10) <= 8):
            result = 'XL' + 'V' + 'I' * (-(5 - (arabnum % 10)))

    else:
        print('nope1')
    return(result)

arabnum = int(input('Введите число '))
result = 'a'
pres = 0
mil = x
cent = y
dec = z
if (0 < arabnum < 4000):
    thou(arabnum)
    dec(arabnum)
    romannum(arabnum)
    print(result)
    print(pres)
else:
    print('Out of conditions')
