SELECT * FROM superstore;

ALTER TABLE superstore
CHANGE `Row ID` row_id INT;
ALTER TABLE superstore
CHANGE `Order ID` order_id varchar(255);
ALTER TABLE superstore
CHANGE `Customer ID` customer_id varchar(255);
ALTER TABLE superstore
CHANGE `Customer Name` customer_name varchar(255);
ALTER TABLE superstore
CHANGE `Sub-Category` Sub_Category text;
ALTER TABLE superstore
CHANGE `Order Date` order_date text;
ALTER TABLE superstore
CHANGE `Ship Date` ship_date text;
ALTER TABLE superstore
CHANGE `Product ID` product_id text;
ALTER TABLE superstore
CHANGE `Product Name` product_name text;
ALTER TABLE superstore
CHANGE `Postal Code` postal_code INT;
ALTER TABLE superstore
CHANGE `Ship Mode` ship_mode text;

#checked the duplicates values
SELECT order_id, product_id,COUNT(*) FROM superstore
GROUP BY order_id, product_id
HAVING COUNT(*) > 1;

#delete duplicate records
SET SQL_SAFE_UPDATES = 0;
DELETE FROM superstore
WHERE row_id IN (5367, 3406);
SET SQL_SAFE_UPDATES = 1;

#1 Total Sales, Quantity, and Profit
SELECT ROUND(SUM(Sales),2) AS total_sales,
ROUND(SUM(Quantity),2) AS total_Quantity,
ROUND(SUM(Profit),2) AS total_Profit FROM superstore;

#2. Unique Customers Whose make any order
SELECT COUNT(DISTINCT(customer_id)) AS 'unique_customers'
FROM superstore;

#3. Top 5 Customers by Total Sales
SELECT customer_id,MAX(customer_name),ROUND(SUM(Sales),2) AS Total_sales FROM superstore
GROUP BY customer_id
ORDER BY SUM(Sales) DESC LIMIT 5;SELECT customer_id,MAX(customer_name) AS 'Customer name',
ROUND(SUM(Sales),2) AS 'Total sales'
FROM superstore
GROUP BY customer_id
ORDER BY 'Total sales' DESC LIMIT 5;

#4. Total Sales by City
SELECT City,
ROUND(SUM(Sales),2) AS 'Sales'
FROM superstore
GROUP BY City
ORDER BY SUM(Sales) DESC;

#5. Sales & Profit by Category
SELECT Category,
ROUND(SUM(Sales),2) AS 'Total_sales',
ROUND(SUM(Profit),2) AS 'Total_profit'  FROM superstore
GROUP BY Category
ORDER BY Total_sales DESC;

#6. Monthly Sales Trend
SELECT MONTHNAME(STR_TO_DATE(order_date,'%m/%d/%Y')) AS month_name,
ROUND(SUM(Sales),2) As total_sales FROM superstore
GROUP BY month_name
ORDER BY total_sales DESC;


#7. Orders with High Discount(>50%) but Negative Profit
SELECT order_id, Discount,Profit FROM Superstore
WHERE Discount > 0.5 AND Profit < 0;

#8. Top 5 Selling Products (by Quantity)
SELECT product_id ,
SUM(Quantity) AS 'Quantity' FROM superstore
GROUP BY product_id
ORDER BY Quantity  DESC LIMIT 5;

#9. Total Profit & Sales by Region and Segment
SELECT Region, Segment,
ROUND(SUM(Sales),2) AS 'Total_sales',
SUM(Profit) AS 'Total_profit' FROM superstore
GROUP BY Region, Segment
ORDER BY 'Total_sales' DESC;

#10 Top 3 Most Profitable Products per Category
WITH Ranked_product AS
(SELECT Category, MIN(product_name),
SUM(Profit) AS 'Total_profit',
RANK() OVER(PARTITION BY Category ORDER BY SUM(Profit) DESC) AS 'rnk'
FROM superstore
GROUP BY Category , product_id
ORDER BY SUM(Profit) DESC)
SELECT * FROM Ranked_product
WHERE rnk <= 3
ORDER BY rnk;

#11 Running Total of Sales by Order Date
SELECT order_date,
ROUND(SUM(SALES),2) AS 'Daily_total_sales',
SUM(SUM(Sales)) OVER(ORDER BY order_date )  AS 'Running_Total_Sales'
FROM superstore
GROUP BY order_date
ORDER BY SUM(SALES) DESC;

#12 Discount Impact Analysis (Subquery) When we give above-average discounts, do we still make a profit?
SELECT ROUND(AVG(Discount),2),
ROUND(AVG(Profit),2)
FROM superstore
WHERE Discount > (
SELECT AVG(Discount) FROM superstore
);

#13 Products with High Sales but Low Profit Margins
SELECT product_name,ROUND(SUM(Sales),2) AS 'Total_sales',
ROUND(SUM(Profit),2) AS 'Total_profit',
ROUND((SUM(Profit) / SUM(Sales))*100,2) AS "Profit_Margins"
FROM superstore
GROUP BY product_id, product_name
HAVING Profit_Margins<5 AND Total_sales>5000
ORDER BY Total_sales DESC;

#14 Track how profitable each customer segment is over time.
SELECT YEAR(STR_TO_DATE(order_date,'%d/%m/%Y')) AS 'Year', Segment,
ROUND(SUM(Sales),2) AS 'Total_sales'
FROM superstore
GROUP BY YEAR(STR_TO_DATE(order_date,'%d/%m/%Y')), Segment
ORDER BY Year LIMIT 3,50;

#15 Negative Profit Detection
SELECT product_name,
ROUND(SUM(SALES),2) AS 'Total_sales',
ROUND(SUM(Profit),2)  AS 'Total_profit'
FROM superstore
GROUP BY product_id, product_name
HAVING Total_profit < 0 ;

#16 FIND customer whose make order less than 4
SELECT customer_id,ROUND(SUM(SALES),2) AS 'Total_sales',
COUNT(DISTINCT(order_id)) AS 'Number_of_orders' FROM superstore
GROUP BY customer_id
HAVING Number_of_orders < 4
ORDER BY Number_of_orders;

#17 Which products have a higher than average sales value?
SELECT product_name ,
ROUND(SUM(Sales),2) 'Total_sales'
FROM superstore
GROUP BY product_id,product_name
HAVING  SUM(Sales) > (SELECT AVG(Total_sales) FROM
(
SELECT product_id,product_name,SUM(Sales) AS 'Total_sales' FROM superstore
GROUP BY product_id,product_name
) AS Poduct_sales);

#18 Which regions have total sales above the average sales of all regions?
SELECT Region, ROUND(SUM(Sales),2) AS 'Total_sales' FROM superstore
GROUP BY Region
HAVING SUM(Sales) > (
SELECT AVG(Total_sales) FROM (
SELECT Region,SUM(Sales) AS 'Total_sales' FROM superstore
GROUP BY Region ) AS Total_sales_region)
ORDER BY Total_sales DESC;

#19 Year-over-Year Sales Growth
SELECT YEAR(str_to_date(order_date,'%m/%d/%Y')) AS 'Year' ,
ROUND(SUM(Sales),2) AS 'Total_sales'
FROM superstore
GROUP BY YEAR(str_to_date(order_date,'%m/%d/%Y'))
ORDER BY Total_sales DESC;

#20 Which Shipping Mode Delivers Fastest
SELECT ship_mode, ROUND(AVG(DATEDIFF(STR_TO_DATE(ship_date, '%m/%d/%Y'),
    STR_TO_DATE(order_date, '%m/%d/%Y')))) AS days_difference
FROM superstore
GROUP BY ship_mode
ORDER BY days_difference ASC;

#21 Total sales by regions
SELECT Region,
ROUND(SUM(Sales),2) AS 'Total sales'
FROM superstore
GROUP BY Region
ORDER BY 'Total sales' DESC;
