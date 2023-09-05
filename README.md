
# Bank Management System

## Description
This is a Python-based Bank Management System that interacts with a MySQL database. It allows bank employees and customers to perform various banking operations, such as account creation, deposits, withdrawals, balance checks, and more.

## Features
- **Customer Interface**: Customers can sign up, log in, and perform transactions.
- **Manager Interface**: Bank managers can view individual transactions, all transactions, and save transaction reports.
- **MySQL Database**: The system stores customer information and transaction records in a MySQL database.

## Requirements
- Python 3.x
- MySQL Database Server
- Python Libraries: mysql.connector, pandas

## Setup
1. Install Python and the required libraries.
2. Set up a MySQL database and configure the `DATABASE_CONFIG` in the code with your database details.
3. Run the code.

## Usage
1. Launch the program.
2. Select either "Manager" or "Customer" mode.
3. Follow the on-screen prompts to perform various banking operations.

## Customer Operations
- Sign Up: Create a new bank account.
- Login: Log in to your account to perform transactions.
- Deposit: Add money to your account.
- Withdraw: Withdraw money from your account.
- Transfer Money: Send money to another account.
- Check Balance: View your account balance.

## Manager Operations
- Individual Transaction: View transactions for a specific account.
- All Transaction: View all transactions.
- Save Report: Save transaction data to an Excel file.

## Important Notes
- Always ensure your MySQL database is up and running before using the program.
- Handle customer data with care and ensure the security of customer information.

