from extract import extract_from_csv
from transform import transform_data
from load import load_to_rds
import config

def main():
    # Step 1: Extract
    df = extract_from_csv('titanic-dataset.csv')
    
    # Step 2: Transform
    df_transformed = transform_data(df)
    
    # Step 3: Load
    load_to_rds(df_transformed, config.db_config)

if __name__ == '__main__':
    main()
