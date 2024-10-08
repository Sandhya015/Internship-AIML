create table books (
    book_id int auto_increment primary key,
    title varchar(255) not null,
    author varchar(255) not null,
    genre varchar(100) not null,
    yearpublished int not null
);

insert into books (title,author,genre,yearpublished)

values
('The Alchemist','Paulo Coelho','Fiction',1988),
('The Da Vinic Code','Dan Brown','Fiction',2003);

select book_id,title,author,yearpublished
from books
where yearpublished >2000;