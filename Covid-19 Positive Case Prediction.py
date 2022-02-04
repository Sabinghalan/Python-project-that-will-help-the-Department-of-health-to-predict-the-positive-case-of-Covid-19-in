"""I have created a python program that will help the Department of health to
 predict the positive case of Covid-19 in each state of Australia.
 This program will ask the user to enter the growth rate, number of days and social distancing compliance to show the result. """


# The import functions that are needed for programming.
import time
import sys

def Open_file(NameOfFile): # Here we defined the function named Open_file.
                          # This function will check whether the file if right type or not.

    try:
        return open(NameOfFile, "rt")
    except Exception as Excep:
        print(type(Excep).__name__ + ": Closing the program. Please use another file.")
        sys.exit()

def main(): # Here we defined the function named main.
            # This function will run the program and calculates all data to write in the file.

    try: # It will handle the errors.
        OutPutFile = OutPutFileName()  # It handles the file.
        g, NoOfDays, s = InPutValue() # It handles the input of users.

        # The output header that is displayed on the screen.
        print("COVID-19 POSITIVE RESULTS:-{0} DAY PREDICTIONS \n".format(NoOfDays))
        print("GROWTH RATE:{0} \n".format(g))
        print("SOCIAL DISTANCING COMPLIANCE:{0}% \n".format(s))

        # Writing the title on report_s.txt file.
        OutPutFile.write("COVID-19 POSITIVE RESULTS:-{0} DAY PREDICTIONS \n".format(NoOfDays))
        OutPutFile.write("GROWTH RATE:{0} \n".format(g))
        OutPutFile.write("SOCIAL DISTANCING COMPLIANCE:{0}% \n".format(s))

        print("Days", end="\t")   # It will print the days on screen.
        OutPutFile.write("Days" + "\t")

        # It will write all states names on a file.
        for i in range(len(STATE)):
            print(STATE[i], end="\t")
            OutPutFile.write(STATE[i] + "\t")
        print("Total")
        OutPutFile.write("Total\n") # It will display total number of covid infected person per day.

        LatestPositiveTest = []  # It is the array for holding the values.
        g = g * (1 -s/ 100) # It will do the growth rate calculation.
        # In this formula:  g represent growth rate, s represent social distancing compliance.

        # It will display as well as write the separator on file.
        print("________________________________________________________________________________________________________")
        OutPutFile.write("_____________________________________________________________________________________________________________\n")

        # It is the nested loop for obtaining the values on 2D table.
        for d in range(NoOfDays): # Here we run upper 'for' loop for number of days.
            TOTAL = 0
            for i in EarlyCase:  # Here we run inner 'for' loop fro early cases of covid-19.
                # Calculating new positive test
                POSITIVE_TEST = i * (g ** d) # In this formula: i represent initial +ve cases, d represent number of days, and g reperent growth rate.
                LatestPositiveTest.append(int(POSITIVE_TEST))
                TOTAL = TOTAL + int(POSITIVE_TEST) # It will add new +ve test to TOTAl.
            LatestPositiveTest.append(TOTAL)   # It will add new +ve cases on array & write to the file.
            print("{0}".format(d + 1), end="\t")
            OutPutFile.write(str(d + 1) + "\t")

            #  Here we run 'for' loop for the range of value in final +ve test writing to file
            for i in range(len(LatestPositiveTest)):
                print(LatestPositiveTest[i], end="\t")
                OutPutFile.write(str(LatestPositiveTest[i]) + "\t") # It will add the number of latest +ve test person to the file.
            LatestPositiveTest = []
            print("\n")
            OutPutFile.write("\n")
        OutPutFile.close()  # It will close the file.
    except FileNotFoundError: # It will do the errors handling.
        print(' Unfortunately, system cannot locate the file')

def InPutFile(): #Here we defined the InputFile function.
                 # This function will read the files & arranged the data in 2 seperate arrays.
    try:
        global STATE, EarlyCase  # The values will store in 'STATE' and 'EarlyCase' arrays.
        FILE = Open_file('Data.txt') # It wll read the content of "Data.txt"file.
        ArrayData = FILE.read().splitlines() # list of each line
        for i in range(len(ArrayData)): # It is the 'for' loop to go through each value in ArrayData.
            if i % 2 == 0:
                STATE.append(ArrayData[i]) # The even index represent the name of state.
            else:
                EarlyCase.append(int(ArrayData[i])) # The odd index represent the early cases.
        FILE.close()    # FILE closing after it is done.
    except FileNotFoundError:
        print("Unfortunately, Cannot find the file called data.txt") # This displayed the error messages on screen.


def OutPutFileName(): # Here, we defined the OutPutFileName function.
    try:
        Sec = str(time.time())  # Here,sec is second. making the time as string.
        s = Sec.split(".")[0]   # It gives time only in unit of second.
        Outputed_FileName = "report_" + s + ".txt"  # It will do naming of output file.
        OutPutFile = open(Outputed_FileName, "a")  # Generating the  output file.
    except FileExistsError:
        print("Sorry, the file is exist previously")  # It will do error handling.
    return OutPutFile


def InPutValue(): # We defined the function named InPutValue.
    while True:
        try:
            NumOfDays = int(input("Enter number of days:"))  # It will return number of days as int datatype.
            GrowingRate = float(input("Enter growth rate:"))  # It will return growing rate in float datatype.
            SocialDistancingCompliance = float(input("Enter social distancing compliance:")) # It will return social distancing compliance in float datatype.

            # It is the "if" condition to handle -ve input.
            if GrowingRate >= 0 and NumOfDays >= 0 and SocialDistancingCompliance >= 0:
                break
            else:
                # Message to user.
                print("Negative value is not excepted. So please enter the positive value") # If user entered the negative value, it will ask them for positive value.
        except ValueError:
            print("You have entered the wrong value type, So please enter the proper value")
    return GrowingRate, NumOfDays, SocialDistancingCompliance


def ConditionStatus(): # Here we defined the function named ConditionStatus.
                       # It will request the user either to continue or terminate the program.
    # It is the boolean for checking whether the user quit or not.
    main() # start function
    condition = True # tell the user to restart program.
    while condition == True:
        try:
            QUERY = input(
                "Hi dear, would you like to predict your prediction on worldwide pandemic Covid-19:(y or n)").upper()
            if QUERY == "Y":
                main()
            elif QUERY == 'N':
                condition = False
            else:
                QUERY = input('Error occur. Please enter the proper input:(y/n)')
        except ValueError:
            print("The input is wrong")

# Key execution part of program

STATE = []  # This array holds the state names.
EarlyCase = []  # This array holds the early cases of covid-19.

InPutFile() # This function will open and read the content of the file.
ConditionStatus()  # This function will run program while everything are okay.
