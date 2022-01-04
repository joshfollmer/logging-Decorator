from datetime import datetime, date

def time_calculator():
    '''
    Function to calculate what percent of the year has passed
    '''
    current_date = date.today()
    day_of_year = datetime.now().timetuple().tm_yday
    percent = str(round(day_of_year / 365, 2))
    #print(f"The date is {current_date}, the year is {percent[2:]}% over")
    result = f"The date is {current_date}, the year is {percent[2:]}% over"
    return result

#print(time_calculator())
