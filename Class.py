class Date:

    def __init__(self,year,month,day):
        # year , month and day are integers
        assert type(year)==int and type(month)==int and type(day)==int, "Date should be number"
        self.year=year
        self.month=month
        self.day=day

    def __str__(self,other):
        # Return a String representation of self    
        return str(self.year), '/', str(self.month), '/', str(other)

    def __add__(self,other):
        #  Return a new date representing the addition    
        assert type(other)==int,"Number of Days that you want to add should be number!"       
        if self.month==12:
            day = self.day+ other
            if day<=29:
                addDay = self.day + other
                return other
            else:
                x_diff_day= other % 29
                y_diff_month = self.month + (other / 29)
                if y_diff_month > 12:
                    y_diff_month = y_diff_month % 12
                    z_diff_year = self.year +( y_diff_month / 12)
                    return z_diff_year,y_diff_month,x_diff_day
                else:
                    return self.year,y_diff_month,x_diff_day

        elif self.month >6 and self.month < 12:
            day = self.day+ other
            if day<=30:
                addDay = self.day + other
            else:
                x_diff_day= other % 30
                y_diff_month = self.month + (other / 30)
                if y_diff_month > 12:
                    y_diff_month = y_diff_month % 12
                    z_diff_year = self.year +( y_diff_month / 12)
                    return z_diff_year,y_diff_month,x_diff_day
                else:
                    return self.year,y_diff_month,x_diff_day

        elif self.month >0 and self.month<= 6:                            
            day = self.day+ other
            if day<=31:
                addDay = self.day + other
            else:
                x_diff_day= other % 31
                y_diff_month = self.month + (other / 31)
                if y_diff_month > 12:
                    y_diff_month = y_diff_month % 12
                    z_diff_year = self.year +( y_diff_month / 12)
                    return z_diff_year,y_diff_month,x_diff_day
                else:
                    return self.year,y_diff_month,x_diff_day


inputDate=input("Enter a date like yyyy-mm/dd ...")
strYear,strMonth,strDay=inputDate.split("-")

addDate = input("Enter the number of days you want to add to the date... ")

add=AddDate(strYear, strMonth, strDay)
add.__add__(addDate)
