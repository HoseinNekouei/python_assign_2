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
###
while True:
    command = input("\n Enter a command (start 'or' end)...")
    if command == "start":       
        date= input("\nPleae Enter a new date like yyyy-mm-dd ... ")

        #pattern validation control
        if check_count(date,"-",1,10,2)== True:    
            if check_count(date,"-",4,5,1)==True and check_count(date,"-",6,8,1) == True:

                str_year,str_month,str_day = date.split("-")
                check_year = check_year(str_year)
                #check_month = check_month(str_month)
                #check_day = check_day(str_day)

                if check_year == True:
                    if check_month(str_month)== True:
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
            continue
        
    elif command == "end":
        print("The application was closed!")
        break
    else:
        print("\nCommand not found!")
