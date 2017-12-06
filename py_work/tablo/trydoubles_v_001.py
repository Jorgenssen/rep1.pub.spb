def dubles():
    k = 0
    d = 0
    
    while d <= 4:
        if input('doublehit '):
            d += 1
            k += 1
        else:
            k -= 1   
        if d == 4:
            print('Go home, bastards!')
            break
        elif d != 4 and k == 3:
            print('Hey, whaaaaat the fuck?!')
            break
                
dubles()
