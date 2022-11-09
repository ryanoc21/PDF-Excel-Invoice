import pandas as pd
from fpdf import FPDF
import glob
from pathlib import Path


class File:
    def __init__(self, files):
        self.files = files
        self.group_files = glob.glob(self.files)

    def process(self):
        for filepath in self.group_files:
            # Read the data frame
            df = pd.read_excel(filepath, sheet_name="Sheet 1")

            # Get the filename to add its info to the PDF
            filename = Path(filepath).stem
            invoice_num = filename.split('-')[0]

            # Create the PDF
            pdf = FPDF(orientation="P", unit="mm", format="A4")
            pdf.add_page()
            pdf.set_font(family='Times', size=16, style='B')
            pdf.cell(w=50, h=8, txt=f'Invoice No. {invoice_num}')
            pdf.output(f"PDF_Reports/{filename}.pdf")


file = File("invoices/*.xlsx")
file.process()
