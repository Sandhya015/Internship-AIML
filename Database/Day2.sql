CREATE TABLE Employees (
    Name VARCHAR(50),
    Age INT,
    Department VARCHAR(50)
);


INSERT INTO Employees (Name, Age, Department) VALUES ('Anjali', 30, 'HR');
INSERT INTO Employees (Name, Age, Department) VALUES ('Vikram', 25, 'IT');
INSERT INTO Employees (Name, Age, Department) VALUES ('Rahul', 28, 'Finance');

SELECT * 
FROM Employees
WHERE Department = 'IT';