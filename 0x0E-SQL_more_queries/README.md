# 0x0E. SQL - More queries

## TOPICS
How To Create a New User and Grant Permissions in MySQL
How To Use MySQL GRANT Statement To Grant Privileges To a User
MySQL constraints
SQL technique: subqueries
Basic query operation: the join
SQL technique: multiple joins and the distinct keyword
SQL technique: join types
SQL technique: union and minus
MySQL Cheat Sheet
The Seven Types of SQL Joins
MySQL Tutorial
SQL Style Guide
MySQL 8.0 SQL Statement Syntax

Extra resources around relational database model design:

Design
Normalization
ER Modeling


## REQUIMENTS 
How to create a new MySQL user
How to manage privileges for a user to a database or table
What’s a PRIMARY KEY
What’s a FOREIGN KEY
How to use NOT NULL and UNIQUE constraints
How to retrieve datas from multiple tables in one request
What are subqueries
What are JOIN and UNION
Connect to your MySQL server:

$ sudo mysql
Welcome to the MySQL monitor.  Commands end with ; or \g.
Your MySQL connection id is 11
Server version: 8.0.25-0ubuntu0.20.04.1 (Ubuntu)

Copyright (c) 2000, 2021, Oracle and/or its affiliates.

Oracle is a registered trademark of Oracle Corporation and/or its
affiliates. Other names may be trademarks of their respective
owners.

Type 'help;' or '\h' for help. Type '\c' to clear the current input statement.

mysql>
mysql> quit
Bye
$
Use “container-on-demand” to run MySQL
In the container, credentials are root/root

Ask for container Ubuntu 20.04
Connect via SSH
OR connect via the Web terminal
In the container, you should start MySQL before playing with it:
$ service mysql start                                                   
 * Starting MySQL database server mysqld 
$
$ cat 0-list_databases.sql | mysql -uroot -p                               
Database                                                                                   
information_schema                                                                         
mysql                                                                                      
performance_schema                                                                         
sys                      
$

### Install MySQL 8.0 on Ubuntu 20.04 LTS
$ sudo apt update
$ sudo apt install mysql-server
...
$ mysql --version
mysql  Ver 8.0.25-0ubuntu0.20.04.1 for Linux on x86_64 ((Ubuntu))

### How to import a SQL dump
$ echo "CREATE DATABASE hbtn_0d_tvshows;" | mysql -uroot -p
Enter password: 
$ curl "https://s3.amazonaws.com/intranet-projects-files/holbertonschool-higher-level_programming+/274/hbtn_0d_tvshows.sql" -s | mysql -uroot -p hbtn_0d_tvshows
Enter password: 
$ echo "SELECT * FROM tv_genres" | mysql -uroot -p hbtn_0d_tvshows
Enter password: 
id  name
1   Drama
2   Mystery
3   Adventure
4   Fantasy
5   Comedy
6   Crime
7   Suspense
8   Thriller
$