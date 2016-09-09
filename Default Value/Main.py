def get_day(day = 'Sunday!!!'):
    if day is '1':
        day = "Monday"
    elif day is '5':
        day = "Friday"
    print(day)

get_day('1')
get_day('5')
get_day()