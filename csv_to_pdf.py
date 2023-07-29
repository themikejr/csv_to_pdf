import os
import csv
import pdfkit

# import cups

# Set options
options = {
    "page-width": "11.00in",
    "page-height": "8.50in",
    "margin-top": "0.75in",
    "margin-right": "0.75in",
    "margin-bottom": "0.75in",
    "margin-left": "0.75in",
    "encoding": "UTF-8",
}

INPUT_DIR = "/Users/themikejr/Downloads/vbs-csv"
OUTPUT_DIR = "./output"

CSS = "styles.css"

for csv_file in os.listdir(INPUT_DIR):
    if csv_file.endswith(".csv"):
        with open(os.path.join(INPUT_DIR, csv_file), encoding="utf-8") as file:
            csv_reader = csv.reader(file)
            csv_data = list(csv_reader)
            group_name = csv_data[1][3]

            headers = csv_data[0]

            remove_cols = ["Family Manager Email", "Group Name"]

            indexes_to_remove = [headers.index(col) for col in remove_cols]

            html = "<html><head></head><body>"
            html += f"<h1>{group_name}</h1>"
            html += '<table style="border: 1px solid black; border-spacing: 8px 12px; border-collapse: collapse;">'

            html += "<tr>"
            for idx, h in enumerate(headers):
                if idx in indexes_to_remove:
                    continue
                else:
                    html += f'<th style="border: 1px solid black; padding: 8px; padding-top: 12px; padding-bottom: 12px;" align="left"><strong>{h}</strong></th>'

            html += "</tr>"

            for row in csv_data[1:]:
                for idx in sorted(indexes_to_remove, reverse=True):
                    del row[idx]

                html += '<tr style="margin-bottom: 20px; border: 1px solid black;">'
                for col in row:
                    html += (
                        f'<td style="border: 1px solid black; padding: 8px">{col}</td>'
                    )
                html += "</tr>"

            html += "</table></body></html>"

        # Generate PDF from HTML
        pdf_path = f"{OUTPUT_DIR}/{csv_file.replace('.csv', '.pdf')}"
        pdfkit.from_string(html, pdf_path, options=options, css=CSS)

print("CSV to PDF conversion complete!")
