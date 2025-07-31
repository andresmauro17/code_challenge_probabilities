
import csv



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
    get_coheficientes()