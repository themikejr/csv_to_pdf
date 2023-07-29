import os
import csv
import pdfkit

# import cups

# Set options
options = {
    "page-size": "Letter",
    "margin-top": "0.75in",
    "margin-right": "0.75in",
    "margin-bottom": "0.75in",
    "margin-left": "0.75in",
    "encoding": "UTF-8",
}

INPUT_DIR = "/Users/themikejr/Downloads/vbs-csv"
OUTPUT_DIR = "./output"

for csv_file in os.listdir(INPUT_DIR):
    if csv_file.endswith(".csv"):
        # Read CSV file
        with open(os.path.join(INPUT_DIR, csv_file), encoding="utf-8") as file:
            csv_reader = csv.reader(file)

            # Generate HTML
            html = "<html><head></head><body>"
            html += '<table style="border: 1px solid black;">'
            for row in csv_reader:
                html += "<tr>"
                for col in row:
                    html += f'<td style="padding: 8px; margin-left: 2px">{col}</td>'
                html += "</tr>"
            html += "</table></body></html>"

        # Generate PDF from HTML
        pdf_path = f"{OUTPUT_DIR}/{csv_file.replace('.csv', '.pdf')}"
        pdfkit.from_string(html, pdf_path, options=options)

print("CSV to PDF conversion complete!")
