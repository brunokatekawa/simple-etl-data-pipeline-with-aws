import pandas as pd

def extract_from_csv(file_path):
    # Extract data from a CSV file
    df = pd.read_csv(file_path)
    print("Data extracted!")
    return df