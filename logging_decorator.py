# Josh Follmer, logging decorator assignment


from time_calculator import time_calculator
from datetime import datetime
from time import time



def log_decorator(funct):
    '''
    Decorator that will log start time, function output, end time, function execution time, and arguments to a file
    '''
    def logger(*args, **kwargs):
        #first opens a file with the alias file (VScode has an option to auto change the terminal directory to the file location which is off by default, very helpful)
        with open('log_file.txt', 'w') as file:
            try:
                #first uses the datetime function to get the current date and time, down to a very small fraction of a second
                current_date = datetime.today()
                #prints the name of a function and the date and time it beings to run. interestingly, when the function returns an int, i get a type error
                file.write(f'Running {funct.__name__} at {current_date}\n')
                #records the start time
                start = time()
                #runs the fucntion, saves the return as a variable
                result = funct(*args, **kwargs)
                #records the end time
                end = time()
                #records the name and and the return of the function
                file.write(f"{funct.__name__} output: {result}\n")
                #gets the date and time again (getting the date is overkill, but why not)
                current_date = datetime.today()
                #calculates the duration of the function           
                duration = end - start
                #records the end date, time, and how long it took
                file.write(f"{funct.__name__} finished running at {current_date}, it took {duration} seconds to complete.\n")
                #prints any arguments given onto two lines. when ive run this they look like two pairs of emtpy brackets, and im assuming thats correct. i couldnt get this to run with a function with arguments
                file.write(f"Arguments: {args}\n")
                file.write(f"Keyword arguments: {kwargs}")
            #suposedly this will write to the file in case of an error, but i purposefully made an erro happen and it printed nothing, so i dont know
            except:
                file.write("Something went wrong")
            #no matter what, it will save the file
            finally:
                file.close()
    #returns the idea of the logger
    return logger

#aliases time_calculator with the decorator
time_logged = log_decorator(time_calculator)
#runs the function with the decorator
time_logged()
