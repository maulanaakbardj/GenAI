import calendar

def generate_calendar(year):
    # Creates a calendar for a given year
    cal = calendar.Calendar()
    cal.setfirstweekday(calendar.SUNDAY)
    months = cal.yeardatescalendar(year, width=3)

    # Display month name and date in calendar format
    for year_month in months:
        for month_weeks in year_month:
            month_name = calendar.month_name[month_weeks[0].month]
            print(f"\n{month_name} {year}")
            print("Su Mo Tu We Th Fr Sa")
            for week in month_weeks:
                for day in week:
                    if day.month == month_weeks[0].month:
                        print(f"{day.day:2d}", end=" ")
                    else:
                        print("  ", end=" ")
                print()

if __name__ == "__main__":
    generate_calendar(2023)
