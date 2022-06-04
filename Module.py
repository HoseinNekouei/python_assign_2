from cProfile import label


class My_Date_Module():
    
    def __init__(self,year,month,day,add_item):
        assert type(year)==int and type(month)==int and type(day)==int and type(add_item) == int , "Date should be number!" 
        self.year=year
        self.month= month
        self.day=day
        self.add_item = add_item

    
    def __add__(self,days_legaly):
        day = self.day + self.add_item
        if day<= days_legaly:
                message = "your date + {} --> < {}/{}/{}"
                print(message.format(self.add_item,self.year,self.month,day))
        else:
            x_diff_day = day % days_legaly
            self.month += day // days_legaly
            if self.month > 12:
                self.year += self.month // 12
                self.month = self.month % 12 
                message = "your date + {} --> < {}/{}/{} >"
                print(message.format(self.add_item,self.year,self.month,x_diff_day))
            else:
                message = "your date + {} --> < {}/{}/{}"
                print(message.format(self.add_item,self.year,self.month,x_diff_day))


class En_Date(My_Date_Module):
    
    def __init__(self,year,month,day):
        super().__init__(year,month,day,add_item)
        self.month = month

    def validity_date(self):
        dayInMonth = [31,28,31,30,31,30,31,31,30,31,30,31]
        days_legaly = dayInMonth[self.month-1]
        return days_legaly


class Fa_Date(My_Date_Module):
    def __init__(self,year,month,day,add_item):
        super().__init__(year,month,day,add_item)
        self.month = month

    def validity_date(self):
        dayInMonth = [31,31,31,31,31,31,30,30,30,30,30,29]
        days_legaly = dayInMonth[self.month-1]
        return days_legaly
    

input_fa_date = input("Enter a Persian Date like yyyy-mm-dd...")
add_item = int(input("Enter a numbers the you want to increase your date..."))

# Get a date and split it
str_year,str_month,str_day = input_fa_date.split("-")

# cast the string variable to int
int_year= int(str_year)
int_month= int(str_month)        
int_day=int(str_day)

validity_object = Fa_Date(int_year,int_month,int_day,add_item)
validity_object.__add__(validity_object.validity_date())