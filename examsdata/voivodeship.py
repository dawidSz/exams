import csv


class Voivodeship:
    def __init__(self, name):
        self.name = name
        self.women = []
        self.men = []
        self.both = []
        self.create_years()

    def create_years(self):
        for it in range(9):
            year = {
                'year': '201{}'.format(it),
                'took': None,
                'passed': None
            }
            self.men.append(year.copy())
            self.women.append(year.copy())
            self.both.append(year.copy())
        self.read_data()

    def read_data(self):
        with open('data.csv', 'r') as data_file:
            csv_readed = csv.reader(data_file, delimiter=';')
            for row in csv_readed:
                if row[0].lower() == self.name:
                    year = int(row[3][3:])
                    if row[1] == 'przystąpiło':
                        took = int(row[4])
                        if row[2] == 'mężczyźni':
                            self.men[year]['took'] = took
                        else:
                            self.women[year]['took'] = took
                    else:
                        passed = int(row[4])
                        if row[2] == 'mężczyźni':
                            self.men[year]['passed'] = passed
                        else:
                            self.women[year]['passed'] = passed

        for year in range(9):
            self.both[year]['took'] = self.men[year]['took'] + self.women[year]['took']
            self.both[year]['passed'] = self.men[year]['passed'] + self.women[year]['passed']

    def count_passing_percentage(self):
        for year in range(9):
            result = self.men[year]['passed'] / self.men[year]['took'] * 100
            print('Rok 201{} - {} %'.format(year, result))


if __name__ == '__main__':
    vv = Voivodeship('lubuskie')
    vv.count_passing_percentage()
