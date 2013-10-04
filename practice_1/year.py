# -*- coding: utf-8 -*-

def main():
    year = raw_input("Enter year:")
    if year == "exit":
        return
    try:
        year = int(year)
        if (not year % 4 and year % 100) or not year % 400:
            print('Leap year')
        else:
            print('Common year')
        main()

    except Exception:
        print('Something wrong with your number')
        main()

main()
