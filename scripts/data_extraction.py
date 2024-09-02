import os
from pdfminer.high_level import extract_text

def extract_text_from_pdf(pdf_path):
    return extract_text(pdf_path)

def extract_from_directory(directory):
    extracted_data = []
    for filename in os.listdir(directory):
        if filename.endswith(".pdf"):
            file_path = os.path.join(directory, filename)
            text = extract_text_from_pdf(file_path)
            # Example extraction logic - adjust based on actual PDF content
            data = {
                "invoice_number": extract_invoice_number(text),
                "date": extract_date(text),
                "amount": extract_amount(text)
            }
            extracted_data.append(data)
    return extracted_data

def extract_invoice_number(text):
    # Placeholder logic; update with actual extraction logic
    # Example: extract invoice number from the text
    import re
    match = re.search(r'Invoice Number:\s*(\S+)', text)
    return match.group(1) if match else 'Unknown'

def extract_date(text):
    # Placeholder logic; update with actual extraction logic
    import re
    match = re.search(r'Date:\s*([\d-]+)', text)
    return match.group(1) if match else 'Unknown'

def extract_amount(text):
    # Placeholder logic; update with actual extraction logic
    import re
    match = re.search(r'Amount:\s*\$([\d.]+)', text)
    return match.group(1) if match else '0.00'
