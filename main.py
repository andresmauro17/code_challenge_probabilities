

import sqlite3
import csv
import logging
import os


logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)
DB_FILE_NAME = 'database.db'

def migrate_database()-> bool:
    """ this method is used to migrate the database in sqlite3 """
    logger.info('Starting database migration')
    if os.path.exists(DB_FILE_NAME):
        os.remove(DB_FILE_NAME)
    conn = None
    try:
        conn = sqlite3.connect(DB_FILE_NAME)
        cursor = conn.cursor()

        # Create table if it doesn't exist
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS processed_data (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                brand TEXT,
                score REAL,
                coefficient REAL,
                probability REAL
            )
        ''')
        conn.commit()
        logger.info('Database migration completed successfully')
        return True
    except sqlite3.Error as e:
        logger.error(f"An error occurred during database migration: {e}")
        return False
    finally:
        if conn:
            conn.close()
            logger.info('Database connection closed')

def insert_data_to_db(records_to_insert)->bool:
    """ this method is used to insert the data into the database """
    logger.info('Starting to insert data into the database')
    conn = None
    try:
        conn = sqlite3.connect(DB_FILE_NAME)
        cursor = conn.cursor()
        cursor.executemany('''
            INSERT INTO processed_data (id, name, brand, score, coefficient, probability)
            VALUES (?, ?, ?, ?, ?, ?)
        ''', records_to_insert)
        conn.commit()
        logger.info('Data inserted successfully')
        return True
    except sqlite3.Error as e:
        logger.error(f"An error occurred while inserting data: {e}")
        return False
    finally:
        if conn:
            conn.close()
            logger.info('Database connection closed')

def get_coheficientes() -> list[tuple] | None:
    """ this method is used to get the coefficients from the csv file """
    logger.info('Starting to process the CSV file')
    conn = sqlite3.connect(DB_FILE_NAME)
    records_to_insert: list[tuple] = []

    with open('import_test.csv', mode='r') as file:
        csv_reader = csv.reader(file, delimiter=';')
        for index, row in enumerate(csv_reader):
            # print(index)
            if( index != 0):
                # print(row)
                id: int= int(row[0]) 
                name: str = row[1]
                brand: str = row[2]
                score: float = float(row[3])
                coheficiente: str | float = name.split(' ')[1]
                coheficiente = float(coheficiente.replace(',', '.'))
                
                # print(f'id: {id}, name: {name}, brand: {brand}, score: {score}, coheficiente: {coheficiente}')


                probability: float = score * coheficiente
                records_to_insert.append((id, name, brand, score, coheficiente, probability))
    return records_to_insert


if __name__ == "__main__":
    was_migrated: bool = migrate_database()
    if was_migrated:
        records_to_insert: list[tuple] | None = get_coheficientes()
        # print(records_to_insert)
        if records_to_insert:
            insert_data_to_db(records_to_insert)