from fpdf import FPDF
import os

def create_invoice(pdf_path, invoice_number, date, amount):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)

    pdf.cell(200, 10, txt=f"Invoice Number: {invoice_number}", ln=True)
    pdf.cell(200, 10, txt=f"Date: {date}", ln=True)
    pdf.cell(200, 10, txt=f"Amount: ${amount}", ln=True)

    pdf.output(pdf_path)

def generate_invoices(output_dir):
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    invoices = [
        {"invoice_number": "INV001", "date": "2024-01-01", "amount": "1000.00"},
        {"invoice_number": "INV002", "date": "2024-06-02", "amount": "1500.00"},
        {"invoice_number": "INV003", "date": "2024-12-03", "amount": "2000.00"}
    ]

    for invoice in invoices:
        pdf_path = os.path.join(output_dir, f"{invoice['invoice_number']}.pdf")
        create_invoice(pdf_path, invoice["invoice_number"], invoice["date"], invoice["amount"])

if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description="Generate sample invoices")
    parser.add_argument('--output_dir', required=True, help='Directory to save generated PDF invoices')
    args = parser.parse_args()

    generate_invoices(args.output_dir)
