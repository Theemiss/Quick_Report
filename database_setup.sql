-- prepares a MySQL server for the project

CREATE DATABASE IF NOT EXISTS quick_report;
CREATE USER IF NOT EXISTS 'Admin'@'localhost' IDENTIFIED BY '55664730';
GRANT ALL PRIVILEGES ON `quick_report`.* TO 'Admin'@'localhost';
GRANT SELECT ON `performance_schema`.* TO 'Admin'@'localhost';
FLUSH PRIVILEGES;

