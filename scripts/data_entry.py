import pandas as pd

def enter_data_into_excel(data, output_file):
    df = pd.DataFrame(data)
    df.to_excel(output_file, index=False)
