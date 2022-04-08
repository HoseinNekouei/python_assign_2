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

#This Function Ckeck the len and validity of month
def check_month(str_month):
    len_month= len(str_month)
    int_month=int(str_month)

    if len_month <=2:
        if str_month.isdigit()==True:
            if int_month>0 and int_month<=12:
                if len_month == 1:
                    str_month= "0"+str_month
                return True,str_month
            else:
                error_message="The month number is incorrect. it shuld be between 1 to 12. "            
                print(error_message)
                return False,str_month
        else:
            error_message = "The value entered is not a number for the year section. "
            print(error_message)
            return False,str_month
    else:
        error_message="The length of month can not grater that 2 character. "
        print(error_message)
        return False,str_month

while True:
    date= input("\nPleae Enter a new date like yyyy-mm-dd ... ")
    #pattern validation control
    if check_count(date,"-",1,10,2)== True:    
        if check_count(date,"-",4,5,1)==True and check_count(date,"-",6,8,1) == True:

            str_year,str_month,str_day = date.split("-")
            check_year_result = check_year(str_year)
            check_month_result = check_month(str_month)
            #check_day = check_day(str_day)

            if check_year_result == True:
                if check_month_result[0] == True:
                    str_month=check_month_result[1]
                    
                    if check_day(str_day)==True:
                        print("The date entered is approved!")
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
