from data_extraction import extract_from_directory
from data_entry import enter_data_into_excel

def process_invoices(input_dir, output_file):
    # Extract data from invoices
    extracted_data = extract_from_directory(input_dir)
    
    # Enter data into an Excel file
    enter_data_into_excel(extracted_data, output_file)

if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description="Process invoices")
    parser.add_argument('--input_dir', required=True, help='Directory with invoice PDFs')
    parser.add_argument('--output_file', required=True, help='Output Excel file')
    args = parser.parse_args()

    process_invoices(args.input_dir, args.output_file)
