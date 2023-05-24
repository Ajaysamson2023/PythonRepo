import calendar


def calender_mod():
    month, day, year = map(int, input("Enter month,day,year:").split())
    week_days = ['MONDAY', 'TUESDAY', 'WEDNESDAY', 'THURSDAY', 'FRIDAY', 'SATURDAY', 'SUNDAY']
    day_name = calendar.weekday(year, month, day)
    print(week_days[day_name])
    return week_days[day_name]