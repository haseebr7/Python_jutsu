def is_leap_year(year):
    if year % 4 == 0: #leap         
        if year % 100 == 0: # not leap
            if year % 400 == 0: #leap
                return True
            else:
                return False
        return True
    else:
        return False


print(is_leap_year(2020))