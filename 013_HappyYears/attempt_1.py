def next_happy_year(year):
    def someyear(year):
        hold_year = year
        if 1000 <= hold_year <= 9000:
            s = set()

            
            str_year = str(hold_year)
            #print(str_year)
            #print(len(str_year))


            for char in str_year:
                s.add(char)
        
            #print(s) # output of '0' and '5'
            #print(len(s))

            if len(s) == 4:
                #print("this is a valid input")
                b = hold_year
                print(hold_year)
                return hold_year
            else:
                #print("this is not a valid input")
                next_happy_year(hold_year + 1)
                
            # 5000
        else:
            print("The year is not valid")

