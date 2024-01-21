import os
import webbrowser
from fpdf import FPDF


class PdfReport:
    """
    Object that is used for generating a pdf file of the bill
    """

    def __init__(self, filename):
        self.filename = filename + ".pdf"

    def generate(self, flatmate1, flatmate2, bill):
        pdf = FPDF("portrait", "pt", "a4")
        pdf.add_page()
        pdf.set_font("arial", "b", 24)
        pdf.image(w=80, h=80, name="files/house.png")
        pdf.cell(w=0, h=80, txt="Flatmates Bill", border=0, align="C", ln=1)
        pdf.cell(w=100, h=40, txt="Period:", border=0)
        pdf.cell(w=150, h=40, txt=self.filename.replace(".pdf", ""), border=0, ln=1)
        pdf.set_font("arial", "", 18)
        pdf.cell(w=100, h=40, txt=flatmate1.name, border=0)
        pdf.cell(w=100, h=40, txt=format_as_currency(flatmate1.pays(bill, flatmate2)), border=0, ln=1)
        pdf.cell(w=100, h=40, txt=flatmate2.name, border=0)
        pdf.cell(w=100, h=40, txt=format_as_currency(flatmate2.pays(bill, flatmate1)), border=0)

        pdf.output(f"files/{self.filename}")

        webbrowser.open("file://" + os.path.realpath(f"files/{self.filename}"))


def format_as_currency(amount):
    """
    Helper method to format number as a string to 2dp with currency symbol
    """
    return "$" + str(round(amount, 2))
