# MySQL

## Flask

[Flask Docs](https://flask.palletsprojects.com/en/2.0.x/)
[CS50 2020 - Lecture 9 - Flask | Harvard](https://www.youtube.com/watch?v=x_c8pTW8ZUc&ab_channel=CS50)

## Flask Blueprint

[Flask Blueprint | Real Python](https://realpython.com/flask-blueprint/)

## Jinja2

[Jinja | Real Python](https://realpython.com/primer-on-jinja-templating/)

[Jinja Docs](https://jinja.palletsprojects.com/en/3.0.x/)

## MySQL information

First, you will need to install MySQL on a computer.
- [Installation of MySQL](https://medium.com/365datascience/installing-mysql-and-getting-acquainted-with-the-interface-cf0f98e599f2)

Then, install mysql.connector.
- [`mysql` - get started](https://www.w3schools.com/python/python_mysql_getstarted.asp)

You need to create schema and then a certain table inside this schema.
Here is the cheatsheet to help you with the basic commands.
- [MySQL cheatsheet](https://gist.github.com/hofmannsven/9164408)

Example of creating a table:

```mysql
CREATE TABLE table_try1 (
  id int auto_increment primary key,
  name varchar(255),
  email text,
  create_date timestamp default CURRENT_TIMESTAMP,
  password varchar(120)
);
```
Check syntax of MySQL. For example here:
- [MySQL Syntax Check](https://www.piliapp.com/mysql-syntax-check/)

You can explore all the possibilities of MySQL here.
- [MySQL docs](https://dev.mysql.com/doc/connector-python/en/)