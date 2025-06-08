# Superstore Sales Analysis

This is my data analysis project using Python and SQL. I used the Superstore dataset to analyze sales and profits, and made some charts with Matplotlib. It was a fun way to learn MySQL and Pandas!

## What's in the Project
- `sql_queries.sql`: SQL queries to analyze sales, profits, and discounts.
- `db_setup.py`: Sets up the MySQL database and loads the Superstore data.
- `sales_analysis.ipynb`: Jupyter notebook that runs the queries and makes charts.
- `Superstore-data.csv`: The dataset (download from Kaggle, e.g., https://www.kaggle.com/datasets/vivek468/superstore-dataset-final).

## What You Need
1. Python: I used Python 3.13, but 3.8+ should work.
2. MySQL: Ensure MySQL is installed and running. Download MySQL Community Edition from https://dev.mysql.com/downloads/ if needed.
3. Python Packages: Install with `pip install mysql-connector-python sqlalchemy pandas matplotlib`.
4. Dataset: Place `Superstore-data.csv` in the same folder as the other files.

## How to Run It
1. Download this project from GitHub.
2. Place `sql_queries.sql`, `db_setup.py`, `sales_analysis.ipynb`, and `Superstore-data.csv` in the same folder.
3. In your terminal, navigate to the project folder and run `jupyter notebook` to open the notebook.
4. Open `sales_analysis.ipynb` and run all cells.
5. Enter your MySQL username, password, host (usually localhost), and database name when asked.
6. Pick a region (Central, East, South, West) for the last query.
7. The notebook will display query results and save three charts: `sales_by_category.png`, `profit_by_state.png`, and `profit_margin_by_state.png` in the project folder.

## Notes
- Ensure MySQL is running before starting (e.g., start the server via MySQL Workbench).
- The CSV must be in the subfolder `data` and in the sae  folder as the other files, or the code won’t find it.

Thanks , I'm learning data analysis, and this was a great way to practice.
