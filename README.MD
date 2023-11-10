# Excel to PDF Invoice Generator

## Overview

This Python script allows you to convert Excel invoice files into PDF format. It reads Excel files, extracts invoice data, and creates corresponding PDF invoices. This tool can be especially useful for automating the process of generating invoices from spreadsheet data.

## Features

- **Excel to PDF Conversion**: Converts Excel invoice files into PDF invoices.

- **Custom Invoice Formatting**: Configures the PDF invoice format, including the company name, logo, and total sum calculation.

- **Batch Processing**: Converts multiple Excel invoice files into PDFs in a batch.

## How It Works

1. Place your Excel invoice files in the "invoices" folder. The script will process all Excel files in this folder.

2. Run the script using Python.

3. For each Excel invoice file, the script reads the data from "Sheet 1."

4. It extracts the invoice number and date from the filename.

5. The script creates a PDF invoice with the extracted data, including a header, invoice details, and a total sum.

6. The PDF invoices are saved in the "PDFs" folder with filenames based on the original Excel file names.

7. The script continues to process all the Excel files in the "invoices" folder.

## Prerequisites

Before using this script, ensure you have the following:

- Python installed on your system.

- Required Python libraries: pandas, glob, fpdf, and pathlib. You can install these libraries using pip if not already installed.

- Excel invoice files in the "invoices" folder.

- A company name and logo (place the logo image as "python.png" in the same directory).

## Customization

- You can customize the PDF invoice format, including fonts, colors, and styling by modifying the script.

- To add additional details or data to your invoices, you can update the PDF generation logic within the script.

## Notes

- This script provides a straightforward way to automate the conversion of Excel invoices to PDF format. It can save time and effort for businesses and individuals who frequently generate invoices.

- Make sure your Excel files are correctly formatted and have data in "Sheet 1" for smooth processing.

- The script is set up to process Excel files in the "invoices" folder, but you can modify the directory path if needed.

- Feel free to extend the script's capabilities, such as sending the generated PDF invoices via email or integrating it into an existing invoicing system.

That's it! Use this script to simplify the process of generating PDF invoices from your Excel invoice data.

## License

This project is licensed under the MIT License. You are free to use and modify the code for your own purposes.
