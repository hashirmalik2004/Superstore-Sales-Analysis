import pandas as pd
from sqlalchemy import create_engine, text
import mysql.connector
    # Sets up a MySQL database for the Superstore dataset.
    # Creates a database, a table for the data, and loads data from a CSV file.
def setup_database():
    user = input("Enter MySQL username: ")
    password = input("Enter MySQL password: ")
    host = input("Enter MySQL host (default: localhost): ") or 'localhost'
    database = input("Enter database name: ") or 'sales_db'
    
    # Connect to MySQL to create database
    conn = mysql.connector.connect(user=user, password=password, host=host)
    cursor = conn.cursor()
    cursor.execute(f"CREATE DATABASE IF NOT EXISTS {database}")
    conn.close()

    # Set up engine for the database
    engine = create_engine(f'mysql+mysqlconnector://{user}:{password}@{host}/{database}')

    # Create table query
    create_table_query = """
    CREATE TABLE IF NOT EXISTS super_store_data (
        row_id BIGINT,
        order_id TEXT,
        order_date DATETIME,
        ship_date TEXT,
        ship_mode TEXT,
        customer_id TEXT,
        customer_name TEXT,
        segment TEXT,
        country TEXT,
        city TEXT,
        state TEXT,
        postal_code BIGINT,
        region TEXT,
        product_id TEXT,
        category TEXT,
        sub_category TEXT,
        product_name TEXT,
        sales DOUBLE,
        quantity BIGINT,
        discount DOUBLE,
        profit DOUBLE
    )
    """
    with engine.connect() as connection:
        connection.execute(text(create_table_query))  # Wrap query with text()

    # Load CSV data
    csv_path = "data\Superstore-data.csv"
    df = pd.read_csv(csv_path, encoding="cp1252")
    df.columns = [c.lower().replace(" ", "_").replace("-", "_") for c in df.columns]
    df["order_date"] = pd.to_datetime(df["order_date"], dayfirst=False, errors="coerce")
    df.to_sql(name="super_store_data", con=engine, if_exists="replace", index=False)
    print("Data loaded into table successfully.")
    return engine