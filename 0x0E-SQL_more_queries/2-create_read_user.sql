--  a script that creates the MySQL server user user_0d_1.
-- >> user_0d_1 should have all privileges on your MySQL server
-- >> The user_0d_1 password should be set to user_0d_1_pwd
-- >> If the user user_0d_1 already exists, your script should not fail
CREATE DATABASE IF NOT EXISTS hbtn_0d_2;
CREATE USER IF NOT EXISTS 'user_0d_2'@'localhost' IDENTIFIED BY 'user_0d_2_pwd';
GRANT USAGE ON *.* TO 'user_0d_2'@'localhost';
GRANT SELECT ON `hbtn_0d_2`.* TO 'user_0d_2'@'localhost';
FLUSH PRIVILEGES;
