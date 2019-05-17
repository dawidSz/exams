class ExamsResults:
    def __init__(self):
        self.texts_to_show = [
            '--- MENU ---\n 1. Średnia zdawalność województwa.\n 2. Procentowa zdawalnosc wojewodztwa.\n 3. Najlepsze województwo danego roku.\n 4. Potencjalna regresja dla danego województwa.\n 5. Porównywarka województw.\n-----------------']
        self.voivodeships_names = ['dolnośląskie', 'kujawsko-pomorskie', 'lubelskie', 'lubuskie', 'łódzkie',
                                   'małopolskie',
                                   'mazowieckie', 'opolskie' 'podkarpackie', 'podlaskie', 'pomorskie', 'śląskie',
                                   'świętokrzyskie', 'warmińsko-mazurskie', 'wielkopolskie', 'zachodniopomorskie']
        self.show_nd_choose(0)

    def show_nd_choose(self, text_number):
        print(self.texts_to_show[text_number])
        while True:
            option = input('opcja >> ')
            try:
                option = int(option)
            except ValueError:
                option = option.strip().lower()
                if option in self.voivodeships_names:
                    return option
                else:
                    print('Bledne dane! Sprobuj jeszcze raz.')
                    continue
            else:
                return option


if __name__ == '__main__':
    app = ExamsResults()
