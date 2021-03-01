# SQL Practices - `SELECT`

Practices set resources are referenced from **[w3resource.com](https://www.w3resource.com)** 

- [SQL Exercises, Practice, Solution - Retrieve data from tables](https://www.w3resource.com/sql-exercises/sql-retrieve-from-table.php)
- [SQL Exercises, Practice, Solution - Using Boolean and Relational operators](https://www.w3resource.com/sql-exercises/sql-boolean-operators.php)
- All practice set and answers are written in PostgreSQL

* * *

# Sample Tables

### `salesman`
  
| salesman_id | name       | city     | commission |
|-------------|------------|----------|------------|
| 5001        | James Hoog | New York | 0.15       |
| 5002        | Nail Knite | Paris    | 0.13       |
| 5005        | Pit Alex   | London   | 0.11       |
| 5006        | Mc Lyon    | Paris    | 0.14       |
| 5007        | Paul Adam  | Rome     | 0.13       |
| 5003        | Lauson Hen | San Jose | 0.12       |	  

&nbsp

### `orders`
	
| ord_no | purch_amt |  ord_date  | customer_id | salesman_id |
|:------:|:---------:|:----------:|:-----------:|:-----------:|
| 70001  | 150.5     | 2012-10-05 | 3005        | 5002        |
| 70009  | 270.65    | 2012-09-10 | 3001        | 5005        |
| 70002  | 65.26     | 2012-10-05 | 3002        | 5001        |
| 70004  | 110.5     | 2012-08-17 | 3009        | 5003        |
| 70007  | 948.5     | 2012-09-10 | 3005        | 5002        |
| 70005  | 2400.6    | 2012-07-27 | 3007        | 5001        |
| 70008  | 5760      | 2012-09-10 | 3002        | 5001        |
| 70010  | 1983.43   | 2012-10-10 | 3004        | 5006        |
| 70003  | 2480.4    | 2012-10-10 | 3009        | 5003        |
| 70012  | 250.45    | 2012-06-27 | 3008        | 5002        |
| 70011  | 75.29     | 2012-08-17 | 3003        | 5007        |
| 70013  | 3045.6    | 2012-04-25 | 3002        | 5001        |

&nbsp

### `customer`

| customer_id | cust_name      | city       | grade | salesman_id |
|-------------|----------------|------------|-------|-------------|
| 3002        | Nick Rimando   | New York   | 100   | 5001        |
| 3007        | Brad Davis     | New York   | 200   | 5001        |
| 3005        | Graham Zusi    | California | 200   | 5002        |
| 3008        | Julian Green   | London     | 300   | 5002        |
| 3004        | Fabian Johnson | Paris      | 300   | 5006        |
| 3009        | Geoff Cameron  | Berlin     | 100   | 5003        |
| 3003        | Jozy Altidor   | Moscow     | 200   | 5007        |
| 3001        | Brad Guzan     | London     |       | 5005        |

&nbsp

### `nobel_win`

| year | subject    | winner                 | country | category       |
|------|------------|------------------------|---------|----------------|
| 1970 | Physics    | Hannes Alfven          | Sweden  | Scientist      |
| 1970 | Physics    | Louis Neel             | France  | Scientist      |
| 1970 | Chemistry  | Luis Federico Leloir   | France  | Scientist      |
| 1970 | Physiology | Julius Axelrod         | USA     | Scientist      |
| 1970 | Physiology | Ulf von Euler          | Sweden  | Scientist      |
| 1970 | Physiology | Bernard Katz           | Germany | Scientist      |
| 1970 | Literature | Aleksandr Solzhenitsyn | Russia  | Linguist       |
| 1970 | Economics  | Paul Samuelson         | USA     | Economist      |
| 1971 | Physics    | Dennis Gabor           | Hungary | Scientist      |
| 1971 | Chemistry  | Gerhard Herzberg       | Germany | Scientist      |
| 1971 | Peace      | Willy Brandt           | Germany | Chancellor     |
| 1971 | Literature | Pablo Neruda           | Chile   | Linguist       |
| 1971 | Economics  | Simon Kuznets          | Russia  | Economist      |
| 1978 | Peace      | Anwar al-Sadat         | Egypt   | President      |
| 1978 | Peace      | Menachem Begin         | Israel  | Prime Minister |
| 1994 | Peace      | Yitzhak Rabin          | Israel  | Prime Minister |
| 1987 | Physics    | Johannes Georg Bednorz | Germany | Scientist      |
| 1987 | Chemistry  | Donald J. Cram         | USA     | Scientist      |
| 1987 | Chemistry  | Jean-Marie Lehn        | France  | Scientist      |
| 1987 | Physiology | Susumu Tonegawa        | Japan   | Scientist      |
| 1987 | Literature | Joseph Brodsky         | Russia  | Linguist       |
| 1987 | Economics  | Robert Solow           | USA     | Economist      |
| 1994 | Literature | Kenzaburo Oe           | Japan   | Linguist       |
| 1994 | Economics  | Reinhard Selten        | Germany | Economist      |

&nbsp

### `item_mast`

| pro_id | pro_name         | pro_price | pro_com |
|--------|------------------|-----------|---------|
| 101    | Mother Board     | 3200.00   | 15      |
| 102    | Key Board        | 450.00    | 16      |
| 103    | ZIP drive        | 250.00    | 14      |
| 104    | Speaker          | 550.00    | 16      |
| 105    | Monitor          | 5000.00   | 11      |
| 106    | DVD drive        | 900.00    | 12      |
| 107    | CD drive         | 800.00    | 12      |
| 108    | Printer          | 2600.00   | 13      |
| 109    | Refill cartridge | 350.00    | 13      |
| 110    | Mouse            | 250.00    | 12      |

&nbsp

### `emp_details`

| emp_idno | emp_fname | emp_lname | emp_dept |
|----------|-----------|-----------|----------|
| 631548   | Alan      | Snappy    | 27       |
| 839139   | Maria     | Foster    | 57       |
| 127323   | Michale   | Robbin    | 57       |
| 526689   | Carlos    | Snares    | 63       |
| 843795   | Enric     | Dosio     | 57       |
| 328717   | Jhon      | Snares    | 63       |
| 444527   | Joseph    | Dosni     | 47       |
| 659831   | Zanifer   | Emily     | 47       |
| 847674   | Kuleswar  | Sitaraman | 57       |
| 748681   | Henrey    | Gabriel   | 47       |
| 555935   | Alex      | Manuel    | 57       |
| 539569   | George    | Mardy     | 27       |
| 733843   | Mario     | Saule     | 63       |

* * *

# Practice Questions

## 1. Simple `Select`
	        
### 1.1. Write a SQL statement to display all the information of all salesmen.

```sql
SELECT * FROM salesman;
```

### 1.2. Write a SQL statement to display specific columns like name and commission for all the salesmen.

```sql
SELECT name, commission FROM salesman;
```

### 1.3. Write a query to display the columns in a specific order like order date, salesman id, order number and purchase amount from for all the orders.

```sql
SELECT ord_date, salesman_id, ord_no, purch_amt FROM orders;
```

### 1.4. Write a query which will retrieve the value of salesman id of all salesmen, getting orders from the customers in orders table without any repeats. 

```sql
SELECT DISTINCT salesman_id FROM orders;
```

### 1.5. Write a SQL statement to display names and city of salesman, who belongs to the city of Paris.

```sql
SELECT name, city FROM salesman 
WHERE city = 'Paris';
```

### 1.6. Write a SQL statement to display all the information for those customers with a grade of 200.

```sql
SELECT * FROM Customer 
WHERE grade=200;
```

### 1.7. Write a SQL query to display the order number followed by order date and the purchase amount for each order which will be delivered by the salesman who is holding the ID 5001.

```sql
SELECT ord_date, ord_no, purch_amt FROM orders
WHERE salesman_id=5001;
```

### 1.8. Write a SQL query to display the Nobel prizes for 1970.

```sql
SELECT * FROM nobel_win WHERE YEAR=1970;
```

```sql
-- different interpretation of instruction
SELECT year,subject,winner FROM nobel_win 
WHERE year=1970; 
```

### 1.9. Write a SQL query to know the winner of the 1971 prize for Literature.

```sql
SELECT winner, country FROM nobel_win
WHERE year=1971 AND subject='Literature';
```


### 1.10. Write a SQL query to display the year and subject that won 'Dennis Gabor' his prize. 

```sql
SELECT year, subject FROM nobel_win 
WHERE winner='Dennis Gabor';
```

### 1.11. Write a SQL query to give the name of the 'Physics' winners since the year 1950.

```sql
SELECT winner FROM nobel_win 
WHERE subject='Physics' AND year>=1950;
```

### 1.12. Write a SQL query to Show all the details (year, subject, winner, country ) of the Chemistry prize winners between the year 1965 to 1975 inclusive.

```sql
SELECT year, subject, winner, counter FROM nobel_win
WHERE subect='Chemistry' AND year>=1965 AND year<=1975;
```

### 1.13. Write a SQL query to show all details of the Prime Ministerial winners after 1972 of Menachem Begin and Yitzhak Rabin.

```sql
SELECT * FROM nobel_win
WHERE category='Prime Minister' AND year > 1972;
```

```sql
-- different interpretation of instruction
SELECT * FROM nobel_win
WHERE year >1972
AND winner IN ('Menachem Begin', 'Yitzhak Rabin');
```


### 1.14. Write a SQL query to show all the details of the winners with first name Louis.

```sql
SELECT * FROM nobel_win
WHERE winner LIKE 'Louse %';
```


### 1.15. Write a SQL query to show all the winners in Physics for 1970 together with the winner of Economics for 1971.

```sql
SELECT * FROM nobel_win
WHERE subject='Physics' AND year=1970
UNION 
SELECT * FROM nobel_win
WHERE subject='Economics' AND year=1971;
```

### 1.16. Write a SQL query to show all the winners of nobel prize in the year 1970 except the subject Physiology and Economics.


```sql
SELECT * FROM nobel_win
WHERE year=1970 AND subject NOT IN ('Physiology', 'Economics');
```

### 1.17. Write a SQL query to show the winners of a 'Physiology' prize in an early year before 1971 together with winners of a 'Peace' prize in a later year on and after the 1974.

```sql
SELECT * FROM nobel_win
WHERE subject='Pysiology' AND year<1971
UNION
SELECT * FROM nobel_win
WHERE subject='Peace' AND year>1974;
```

### 1.18. Write a SQL query to find all details of the prize won by Johannes Georg Bednorz.

```sql
SELECT * FROM nobel_win
WHERE winner='Johannes Georg Bednorz;
```

### 1.19. Write a SQL query to find all the details of the nobel winners for the subject not started with the letter 'P' and arranged the list as the most recent comes first, then by name in order.

```sql
SELECT * FROM nobel_win
WHERE subject NOT LIKE 'P%'
ORDER BY year DESC, winner;
```

### 1.20. Write a SQL query to find all the details of 1970 winners by the ordered to subject and winner name; but the list contain the subject Economics and Chemistry at last.

```sql
SELECT * FROM nobel_win
WHERE year=1970
ORDER BY 
	CASE WHEN subject IN ('Economics', 'Chemistry') THEN 1 ELSE 0 END ASC,
	subject,
	winnerl;
```

### 1.21. Write a SQL query to find all the products with a price between Rs.200 and Rs.600.

```sql
SELECT * FROM item_mast
WHERE pro_price>=200 AND pro_price<=600;
```

```sql
-- better approach
SELECT * FROM item_mast
WHERE pro_price BETWEEN 200 AND  600;
```

### 1.22. Write a SQL query to calculate the average price of all products of the manufacturer which code is 16.

```sql
SELECT AVG(pro_price) FROM item_mast
WHERE pro_com=16;
```


### 1.23. Write a SQL query to find the item name and price in Rs.

```sql
SELECT 
	pro_name AS 'item name', 
	pro_price AS 'price in Rs'
	FROM item_mast;
```

### 1.24. Write a SQL query to display the name and price of all the items with a price is equal or more than Rs.250, and the list contain the larger price first and then by name in ascending order.

```sql
SELECT pro_name, pro_price FOM item_mast
WHERE pro_price>=250
ORDER BY pro_price desc, pro_name;
```

### 1.25. Write a SQL query to display the average price of the items for each company, showing only the company code.

```sql
SELECT AVG(pro_price), pro_com FROM item_mast
GROUP BY pro_com;
```

### 1.26. Write a SQL query to find the name and price of the cheapest item(s). 

```sql
SELECT pro_name, pro_price FROM item_mast
WHERE pro_price = (SELECT MIN(pro_price) from item_mast);
```


### 1.27. Write a query in SQL to find the last name of all employees, without duplicates.

```sql
SELECT DISTINCT emp_lname FROM emp_details;
```

### 1.28. Write a query in SQL to find the data of employees whose last name is 'Snares'.

```sql
SELECT * FROM emp_details WHERE emp_lname='Snares';
```

### 1.29. Write a query in SQL to display all the data of employees that work in the department 57.

```sql
SELECT * FROM emp_details WHERE emp_dept=57;
```


## 2. Boolean & Relational Operators

### 2.1. Write a query to display all customers with a grade above 100.

```sql
SELECT * FROM customer
WHERE grade > 100;
```

### 2.2. Write a query statement to display all customers in New York who have a grade value above 100.

```sql
SELECT * FROM customer
WHERE city = 'New York' AND grade > 100;
```

### 2.3. Write a SQL statement to display all customers, who are either belongs to the city New York or had a grade above 100.

```sql
SELECT * FROM customers
WHERE city = 'New York' OR grade > 100;
```


### 2.4. Write a SQL statement to display all the customers, who are either belongs to the city New York or not had a grade above 100.

```sql
SELECT * FROM customer
WHERE city = 'New York' OR grade <= 100;
```

```sql
-- other approach
SELECT * FROM customer
WHERE city = 'New York' OR NOT grade > 100;
```

### 2.5. Write a SQL query to display those customers who are neither belongs to the city New York nor grade value is more than 100.

```sql
SELECT * FROM customer
WHERE city NOT 'New York' AND NOT grade > 100;
```

```sql
-- other approach
SELECT * FROM customer
WHERE NOT (city = 'New York' AND grade > 100);
```

### 2.6. Write a SQL statement to display either those orders which are not issued on date 2012-09-10 and issued by the salesman whose ID is 5005 and below or those orders which purchase amount is 1000.00 and below.

```sql
SELECT * FROM orders
WHERE NOT (
	(ord_date = '2012-09-10' AND salesman_id > 5005) OR 
	purch_amt > 1000.00
);
```

### 2.7. Write a SQL statement to display salesman_id, name, city and commission who gets the commission within the range more than 0.10% and less than 0.12%.

```sql
SELECT salesman_id, name, city, commission FROM salesman
WHERE commission > 0.10 AND commission < 0.12;
```

### 2.8. Write a SQL query to display all orders where purchase amount less than 200 or exclude those orders which order date is on or greater than 10th Feb,2012 and customer id is below 3009.

```sql
SELECT * FROM orders
WHERE (
	purch_amt < 200 OR 
	NOT(ord_date >= '2012-02-10' AND customer_id < 3009)
);
```

### 2.9. Write a SQL statement to exclude the rows which satisfy 1) order dates are 2012-08-17 and purchase amount is below 1000 2) customer id is greater than 3005 and purchase amount is below 1000.

```sql
SELECT * FROM orders
WHERE NOT (
	(ord_date = '2012-08-17' OR customer_id > 3005 ) AND
	purch_amt < 1000
);
```

### 2.10. Write a SQL query to display order number, purchase amount, achieved, the unachieved percentage for those order which exceeds the 50% of the target value of 6000.

```sql
SELECT 
	ord_no, 
	purch_amt, 
	(purch_amt / 6000 * 100) AS "Achieved%",
	((6000-purch_amt) / 6000 * 100) AS "Unachieved%"
FROM orders
WHERE (purch_amt / 6000 * 100) > 50;
```

### 2.11. Write a query in SQL to find the data of employees whose last name is Dosni or Mardy.

```sql
SELECT * FROM emp_details
WHERE emp_lname = 'Dosni' OR emp_lname = 'Mardy';
```

### 2.12. Write a query in SQL to display all the data of employees that work in department 47 or department 63.

```sql
SELECT * FROM emp_details
WHERE emp_dept = 47 OR emp_dept = 63;
```