
input_date = input("Enter a date like <yyyy-mm-ss>...")
add_day = int(input("Enter number of days that you want increment the date..."))

input_date = input_date.split("-")
year = int(input_date[0])
month = int(input_date[1])
day = int(input_date[2])

dayInMonth = [31,31,31,31,31,31,30,30,30,30,30,29]
max_possible = dayInMonth[month-1]

x_diff_day = lambda days,add_day, max_possible: ((days+add_day) % max_possible)
x_diff_month = lambda days,add_day,max_possible, month : (((days+add_day) // max_possible ) + month )

def increment_day(year,month,day,add_day,max_possible):
    month = x_diff_month(day,add_day,max_possible,month)
    day = x_diff_day(day,add_day,max_possible)
    if month > 12:
        year += month // 12
        month = month % 12

    message = "your date + {} --> < {}/{}/{}"
    print(message.format(add_day,year,month,day))                  

increment_day(year,month,day,add_day,max_possible)