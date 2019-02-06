"""
This program is to check 
a. try method
b. csv.reader
"""

import os
import csv

# function to get the user input for weight an height
def user_input():
#To verify if the user has entered the data in the right format for weight
    while True:
        print("Enter weight in kgs")
        try:
            user_weight = float(input())
            if isinstance(user_weight,float):
                break

        except ValueError:
         print("The entered value is not correct")
    
# To verify if the User has entered the data in the right format for height
    while True:
        print("Enter height in mtrs")

        try:
            user_height = float(input())
            if isinstance(user_height,float):
                break
        except ValueError:

            print("The entered value in mtrs is not correct")
    return user_weight,user_height       

# Formula to calculate bmi
def calculate_bmi(user_weight,user_height):

    bmi = user_weight/(user_height*user_height)

# return the bmi value to the function
    return bmi
# To check to which category the BMI falls into and display the message
def bmi_category(bmi):
    "This function checks if the user is underweight, normal, overweight or obese"    
    if bmi <= 18.5:
         print("The user is considered as underweight")
    elif bmi > 18.5 and bmi < 24.9:
         print("The user is considered as normal weight")
    elif bmi > 25 and bmi <= 29.9:
        print("The user is considered as overweight")
    elif bmi >=30:
        print("The user is considered as obese")

# To read the csv file and compare with the bmi resutl and match with the player name
def compare_userbmi_with_player(bmi):
    print(type(bmi))
    csv_file = open ('..','data',"all_players_data.csv","r")
    matched_player = []
    csv_reader = csv.reader(csv_file, delimiter=',')
    next(csv_reader)
    #line_count = 0
    #for row in csv_reader:
    for i, row in enumerate(csv_reader):
        print(type(row[3]))
        bmi_value_in_row = float(row[3])
        player_name = row[0]
        if float(bmi_value_in_row) == bmi:
            matched_player.append({player_name:bmi_value_in_row})
    if not matched_player:
        print("No matching data")
    else:
        print("Your BMI is matching with")
        print (matched_player)


if __name__ == "__main__":
    
    # Function to get the User input
    user_weight,user_height= user_input()
    # Function to calculate BMI
    bmi_value = calculate_bmi(user_weight,user_height)
    print("Your BMI is:" , bmi_value)
   # Function to determine the BMI Category
    bmi_category(bmi_value)
    #Function to compare the player name with BMI value
    compare_userbmi_with_player(bmi_value)