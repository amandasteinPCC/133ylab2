#******************************************************************************
# Author:           Khanh Vu, Amanda Stein, Olga Sotiriadi
# Lab:              Lab 2
# Date:             01.18.2022 01.20.2022
# Description:      Tuition estimation program. The program promts user for Student name, number of credits taken each 
# term. The program calculates the total tuition cost a year based on number of credits taken and print out the 
# result. Also, it calculates the tuition cost next year, both during and after covid. 
# Input:            str name,str ID, int credit, float costPerCredit 
# Output:           str name, str ID, int credit, todayDate, float totalCost, float nextTotalCost, datetime theDate
# Sources:       Amanda Stein Reasearch: Cost during covid .6%, #pre COVID 8% annually https://finaid.org and www.bloomberg.com
#******************************************************************************
#Khanh
import datetime
theDate = datetime.date.today()

costPerCredit = 123.25

def main():
  # Khanh - Step 1: print out welcome statement
  print ('Welcome! This is the Tuition calculation program!\n')
  
  # Amanda - Step 2: prompt user for Student Name, number of credits taken
  name, ID, credit = userInput()

  # Khanh - Step 3: calculate the total cost
  totalCost = calculateTotalCost(credit, costPerCredit)
  
  #Amanda: Step 4 - Cost next year
  nextTotalCost = nextYearCost(totalCost)
  
  # Olga - Step 5: print the date, the student's name, number of credits taken and the total cost 
  printResult(name, ID, credit, totalCost, nextTotalCost)

#Amanda Stein
def userInput():
  name = input("Enter your name:  ")
  ID = input("Enter your student ID: ")
  credit = int(input("Enter your total credits this term: "))

  return name, ID, credit
  
# Khanh 
def calculateTotalCost(credit, costPerCredit):
  totalCost = round(credit * costPerCredit,2)
  return totalCost

# Everyone edited, Kahn if, Amanda else, Olga debug
def nextYearCost(totalCost):
  covid = input("Is COVID over, 'y' for yes, 'n' for no: ")
  if covid == "y": 
    growthRate = 0.006
    totalCost *= (1 + growthRate)
    nextTotalCost = round(totalCost, 2)
  else: 
    growthRate = .08
    totalCost *= (1 + growthRate)
    nextTotalCost = round(totalCost, 2)
  return nextTotalCost
  
#Olga Sotiriadi
#Print the date, the student's name, ID, number of credits taken and the total #costs for current and the next year
def printResult(name, ID, credit, totalCost, nextTotalCost):
  print("\nThe student's name is ", name, 
  "\nStudent ID is " + ID,
  "\nToday is ", theDate)
  print("\nYour number of credits is {0} \nYour total tuition is ${1}".format(credit, totalCost))
  print("The estimated next year's cost will be ${0}".format(nextTotalCost))
  print("\nThank you for using the Tuition calculation program!")

main()