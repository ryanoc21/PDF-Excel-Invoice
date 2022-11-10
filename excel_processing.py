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
            # Get the filename to add its info to the PDF
            filename = Path(filepath).stem
            invoice_num = filename.split('-')[0]
            date = filename.split('-')[1]

            # Create the PDF
            pdf = FPDF(orientation="P", unit="mm", format="A4")
            pdf.add_page()
            pdf.set_font(family='Times', size=16, style='B')
            pdf.cell(w=50, h=8, txt=f'Invoice No. {invoice_num}',ln=1)
            pdf.cell(w=50,h=8,txt=f'Date: {date}',ln=1)

            # Read the data frame
            df = pd.read_excel(filepath, sheet_name="Sheet 1")
            df_columns = list(df.columns)
            pdf.set_font(family='Times', size=10, style='B')
            pdf.cell(w=30, h=8, txt=str(df_columns[0]), border=1)
            pdf.cell(w=65, h=8, txt=str(df_columns[1]), border=1)
            pdf.cell(w=35, h=8, txt=str(df_columns[2]), border=1)
            pdf.cell(w=30, h=8, txt=str(df_columns[3]), border=1)
            pdf.cell(w=30, h=8, txt=str(df_columns[4]), border=1, ln=1)

            # Loop over the data
            for index,row in df.iterrows():
                pdf.set_font(family='Times',size=10)
                pdf.cell(w=30,h=8,txt=str(row['product_id']),border=1)
                pdf.cell(w=65, h=8, txt=str(row['product_name']),border=1)
                pdf.cell(w=35, h=8, txt=str(row['amount_purchased']),border=1)
                pdf.cell(w=30, h=8, txt=str(row['price_per_unit']),border=1)
                pdf.cell(w=30, h=8, txt=str(row['total_price']),border=1,ln=1)

            # Add a total price
            total_price = df['total_price'].sum()
            pdf.set_font(family='Times', size=10)
            pdf.cell(w=30, h=8, txt=" ", border=1)
            pdf.cell(w=65, h=8, txt=" ", border=1)
            pdf.cell(w=35, h=8, txt=" ", border=1)
            pdf.cell(w=30, h=8, txt=" ", border=1)
            pdf.cell(w=30,h=8,txt=str(total_price),border=1,ln=1)

            # Add a summary of the data
            pdf.set_font(family='Times',size=14,style='B')
            pdf.cell(w=0,h=8,txt=f'The total price is {total_price} euros',ln=1)
            pdf.image('invoice.png',5,5)

            pdf.output(f"PDF_Reports/{filename}.pdf")




