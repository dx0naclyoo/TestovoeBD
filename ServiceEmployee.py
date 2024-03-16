from typing import List

import psycopg2

from Database import DatabaseHandler
from models import Employee


class EmployeeDirectory(DatabaseHandler):
    def create_table_employee(self):
        create_table_query = """
        CREATE TABLE IF NOT EXISTS employees (
            id SERIAL PRIMARY KEY,
            full_name VARCHAR(100),
            birth_date DATE,
            gender VARCHAR(10)
        );
        """
        self.execute_query(create_table_query)

    def add_employee(self, employee: Employee):
        insert_data_query = """
                INSERT INTO employees (full_name, birth_date, gender) VALUES (%s, %s, %s);"""
        try:
            self.execute_query(insert_data_query, (employee.fullname, employee.birth_date, employee.gender))
            print("Employee added successfully")
        except psycopg2.IntegrityError as e:
            print("Error adding employee:", e)

    def add_list_employees(self, list_employees: List):
        query = """INSERT INTO employees (full_name, birth_date, gender) VALUES (%s, %s, %s)"""
        try:
            self.execute_many(query, list_employees)
        except psycopg2.Error as e:
            print("Error add list employees", e)

    def fetch_unique_employees(self):
        select_data_query = """
            SELECT full_name, birth_date
            FROM employees
            GROUP BY full_name, birth_date;
            """
        try:
            uniq_employees = self.fetch_data(select_data_query)
            return uniq_employees
        except psycopg2.Error as e:
            print("Error fetch unique employees", e)

    def fetch_f_male(self):
        query = """SELECT * FROM employees WHERE full_name LIKE 'F%' AND gender = 'Male';"""
        try:
            employee = self.fetch_data(query)
            return employee
        except psycopg2.Error as e:
            print("Error fetch f male employees", e)
