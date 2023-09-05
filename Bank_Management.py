import mysql.connector as ms
import time as t
import pandas as pd
import re

# Constants
DATABASE_CONFIG = {
    "hostname": "localhost",
    "username": "root",
    "password": "root",
    "database": "newdb"
}

class BankDB:
    def __init__(self):
        self.conn = None
        self.cursor = None

    def connect(self):
        try:
            self.conn = ms.connect(
                user=DATABASE_CONFIG["username"],
                password=DATABASE_CONFIG["password"],
                host=DATABASE_CONFIG["hostname"],
                auth_plugin='mysql_native_password',
                db=DATABASE_CONFIG["database"]
            )
            self.cursor = self.conn.cursor()
        except ms.Error as err:
            print(f"Error connecting to the database: {err}")
            exit(1)

    def close(self):
        if self.conn:
            self.conn.close()

    def execute_query(self, query, params=None):
        try:
            if params:
                self.cursor.execute(query, params)
            else:
                self.cursor.execute(query)
            self.conn.commit()
        except ms.Error as err:
            print(f"Database error: {err}")
            self.conn.rollback()

class Bank:
    def __init__(self):
        self.db = BankDB()

    def start(self):
        while True:
            print("********** BANK MANAGEMENT **********")
            print("1. Manager")
            print("2. Customer")
            print("3. Exit")
            choice = input("Enter Your Choice : ")
            if choice == "1":
                self.manager()
            elif choice == "2":
                while True:
                    print("1. Sign Up")
                    print("2. Login")
                    print("3. Exit")
                    choice = input(" Enter Your Choice : ")
                    if choice == "1":
                        self.sign_up()
                    elif choice == "2":
                        self.sign_in()
                    elif choice == "3":
                        break
                    else:
                        print("ALERT: INVALID CHOICE !")
            elif choice == "3":
                break
            else:
                print("ALERT: INVALID CHOICE !")

    def sign_up(self):
        print("************************* SIGN UP *************************")
        name = input("Enter Your Name : ")
        password = input("Enter Your Password : ")
        mobile = input("Enter Your Mobile no. : ")
        amount = 0
        if re.match(r'^\d{10}$', mobile):
            cust_name = name[:2]
            cur.execute("select count(name) from bank where name like '{0}%'".format(cust_name))
            fetch_count = cur.fetchone()
            cust_count = fetch_count[0]
            cust_count += 1
            cust_id = cust_name.casefold() + str(cust_count) + '@abc'
            try:
                cur.execute("insert into bank values (%s, %s, %s, %s, %s)", (name, cust_id, password, mobile, amount))
                conn.commit()
                print("SUCCESS: DATA ADDED SUCCESSFULLY !")
            except ms.Error:
                print("ALERT: MOBILE NO ALREADY EXISTS !")
        else:
            print("ALERT: ENTER A VALID MOBILE NUMBER !")

    def sign_in(self):
        print("************************* LOGIN *************************")
        cust_id = input("Enter Your ID : ")
        password = input("Enter Your Password : ")
        try:
            cur.execute("select count(*) from bank where id = %s and password = %s", (cust_id, password))
            dt = cur.fetchone()
            for i in dt:
                if i:
                    print("SUCCESS: LOGIN SUCCESSFULLY !")
                    print("*********************** WELCOME TO ABC BANK ***********************")
                    while True:
                        print("1. Deposit")
                        print("2. Withdraw")
                        print("3. Transfer Money")
                        print("4. Check Balance")
                        print("5. Exit")
                        choice = input("Enter Your Choice : ")
                        if choice == "1":
                            self.deposit(cust_id)
                        elif choice == "2":
                            self.withdraw(cust_id)
                        elif choice == "3":
                            self.transfer_money(cust_id)
                        elif choice == "4":
                            self.check_balance(cust_id)
                        elif choice == "5":
                            break
                        else:
                            print("ALERT: INVALID CHOICE !")
                else:
                    print("ALERT: INVALID PASSWORD !")
        except ms.Error:
            print("ALERT: INVALID NAME !")

    def deposit(self, cust_id):
        dep_id = cust_id
        process = 'Deposit'
        print("************************* DEPOSIT *************************")
        try:
            dep_amount = int(input("Enter Amount to Deposit RS.: "))
            cur.execute("select Balance from bank where id = %s", (dep_id,))
            fetch_amount = cur.fetchone()
            old_amount = fetch_amount[0]
            new_amount = old_amount + dep_amount
            cur.execute("update bank set Balance = %s where id = %s", (new_amount, dep_id))
            conn.commit()
            cur.execute("insert into transaction values (%s, %s, %s, %s, %s)", (dep_id, old_amount, dep_amount, new_amount, process))
            conn.commit()
            print("Processing ...")
            t.sleep(5)
            print("SUCCESS: DEPOSITED SUCCESSFULLY")
        except ValueError:
            print("ALERT: CHECK AMOUNT AGAIN")

    def withdraw(self, cust_id):
        dep_id = cust_id
        process = "Withdrawl"
        print("************************* WITHDRAW *************************")
        try:
            withdraw_amount = int(input("Enter Amount to Withdraw RS.: "))
            cur.execute("select Balance from bank where id = %s", (dep_id,))
            fetch_amount = cur.fetchone()
            old_amount = fetch_amount[0]
            new_amount = old_amount - withdraw_amount
            if new_amount >= 0:
                cur.execute("update bank set Balance = %s where id = %s", (new_amount, dep_id))
                conn.commit()
                cur.execute("insert into transaction values (%s, %s, %s, %s, %s)", (dep_id, old_amount, withdraw_amount, new_amount, process))
                conn.commit()
                print("Withdrawing Amount .... ")
                t.sleep(3)
                print("SUCCESS: TAKE YOUR CASH")
            else:
                print("ALERT: INSUFFICIENT BALANCE")
        except ValueError:
            print("ALERT: CHECK AMOUNT AGAIN")

    def check_balance(self, cust_id):
        print("************************* CHECK BALANCE *************************")
        dep_id = cust_id
        cur.execute("select Balance from bank where id = %s", (dep_id,))
        fetch_amount = cur.fetchone()
        print("Your Balance Amount RS.: ", fetch_amount[0])

    def transfer_money(self, cust_id):
        dep_id = cust_id
        print("************************* TRANSFER MONEY *************************")
        trans_id = input("Enter ID to Transfer Money : ")
        try:
            trans_amount = int(input("Enter Amount to Transfer : "))
            try:
                cur.execute("select Balance from bank where id = %s", (dep_id,))
                fetch_amount = cur.fetchone()
                old_amount = fetch_amount[0]
                new_amount = old_amount - trans_amount
                cur.execute("update bank set Balance = %s where id = %s", (new_amount, dep_id))
                conn.commit()
                cur.execute("insert into transaction values (%s, %s, %s, %s, %s)", (dep_id, old_amount, trans_amount, new_amount, 'AmountSent'))
                conn.commit()
                print("Transferring Amount.... ")
                cur.execute("select Balance from bank where id = %s", (trans_id,))
                fetch_amount = cur.fetchone()
                old_amount = fetch_amount[0]
                new_amount = old_amount + trans_amount
                cur.execute("update bank set Balance = %s where id = %s", (new_amount, trans_id))
                cur.execute("insert into transaction values (%s, %s, %s, %s, %s)", (trans_id, old_amount, trans_amount, new_amount, 'AmountReceived'))
                conn.commit()
                t.sleep(5)
                print("SUCCESS: AMOUNT TRANSFERRED SUCCESSFULLY")
            except ms.Error:
                print("ALERT: CHECK ID AGAIN")
        except ValueError:
            print("ALERT: CHECK AMOUNT AGAIN")

    def manager(self):
        emp_id = input("Enter Your ID : ")
        emp_pass = input("Enter Your Password : ")
        cur.execute("select count(*) from bank_emp where id = %s and password = %s", (emp_id, emp_pass))
        fetch_count = cur.fetchone()
        count = fetch_count[0]
        if count:
            print("SUCCESS: LOGIN SUCCESSFULLY")
            while True:
                print("1. Individual Transaction")
                print("2. All Transaction")
                print("3. Save Report")
                print("4. Exit")
                choice = input("Enter Your Choice : ")
                if choice == "1":
                    self.individual_transaction()
                elif choice == "2":
                    self.all_transaction()
                elif choice == "3":
                    self.save_report()
                elif choice == "4":
                    break
                else:
                    print("ALERT: INVALID CHOICE !")
        else:
            print("ALERT: CHECK ID OR PASSWORD !")

    def individual_transaction(self):
        try:
            trans_id = input("Enter ID : ")
            cur.execute("select * from transaction where id = %s", (trans_id,))
            trans_details = cur.fetchall()
            for i in trans_details:
                print(i)
                t.sleep(0.5)
        except ms.Error:
            print("No Transactions Found !")

    def all_transaction(self):
        cur.execute("select * from transaction")
        transactions = cur.fetchall()
        for i in transactions:
            print(i)
            t.sleep(0.3)

    def save_report(self):
        data_report2 = []
        d3 = ['ID', 'Old_Amount', 'Process_Amount', 'Total', 'Transaction_Type']
        cur.execute("select * from transaction")
        transactions = cur.fetchall()
        for i in transactions:
            data_report2.append(dict(zip(d3, i)))
        df = pd.DataFrame(data=data_report2)
        df.to_excel('data2.xlsx', index=False)

if __name__ == "__main__":
    conn = ms.connect(user=DATABASE_CONFIG["username"], password=DATABASE_CONFIG["password"], host=DATABASE_CONFIG["hostname"], auth_plugin='mysql_native_password', db=DATABASE_CONFIG["database"])
    cur = conn.cursor()
    obj = Bank()
    obj.start()
