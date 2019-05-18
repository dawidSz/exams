from examsdata import territory


class ExamsResults:
    def __init__(self):
        self.voivodeships_names = ['dolnośląskie', 'kujawsko-pomorskie', 'lubelskie', 'lubuskie', 'łódzkie',
                                   'małopolskie',
                                   'mazowieckie', 'opolskie', 'podkarpackie', 'podlaskie', 'pomorskie', 'śląskie',
                                   'świętokrzyskie', 'warmińsko-mazurskie', 'wielkopolskie', 'zachodniopomorskie']
        self.show_menu()

    def show_menu(self):
        print(
            '--- MENU ---\n 1. Średnia zdawalność województw.\n 2. Procentowa zdawalnosc wojewodztwa.\n 3. Najlepsze województwo danego roku.\n 4. Potencjalna regresja dla danego województwa.\n 5. Porównywarka województw.\n-----------------')
        while True:
            option = input('opcja >> ')
            try:
                option = int(option)
            except ValueError:
                print('Bledne dane! Wybierz jeden z numerów z listy.')
                continue
            else:
                if option not in (1, 2, 3, 4, 5):
                    print('Nie ma takiej opcji!')
                    continue
                self.execute_option(option)
                break

    def execute_option(self, option):
        if option == 1:
            self.count_avg()
        elif option == 2:
            self.show_passing_perc()
        elif option == 3:
            self.best_of_year()
        elif option == 4:
            self.show_regr()
        elif option == 5:
            self.compare()

    def count_avg(self):
        print('Wybrałeś opcję sprawdzenia średniej zdawalności województw dla danego rocznika.')
        while True:
            year, sex = self.div_msg('Podaj rocznik, który chcesz zbadać (opcjonalnie dodaj płeć): ')
            try:
                year = int(year)
            except ValueError:
                print('Niestety takiego rocznika nie ma w bazie. Spróbuj jeszcze raz.')
                continue
            else:
                year = year - 2010
                country = territory.Territory('Polska')
                result = country.data[sex][year]['passed'] / 16
                print('Średnia na województwo: {}'.format(result))
                break

        self.show_menu()

    def show_passing_perc(self):
        print('Wybrałeś opcję pokazania procentowej zdawalnośco dla danego województwa.')
        while True:
            vv, sex = self.div_msg('Podaj województwo, które chcesz zbadać (opcjonalnie dodaj płeć): ')
            vv = vv.strip()
            if vv in self.voivodeships_names:
                vv = territory.Territory(vv)
                for year in range(9):
                    print('201{} - {} %'.format(year, vv.passing_perc[sex][year]))
                break
            else:
                print('Nie ma takiego województwa. Spróbuj jeszcze raz!')
                continue

        self.show_menu()

    def best_of_year(self):
        print('Wybrałeś opcję pokazania najlepszego województwa danego roku.')
        while True:
            year, sex = self.div_msg('Podaj rocznik, który chcesz zbadać (opcjonalnie dodaj płeć): ')
            try:
                year = int(year)
            except ValueError:
                print('Niestety takiego rocznika nie ma w bazie. Spróbuj jeszcze raz.')
                continue
            else:
                year = year - 2010
                results = []
                for name in self.voivodeships_names:
                    vv = territory.Territory(name)
                    results.append(vv.passing_perc[sex][year])
                best = max(results)
                best_idx = results.index(best)
                print('Województwo z najlepszymi wynikami danego roku to woj. {}.'.format(
                    self.voivodeships_names[best_idx]))
                break

        self.show_menu()

    def show_regr(self):
        print('Wybrałeś opcję pokazania regresji województw.')
        while True:
            opt = input('Czy chcesz konkretne dane na temat kobiet/mężczyzn? [k/m]? ')
            if opt == 'k':
                sex = 'women'
                break
            elif opt == 'm':
                sex = 'men'
                break
            elif not opt:
                sex = 'both'
                break
            else:
                print('Nietety nie ma takiej opcji. Sprobuj jeszcze raz.')
                continue

        for name in self.voivodeships_names:
            vv = territory.Territory(name)
            print('Woj. {}: '.format(name))
            for regr in vv.regressions[sex]:
                print('\t {}'.format(regr))

    def compare(self):
        print('Wybrałeś porównywarkę.')
        sex = 'both'
        while True:
            msg = input('Podaj dwa województwa i opcjonalnie płeć [k/m]:')
            msg = msg.split()
            try:
                vv1 = msg[0]
                vv2 = msg[1]
                if len(msg) == 3:
                    if msg[2] == 'k':
                        sex = 'women'
                    elif msg[2] == 'm':
                        sex = 'men'
            except IndexError:
                print('Niestety podano błędne dane :< Spróbuj jeszcze raz.')
                continue

            if vv1 in self.voivodeships_names and vv2 in self.voivodeships_names:
                vv1 = territory.Territory(vv1)
                vv2 = territory.Territory(vv2)
                print(vv1.passing_perc['women'])
                print(vv2.passing_perc['women'])
                for year in range(9):
                    win = 'Remis!'
                    if vv1.passing_perc[sex][year] > vv2.passing_perc[sex][year]:
                        win = vv1.name
                    elif vv1.passing_perc[sex][year] < vv2.passing_perc[sex][year]:
                        win = vv2.name
                    print('201{} - {}'.format(year, win))
                break

            else:
                print('Coś poszło nie tak! Spróbuj wpisać nazwy jeszcze raz :>')
                continue

        self.show_menu()

    def div_msg(self, comment):
        sex = 'both'
        msg = input(comment).strip()
        if 'kobiety' in msg:
            sex = 'women'
            res = msg.strip('kobiety')
        elif 'mężczyźni' in msg:
            sex = 'men'
            res = msg.strip('mężczyźni')
        else:
            res = msg.strip()

        return res, sex


if __name__ == '__main__':
    app = ExamsResults()
