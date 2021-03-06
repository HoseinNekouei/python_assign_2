#This function check the entered date pattern
def check_count(value,symbol,start,end,check_param):
    if value.count(symbol,start,end)==check_param:
        return True
    else:
        error_message="The entered date pattern is incorrect."
        print(error_message)

#This function check len and validity of year
def check_year(str_year):
    if len(str_year)==4:
        if int(str_year) <= 1401:
            if str_year.isdigit()==True:
                return True
            else:
                error_message ="The value entered is not a number for the year section."
                print(error_message) 
        else:
            error_message ="The year number is greater than 1401."
            print(error_message)
    else:
        error_message= " The length of year is incorrect."
        print(error_message)

#The function for checking tha leap year
def is_leap(str_year,str_month):
    z=int(str_year)%4
    if z == 0 and int(str_month)==12:
        message=("This year is a leap!")
        print(message)
        return True,str_month
    else:
        error_message="This year is not a leap!"
        print(error_message)
        return False,str_month    

#This Function Ckeck the len and validity of month
def check_month(str_month):
    len_month= len(str_month)

    if len_month <=2:
        if str_month.isdigit()==True:
            int_month=int(str_month)
            if int_month>0 and int_month<=12:
                if len_month == 1:
                    str_month= "0"+str_month
                return True,str_month
            else:
                error_message="The month number is incorrect. it shuld be between 1 to 12. "            
                print(error_message)
                return False
        else:
            error_message = "The value entered is not a number for the year section. "
            print(error_message)
            return False
    else:
        error_message="The length of month can not grater that 2 character. "
        print(error_message)
        return False

# This Function Check the validity of day
def check_day(str_day,str_month,leap_param):
    len_day=len(str_day)
    int_month=int(str_month)

    if len_day<=2:
        if str_day.isdigit()==True:
            int_day= int(str_day)
            x=dayInMonth[int_month-1]
    
            if len_day==1:
                str_day="0"+str_day

            if leap_param==False:
                if int_day <= x:
                    return str_day,str_month, True
                else:
                    error_message="The number of days entered is more than the number of days allowed this month. "
                    print(error_message)
                    return str_day,str_month, False
            elif leap_param==True and int_month==12:
                if int_day <= 30:
                    return str_day,str_month, True
            elif leap_param == True and int_month < 12:
                x=dayInMonth[int_month-1]
                if int_day <=x:
                    return str_day,str_month, True
            else:
                error_message="an error exist on chack_day function"
                print(error_message)                
                return str_day,str_month, False
        else:
            error_message = "The value entered is not a number for the year section. "
            print(error_message)
            return str_day,str_month, False
    else:
        error_message="The length of day can not grater that 2 character. "
        print(error_message)
        return str_day,str_month, False


dayInMonth = [31,31,31,31,31,31,30,30,30,30,30,29]
dayInMonthInWord =["Farvardin","Ordibehesht","Khordad","Tir","Mordad","Shahrivar"
                       ,"Mehr","Aban","Azar","Dey","Bahman","Esfand"]

while True:
    date= input("\nPleae Enter a new date like yyyy-mm-dd ... ")    
    
    #pattern validation
    if check_count(date,"-",1,10,2)== True:    
        if check_count(date,"-",4,5,1)==True and check_count(date,"-",6,8,1) == True:

            #split input and Check the year character after pattern validation 
            str_year,str_month,str_day = date.split("-")
            check_year_result = check_year(str_year)

            #check month if year number was valid!
            if check_year_result == True:
                check_month_result = check_month(str_month)
    
                #check day if the month was valid and replace month if it was 1 charecter
                if check_month_result[0] == True:
                    str_month=check_month_result[1]
                    is_leap_result=is_leap(str_year, str_month)

                    check_day_result = check_day(str_day,is_leap_result[1],is_leap_result[0])
                    
                    #print the approval message if day has been valided and replace the day number if it was 1 character
                    if check_day_result[2]==True:
                        str_day=check_day_result[0]
                        str_month = check_day_result[1]
                        date_message = "The date {}/{}/{} is approved"
                        print(date_message.format(str_year,str_month,str_day))
                    else:
                        print("Try again!")
                else:
                    print("Try again!")
            else:
                print("Try again!")
        else:
            print("Try again!")
    else:
        print("Try again!")
