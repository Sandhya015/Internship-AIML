-- Create the Customers table
CREATE TABLE IF NOT EXISTS Customers (
    CustomerID INT AUTO_INCREMENT PRIMARY KEY, -- Primary key with clustered index
    CustomerName VARCHAR(50) NOT NULL,
    CustomerAddress VARCHAR(50) NOT NULL
);

-- Create the Products table
CREATE TABLE IF NOT EXISTS Products (
    ProductID INT AUTO_INCREMENT PRIMARY KEY, -- Primary key with clustered index
    ProductName VARCHAR(50) NOT NULL
);

-- Insert data into Customers table
INSERT INTO Customers (CustomerName, CustomerAddress)
VALUES
('Raj Sharma', 'Delhi'),
('Priya Singh', 'Mumbai');

-- Insert data into Products table
INSERT INTO Products (ProductName)
VALUES
('Rice'),
('Wheat');

-- Create a non-clustered index on ProductName
CREATE INDEX idx_NonClustered_ProductName
ON Products(ProductName);
