from sqlalchemy import create_engine

def load_to_rds(df, db_config):
    # Create a connection to the RDS database
    print('Connecting to database...')
    engine = create_engine(f"postgresql://{db_config['username']}:{db_config['password']}@{db_config['endpoint']}:{db_config['port']}/{db_config['database']}")
    
    # Load data into the RDS table
    print('Loading data...')
    df.to_sql('users', engine, if_exists='replace', index=False)
    print("Data loaded successfully!")
