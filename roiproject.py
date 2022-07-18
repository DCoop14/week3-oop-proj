# Here we assume that we have a client coming to us asking for an automated Rental Property Calculator. 
# Our client's name is Brandon from a company called "Bigger Pockets". Below, you will find a video of what Brandon usually does to calculate his Rental Property ROI.
# Using Visual Studio Code/Jupyter Notebook, and Object Oriented Programming create a program that will calculate the Return on Investment(ROI) for a rental property.

from cmath import exp
from operator import inv
from re import sub
from winreg import ExpandEnvironmentStrings
from xml.etree.ElementInclude import include

from more_itertools import value_chain
from sympy import div


class roi():
  

    def __init__(self, investment = {}, income = {}, expenses = {}, total_investment = {}):
        self.investment = investment
        self.income = income
        self.expenses = expenses
        self.total_investment = total_investment

    def investment_a(self):
        while True:
            investment = int(input())
            print("Investment" + " " + str(investment))

    def income_a(self):
       while True: 
            rental_income = int(input("Enter rental income" + " "))
            laundry_income = int(input("Enter laundry income" + " "))
            storage_income = int(input("Enter storage income" + " "))
            misc_income = int(input("Enter misc income" + " "))
            total_income = [rental_income, laundry_income, storage_income, misc_income]
            total_income = sum(total_income)
            print("Total income" + " " + str(total_income))
            break

    def expenses_a(self):
        while True:
            tax_expenses = int(input("Enter Tax expense" + " "))
            insurance_expenses = int(input("Enter Insurance expense" + " "))
            hoa_expenses = int(input("Enter HOA expense" + " "))
            lawncare_expenses = int(input("Enter Lawncare expense" + " "))
            vacancy_expenses = int(input("Enter Vacancy expense" + " "))
            repairs_expenses = int(input("Enter Repairs expense" + " "))
            capex_expenses = int(input("Enter CapEx expense" + " "))
            propertymgt_expenses = int(input("Enter Property Mgt expense" + " "))
            mortgage_expenses = int(input("Enter Mortgage expense" + " "))
            total_expenses = [tax_expenses, insurance_expenses, hoa_expenses, lawncare_expenses, vacancy_expenses,repairs_expenses, capex_expenses, propertymgt_expenses, mortgage_expenses]
            total_expenses = sum(total_expenses)
            print("Total expenses" + " " + str(total_expenses))
            break

    def totalinvestment_a(self):
        while True:
            down_payment = int(input("Enter Down Payemnt" + " "))
            closing_costs = int(input("Enter Closing Costs" + " "))
            rehab_budget = int(input("Enter Rehab Budget" + " "))
            misc_other = int(input("Enter Misc/Other" + " "))
            total_investment = [down_payment, closing_costs, rehab_budget, misc_other]
            total_investment = sum(total_investment)
            print("Total investment" + " " + str(total_investment))
            break



    def roi(investment, total_income, total_expenses, total_investment):
        while True:
            cash_flow = sub(total_income - total_expenses) * 12
            roi = div(cash_flow % total_investment)*100
            return roi
            

   # def func(self):
  #          print("Enter rental income" + +self.income)


calculator = roi()
calculator.income_a()
calculator.expenses_a()
calculator.totalinvestment_a()
calculator.investment_a()
calculator.roi()
