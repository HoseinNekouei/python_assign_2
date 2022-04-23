from ast import Return


class My_Date_Module():

    def __init__(self,year,month,day):
        assert type(year)==int and type(month)==int and type(day)==int, "Date should be number!" 
        self.year=year
        self.month= month
        self.day=day

    
    def __add__(self,add_item,month_legal,day_legal):
        assert type(add_item) == int ,"Should  be number!"
        day=self.day + add_item
        if day<= day_legal:
            return self.year , self.month , self.day
        else:
            x_diff_day = day % day_legal
            self.month += day // day_legal
            if self.month > month_legal:
                self.year += self.month // month_legal
                self.month = self.month % month_legal
                return self.year, self.month, self.day
            else:
                return self.year,self.month,self.day


class En_Date(My_Date_Module):
    
    def __init__(self,year,month,day,other):
        super().__init__(year,month,day)
        self.hosein= other
        


class Fa_Date(My_Date_Module):
    pass

fa_date = Fa_Date()
fa_date.__add__()


input_date = input("Enter a Persian Date like yyyy-mm-dd...")
input_add= input("Enter a numbers the you want to increase your date...")
        

