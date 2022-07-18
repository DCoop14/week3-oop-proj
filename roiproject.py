# Here we assume that we have a client coming to us asking for an automated Rental Property Calculator. 
# Our client's name is Brandon from a company called "Bigger Pockets". Below, you will find a video of what Brandon usually does to calculate his Rental Property ROI.
# Using Visual Studio Code/Jupyter Notebook, and Object Oriented Programming create a program that will calculate the Return on Investment(ROI) for a rental property.

from cmath import exp
from operator import inv
from winreg import ExpandEnvironmentStrings
from xml.etree.ElementInclude import include

from more_itertools import value_chain


class roi():
  

    def __init__(self, investment = {}, income = {}, expenses = {}, total_investment = {}):
        self.investment = investment
        self.income = income
        self.expenses = expenses
        self.total_investment = total_investment

    def income_a(self):
       while True: 
            rental_income = int(input("Enter rental income"))
            laundry_income = int(input("Enter laundry income"))
            storage_income = int(input("Enter storage income"))
            misc_income = int(input("Enter misc income"))
            total_income = [rental_income, laundry_income, storage_income, misc_income]
            total_income = 0
            self.new_method(total_income)
            break

    def new_method(self, total_income):
        for i in total_income:
            total = total + i 
        print(total_income)

    def expenses_a(self):
        while True:
            tax_expenses = int(input("Enter Tax expense"))
            insurance_expenses = int(input("Enter Insurance expense"))
            hoa_expenses = int(input("Enter HOA expense"))
            lawncare_expenses = int(input("Enter Lawncare expense"))
            vacancy_expenses = int(input("Enter Vacancy expense"))
            repairs_expenses = int(input("Enter Repairs expense"))
            capex_expenses = int(input("Enter CapEx expense"))
            propertymgt_expenses = int(input("Enter Property Mgt expense"))
            mortgage_expenses = int(input("Enter Mortgage expense"))
            break

    def totalexpense_a(self):
        while True:
            total_investment = int(input("Enter Down Payemnt"))
            total_investment = int(input("Enter Closing Costs"))
            total_investment = int(input("Enter Rehab Budget"))
            total_investment = int(input("Enter Misc/Other"))
            break



 #   def roi(investment, income, expenses, total_investment):
 #       cash_flow = income - expenses * 12
 #      roi = (cash_flow % total_investment)*100
 #       print(roi)

 #   def func(self):
 #       print("Enter rental income" + +self.income)


calculator = roi()
calculator.income_a()
#calculator.expenses_a()
#calculator.totalexpense_a()