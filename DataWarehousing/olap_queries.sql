-- ============================================
-- OLAP QUERIES FOR RETAIL DATA WAREHOUSE
-- ============================================

------------------------------------------------
-- 1. ROLL-UP QUERY
-- Total sales by country and quarter
------------------------------------------------
SELECT
    c.country,
    CASE
        WHEN strftime('%m', f.Date) BETWEEN '01' AND '03' THEN 'Q1'
        WHEN strftime('%m', f.Date) BETWEEN '04' AND '06' THEN 'Q2'
        WHEN strftime('%m', f.Date) BETWEEN '07' AND '09' THEN 'Q3'
        WHEN strftime('%m', f.Date) BETWEEN '10' AND '12' THEN 'Q4'
    END AS quarter,
    SUM(f.total_sales) AS total_sales
FROM SalesFact f
JOIN CustomerDim c ON f.customer_id = c.customer_id
GROUP BY c.country, quarter
ORDER BY c.country, quarter;


------------------------------------------------
-- 2. DRILL-DOWN QUERY
-- Sales details for a specific country by month
-- Change 'UK' to any country in your dataset
------------------------------------------------
SELECT
    c.country,
    strftime('%Y', f.Date) AS year,
    strftime('%m', f.Date) AS month,
    SUM(f.total_sales) AS monthly_sales
FROM SalesFact f
JOIN CustomerDim c ON f.customer_id = c.customer_id
WHERE c.country = 'UK'   -- change to Kenya, USA, Germany, etc.
GROUP BY c.country, year, month
ORDER BY year, month;

------------------------------------------------
-- 3. SLICE QUERY
-- Total sales for the Electronics category
------------------------------------------------
SELECT 
    p.category,
    SUM(f.total_sales) AS electronics_sales
FROM SalesFact f
JOIN dim_product p ON f.product_id = p.product_id
WHERE p.category = 'Electronics'
GROUP BY p.category;