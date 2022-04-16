class M_Date:

    def __init__(self,year,month,day):
        # year , month and day are integers
        assert type(year)==int and type(month)==int and type(day)==int, "Date should be number"
        self.year=year
        self.month=month
        self.day=day

    def __add__(self,other):
        #  Return a new date representing the addition    
        assert type(other)==int,"Number of Days that you want to add should be number!"       
        if self.month==12:
            day = self.day+ other
            if day<=29:
                return self.year,self.month, day
            else:
                x_diff_day= day % 29
                y_diff_month = self.month + (day // 29)
                if y_diff_month > 12:
                    z_diff_year = self.year +( y_diff_month // 12)
                    y_diff_month %= 12
                    return z_diff_year,y_diff_month,x_diff_day
                else:
                    return self.year,y_diff_month,x_diff_day

        elif self.month >6 and self.month < 12:
            day = self.day+ other
            if day<=30:
                return self.year,self.month, day
            else:
                x_diff_day= day % 30
                y_diff_month = self.month + (day // 30)
                if y_diff_month > 12:
                    z_diff_year = self.year +( y_diff_month // 12)
                    y_diff_month %= 12
                    return z_diff_year,y_diff_month,x_diff_day
                else:
                    return self.year,y_diff_month,x_diff_day

        elif self.month >0 and self.month<= 6:                            
            day = self.day+ other
            if day<=31:
                return self.year,self.month, day
            else:
                x_diff_day= day % 31
                y_diff_month = self.month + (day // 31)
                if y_diff_month > 12:
                    z_diff_year = self.year +( y_diff_month // 12)
                    y_diff_month %= 12
                    return z_diff_year,y_diff_month,x_diff_day
                else:
                    return self.year,y_diff_month,x_diff_day


while True:
    inputDate=input("\nEnter a date like yyyy-mm-dd ...")
    strYear,strMonth,strDay=inputDate.split("-")

    if strYear.isdigit() and strMonth.isdigit() and strDay.isdigit():    
        intYear= int(strYear)
        intMonth=int(strMonth)
        intDay=int(strDay)

        addDay = input("Enter the number of days you want to add to the date...")
        addDay = int(addDay)

        # Initialization  
        addition = M_Date(intYear, intMonth, intDay)
        

        #Call Method
        newDate = addition.__add__(addDay)
        print("New Date is: ", newDate[0],'/',newDate[1],'/',newDate[2],end="\n")
    else:
        print("Date should be number!")
        exit()
