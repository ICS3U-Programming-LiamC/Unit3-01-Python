#!/usr/bin/env python3

# Created by: Liam Csiffary
# Created on: May 7, 2021
# This program calculates the total cost of
# something depending on the province and the subtotal


# import my constants so that I can have the tax numbers
import constants

# this is the fucntion that does everything
def tax_calculator():
    # get the users province
    province = input("Choose the Province you want tax for, options are: \
    \nManitoba (MB), Saskatchewan (SK), Alberta (AB), \
    \nNew Brunswick (NB), Québec (QC). \
    \n\n(Please only put the abbreviated form):")

    # get the subtotal 
    subtotal = int(input("What is the subtotal: "))

    # depending on the province import the correct tax for that province
    if province == "MB":
        province_tax = constants.MB

    if province == "SK":
        province_tax = constants.SK

    if province == "AB":
        province_tax = constants.AB

    if province == "NB":
        province_tax = constants.NB

    if province == "QC":
        province_tax = constants.QC

    # then with this tax and the subtotal calculate the total cost
    total = province_tax * subtotal + subtotal

    # round the numbers and tell the user what the tax in that province is
    # and then tell them their total 
    print("The tax in {0} is {1:.1f}%".format(province, province_tax*100))
    print("Your total is ${0:.2f}".format(total))

    # ask the iser if they want to restart the program
    restart = input("Would you like to run the program again?(y/n): ")

    # if they do want to restart it then restart it
    if restart == "y":
        tax_calculator()

    if restart == "Y":
        tax_calculator()

# initial bootup of the program
if __name__ == "__main__":
    tax_calculator()
