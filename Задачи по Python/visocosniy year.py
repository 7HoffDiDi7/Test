def is_year_leap(year):
    if year % 400 == 0:
        return (True)
    if year % 100 == 0:
        return (False)
    if year % 4 == 0:
        return (True)
    else:
        return(False)
    
print("Программа определяет был ли введеный вами год, или будет високосным.\n")

YEAR = is_year_leap(int(input("Введите год: ")))
print("Если программа выводит 'True', то год был високосным, а если 'False', то нет.")
print(YEAR)