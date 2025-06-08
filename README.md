# Superstore Sales Analysis

I created this project to learn data analysis by exploring the Superstore dataset, a Kaggle dataset, with Python and SQL. I used Pandas to load and analyze sales and profit data, set up databases and tables with MySQL, extracted valuable information with SQL queries, and visualized results with Matplotlib plots using Jupyter Notebook. Through this, I gained skills in data handling, database management, and data visualization.

## What's in the Project
- `sql_queries.sql`: SQL queries to analyze sales, profits, and discounts.
- `db_setup.py`: Sets up the MySQL database and loads the Superstore data.
- `superstore_sales_analysis.ipynb`: Jupyter notebook that runs the queries and makes charts.
- `data/Superstore-data.csv`: The dataset (included; update from Kaggle at https://www.kaggle.com/datasets/vivek468/superstore-dataset-final if needed).

## How to Run It
1. Install Python 3.8+ and packages: `pip install mysql-connector-python sqlalchemy pandas matplotlib`.
2. Ensure all files (`sql_queries.sql`, `db_setup.py`, `superstore_sales_analysis.ipynb`) and the `data` folder are in one project folder.
3. Run `jupyter notebook` in the terminal, then open `superstore_sales_analysis.ipynb` and run all cells.
4. Enter your MySQL username, password, host (usually localhost), and database name when asked.
5. Pick a region (Central, East, South, West) for the last query.
6. Check `output plots/` for charts (`sales_by_category.png`, `profit_by_state.png`, `profit_margin_by_state.png`).

## Notes
- Start MySQL (e.g., via Workbench) before running.
- Keep `Superstore-data.csv` in the `data` subfolder; charts save to `output plots/`.
