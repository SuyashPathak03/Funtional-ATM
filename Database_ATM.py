import mysql.connector

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="admin",
    database="atm_machine"
)
c = conn.cursor()

accounts = """CREATE TABLE accounts (account_id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,customer_id INT NULL,
    account_number VARCHAR(20) NOT NULL UNIQUE, pin_code CHAR(4) NOT NULL, balance FLOAT(15,2) DEFAULT 0.00,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP);"""
c.execute(accounts)

admins = """CREATE TABLE admins ( admin_id INT NOT NULL AUTO_INCREMENT PRIMARY KEY, username VARCHAR(50) NOT NULL UNIQUE,
    password VARCHAR(50) NOT NULL);"""
c.execute(admins)

customers = """CREATE TABLE customers (customer_id INT NOT NULL AUTO_INCREMENT PRIMARY KEY, name VARCHAR(50) NOT NULL,
    email VARCHAR(100) NULL UNIQUE, phone VARCHAR(15) NULL, address VARCHAR(255) NULL, created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP);"""
c.execute(customers)

transactions = """CREATE TABLE transactions (transaction_id INT NOT NULL AUTO_INCREMENT PRIMARY KEY, account_id INT NULL,
    transaction_type ENUM('deposit', 'withdrawal') NOT NULL, amount DECIMAL(10,2) NOT NULL, transaction_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP);"""
c.execute(transactions)

conn.commit()
c.close()
conn.close()

