import sys

def main():
    year = int(sys.argv[1])
    month = int(sys.argv[2])
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