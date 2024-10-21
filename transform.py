def transform_data(df):
    # Clean the data, e.g., drop rows with missing data
    # We'll drop 'Cabin' column as it has too many null values
    df_cleaned = df.drop('Cabin', axis=1).dropna() 
    
    # Select specific columns
    df_transformed = df_cleaned[['Name', 'Age']]

    print('Data transformed!')
    
    return df_transformed
