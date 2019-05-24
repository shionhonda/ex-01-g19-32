import sys

def is_int(s):
    try: 
        int(s)
        return True
    except ValueError:
        return False

def main():
    usage = 'illigal inputs; usage: python leapmonth.py year month'

    if len(sys.argv) != 3:
        print(usage)
        return
    

    year = sys.argv[1]
    month = sys.argv[2]

    if not (is_int(year) and is_int(month)):
        print(usage)
        return
    else:
        year = int(year)
        month = int(month)

    
    if year < 0 or year > 3000 or month < 1 or month > 12:
        print(usage)
        return
    if month == 2:
        if year % 4 == 0 and year % 100 != 0 or year % 400 == 0 :
            days = 29
        else:
            days = 28
    else:
        if month in (1,3,5,7,8,10,12):
            days = 31
        else:
            days = 30

    print("Month of ", month, "/", year, " has ", days, " days.", sep="")

if __name__ == '__main__':
    main()
