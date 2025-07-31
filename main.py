

import sqlite3
import csv
import logging
import os


logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)
DB_FILE_NAME = 'database.db'

def migrate_database()  :
    """ this method is used to migrate the database in sqlite3 """
    logger.info('Starting database migration')
    if os.path.exists(DB_FILE_NAME):
        os.remove(DB_FILE_NAME)
    return None
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
        return None
    except sqlite3.Error as e:
        logger.error(f"An error occurred during database migration: {e}")
        if conn:
            conn.close()
            logger.info('Database connection closed')
        return None

def get_coheficientes() :
    """ this method is used to get the coefficients from the csv file """
    coheficientes = []  

    with open('import_test.csv', mode='r') as file:
        csv_reader = csv.reader(file, delimiter=';')
        for index, row in enumerate(csv_reader):
            # print(index)
            if( index != 0):
                # print(row)
                name = row[1]
                score = float(row[3])   
                coheficiente= name.split(' ')[1]
                coheficiente = float(coheficiente.replace(',', '.'))

                print(type(score), type(coheficiente))
                probability = score * coheficiente
                print(probability)


if __name__ == "__main__":
    migrate_database()
    # get_coheficientes()