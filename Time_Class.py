class My_Time:

    def __init__(self,hh,mm,ss):
        # Hour, Minute and Second are Integer
        assert type(hh)==int and type(mm)==int and type(ss)==int, "The Timme Should be Interger"
        self.Hour=hh
        self.Minute=mm
        self.Second=ss
        
    def __add__(self,other):
        
        #  Return a new Time representing the addition    
        assert type(other)==int,"Number of Times that you want to add should be number!"       

        second = self.Second + other
        if second > 60:
            # Return The new Second
            x_div_second = second // 60
            second %= 60
            minute = self.Minute + x_div_second
            if minute >= 60:
                y_div_minute = minute // 60
                minute %= 60
                hour = self.Hour + y_div_minute
                if hour == 24: hour = 0                    
                if minute == 0: minute = 0
                return hour,minute,second    
            else:
                return self.Hour,minute,second
        else:
            return self.Hour,self.Minute,second


while True:
    inputTime=input("\nEnter a Time like hh:mm:ss ...")
    strHour,strMinute,strSecond=inputTime.split(":")

    if strHour.isdigit() and strMinute.isdigit() and strSecond.isdigit():    
        intHour= int(strHour)
        intMinute=int(strMinute)
        intSecond=int(strSecond)

        addSecond = input("Enter the number of Seconds you want to add to the Time...")
        addSecond = int(addSecond)

        # Initialization  
        addition = My_Time(intHour, intMinute, intSecond)
        

        #Call Method
        newTime = addition.__add__(addSecond)
        print("New Time is: ", newTime[0],':',newTime[1],':',newTime[2],end="\n")
    else:
        print("Time should be number!")
        exit()

