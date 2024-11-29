-- Step 1: Create the Employees table
CREATE TABLE Employees (
    Name VARCHAR(50),
    Age INT,
    Department VARCHAR(50)
);

-- Step 2: Insert employees into the Employees table
INSERT INTO Employees (Name, Age, Department)
VALUES ('Anjali', 30, 'HR');

INSERT INTO Employees (Name, Age, Department)
VALUES ('Vikram', 25, 'IT');

INSERT INTO Employees (Name, Age, Department)
VALUES ('Rahul', 28, 'Finance');
