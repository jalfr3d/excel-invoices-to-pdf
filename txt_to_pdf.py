import glob
from fpdf import FPDF
from pathlib import Path

filepaths = glob.glob("txt/*.txt")
# one pdf document for the script
pdf = FPDF(orientation="P", unit="mm", format="A4")

for filepath in filepaths:
    # add a page to the pdf document for each text files
    pdf.add_page()
    # get file name as a string
    filename = Path(filepath).stem
    capitalize_name = filename.capitalize()

    pdf.set_font(family="Times", size=16, style="B")
    pdf.cell(w=50, h=8, txt=capitalize_name, align="L", ln=1)

    # Get the content for each text file
    with open(filepath, "r") as file:
        content = file.read()
    # Add the text file content to the PDF
    pdf.set_font(family="Times", size=12)
    pdf.multi_cell(w=0, h=6, txt=content)

# Produce the PDF
pdf.output("txttopdf/animals.pdf")
