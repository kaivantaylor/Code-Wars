# HAPPY YEARS
def some_func(year):
    if 1000 <= year <= 9000:
        print("Hello")
        s = set()

        
        str_year = str(year)
        print(str_year)
        print(len(str_year))


        for char in str_year:
            s.add(char)
    
        print(s) # output of '0' and '5'
        print(len(s))

        if len(s) == 4:
            print("this is a valid input")
            print(year)
        else:
            print("this is not a valid input")
            some_func(year + 1)
            
        # 5000
    else:
        print("The year is not valid")

some_func(1001)
