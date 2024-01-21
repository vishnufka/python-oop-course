#!/usr/bin/env python3
from flat import Bill, Flatmate
from report import PdfReport


def __main__():
    amount = float(input("Enter bill amount: "))
    bill = Bill(amount, "July 2022")

    flatmate1_name = input("Enter flatmate1 name: ")
    flatmate1_days = int(input(f"{flatmate1_name}, enter days in house: "))
    flatmate1 = Flatmate(flatmate1_name, flatmate1_days)

    flatmate2_name = input("Enter flatmate2 name: ")
    flatmate2_days = int(input(f"{flatmate2_name}, enter days in house: "))
    flatmate2 = Flatmate(flatmate2_name, flatmate2_days)

    pdf = PdfReport(filename=bill.period)

    pdf.generate(flatmate1, flatmate2, bill)


__main__()
