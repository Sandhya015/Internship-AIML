CREATE TABLE Books(
    BookID INT AUTO_INCREMENT PRIMARY KEY,
    Title  VARCHAR(255) NOT NULL,
    Author VARCHAR(255) NOT NULL,
    Genre VARCHAR(100) NOT NULL,
    YearPublished INT NOT NULL
);

INSERT INTO Books(Title,Author,Genre,YearPublished)
VALUES('The Alchemist','Paulo Coelho','Fiction',1988);

SELECT * FROM Books;