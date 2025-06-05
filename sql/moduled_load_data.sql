-- Table data pumping

SET FOREIGN_KEY_CHECKS = 0;

-- CATEGORIES
LOAD DATA INFILE 'C:/Users/Pedro/Desktop/SoyHenry/Proyecto-Integrador/data/categories.csv'
INTO TABLE categories
FIELDS TERMINATED BY ','
LINES TERMINATED BY '\n'
IGNORE 1 LINES;

-- COUNTRIES
LOAD DATA INFILE 'C:/Users/Pedro/Desktop/SoyHenry/Proyecto-Integrador/data/countries.csv'
INTO TABLE countries
FIELDS TERMINATED BY ',' 
LINES TERMINATED BY '\n' 
IGNORE 1 LINES;

-- CITIES
LOAD DATA INFILE 'C:/Users/Pedro/Desktop/SoyHenry/Proyecto-Integrador/data/cities.csv'
INTO TABLE cities
FIELDS TERMINATED BY ',' 
LINES TERMINATED BY '\n' 
IGNORE 1 LINES;

-- CUSTOMERS
LOAD DATA INFILE 'C:/Users/Pedro/Desktop/SoyHenry/Proyecto-Integrador/data/customers.csv'
INTO TABLE customers
FIELDS TERMINATED BY ',' 
LINES TERMINATED BY '\n' 
IGNORE 1 LINES
(
  CustomerID,
  FirstName,
  @MiddleInitial,
  LastName,
  Email,
  Phone
)
SET
  MiddleInitial = LEFT(NULLIF(@MiddleInitial, 'NULL'), 1); -- Transforms the string "NULL" into a real null type

-- EMPLOYEES
LOAD DATA INFILE 'C:/Users/Pedro/Desktop/SoyHenry/Proyecto-Integrador/data/employees.csv'
INTO TABLE employees
FIELDS TERMINATED BY ',' 
LINES TERMINATED BY '\n' 
IGNORE 1 LINES;

-- PRODUCTS
LOAD DATA INFILE 'C:/Users/Pedro/Desktop/SoyHenry/Proyecto-Integrador/data/products.csv'
INTO TABLE products
FIELDS TERMINATED BY ',' 
LINES TERMINATED BY '\n' 
IGNORE 1 LINES
(
    ProductID,
    ProductName,
    Price,
    CategoryID,
    Class,
    @ModifyDate,
    Resistant,
    IsAllergic,
)
SET ModifyDate = convert_custom_time(@ModifyDate);


-- SALES
LOAD DATA INFILE 'C:/Users/Pedro/Desktop/SoyHenry/Proyecto-Integrador/data/sales.csv'
INTO TABLE sales
FIELDS TERMINATED BY ',' 
LINES TERMINATED BY '\n' 
IGNORE 1 LINES;

SET FOREIGN_KEY_CHECKS = 1;




