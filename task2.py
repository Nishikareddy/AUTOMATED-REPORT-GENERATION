import pandas as pd
from fpdf import FPDF

# Read CSV data
data = pd.read_csv("data.csv")

# Perform analysis
average_score = data["Score"].mean()
highest_score = data["Score"].max()
lowest_score = data["Score"].min()
topper = data.loc[data["Score"].idxmax(), "Name"]

# Create PDF Report
pdf = FPDF()
pdf.add_page()

# Title
pdf.set_font("Arial", 'B', 16)
pdf.cell(0, 10, "Student Score Report", ln=True, align="C")

pdf.set_font("Arial", '', 12)
pdf.ln(10)

# Summary Section
pdf.cell(0, 10, f"Average Score: {average_score:.2f}", ln=True)
pdf.cell(0, 10, f"Highest Score: {highest_score}", ln=True)
pdf.cell(0, 10, f"Lowest Score: {lowest_score}", ln=True)
pdf.cell(0, 10, f"Topper: {topper}", ln=True)

pdf.ln(10)
pdf.set_font("Arial", 'B', 12)
pdf.cell(0, 10, "Detailed Scores:", ln=True)

# Table Header
pdf.set_font("Arial", 'B', 11)
pdf.cell(40, 10, "Name", 1)
pdf.cell(40, 10, "Subject", 1)
pdf.cell(40, 10, "Score", 1)
pdf.ln()

# Table Rows
pdf.set_font("Arial", '', 11)
for index, row in data.iterrows():
    pdf.cell(40, 10, row["Name"], 1)
    pdf.cell(40, 10, row["Subject"], 1)
    pdf.cell(40, 10, str(row["Score"]), 1)
    pdf.ln()

# Save the report
pdf.output("sample_report.pdf")

print("✅ PDF report generated: sample_report.pdf")
