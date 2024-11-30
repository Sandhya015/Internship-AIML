CREATE TABLE Customers (
    CustomerID INT PRIMARY KEY,
    CustomerName VARCHAR(50),
    CustomerAddress VARCHAR(50)
);

INSERT INTO Customers (CustomerID, CustomerName, CustomerAddress)
VALUES
(1, 'Raj Sharma', 'Delhi'),
(2, 'Priya Singh', 'Mumbai');


CREATE TABLE Products (
    ProductID INT PRIMARY KEY,
    ProductName VARCHAR(50)
);

INSERT INTO Products (ProductID, ProductName)
VALUES
(1, 'Rice'),
(2, 'Wheat');
