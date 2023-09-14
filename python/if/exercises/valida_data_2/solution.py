from bissexto import eh_bissexto
def valida_data(d, m, a):
    ano = eh_bissexto(a)
    if ano == True:
        if m == 1:
            if 1 <= d <= 31:
                return True
        if m == 2:
            if 1 <= d <= 30:
                return True
        if m == 3:
            if 1 <= d <= 31:
                return True
        if m == 4:
            if 1 <= d <= 30:
                return True
        if m == 5:
            if 1 <= d <= 31:
                return True
        if m == 6:
            if 1 <= d <= 30:
                return True
        if m == 7:
            if 1 <= d <= 31:
                return True
        if m == 8:
            if 1 <= d <= 31:
                return True
        if m == 9:
            if 1 <= d <= 30:
                return True
        if m == 10:
            if 1 <= d <= 31:
                return True
        if m == 11:
            if 1 <= d <= 30:
                return True
        if m == 12:
            if 1 <= d <= 31:
                return True
        else:
            return False
                
    else:
        if m == 1:
            if 1 <= d <= 31:
                return True
        if m == 2:
            if 1 <= d <= 28:
                return True
        if m == 3:
            if 1 <= d <= 31:
                return True
        if m == 4:
            if 1 <= d <= 30:
                return True
        if m == 5:
            if 1 <= d <= 31:
                return True
        if m == 6:
            if 1 <= d <= 30:
                return True
        if m == 7:
            if 1 <= d <= 31:
                return True
        if m == 8:
            if 1 <= d <= 31:
                return True
        if m == 9:
            if 1 <= d <= 30:
                return True
        if m == 10:
            if 1 <= d <= 31:
                return True
        if m == 11:
            if 1 <= d <= 30:
                return True
        if m == 12:
            if 1 <= d <= 31:
                return True
        else:
            return False