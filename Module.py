from ast import Return
from typing_extensions import Self


class My_Date_Module():

    def __init__(self,year,month,day):
        assert type(year)==int and type(month)==int and type(day)==int, "Date should be number!" 
        self.year=year
        self.month= month
        self.day=day

    
    def __add__(self,other,day_valid):
        assert type(other) == int ,"Should  be number!"
        day=self.day + other
        if day<= day_valid:
            return self.year , self.month , self.day
        else:
            x_diff_day = day % day_valid
            self.month += day // day_valid
            if self.month > 12:
                self.year += self.month // 12
                self.month = self.month % 12
                return self.year, self.month, x_diff_day
            else:
                return self.year,self.month,x_diff_day


class En_Date(My_Date_Module):
    
    def __init__(self,year,month,day,other):
        super().__init__(year,month,day)
        self.hosein= other
        

class Fa_Date(My_Date_Module):

    def __init__(self,add_item):
        self.add_item=add_item

    dayInMonth = [31,31,31,31,31,31,30,30,30,30,30,29]
    global days_legaly 
    days_legaly = dayInMonth[super().month-1]
    




input_fa_date = input("Enter a Persian Date like yyyy-mm-dd...")
input_add= input("Enter a numbers the you want to increase your date...")

# Get a date and split it
str_year,str_month,str_day = input_fa_date.split("-")

# cast the string variable to int
int_year= int(str_year)
int_month= int(str_month)        
int_day=int(str_day)
add_item = int(input_add)

init_object = My_Date_Module()
init_object.__init__(int_year,int_month,int_day)
validity_object = Fa_Date()
validity_object.__init__(add_item)

