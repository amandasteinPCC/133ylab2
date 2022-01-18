# ******************************************************************************
# Author:           Khanh Vu, Amanda Stein, Olga
# Lab:              Lab 2
# Date:             01.18.2022
# Description:      Tuition estimation program that promts user for Student name, number of credits taken each term. The program will calculate the total tuition cost based on number of credits taken and print out the result.
# Input:            str name,str ID, int credit, float costPerCredit
# Output:           studentName, totalCost, todayDate
# Sources:          Lab 2 specifications
#                   and any other substantial aids, like web pages or students
#                   who helped you.
# Algorithm:
# ******************************************************************************
# Khanh
import datetime

theTime = datetime.datetime.now()
theDate = datetime.date.today()

costPerCredit = 123.25


def main():
    # Khanh - Step 1: print out welcome statement
    print("Welcome! This is the Tuition calculation program!")

    # Amanda - Step 2: prompt user for Student Name, number of credits taken
    name, ID, credit = userInput()

    # Khanh - Step 3: calculate the total cost
    totalCost = calculateTotalCost(credit, costPerCredit)
    totalCost = round(totalCost, 2)

    # Olga - Step 4: print the date, the student's name, number of credits taken and the total cost
    printResult(name, ID, credit, totalCost)


# Amanda Stein
def userInput():
    name = input(" Enter your name:  ")
    ID = input(' Enter your student ID: ')
    credit = int(input('Enter your total credits this term: '))

    return name, ID, credit


# Khanh
def calculateTotalCost(credit, costPerCredit):
    totalCost = credit * costPerCredit
    return totalCost


# Olga Sotiriadi
# Print the date, the student's name, ID, number of credits taken and the total cost
def printResult(name, ID, credit, totalCost):
    print("Today is ", theDate)
    print(name, " " + ID)
    print("Your number of credits is {0}, Your total tuition is {1}".format(credit, totalCost))
    print("Thank you for using Tuition calculation program!")


main()