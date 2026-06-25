from datetime import date,datetime

def calculate_age(day:int, month:int,year:int):
    today=date.today()
    age=today.year-year
    if(today.month,today.day)<(month,day):
        age-=1;
        return age;