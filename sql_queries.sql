-- Superstore Analysis Queries
-- This file contains SQL queries for analyzing sales data from the Superstore dataset.
-- Each query aggregates data to provide insights into sales, profit, and discounts.


-- Query 1: Sales by region
SELECT region, SUM(sales)
FROM super_store_data
GROUP BY region;

-- Query 2: Sales by category
SELECT category, SUM(sales)
FROM super_store_data
GROUP BY category;

-- Query 3: Sales by top 5 sub-categories
SELECT sub_category, SUM(sales)
FROM super_store_data
GROUP BY sub_category
LIMIT 5;

-- Query 4: Sales by year-month
SELECT DATE_FORMAT(order_date, '%Y-%m'), SUM(sales)
FROM super_store_data
GROUP BY DATE_FORMAT(order_date, '%Y-%m');

-- Query 5: Profit by state
SELECT state, SUM(profit)
FROM super_store_data
GROUP BY state
ORDER BY SUM(profit) DESC;

-- Query 6: Quantity by category
SELECT category, SUM(quantity)
FROM super_store_data
GROUP BY category;

-- Query 7: Average sales per order by category
SELECT category, ROUND(SUM(sales)/COUNT(DISTINCT order_id), 2) AS average_sales_per_order
FROM super_store_data
GROUP BY category
ORDER BY average_sales_per_order DESC;

-- Query 8: Top 3 states by profit margin
SELECT state, ROUND((SUM(profit)/SUM(sales))*100, 2) AS profit_margin
FROM super_store_data
GROUP BY state
HAVING SUM(sales) > 0
ORDER BY profit_margin DESC
LIMIT 3;

--Query 9: Dynamic sales by region and month, implemented in sales_analysis.ipynb

-- Query 10: Orders with high discounts
SELECT category, COUNT(DISTINCT order_id) AS high_discount_orders
FROM super_store_data
WHERE discount > 0.2
GROUP BY category
ORDER BY high_discount_orders DESC;