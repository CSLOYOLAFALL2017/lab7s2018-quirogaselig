#Programmers: Noah Selig & Sebastian Quiroga
#Course: CS151.01, Professor Franceschi
#Date: 3/23/2018
#Lab Assignment: 7
#Problem Statement: This program is designed for the user to select an exisiting file name and it will read and process the file for films. It will output the highest profit, as well as all the profits in a new file named by the user.
#Data in: User selected file and equations
#Data Out: New user named file with data stored in it
#Other files needed: movies.csv, test.csv
#Credits:

#Get a file from the user
def user_file_name():
    #True
    validFileName = True
    while validFileName:
        #valid file name will be an existing file
        try:
            filename = input ("\nEnter the name of the file: ")
            file = open(filename, "r")
            file.close()
            return filename
        #FileNotFoundError will keep asking user
        except FileNotFoundError:
            print("\nThe file does not exist")
            print (filename, "is NOT valid, try again")

#Function for the movie profit with the user file selection as parameter
def movie_profit(filename):
    data_file = open(filename, "r")
    #open user selected file for reading
    lines = data_file.readlines()
    max_profit = 0
    data_file.close()
#find max profit in selected file
    for line in lines:
        line = line.strip()
        #the comma is the delimiter in the file
        release, title, budget, gross = line.split(",")
        #convert strings to floats
        budget = float(budget)
        gross = float(gross)
        #equation= gross-budget
        profit = gross - budget

        if profit >= max_profit:
            max_profit = profit
            title_x = title
#return the highest profit with the movie title
    return "\nThe highest profit of all movies listed is: " + str(max_profit) + (" , ") + str(title_x)

#Function for writing current information to a new user selected file
def user_write_file(in_file_name, out_file_name):
#open file for reading
    in_file = open(in_file_name, "r")
#open file for user to write to
    out_file = open(out_file_name, "w")
    lines = in_file.readlines()


    for line in lines:
        line = line.strip()
        release, title, budget, gross = line.split(",")
        budget = float(budget)
        gross = float(gross)
        profit = gross - budget
        print (release, "," , title, ", " "Profit: $%.2f" % profit, "\n", end= "", file = out_file)

    in_file.close()
    out_file.close()

#Dfeine main for calling all previous functions
def main():
    print ("This program is designed for the user to select an exisiting file name and it will read and process the file for films. It will output the highest profit, as well as all the profits and movie titles in a new file named by the user.")
    file = user_file_name()
    print (file)
    profit = movie_profit(file)
    print(profit)
    new_user_file = input("\nPlease name a file to store data in: ")
    user_write_file(file,new_user_file )


main()







