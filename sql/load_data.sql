-- Database Creation
CREATE DATABASE IF NOT EXISTS db;
USE db;


-- Table creation
-- CATEGORIES
CREATE TABLE IF NOT EXISTS categories(
    CategoryID  INT AUTO_INCREMENT PRIMARY KEY,
    CategoryName VARCHAR(100) NOT NULL
);

-- PRODUCTS
CREATE TABLE IF NOT EXISTS products (
    ProductID INT PRIMARY KEY,
    ProductName VARCHAR(45),
    Price DECIMAL(10,0),
    CategoryID INT,
    Class VARCHAR(45),
    ModifyDate DATE,
    Resistant VARCHAR(45),
    IsAllergic VARCHAR(10),
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
  MiddleInitial = LEFT(NULLIF(@MiddleInitial, 'NULL'), 1);

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
IGNORE 1 LINES;

-- SALES
LOAD DATA INFILE 'C:/Users/Pedro/Desktop/SoyHenry/Proyecto-Integrador/data/sales.csv'
INTO TABLE sales
FIELDS TERMINATED BY ',' 
LINES TERMINATED BY '\n' 
IGNORE 1 LINES;

SET FOREIGN_KEY_CHECKS = 1;




