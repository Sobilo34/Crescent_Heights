-- creates dev account and database for CHO portfolio project

CREATE DATABASE IF NOT EXISTS CHO_dev_db;
CREATE USER IF NOT EXISTS 'CHO_dev'@'localhost' IDENTIFIED BY 'CHO_dev_secret';
GRANT ALL PRIVILEGES ON `CHO_dev_db`.* TO 'CHO_dev'@'localhost';
GRANT SELECT ON `performance_schema`.* TO 'CHO_dev'@'localhost';
FLUSH PRIVILEGES;
