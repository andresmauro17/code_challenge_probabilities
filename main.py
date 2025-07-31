

import csv
import logging


logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def migrate_database()  :
    """ this method is used to migrate the database in sqlite3 """
    logger.info('Starting database migration')
    

def get_coheficientes()   :
    print('hey')

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