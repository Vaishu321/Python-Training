CREATE DATABASE retail_db;
USE retail_db;

CREATE TABLE customers (
customer_id INT PRIMARY KEY,
customer_name VARCHAR(50),
email VARCHAR(80),
city VARCHAR(50)
);

CREATE TABLE orders (
order_id INT PRIMARY KEY,
order_date DATE,
customer_id INT NULL,
total_amount DECIMAL(10,2),
product_id INT NULL
);

CREATE TABLE products (
product_id INT PRIMARY KEY,
product_name VARCHAR(100),
category VARCHAR(50),
price DECIMAL(10,2)
);

INSERT INTO customers VALUES
(1, 'Aisha Khan', 'aisha@xyz.com', 'Mumbai'),
(2, 'Rahul Sharma', 'rahul@xyz.com', 'Delhi'),
(3, 'John Daniel', 'john@xyz.com', 'Bangalore'),
(4, 'Meera Iyer', 'meera@xyz.com', 'Chennai'),
(5, 'Sanjay Patel', 'sanjay@xyz.com', 'Hyderabad');

INSERT INTO products VALUES
(101, 'Laptop HP 15', 'Electronics', 52000),
(102, 'Samsung Phone A54', 'Electronics', 28000),
(103, 'Jeans Blue Fit', 'Fashion', 1500),
(104, 'T-Shirt Classic', 'Fashion', 700),
(105, 'Wireless Mouse', 'Accessories', 900),
(106, 'Rice 5KG Bag', 'Groceries', 320),
(107, 'Olive Oil 1L', 'Groceries', 540),
(108, 'Printer Canon G2012', 'Electronics', 12500);

INSERT INTO orders VALUES
(1001, '2024-01-05', 1, 52000, 101),
(1002, '2024-01-06', 2, 28000, 102),
(1003, '2024-01-07', 3, 1500, 103),
(1004, '2024-01-07', 1, 700, 104),
(1005, '2024-01-08', 2, 900, 105),
(1006, '2024-01-08', NULL, 320, 106), -- customer unknown
(1007, '2024-01-09', 1, 540, NULL), -- product unknown
(1008, '2024-01-10', 3, 12500, 108),
(1009, '2024-01-10', 4, 320, 106),
(1010, '2024-01-11', NULL, 700, 104), -- customer null
(1011, '2024-01-12', 2, 540, 107); -- product exists but never order

-- SECTION A: INNER JOIN (10)
-- 1. List all orders with customer names and email.

SELECT o.order_id, c.customer_name, c.email
FROM orders o
INNER JOIN customers c
ON c.customer_id=o.customer_id;

-- 2. Show product name, category, price for every ordered product.
SELECT  o.order_id, o.product_id, p.product_name, p.category , p.price 
FROM orders o
INNER JOIN products p
ON p.product_id=o.product_id;

-- 3. List all orders with customer name and product name.
SELECT  c.customer_id, o.order_id, c.customer_name, p.product_name
FROM customers c
INNER JOIN orders o
ON c.customer_id=o.customer_id
INNER JOIN products p
ON o.product_id=p.product_id;

-- 4. Show customer name and total_amount for all valid customer orders.
SELECT o.order_id, c.customer_name, o.total_amount
FROM customers c
INNER JOIN orders o
ON c.customer_id = o.customer_id;
-- 5. List all Electronics products that have been ordered.
SELECT o.order_id, p.product_name, p.category
FROM products p
INNER JOIN orders o
ON o.product_id=p.product_id
WHERE p.category="Electronics";

-- 6. Find customers who ordered Fashion products.
SELECT o.order_id, p.product_name,c.customer_name, p.category
FROM products p
INNER JOIN orders o
ON o.product_id=p.product_id
INNER JOIN customers c
ON c.customer_id = o.customer_id
WHERE p.category="Fashion";

-- 7. Show all orders above 1000 with customer and product details.
SELECT o.order_id, p.product_name,c.customer_name, p.price
FROM products p
INNER JOIN orders o
ON o.product_id=p.product_id
INNER JOIN customers c
ON c.customer_id = o.customer_id
WHERE p.price>1000;

-- 8. Show customers from Mumbai who placed at least one order.
SELECT c.customer_name, c.city
FROM customers c
INNER JOIN orders o
ON c.customer_id = o.customer_id
WHERE c.city="Mumbai";

-- 9. Show number of orders per customer (using INNER JOIN + GROUP BY).
SELECT c.customer_id, 
		COUNT(o.order_id) AS Total_Orders, 
        c.customer_name
FROM customers c
INNER JOIN orders o
ON c.customer_id=o.customer_id
GROUP BY customer_id;

-- 10. List all customers and the total amount they have spent.
SELECT  c.customer_id, 
        c.customer_name,
        SUM(p.price) AS Total_amount
FROM customers c
INNER JOIN orders o
ON c.customer_id=o.customer_id
INNER JOIN products p
ON p.product_id=o.product_id
GROUP BY c.customer_id;

-- SECTION B: LEFT JOIN (Orders → Customers)
-- 11. Show all orders, even those without customer info.
SELECT o.order_id, c.customer_name, o.total_amount
FROM orders o
LEFT JOIN customers c
ON c.customer_id=o.customer_id;

-- 12. Find all orders where customer_id is NULL.
SELECT * 
FROM orders 
WHERE customer_id IS NULL;

-- 13. Display orders with customer city (NULL when customer is missing).
SELECT o.order_id, c.customer_name, c.city
FROM orders o
LEFT JOIN customers c
ON o.customer_id=c.customer_id;

-- 14. Show all customer names and the number of orders they placed (include zero).
SELECT c.customer_name, 
	   COUNT(o.order_id) AS total_orders
FROM customers c
LEFT JOIN orders o
ON c.customer_id=o.customer_id
GROUP BY(c.customer_id);

-- 15. Show customers who have not placed ANY order.
SELECT c.customer_name, 
	   COUNT(o.order_id) AS total_orders
FROM customers c
LEFT JOIN orders o
USING (customer_id)
WHERE o.order_id IS NULL
GROUP BY(c.customer_id);

-- 16. Show all orders and label missing customers as “Guest Checkout”.
SELECT o.order_id, IFNULL(c.customer_name,"Guest Checkout") AS Customer_name, o.total_amount
FROM orders o
LEFT JOIN customers c
ON c.customer_id=o.customer_id;

-- 17. Show orders that have missing product details.
SELECT o.order_id, o.order_date, o.total_amount
FROM orders o
LEFT JOIN products p 
ON o.product_id = p.product_id
WHERE p.product_id IS NULL;
-- 18.  Show orders placed by customers from Delhi or missing customer info.
SELECT o.order_id, o.order_date, o.total_amount, c.city
FROM orders o
LEFT JOIN customers c 
ON o.customer_id = c.customer_id
WHERE c.city = 'Delhi' OR c.customer_id IS NULL;
-- 19. Count total orders including ones without customer linkage.
SELECT COUNT(*) AS total_orders
FROM orders;
-- 20. Show the percentage of orders with missing customers.

SELECT COUNT(*)*100.0/(SELECT COUNT(*) FROM orders) AS percent_of_orders
FROM orders o
LEFT JOIN customers c 
ON o.customer_id = c.customer_id
WHERE c.customer_id IS NULL;

-- 21. Show all products and the orders associated with them (NULL for unused products).
SELECT p.product_name, o.order_id, o.order_date
FROM products p
RIGHT JOIN orders o 
ON p.product_id = o.product_id;
-- 22.  List products that have never been ordered
SELECT p.product_id, p.product_name
FROM orders o
RIGHT JOIN products p 
ON p.product_id = o.product_id
WHERE o.order_id IS NULL;
-- 23. Show Electronics products and the number of times they were ordered.
SELECT p.product_name, COUNT(o.order_id)
FROM orders o
RIGHT JOIN products p 
ON p.product_id = o.product_id
WHERE p.category = 'Electronics'
GROUP BY p.product_name;
-- 24. Show Groceries products and their rst order date.
SELECT p.product_name, MIN(o.order_date) AS first_order_date
FROM orders o
RIGHT JOIN products p 
ON p.product_id = o.product_id
WHERE p.category = 'Groceries'
GROUP BY p.product_name;
-- 25. List all products with their total sales, including those with zero sales.
SELECT p.product_name, SUM(o.total_amount) AS total_sales
FROM orders o
RIGHT JOIN products p ON p.product_id = o.product_id
GROUP BY p.product_name;
-- 26. For each category, show number of ordered products (include zero).
SELECT p.category, COUNT(DISTINCT o.product_id) AS ordered_products
FROM orders o
RIGHT JOIN products p ON p.product_id = o.product_id
GROUP BY p.category;
-- 27. Show products that were ordered by customers from Bangalore.
SELECT DISTINCT p.product_name
FROM (orders o
      INNER JOIN customers c ON o.customer_id = c.customer_id)
RIGHT JOIN products p ON p.product_id = o.product_id
WHERE c.city = 'Bangalore' AND o.order_id IS NOT NULL;

-- 28. Show products missing from order table (never sold).
SELECT p.product_id, p.product_name
FROM orders o
RIGHT JOIN products p ON p.product_id = o.product_id
WHERE o.order_id IS NULL;
-- 29. Show the count of orders grouped by product name (including zero).
SELECT p.product_name, COUNT(o.order_id) AS order_count
FROM orders o
RIGHT JOIN products p ON p.product_id = o.product_id
GROUP BY p.product_name;

-- 30. Show products that appeared in at least one NULL customer order.
SELECT DISTINCT p.product_name
FROM orders o
RIGHT JOIN products p ON p.product_id = o.product_id
WHERE o.customer_id IS NULL;


