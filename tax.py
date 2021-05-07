#!/usr/bin/env python3

# Created by: Liam Csiffary
# Created on: May 7, 2021
# This program calculates the total cost of
# somethign depending on the province and the subtotal


import constants


def tax_calculator():
    province = input("Choose the Province you want tax for, options are: \
    \nManitoba (MB), Saskatchewan (SK), Alberta (AB), \
    \nNew Brunswick (NB), Québec (QC). \
    \n\n(Please only put the abbreviated form):")

    subtotal = int(input("What is the subtotal: "))

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

    total = province_tax * subtotal + subtotal

    print("The tax in {0} is {1:.1f}%".format(province, province_tax*100))
    print("Your total is ${0:.2f}".format(total))

    restart = input("Would you like to run the program again?(y/n): ")

    if restart == "y":
        tax_calculator()

    if restart == "Y":
        tax_calculator()


if __name__ == "__main__":
    tax_calculator()
