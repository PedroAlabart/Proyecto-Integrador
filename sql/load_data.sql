
-- =======================
-- Schema
-- ========================

-- Database Creation
CREATE DATABASE IF NOT EXISTS SalesTransactions;
USE SalesTransactions;

-- Table creation
-- CATEGORIES
CREATE TABLE IF NOT EXISTS categories(
    CategoryID  INT AUTO_INCREMENT PRIMARY KEY,
    CategoryName VARCHAR(100) NOT NULL
);

-- PRODUCTS
CREATE TABLE IF NOT EXISTS products (
    ProductID INT PRIMARY KEY,
    ProductName VARCHAR(45) NOT NULL,
    Price DECIMAL(10,2) NOT NULL, -- Opte por 3 decimales
    CategoryID INT NOT NULL,
    Class VARCHAR(45) DEFAULT 'Uknnown',
    ModifyDate DATETIME,
    Resistant VARCHAR(45) DEFAULT 'Uknnown',
    IsAllergic VARCHAR(10) DEFAULT 'Uknnown',
    ViabilityDays DECIMAL(3,0),
    FOREIGN KEY (CategoryID) REFERENCES categories(CategoryID)
);
-- COUNTRIES
CREATE TABLE IF NOT EXISTS countries (
    CountryID INT PRIMARY KEY,
    CountryName VARCHAR(45),
    CountryCode VARCHAR(2)
);
-- CITIES
CREATE TABLE IF NOT EXISTS cities (
    CityID INT PRIMARY KEY,
    CityName VARCHAR(45),
    Zipcode DECIMAL(6,0),
    CountryID INT,
    FOREIGN KEY (CountryID) REFERENCES countries(CountryID)
);
-- CUSTOMERS
CREATE TABLE IF NOT EXISTS customers (
    CustomerID INT PRIMARY KEY,
    FirstName VARCHAR(45),
    MiddleInitial VARCHAR(1),
    LastName VARCHAR(45),
    CityID INT,
    Address VARCHAR(90),
    FOREIGN KEY (CityID) REFERENCES cities(CityID)
);

CREATE TABLE IF NOT EXISTS employees (
    EmployeeID INT PRIMARY KEY,
    FirstName VARCHAR(45),
    MiddleInitial VARCHAR(1),
    LastName VARCHAR(45),
    BirthDate DATE,
    Gender VARCHAR(1),
    CityID INT,
    HireDate DATE,
    FOREIGN KEY (CityID) REFERENCES cities(CityID)
);

CREATE TABLE IF NOT EXISTS sales (
    SalesID INT PRIMARY KEY,
    SalesPersonID INT,
    CustomerID INT,
    ProductID INT,
    Quantity INT,
    Discount DECIMAL(10,2),
    TotalPrice DECIMAL(20,2),
    SalesDate DATETIME,
    TransactionNumber VARCHAR(255),
    CityID INT,
    CountryID INT,
    FOREIGN KEY (SalesPersonID) REFERENCES employees(EmployeeID),
    FOREIGN KEY (CustomerID) REFERENCES customers(CustomerID),
    FOREIGN KEY (ProductID) REFERENCES products(ProductID),
    FOREIGN KEY (CityID) REFERENCES cities(CityID),
    FOREIGN KEY (CountryID) REFERENCES countries(CountryID)
);

-- =======================
-- Functions
-- ========================
DELIMITER $$
CREATE FUNCTION IF NOT EXISTS convert_custom_time(input VARCHAR(10)) RETURNS TIME
DETERMINISTIC
BEGIN
    DECLARE h INT;
    DECLARE m_decimal DECIMAL(5,2);
    DECLARE total_seconds INT;

    SET h = FLOOR(SUBSTRING_INDEX(input, ':', 1));
    SET m_decimal = CAST(SUBSTRING_INDEX(input, ':', -1) AS DECIMAL(5,2));

    SET total_seconds = h * 3600 + FLOOR(m_decimal) * 60 + ROUND((m_decimal - FLOOR(m_decimal)) * 60);

    RETURN SEC_TO_TIME(total_seconds);
END $$
DELIMITER ;

DELIMITER $$
CREATE FUNCTION IF NOT EXISTS separate_address_from_address_number(input VARCHAR(10)) RETURNS TIME
DETERMINISTIC
BEGIN
    DECLARE h INT;
    DECLARE m_decimal DECIMAL(5,2);
    DECLARE total_seconds INT;

    SET h = FLOOR(SUBSTRING_INDEX(input, ':', 1));
    SET m_decimal = CAST(SUBSTRING_INDEX(input, ':', -1) AS DECIMAL(5,2));

    SET total_seconds = h * 3600 + FLOOR(m_decimal) * 60 + ROUND((m_decimal - FLOOR(m_decimal)) * 60);

    RETURN SEC_TO_TIME(total_seconds);
END $$
DELIMITER ;



-- =======================
-- Data Loading
-- ========================

-- Table data pumping

SET FOREIGN_KEY_CHECKS = 0;

-- CATEGORIES
LOAD DATA INFILE 'C:/Users/Pedro/Desktop/SoyHenry/Proyecto-Integrador/data/categories.csv'
IGNORE
INTO TABLE categories
FIELDS TERMINATED BY ','
LINES TERMINATED BY '\n'
IGNORE 1 LINES;

-- COUNTRIES
LOAD DATA INFILE 'C:/Users/Pedro/Desktop/SoyHenry/Proyecto-Integrador/data/countries.csv'
IGNORE
INTO TABLE countries
FIELDS TERMINATED BY ',' 
LINES TERMINATED BY '\n' 
IGNORE 1 LINES;

-- CITIES
LOAD DATA INFILE 'C:/Users/Pedro/Desktop/SoyHenry/Proyecto-Integrador/data/cities.csv'
IGNORE
INTO TABLE cities
FIELDS TERMINATED BY ',' 
LINES TERMINATED BY '\n' 
IGNORE 1 LINES;

-- CUSTOMERS
LOAD DATA INFILE 'C:/Users/Pedro/Desktop/SoyHenry/Proyecto-Integrador/data/customers.csv'
IGNORE
INTO TABLE customers
FIELDS TERMINATED BY ',' 
LINES TERMINATED BY '\n' 
IGNORE 1 LINES
(
  CustomerID,
  FirstName,
  @MiddleInitial,
  LastName,
  CityID,
  Address
)
SET
  MiddleInitial = LEFT(NULLIF(@MiddleInitial, 'NULL'), 1); -- Transforms the string "NULL" into a real null type

-- EMPLOYEES
LOAD DATA INFILE 'C:/Users/Pedro/Desktop/SoyHenry/Proyecto-Integrador/data/employees.csv'
IGNORE
INTO TABLE employees
FIELDS TERMINATED BY ',' 
LINES TERMINATED BY '\n' 
IGNORE 1 LINES;

-- PRODUCTS
LOAD DATA INFILE 'C:/Users/Pedro/Desktop/SoyHenry/Proyecto-Integrador/data/products.csv'
IGNORE
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
    IsAllergic
)
SET ModifyDate = convert_custom_time(@ModifyDate);


-- SALES
LOAD DATA INFILE 'C:/Users/Pedro/Desktop/SoyHenry/Proyecto-Integrador/data/sales.csv'
IGNORE
INTO TABLE sales
FIELDS TERMINATED BY ',' 
LINES TERMINATED BY '\n' 
IGNORE 1 LINES;

SET FOREIGN_KEY_CHECKS = 1;





