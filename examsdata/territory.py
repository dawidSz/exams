import csv


class Territory:
    def __init__(self, name):
        self.name = name.lower()
        self.data = {
            'women': [],
            'men': [],
            'both': []
        }
        self.passing_perc = {
            'women': [],
            'men': [],
            'both': []
        }
        self.regressions = {
            'women': [],
            'men': [],
            'both': []
        }
        self.create_years()

    def create_years(self):
        for it in range(9):
            year = {
                'year': '201{}'.format(it),
                'took': None,
                'passed': None
            }
            self.data['men'].append(year.copy())
            self.data['women'].append(year.copy())
            self.data['both'].append(year.copy())
        self.read_data()

    def read_data(self):
        with open('data.csv', 'r') as data_file:
            csv_readed = csv.reader(data_file, delimiter=';')
            for row in csv_readed:
                if row[0].lower() == self.name:
                    year = int(row[3][3:])
                    if row[2] == 'mężczyźni':
                        sex = 'men'
                    else:
                        sex = 'women'
                    if row[1] == 'przystąpiło':
                        opt = 'took'
                    else:
                        opt = 'passed'
                    self.data[sex][year][opt] = int(row[4])

        for year in range(9):
            self.data['both'][year]['took'] = self.data['men'][year]['took'] + self.data['women'][year]['took']
            self.data['both'][year]['passed'] = self.data['men'][year]['passed'] + self.data['women'][year]['passed']

        self.count_passing_percentage()

    def count_passing_percentage(self):
        for year in range(9):
            result = self.data['men'][year]['passed'] / self.data['men'][year]['took'] * 100
            self.passing_perc['men'].append(result)
            result = self.data['women'][year]['passed'] / self.data['women'][year]['took'] * 100
            self.passing_perc['women'].append(result)
            result = self.data['both'][year]['passed'] / self.data['both'][year]['took'] * 100
            self.passing_perc['both'].append(result)

        self.count_regressions()

    def count_regressions(self):
        for it in range(8):
            for key in self.passing_perc.keys():
                if self.passing_perc[key][it] > self.passing_perc[key][it + 1]:
                    self.regressions[key].append('201{} > 201{}'.format(it, it + 1))


if __name__ == '__main__':
    vv = Territory('Polska')
